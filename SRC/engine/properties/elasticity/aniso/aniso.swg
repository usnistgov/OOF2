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

%module(package="ooflib.SWIG.engine.properties.elasticity.aniso") aniso

%{
#include "engine/properties/elasticity/aniso/aniso.h"
#include "engine/properties/elasticity/cijkl.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/elasticity.swg"
%import "engine/properties/elasticity/cijkl.swg"
#endif // NOSECONDIMPORTS

class CAnisoElasticity : public Elasticity {
public:
  CAnisoElasticity(PyObject *registry, PyObject *self, char *name, Cijkl &c);
  ~CAnisoElasticity();
  const Cijkl crystal_cijkl();
};

%pythoncode "engine/properties/elasticity/aniso/aniso.spy"

#endif // ANISO_SWG
