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

%module(package="ooflib.SWIG.engine.properties.elasticity.largestrain") largestrain

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/cijkl.swg"
%import "engine/properties/elasticity/elasticity.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/properties/elasticity/largestrain/largestrain.h"
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


%pythoncode "engine/properties/elasticity/largestrain/largestrain.spy"

#endif // LARGESTRAIN_SWG
