// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PROPERTIES_SWG
#define PROPERTIES_SWG

// TODO: "property" is a bad choice for a module name in Python.  It's
// not a reserved word, so it's legal, but it might be confusing (at
// best).

%module(package="ooflib.SWIG.engine") property
%include "common/typemaps.swg"

%{
#include "engine/property.h"
#include "engine/csubproblem.h"
%}

%nodefaultctor Property;

class Property {
public:
  ~Property();
  const std::string &name();
  const std::string &classname(); // Returns the name of the derived class.
  bool is_computable(CSubProblem*);
  void cache_active(CSubProblem*, bool);
  bool currently_active(CSubProblem*);
  void cache_nonlinearity(CSubProblem*, bool);
  bool currently_nonlinear(CSubProblem*);
  PyObject *registration();

  // Methods that are redefined in pypropertywrapper.h must be swigged
  // under different names, so that Python won't call the wrapper
  // function recursively if the method is *not* redefined in a
  // derived Python Property class.

  // ********* CAUTION *********************************************
  // The %rename line below applies to all member functions below it
  // in this *file*, not just the ones in this class.  That's ok, at
  // the moment, but if other methods that shouldn't be renamed are
  // added it'll be confusing.  It's supposed to be possible to
  // restrict the renaming to a particular class by adding
  // '%$classname="TheClassName"' to the predicates in the command,
  // but that doesn't seem to work.  When I try it, nothing is
  // renamed, using swig 4.0.2.
  // ***************************************************************
  // A problem with using %rename like this is that someone searching
  // the code for c_cross_reference, c_precompute, c_is_symmetric_K,
  // etc won't find anything, except possibly in this comment.
  %rename("c_%s", %$isfunction, %$ismember) "";
  //  %rename("c_%s", %$isfunction, %$classname="Property") "";

  void cross_reference(Material*);
  void precompute(FEMesh*);
  bool is_symmetric_K(const CSubProblem*);
  bool is_symmetric_C(const CSubProblem*);
  bool is_symmetric_M(const CSubProblem*);
  bool constant_in_space();
  void begin_element(CSubProblem*, Element*);
  void end_element(CSubProblem*, Element*);
  void post_process(CSubProblem*, Element*);
  void output(FEMesh*, Element*, PropertyOutput*, MasterPosition&, OutputVal*);
};

PYTHONEXPORTABLE(Property);

// None of the methods defined in the derived classes need to be
// called from Python, but the class hierarchy has to be known.

%nodefaultctor PhysicalProperty;

class PhysicalProperty : public Property {};

%nodefaultctor FluxProperty;

class FluxProperty : public PhysicalProperty {};

%nodefaultctor EqnProperty;

class EqnProperty : public PhysicalProperty {};

%nodefaultctor AuxiliaryProperty;

class AuxiliaryProperty : public Property {};
  

double deriv_eps;

%pythoncode "engine/property.spy"

// Cancel the earlier %rename, so that this file can be safely
// imported into another swig file.
%rename("%s") "";

#endif // PROPERTIES_SWG
