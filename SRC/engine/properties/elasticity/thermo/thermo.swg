// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ELASTICITY_THERMO_SWG
#define ELASTICITY_THERMO_SWG

%module(package="ooflib.SWIG.engine.properties.elasticity.thermo") thermo

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/cijkl.swg"
%import "engine/properties/elasticity/elasticity.swg"

%{
#include "engine/properties/elasticity/thermo/thermo.h"
%}

class ThermoElasticityProp : public Elasticity {
public:
  ThermoElasticityProp(std::string&, PyObject*, Cijkl &cijkl,
		       double t0, double dmudt);
};


%pythoncode "engine/properties/elasticity/thermo/thermo.spy"

#endif // ELASTICITY_THERMO_SWG
