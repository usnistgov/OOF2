// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ANISO_SWG
#define ANISO_SWG

%module aniso

%{
#include "engine/property/elasticity/aniso/aniso.h"
#include "engine/property/elasticity/cijkl.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property/elasticity/elasticity.swg"
%import "engine/property/elasticity/cijkl.swg"
#endif // NOSECONDIMPORTS

//%pragma(python) code="from ooflib.SWIG.engine.property.elasticity.elasticity import ElasticityPtr"
//%pragma(python) code="from ooflib.SWIG.engine.property.elasticity.cijkl import CijklPtr"

class CAnisoElasticity : public Elasticity
{
public:
  CAnisoElasticity(PyObject *registry, PyObject *self, char *name, Cijkl &c);
  ~CAnisoElasticity();
  const Cijkl crystal_cijkl();
};

%pythoncode "engine/property/elasticity/aniso/aniso.spy"

#endif // ANISO_SWG
