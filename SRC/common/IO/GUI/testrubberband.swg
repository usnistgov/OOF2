// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef TESTRUBBERBAND_SWG
#define TESTRUBBERBAND_SWG

%module(package="ooflib.SWIG.common.IO.GUI") testrubberband

 //%include "common/typemaps.swg"

%{
  #include "common/IO/GUI/testrubberband.h"
%}

void testRubberBand();

#endif // TESTRUBBERBAND_SWG
