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

%module iso

%{
#include "engine/property/elasticity/iso/iso.h"
%}

%include "common/typemaps.swg"
%pragma(python) code="from ooflib.SWIG.engine.property.elasticity.elasticity import ElasticityPtr"
%import "engine/property/elasticity/elasticity.swg"

%pragma(python) code="from ooflib.SWIG.engine.property.elasticity.cijkl import CijklPtr"
%import "engine/property/elasticity/cijkl.swg"


class CIsoElasticityProp : public Elasticity {
public:
  CIsoElasticityProp(PyObject*, PyObject*, char*, Cijkl&);
  ~CIsoElasticityProp();
};

%pythoncode "engine/property/elasticity/iso/iso.spy"

#endif // ISO_SWG
