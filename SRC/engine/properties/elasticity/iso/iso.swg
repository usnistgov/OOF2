// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ISO_SWG
#define ISO_SWG

%module(package="ooflib.SWIG.engine.properties.elasticity.iso") iso

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/elasticity.swg"
%import "engine/properties/elasticity/cijkl.swg"

%{
#include "engine/properties/elasticity/iso/iso.h"
%}

class CIsoElasticityProp : public Elasticity {
public:
  CIsoElasticityProp(PyObject*, PyObject*, std::string&, Cijkl&);
  ~CIsoElasticityProp();
};

%pythoncode "iso.spy"

#endif // ISO_SWG
