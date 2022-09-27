// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef ELASTICITY_VISCO_SWG
#define ELASTICITY_VISCO_SWG

%module(package="ooflib.SWIG.engine.properties.elasticity.visco") visco

%{
#include "engine/properties/elasticity/cijkl.h"
#include "engine/properties/elasticity/elasticity.h"
#include "engine/properties/elasticity/visco/visco.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/elasticity.swg"
%import "engine/properties/elasticity/cijkl.swg"
#endif // NOSECONDIMPORTS

class CViscoElasticity : public Property {
public:
  CViscoElasticity(PyObject *, const std::string&, Cijkl&);
  ~CViscoElasticity();
};


%pythoncode "engine/properties/elasticity/visco/visco.spy"

#endif // ELASTICITY_VISCO_SWG
