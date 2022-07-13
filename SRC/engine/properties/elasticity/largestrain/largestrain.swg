// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef LARGESTRAIN_SWG
#define LARGESTRAIN_SWG

%module largestrain

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
 //%import "engine/propertyhdr.swg"
%import "engine/properties.swg"
%import "engine/property/elasticity/cijkl.swg"
%import "engine/property/elasticity/elasticity.swg"
#endif // NOSECONDIMPORTS

// %pragma(python) code="from ooflib.SWIG.engine.property.elasticity.cijkl import CijklPtr"
// %pragma(python) code="from ooflib.SWIG.engine.property.elasticity.elasticity import ElasticityPtr"

%{
#include "engine/property/elasticity/largestrain/largestrain.h"
%}


class CIsoLargeStrainElasticity : public Elasticity {
public:
  CIsoLargeStrainElasticity(PyObject*, PyObject*, char*, Cijkl&);
  ~CIsoLargeStrainElasticity();
};

class CAnisoLargeStrainElasticity : public Elasticity {
public:
  CAnisoLargeStrainElasticity(PyObject*, PyObject*, char*, Cijkl&);
  ~CAnisoLargeStrainElasticity();
};


%pythoncode "engine/property/elasticity/largestrain/largestrain.spy"

#endif // LARGESTRAIN_SWG
