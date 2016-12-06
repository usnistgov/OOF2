// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#include <oofconfig.h>
#ifdef DEBUG
#include <assert.h>
#endif
#include "common/activearea.h"
#include "common/cmicrostructure.h"
#include "common/coord.h"
#include "common/pixelattribute.h"
#include "common/IO/stringimage.h"
#include "common/tostring.h"
#include "common/trace.h"
#include "common/printvec.h"
#include "engine/cnonlinearsolver.h"
#include "engine/csubproblem.h"
#include "engine/elementnodeiterator.h"
#include "engine/ooferror.h"
#include "engine/property/color/color.h"
#include "engine/IO/propertyoutput.h"
#include "engine/linearizedsystem.h"
#include "engine/element.h"
#include "engine/equation.h"
#include "engine/flux.h"
#include "engine/mastercoord.h"
#include "engine/material.h"
#include "engine/equation.h"
#include "engine/smallsystem.h"
#include <iostream>
#include <vector>
#include <map>


//Interface branch
Material::Material(const std::string &nm,
		   const std::string &materialtype)
  : name_(nm),
    type_(materialtype),
    fluxprop(Flux::allfluxes().size()),
    // active_fluxes(Flux::allfluxes().size()),
    // active_eqns(Equation::all().size()),
    outputprop(nPropertyOutputRegistrations()),
    self_consistent_(true)
{
  // Ensure that keys exist in the maps for all the fluxes and
  // equations.  This may not be strictly necessary, since std::maps
  // will create pairs as required by the operator[] function, but it
  // seems wise.

  for(std::vector<Flux*>::const_iterator fi = Flux::allfluxes().begin();
      fi!=Flux::allfluxes().end(); ++fi)
    fluxpropmap[*fi] = FluxPropList();
  for(std::vector<Equation*>::const_iterator ei = Equation::all().begin();
      ei!=Equation::all().end(); ++ei)
    eqnpropmap[*ei] = std::vector<EqnProperty*>();
}

Material::~Material() {}

const TimeStamp &Material::getTimeStamp() const {
  return timestamp;
}

