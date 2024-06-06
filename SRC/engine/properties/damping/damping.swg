// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef DAMPING_SWG
#define DAMPING_SWG

%module(package="ooflib.SWIG.engine.properties.damping") damping

%{
#include "engine/properties/damping/damping.h"
%}

%include "common/typemaps.swg"
%import "engine/property.swg"

class IsotropicDampingProp : public EqnProperty {
public:
  IsotropicDampingProp(std::string&, PyObject*, double);
};

%pythoncode "engine/properties/damping/damping.spy"

#endif // DAMPING_SWG
