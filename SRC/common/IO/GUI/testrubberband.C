#include <iostream>
#include <oofcanvasgui.h>

// This was compiled into its own library for debugging.  To resurrect
// it, search for and uncomment code containing testrubberband in the top
// CMakeLists.txt and the one in SRC/common/IO/GUI.

void testRubberBand() {
  std::cerr << "testRubberBand in debugrubberband.C" << std::endl;
  OOFCanvas::CanvasCurve *trail = new OOFCanvas::CanvasCurve();
  std::cerr << "testRubberBand: trail=" << trail << std::endl;
  std::cerr << "testRubberBand: calling setLineColor" << std::endl;
  trail->setLineColor(OOFCanvas::red);
  std::cerr << "testRubberBand: calling setLineWidthInPixels" << std::endl;
  trail->setLineWidthInPixels(17);
  std::cerr << "testRubberBand: done" << std::endl;
}
