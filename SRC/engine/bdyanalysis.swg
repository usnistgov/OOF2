// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef BDYANALYSIS_SWG
#define BDYANALYSIS_SWG

%module(package="ooflib.SWIG.engine") bdyanalysis

%include "common/typemaps.swg"
%import "engine/outputval.swg"
%import "engine/flux.swg"
%import "engine/field.swg"
%import "engine/edgeset.swg"
%import "engine/femesh.swg"

%{
#include "engine/bdyanalysis.h"
#include "engine/edgeset.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/outputval.h"
%}

ArithmeticOutputValue integrateFlux(FEMesh*, Flux*, EdgeSet*);
ArithmeticOutputValue averageField(FEMesh*, Field*, EdgeSet*);

#endif // BDYANALYSIS_SWG
