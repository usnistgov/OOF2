// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELSETBOUNDARY_SWG
#define PIXELSETBOUNDARY_SWG

%module(package="ooflib.SWIG.common") pixelsetboundary

%include "common/typemaps.swg"

%{
#include <common/pixelsetboundary.h>
%}

double tilingfactor;
int mintilescale;
int fixed_subdivision;
void printHomogStats();

#endif // PIXELSETBOUNDARY_SWG
