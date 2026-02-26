// -*- C++ -*-

#include <iostream>
#include <oofcanvasgui.h>

// This can be compiled into its own library for debugging.  To enable
// it, search for and uncomment code containing testrubberband in the
// top CMakeLists.txt and the one in SRC/common/IO/GUI.

// OOF2 builds a shared library called liboof2testrubberband that
// contains only this function, and a python module called
// testrubberband to call it.  rbtest.py just imports the module and
// calls the function, which crashes because the wrong CanvasCurve
// methods are called, as if the vtable is incorrect.

// The same thing happens when the function is called from oof2.
// rbtest doesn't start oof2, it just uses the oof2 infrastructure to
// build and call the module.

// OTOH, CANVASTEST/canvastest calls a copy of the same testRubberBand
// function directly from C++ and it doesn't crash.  It creates a
// shared library, liboof2debug, containing the function and links to
// the library.

// OTOOH, canvastest2 links to liboof2testrubberband, and
// crashes. liboof2debug in CANVASTEST and liboof2testrubberband in
// OOF2 ought to be identical.

// RESOLVED, I think.  OOF2 files that includ oofcanvasgui.h need to
// be compiled with -DOOFCANVAS_USE_PYTHON or the PythonExportable
// classes in OOFCanvas won't be declared correctly in OOF2.

void testRubberBand() {
  std::cerr << "*** testRubberBand in testrubberband.C ***" << std::endl;
  OOFCanvas::CanvasCurve *trail = new OOFCanvas::CanvasCurve();
  std::cerr << "testRubberBand: trail=" << trail << std::endl;
  std::cerr << "testRubberBand: calling setLineColor" << std::endl;
  trail->setLineColor(OOFCanvas::red);
  std::cerr << "testRubberBand: calling setLineWidthInPixels" << std::endl;
  trail->setLineWidthInPixels(17);
  std::cerr << "testRubberBand: done" << std::endl;
}

