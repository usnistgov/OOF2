// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef SKELETONRELAXATIONRATE_SWG
#define SKELETONRELAXATIONRATE_SWG

%module(package="ooflib.SWIG.engine.properties.skeletonrelaxationrate") skeletonrelaxationrate

%include "common/typemaps.swg"
%import "engine/property.swg"

%{
#include "engine/properties/skeletonrelaxationrate/skeletonrelaxationrate.h"
%}

class SkeletonRelaxationRate : public Property {
public:
  SkeletonRelaxationRate(PyObject *reg, char *name, double alpha, double beta);
  const double alpha();
};

%pythoncode "engine/properties/skeletonrelaxationrate/skeletonrelaxationrate.spy"

#endif // SKELETONRELAXATIONRATE_SWG
