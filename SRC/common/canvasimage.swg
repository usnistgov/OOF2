// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CANVASIMAGE_SWG
#define CANVASIMAGE_SWG

// This file defines the CanvasImage and NewCanvasImage typemaps for
// returning an OOFCanvas::CanvasImage from C++ to Python.  The
// typemaps aren't in common/typemaps.swg in order to avoid including
// oofcanvas.h in all swig C++ output files.

// This file doesn't define a module and shouldn't be swigged
// directly.  It should be %included in other swig files, not
// %imported.

%include "typemaps.swg"

%{
  #include <oofcanvas.h>
  typedef OOFCanvas::CanvasImage CanvasImage;
  typedef OOFCanvas::CanvasImage NewCanvasImage;
%}

PYTHONEXPORTABLE(CanvasImage);


#endif // CANVASIMAGE_SWG
