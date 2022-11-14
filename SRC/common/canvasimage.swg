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

%module(package="ooflib.SWIG.common") canvasimage

// The CanvasImage and NewCanvasImage typemaps are for returning an
// OOFCanvas::CanvasImage from C++ to Python.  This requires some
// extra work because we can't use %import "oofcanvas/oofcanvas.swg",
// since that file isn't part of OOF2.  So these typemaps explicitly
// do what would have been done if swig had known about the
// OOFCanvas::CanvasImage class.

// These aren't in common/typemaps.swg in order to avoid including
// oofcanvas.h in all swig C++ output files.

%{
  #include <oofcanvas.h>
  typedef OOFCanvas::CanvasImage NewCanvasImage;
%}

%typemap(out) OOFCanvas::CanvasImage* {  
   // typemap(out) OOFCanvas::CanvasImage*
  $result = $1->pythonObject(false);
}

%typemap(newfree) OOFCanvas::CanvasImage* {
  // typemap(newfree) OOFCanvas::CanvasImage*
  delete $1;
 }

%typemap(out) NewOOFCanvasImage* {
   // typemap(out) NewOOFCanvasImage*
  $result = $1->pythonObject(true);
}

#endif // CANVASIMAGE_SWG