std::ostream &operator<<(std::ostream &os, const Material &mat) {
  os << "Material('" << mat.name();
  for(std::vector<Property*>::size_type i=0; i<mat.property.size(); i++)
    os << ", " << *mat.property[i];
  os << "')";
  return os;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


// Special local class for keeping track of which *types* of
// properties are present in the material.  There can only be one
// property of each type in a well-formed material.

class MaterialPropertyRegistration {
private:
  const std::string tag;
  Property *property;
  MaterialPropertyRegistration(Property *p, const std::string &str)
    : tag(str), property(p)
  {}
  friend class MaterialPropertyRegistry;
};

// Register a property under the name "tag"
void MaterialPropertyRegistry::registr(Property *prop, const std::string &tag) {
  if(fetch(tag)) {		// Can't have two Properties with the same name
    throw ErrRedundantProperty(tag);
  }
  reg.push_back(new MaterialPropertyRegistration(prop, tag));
}

// Find the property registered with the name "tag"
Property *MaterialPropertyRegistry::fetch(const std::string &tag) const {
  for(std::vector<MaterialPropertyRegistration*>::size_type i=0; i<reg.size();
      i++)
    {
      if(reg[i]->tag == tag) {
	return reg[i]->property;
      }
    }
  return 0;
}

MaterialPropertyRegistry::~MaterialPropertyRegistry() {
  clear();
}

void MaterialPropertyRegistry::clear() {
  for(std::vector<MaterialPropertyRegistration*>::size_type i=0; i<reg.size();
      i++)
    delete reg[i];
  reg.clear();
}

#ifdef DEBUG
void MaterialPropertyRegistry::dump(std::ostream &os) const {
  for(std::vector<MaterialPropertyRegistration*>::size_type i=0; i<reg.size();
      i++)
    {
      os << reg[i]->property->name()
	 << " (" << reg[i]->property->classname() << ") "
	 << reg[i]->tag << std::endl;
    }
}
#endif // DEBUG

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


Property *Material::getProperty(int i) const {
  return property[i];
}


void Material::add1Property(Property *prop) {
  property.push_back(prop);
  ++timestamp;
}

void Material::remove1Property(Property *prop) {
  for(std::vector<Property*>::iterator p=property.begin(); p<property.end();
      ++p)
    {
      if(*p == prop) {
	property.erase(p);
	++timestamp;
	return;
      }
    }
  throw ErrNoSuchProperty(name(), prop->name());
}

void Material::registerPropertyType(Property *p, const std::string &nm) {
  // Called by Property::bookkeeping().
  registry.registr(p, nm);
}

// Return the property whose type is given by the string.
Property *Material::fetchProperty(const std::string &nm) const {
  Property *prop = registry.fetch(nm);
  if(!prop) {
    throw ErrNoSuchProperty(name(), nm);
  }
  return prop;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Material::clear_fluxproplist() {
  for(std::vector<FluxPropList>::size_type i=0; i< fluxprop.size(); i++)
    fluxprop[i].clear();
  for(FluxPropMap::iterator fpi=fluxpropmap.begin(); fpi!=fluxpropmap.end();
      ++fpi)
    {
      (*fpi).second.clear();
    }

}

void Material::clear_eqnproplist() {
  for(EqnPropMap::iterator epi=eqnpropmap.begin(); epi!=eqnpropmap.end(); ++epi)
    {
      (*epi).second.clear();
    }
}

void Material::clear_xref() {
  clear_fluxproplist();
  clear_eqnproplist();
  clear_outputprop();
  registry.clear();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Material::registerFlux(Property *prop, const Flux *flux) {
  // This property contributes to this flux.  Called by
  // Property::bookkeeping().
  FluxProperty *p = dynamic_cast<FluxProperty*>(prop);
  fluxprop[flux->index()].push_back(p);
  fluxpropmap[flux].push_back(p);
}

void Material::registerEqn(Property *prop, const Equation *eqn) {
  // This property contributes directly to this equation.  Called by
  // Property::bookkeeping.
  eqnpropmap[eqn].push_back(dynamic_cast<EqnProperty*>(prop));
}

// Routine to query whether or not this material has properties which
// contribute to the indicated flux -- this is true if the
// corresponding fluxprop entry has nonzero length.
bool Material::contributes_to_flux(const Flux *flux) const {
  if (fluxprop[flux->index()].size() != 0) {
    return true;
  }
  return false;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Material::registerOutput(Property *prop, const std::string &outputname) {
  // The given Property, which is present in this material,
  // contributes to the given PropertyOutput.
  PropertyOutputRegistration *reg = getPropertyOutputReg(outputname);
  if(!reg)
    throw ErrProgrammingError("PropertyOutputRegistration " + outputname
			      + " not found!", __FILE__, __LINE__);
  outputprop[reg->index()].push_back(prop);
}

void Material::clear_outputprop() {
  for(std::vector<std::vector<Property*> >::size_type i=0; i<outputprop.size();
      i++)
    outputprop[i].clear();
};

const std::vector<Property*> &
Material::outputProperties(const PropertyOutput *pout) const {
  return outputprop[pout->index()];
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Element start/end.  Since each element has a unique material,
// these can only be called once per element.  The reason they're
// here is because the Material is the one with the handy-dandy
// list of properties.
void Material::begin_element(const CSubProblem *subproblem, const Element *el)
  const
{
  for(std::vector<Property*>::size_type i=0;i<property.size();i++) {
    if(property[i]->currently_active(subproblem)) {
      property[i]->begin_element(subproblem, el);
    }
  }
}

void Material::end_element(const CSubProblem *subproblem, const Element *el)
  const
{
  for(std::vector<Property*>::size_type i=0;i<property.size();i++) {
    if(property[i]->currently_active(subproblem)) {
      property[i]->end_element(subproblem, el);
    }
  }
}

void Material::cprecompute(CSubProblem *subproblem) {
  // Build the lists of fluxes and equations which have contributions
  // from active fields.  A flux is active if an active property
  // contributes to it, and a property is active if every field it
  // depends on is defined.  An equation is active if it's being
  // solved.
  subproblem->clear_active_fluxes(this);
  std::vector<Flux*> &active_fluxes = subproblem->active_fluxes(this);
  subproblem->clear_active_equations(this);
  std::vector<Equation*> &active_eqns = subproblem->active_equations(this);
  std::vector<Flux*> &flxs = Flux::allfluxes();
  for(std::vector<Flux*>::iterator fi = flxs.begin(); fi!=flxs.end();++fi) {
    if (subproblem->is_active_flux(*(*fi)))
      active_fluxes.push_back(*fi);
  }

  std::vector<Equation*> &eqns = Equation::all();
  for(std::vector<Equation*>::iterator ei = eqns.begin(); ei!=eqns.end();++ei) {
    if (subproblem->is_active_equation(*(*ei)))
      active_eqns.push_back(*ei);
  }
}

int Material::integrationOrder(const CSubProblem *subproblem,
			       const Element *element)
  const
{
  int maxorder = 0;
  const std::vector<Equation*> &active_eqns =
    subproblem->active_equations(this);
  const std::vector<Flux*> &active_fluxes = subproblem->active_fluxes(this);

  for(std::vector<Flux*>::const_iterator fluxi = active_fluxes.begin();
      fluxi != active_fluxes.end(); ++fluxi)
    {
      FluxPropMap::const_iterator stupid = fluxpropmap.find(*fluxi);
      const FluxPropList &flux_prop_list = (*stupid).second;
      const Flux *flux = (*stupid).first;

      // Loop over active FluxEquations that use this flux.
      for(std::vector<Equation*>::const_iterator eqn=flux->getEqnList().begin();
	  eqn!=flux->getEqnList().end(); ++eqn)
	{

	  for(FluxPropList::const_iterator property = flux_prop_list.begin();
	      property != flux_prop_list.end(); ++property)
	    {
	      int order = (*property)->integration_order(subproblem, element) +
		(*eqn)->integration_order(element);
	      if(order > maxorder)
		maxorder = order;
	    }
	}
    }
  
  for(std::vector<Equation*>::const_iterator eqn=active_eqns.begin();
      eqn != active_eqns.end(); ++eqn)
    {
      EqnPropMap::const_iterator stupid = eqnpropmap.find(*eqn);
      const EqnPropList &proplist = (*stupid).second;
      for(std::vector<EqnProperty*>::const_iterator property=proplist.begin();
	  property != proplist.end(); ++property)
	{
	  int order = (*property)->integration_order(subproblem, element) +
	    (*eqn)->integration_order(element);
	  if(order > maxorder)
	    maxorder = order;
	}
	  
    }
  return maxorder;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Post-processing is initially very simple -- just call each
// member property's post_process routine....
void Material::post_process(CSubProblem *subproblem, const Element *el) const {
  for(std::vector<Property*>::size_type i=0; i<property.size(); i++) {
    property[i]->post_process(subproblem, el);
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Make_linear_system, already inside the gausspoint loop.
// Called from Element::make_linear_system.
void Material::make_linear_system(const CSubProblem *subproblem,
				  const Element *el,
				  const GaussPointIterator &gpt,
				  const std::vector<int> &dofmap,
				  double time,
				  const CNonlinearSolver *nlsolver,
				  LinearizedSystem &linearized_system)
  const
{
  // By the time we are called, we are promised that cross_reference
  // has been run, and that the material is in a consistent state.
  GaussPoint pt = gpt.gausspoint(); // current gauss pt from gauss pt iterator
  FEMesh *mesh = subproblem->mesh;

  FluxSysMap fluxdata;

  const std::vector<Flux*> &active_fluxes = subproblem->active_fluxes(this);

  for (std::vector<Flux*>::const_iterator fluxi = active_fluxes.begin();
       fluxi != active_fluxes.end(); ++fluxi)
    {
      // "SmallSystem" is a set of 3 matrices and a vector.
      SmallSystem *flux_small_sys = (*fluxi)->initializeSystem( el );
      SmallSystem *property_flux_info = (*fluxi)->initializeSystem( el );
	  
      // Use "at", because everything is const. Actually, don't use it,
      // because it's not standard.  Use "find" instead.
      FluxPropMap::const_iterator stupid = fluxpropmap.find(*fluxi);
      const FluxPropList &flux_prop_list = (*stupid).second;

      // Compute the flux info for each property associated with current flux.
      // There should only be FluxProperties in the list.
      for (FluxPropList::const_iterator property = flux_prop_list.begin();
           property != flux_prop_list.end(); ++property)
	{
	  // if the property is active in the current subproblem,
	  // calculate its contributions to the active flux
	  if ( (*property)->currently_active(subproblem) ) {
	    (*property)->begin_point( mesh, el, (*fluxi), pt );
	    (*property)->make_flux_contributions(mesh, el, *fluxi, pt, time,
						 nlsolver, property_flux_info);
	    (*property)->end_point( mesh, el, (*fluxi), pt );
	    
	    // add the flux contributions of the property to the flux
	    // small system
	    *flux_small_sys += *property_flux_info;
	    property_flux_info->reset();
	  } // End of if (property active in subproblem)
	  
      } // End of active flux property list loop.

      fluxdata[*fluxi] = flux_small_sys;
      delete property_flux_info;
    } // End of active flux loop.

  // Now, for each equation, build the direct contributions
  // in the equation lists.

  // TODO: For point-wise constraint equations, "activity" might be
  // true at some gausspoints and false at others.  We are already
  // inside the gausspoint loop, so for us here it's just true or
  // false, but the question is not answered by the active_eqns
  // iterator.  It may make sense to iterate over these separately,
  // but the constraint handling *property* is still in the material,
  // so we still have to do this in this routine somewhere.

  const std::vector<Equation*> &active_eqns = 
    subproblem->active_equations(this);

  for(std::vector<Equation*>::const_iterator eqn = active_eqns.begin();
      eqn != active_eqns.end();  ++eqn)
  {
    SmallSystem *eqndata = (*eqn)->initializeSystem( el );
    SmallSystem *property_eqn_info = (*eqn)->initializeSystem(el);

    EqnPropMap::const_iterator stupid = eqnpropmap.find(*eqn);
    const EqnPropList &eqn_prop_list = (*stupid).second;

    // TODO MAYBE: In principle, there could be another begin_point
    // hook here to call the property with the appropriate equation.
    // If such a thing turns out to be needed, follow the begin_point
    // pattern for fluxes.
    for(std::vector<EqnProperty*>::const_iterator property=eqn_prop_list.begin();
	property != eqn_prop_list.end(); ++property)
      {
	if ( (*property)->currently_active(subproblem) ) {
	  (*property)->make_equation_contributions(mesh, el, *eqn, pt, time,
						   nlsolver, property_eqn_info);

	  // add the eqn contributions of the property to the eqn
	  // small system
	  *eqndata += *property_eqn_info;
	  property_eqn_info->reset();
	}
      } // End of property loop.
    
    // Finally, we use the computed fluxdata and eqndata to make
    // the contributions to the global vectors and matrices.
    // Here dofmap is the Element's localDoFmap, which maps local
    // element dof indices to global ones.

    (*eqn)->make_linear_system( subproblem, el, pt, dofmap,
			        fluxdata, eqndata,
				nlsolver, linearized_system );
    delete eqndata;
    delete property_eqn_info;
  } // End of equation loop.

  // Clean up fluxdata map.
  for (FluxSysMap::iterator fi = fluxdata.begin(); fi != fluxdata.end(); ++fi) {
    delete (*fi).second;
    (*fi).second = 0;
  }
  // fluxdata object goes out of scope and is destroyed.
} // End of 'Material::make_linear_system'


// find_fluxdata is called by Flux::evaluate when computing a flux
// value. It's not used directly for matrix construction.

void Material::find_fluxdata(const FEMesh *mesh, const Element *el,
			     const Flux *flux, const MasterPosition &mpos,
			     SmallSystem *fluxdata) const {
  FluxPropMap::const_iterator stupid = fluxpropmap.find(flux);
  const FluxPropList &fpl = (*stupid).second;
  double time = mesh->getCurrentTime();
  
  for(FluxPropList::const_iterator fp=fpl.begin(); fp!=fpl.end(); ++fp) {
    (*fp)->begin_point(mesh, el, flux, mpos);
    // Instead of checking fields, we rely on the field-evaluation
    // exception, because field activities are not necessarily set
    // correctly except during linearized-system construction.
    try {
      (*fp)->flux_value(mesh, el, flux, mpos, time, fluxdata);
    }
    catch (ErrNoSuchField &exc) {
    }
    (*fp)->end_point(mesh, el, flux, mpos);
  }
}


//=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=

// Returns a FluxPropList for a give Flux.
FluxPropList Material::get_flux_props(const Flux *fluks) const
{
  return fluxprop[fluks->index()];
}

#ifdef DEBUG
void Material::dump(std::ostream &os) const {
  os << "Material " << name() << ":" << std::endl;
  registry.dump(os);
}

#endif // DEBUG

//=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=

// Materials are assigned to Microstructure pixels with a
// PixelAttribute class.  See common/pixelattribute.h for details.

const std::string
MaterialAttributeRegistration::classname_("MaterialAttributeRegistration");
const std::string
MaterialAttributeRegistration::modulename_("ooflib.SWIG.engine.material");

static MaterialAttributeRegistration *matattrreg;

// The MaterialAttributeGlobalData class keeps track of how many
// pixels are assigned to each Material in a Microstructure.  This
// provides a quick way of determining which Materials are used in the
// Microstructure, which allows the Microstructure to respond to
// changes in Materials without looking through all of its pixels to
// see if the changed Material is present.

// MatMap counts how many times each Material is used in the
// Microstructure.
typedef std::map<const Material*, int, ltidobject> MatMap;

class MaterialAttributeGlobalData : public PixelAttributeGlobalData {
public:
  const CMicrostructure *microstructure;
  MatMap matmap;

  // getCount creats an entry for the material if it does not exist in
  // the map.  If you just want to query, use "count", below.
  int &getCount(const Material *mat) {
    MatMap::iterator i = matmap.find(mat);
    if(i == matmap.end()) {
      matmap[mat] = 0;
      return matmap[mat];
    }
    return (*i).second;
  }

  int count(const Material *mat) const {
    MatMap::const_iterator i = matmap.find(mat);
    if(i == matmap.end()) return 0;
    return (*i).second;
  }

  void remove(const Material *mat) {
    MatMap::iterator i = matmap.find(mat);
    if (i!=matmap.end())
      matmap.erase(i);
  }

  MaterialAttributeGlobalData(const CMicrostructure *microstructure)
    : microstructure(microstructure)
  {}
  void materialAddedToPixel(const Material *mat) {
    if(mat)
      getCount(mat)++;
  }
  void materialRemovedFromPixel(const Material *mat) {
    if(mat)
      getCount(mat)--;
  }

  std::vector<const Material*> *getMaterials() const {
    std::vector<const Material*> *mvec = new std::vector<const Material*>;
    for(MatMap::const_iterator i=matmap.begin(); i!=matmap.end(); ++i)
      if((*i).second > 0)
	mvec->push_back((*i).first);
    return mvec;
  }
  TimeStamp getTimeStamp() const {
    TimeStamp latest = timeZero;
    for(MatMap::const_iterator i=matmap.begin(); i!=matmap.end(); ++i) {
      const Material *mat = (*i).first;
      int count = (*i).second;
      if(count > 0) {
	const TimeStamp &ts = mat->getTimeStamp();
	if(ts > latest)
	  latest = ts;
      }
    }
    return latest;
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

MaterialAttributeRegistration::MaterialAttributeRegistration()
  : PxlAttributeRegistration("Material")
{
  matattrreg = this;
}

PixelAttributeGlobalData *
MaterialAttributeRegistration::createAttributeGlobalData(const
							 CMicrostructure *ms)
  const
{
  return new MaterialAttributeGlobalData(ms);
}

void MaterialAttribute::set(const Material *m) {
  material = m;
}

// getMaterialMap and getConstMaterialMap are provided so that
// matattrreg can be a static variable in this file, but still make
// the map available to others.

Array<PixelAttribute*> &getMaterialMap(const CMicrostructure *ms) {
  return matattrreg->map(ms);
}

const Array<PixelAttribute*> &getConstMaterialMap(const CMicrostructure *ms) {
  return matattrreg->map(ms);
}
// Find all the MaterialAttributes in the given microstructure which
// refer to this material, and clear them.  If the material count is
// nonzero, iterate over all of of the MaterialAttributes and check
// them individually.

// TODO LATER: It is possible to be more clever about this, having the
// materials maintain a list of attributes which refer to them, and
// keeping it up to date, by tracking all MaterialAttribute set
// operations.  This is currently not done, because it imposes a large
// storage and searching cost on the materials themselves.  Searching
// through the whole array is probably slower, but it happens less
// frequently.

bool Material::cleanAttributes(CMicrostructure *ms) const {
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->globalData(ms));
#ifdef DEBUG
  assert(gd!=0);
#endif
  if (gd->count(this)!=0) {
    const Array<PixelAttribute*> &mat_attrs = matattrreg->map(ms);
    for(Array<PixelAttribute*>::const_iterator i=mat_attrs.begin();
	i!=mat_attrs.end(); ++i) {
      MaterialAttribute *ma = dynamic_cast<MaterialAttribute*>(*i);
#ifdef DEBUG
      assert(ma!=0);
#endif
      if (this == ma->get())
	ma->set(0);
    }
    // Remove this material from the map, if it's present.
    gd->remove(this);
    ms->recategorize();
    return true;
  }
  return false;
}

bool Material::replaceAttributes(CMicrostructure *ms, Material *newmat) const {
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->globalData(ms));
#ifdef DEBUG
  assert(gd!=0);
#endif
  if (gd->count(this)!=0) {
    const Array<PixelAttribute*> &mat_attrs = matattrreg->map(ms);
    for(Array<PixelAttribute*>::const_iterator i=mat_attrs.begin();
	i!=mat_attrs.end(); ++i) {
      MaterialAttribute *ma = dynamic_cast<MaterialAttribute*>(*i);
#ifdef DEBUG
      assert(ma!=0);
#endif
      if (this == ma->get()) {
	ma->set(newmat);
	gd->materialAddedToPixel(newmat);
      }
    }
    // Remove this material from the map, if it's present.
    gd->remove(this);
    ms->recategorize();
    return true;
  }
  return false;
}

bool MaterialAttribute::operator<(const PixelAttribute &other) const {
  const MaterialAttribute &othermat =
    dynamic_cast<const MaterialAttribute&>(other);
  if(material != 0 && othermat.material != 0)
    return material->name() < othermat.material->name();
  if(material == 0 && othermat.material != 0)
    return true;
  return false;
}

void MaterialAttribute::print(std::ostream &os) const {
  if(material)
    os << "Material(" << material->name() << ")";
  else
    os << "[No Material]";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Material::assignToPixels(CMicrostructure *microstructure,
			      const std::vector<ICoord> *pxls) const
{
  // First, remove the old material, if any.
  removeMaterialFromPixels(microstructure, *pxls);

  Array<PixelAttribute*> &matMap = matattrreg->map(microstructure);
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->
					       globalData(microstructure));
#ifdef DEBUG
  assert(gd!=0);
#endif
  const ActiveArea *activearea = microstructure->getActiveArea();
  for(std::vector<ICoord>::const_iterator i=pxls->begin(); i<pxls->end(); ++i) {
    if(activearea->isActive(*i)) {
      MaterialAttribute *matAtt = dynamic_cast<MaterialAttribute*>(matMap[*i]);
      matAtt->set(this);
      gd->materialAddedToPixel(this);
    }
  }
  microstructure->recategorize();
}

void Material::assignToPixelGroup(CMicrostructure *microstructure,
				  const PixelSet *pixset) const
{
  // Assign material to the pixels in the given group.
  assignToPixels(microstructure, pixset->members());
}

void Material::assignToAllPixels(CMicrostructure *microstructure) const {
  Array<PixelAttribute*> &matMap = matattrreg->map(microstructure);
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->
					       globalData(microstructure));
#ifdef DEBUG
  assert(gd!=0);
#endif
  const ActiveArea *activearea = microstructure->getActiveArea();
  for(Array<PixelAttribute*>::iterator i=matMap.begin(); i!=matMap.end(); ++i) {
    if(activearea->isActive(i.coord())) {
      MaterialAttribute *matAtt = dynamic_cast<MaterialAttribute*>(*i);
#ifdef DEBUG
      assert(matAtt!=0);
#endif
      gd->materialRemovedFromPixel(matAtt->get());
      matAtt->set(this);
      gd->materialAddedToPixel(this);
    }
  }
  microstructure->recategorize();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

int Material::nPixelsInMicrostructure(const CMicrostructure *microstructure)
  const
{
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->
					       globalData(microstructure));
#ifdef DEBUG
  assert(gd!=0);
#endif
  return gd->count(this);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void removeMaterialFromPixels(CMicrostructure *microstructure,
			      const std::vector<ICoord> &pxls)
{
  Array<PixelAttribute*> &matMap = matattrreg->map(microstructure);
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->
					       globalData(microstructure));
#ifdef DEBUG
  assert(gd!=0);
#endif
  const ActiveArea *activearea = microstructure->getActiveArea();
  for(std::vector<ICoord>::const_iterator i=pxls.begin(); i<pxls.end(); ++i) {
    if(activearea->isActive(*i)) {
      MaterialAttribute *matAtt = dynamic_cast<MaterialAttribute*>(matMap[*i]);
#ifdef DEBUG
      assert(matAtt!=0);
#endif
      gd->materialRemovedFromPixel(matAtt->get());
      matAtt->set(0);
    }
  }
  microstructure->recategorize();
}

void removeMaterialFromPixels(CMicrostructure *microstructure,
				const PixelSet *pixset)
{
  removeMaterialFromPixels(microstructure, *pixset->members());
}

void removeAllMaterials(CMicrostructure *microstructure) {
  Array<PixelAttribute*> &matMap = matattrreg->map(microstructure);
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->
					       globalData(microstructure));
#ifdef DEBUG
  assert(gd!=0);
#endif
  const ActiveArea *activearea = microstructure->getActiveArea();
  for(Array<PixelAttribute*>::iterator i=matMap.begin(); i!=matMap.end(); ++i) {
    if(activearea->isActive(i.coord())) {
      MaterialAttribute *matAtt = dynamic_cast<MaterialAttribute*>(*i);
#ifdef DEBUG
      assert(matAtt!=0);
#endif
      gd->materialRemovedFromPixel(matAtt->get());
      matAtt->set(0);
    }
  }
  microstructure->recategorize();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

TimeStamp getMaterialTimeStamp(const CMicrostructure *microstructure) {
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->
					       globalData(microstructure));
#ifdef DEBUG
  assert(gd!=0);
#endif
  return gd->getTimeStamp();
}

const Material *getMaterialFromCategory(const CMicrostructure *microstructure,
					int category)
{
  const ICoord &where = microstructure->getRepresentativePixel(category);
  return getMaterialFromPoint(microstructure, &where);
}

const Material *getMaterialFromPoint(const CMicrostructure *microstructure,
				     const ICoord *where)
{
  Array<PixelAttribute*> &matMap = matattrreg->map(microstructure);
  MaterialAttribute *matAtt = dynamic_cast<MaterialAttribute*>(matMap[*where]);
#ifdef DEBUG
  assert(matAtt!=0);
#endif
  return matAtt->get();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

MaterialImage::MaterialImage(CMicrostructure *microstructure,
			     const CColor *noMaterial,
			     const CColor *noColor)
  : microstructure(microstructure),
    noMaterial(*noMaterial),
    noColor(*noColor)
{}

const Coord &MaterialImage::size() const {
  return microstructure->size();
}

const ICoord &MaterialImage::sizeInPixels() const {
  return microstructure->sizeInPixels();
}

void MaterialImage::fillstringimage(StringImage *strimg) const {
  const Array<PixelAttribute*> &matMap = matattrreg->map(microstructure);
  for(Array<PixelAttribute*>::const_iterator i=matMap.begin(); i!=matMap.end();
      ++i)
    {
      MaterialAttribute *matAtt = dynamic_cast<MaterialAttribute*>(*i);
      const Material *mat = matAtt->get();
      if(mat) {
	try {
	  Property *cprop = mat->fetchProperty("Color");
	  ColorProp *colorprop = dynamic_cast<ColorProp*>(cprop);
	  const CColor &cc = colorprop->color();
	  strimg->set(&i.coord(), &cc);
	}
	catch(ErrNoSuchProperty &exc) {
	  strimg->set(&i.coord(), &noColor);
	}
      }	// if mat
      else
	strimg->set(&i.coord(), &noMaterial);
    }
}

#if DIM==3

// TODO 3D: This code could be organized better to avoid the overlaps
// with the fillstringimage method used in 2D and the image padding
// code from oofimage3d

// TODO 3D: We probably also want to store this as a single component
// image where the single scalar is the material index and make color
// transfer functions which convert the index to the material color.
// Access material index as mat->objectid().  Will need to drastically
// change how color transfer functions are created in the canvas for
// this to work for display.

void setVoxel(vtkImageData *image, const ICoord coord, const CColor cc) {
  image->SetScalarComponentFromFloat(coord(0),coord(1),coord(2),0,255*cc.getRed());
  image->SetScalarComponentFromFloat(coord(0),coord(1),coord(2),1,255*cc.getGreen());
  image->SetScalarComponentFromFloat(coord(0),coord(1),coord(2),2,255*cc.getBlue());
  image->SetScalarComponentFromFloat(coord(0),coord(1),coord(2),3,255*(1-cc.getAlpha()));
}

PyObject* MaterialImage::getImageData() {
  const Array<PixelAttribute*> &matMap = matattrreg->map(microstructure);
  vtkImageData *image = vtkImageData::New();
  ICoord sizeInPixels = microstructure->sizeInPixels();
  image->SetDimensions(sizeInPixels(0),sizeInPixels(1),sizeInPixels(2));
  image->SetScalarTypeToUnsignedChar();
  image->SetNumberOfScalarComponents(4);
  image->AllocateScalars();

  for(Array<PixelAttribute*>::const_iterator i=matMap.begin(); i!=matMap.end();
      ++i)
    {
      MaterialAttribute *matAtt = dynamic_cast<MaterialAttribute*>(*i);
      const Material *mat = matAtt->get();
      if(mat) {
	try {
	  Property *cprop = mat->fetchProperty("Color");
	  ColorProp *colorprop = dynamic_cast<ColorProp*>(cprop);
	  const CColor &cc = colorprop->color();
	  setVoxel(image, i.coord(), cc);
	}
	catch(ErrNoSuchProperty &exc) {
	  setVoxel(image, i.coord(), noColor);
	}
      }	// if mat
      else
	setVoxel(image, i.coord(), noMaterial);
    }

  // copied from oofimage3d.C
  image->Update();
  int *currentextent = image->GetExtent();
  int newextent[6] = {0,0,0,0,0,0};
  vtkImageConstantPad *padder;
  // Be careful to not overwrite the extent in the current image.
  for(int i = 1; i<7; i+=2) newextent[i]=currentextent[i]+1;

  padder = vtkImageConstantPad::New();
  padder->SetInputConnection(image->GetProducerPort());
  padder->SetOutputWholeExtent(newextent);
  padder->SetOutputNumberOfScalarComponents(4);
  padder->SetConstant(255);

  image = padder->GetOutput();
  image->Update();

  return vtkPythonGetObjectFromPointer(image);
}


#endif

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Return a list of all Materials used in a Microstructure.
std::vector<const Material*> *
getMaterials(const CMicrostructure *microstructure) {
  MaterialAttributeGlobalData *gd =
    dynamic_cast<MaterialAttributeGlobalData*>(matattrreg->
					       globalData(microstructure));
#ifdef DEBUG
  assert(gd!=0);
#endif
  return gd->getMaterials();
}
