// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/ccolor.h"
#include "common/IO/GUI/rubberband.h"
#include "common/IO/GUI/gfxbrushstyle.h"

// Definitions of RubberBand subclass(es) that aren't defined in
// oofcanvas for some reason.

// The BrushRubberBand draws a curve along the centerline of the brush
// stroke and also outlines the brush.

BrushRubberBand::BrushRubberBand(GfxBrushStyle *brush)
  : style(brush),
    trail(nullptr)
{
  std::cerr << "BrushRubberBand::ctor: " << this << std::endl;
}

BrushRubberBand::~BrushRubberBand() {
  std::cerr << "BrushRubberBand::dtor: " << this << std::endl;
}

// Using gdb on the Linux VM
// % gdb --args python ~/bin/oof2 --debug --script canvasbug2.py --unthreaded
//   (gdb) break BrushRubberBand::start
//   (gdb) run
// Make a selection using the brush.
// After the break point, step though using n until trail is created.

// Incorrect functions are called in OOFCanvas::CanvasCurve* trail But
// vtbl seems to contain the correct pointers: in gdb, "info vtbl
// trail" prints the same addresses as "print trail->setLineColor",
// etc.

// Changing the order of the function declarations in CanvasShape
// changes which mistakes are made.  When the order is
// [setLineWidthInPixels, setLineColor, setLineWidth] in canvasshape.h

// on Linux setLineWidthInPixels calls classname, and setLineColor
// calls print.

// on Mac, setLineWidthInPixels calls ???, setLineColor calls print.

// When the order is [setLineColor, setLineWidth,
// setLineWidthInPixels],

// on Linux setLineWidthInPixels calls setLineColor, and setLineColor
// calls classname.

// on Mac, setLineWidthInPixels calls setLineColor (and crashes immediately).

// Adding dummy vfuncs to CanvasSegments that just call the base class
// methods doesn't change anything.  Order of vfuncs in CanvasSegments
// declaration doesn't matter -- presumably it doesn't affect the
// vtable.


void BrushRubberBand::start(OOFCanvas::CanvasLayer *lyr,
			    const OOFCanvas::Coord &pt)
{
  std::cerr << "BrushRubberBand::start: " << this << " " << pt << std::endl;
  KeyHolder kh(lock);
  OOFCanvas::RubberBand::start(lyr, pt);

  std::cerr << "BrushRubberBand::start: creating CanvasCurve for trail" << std::endl;
  trail = new OOFCanvas::CanvasCurve();

  // lineWidth and color are defined in the OOFCanvas::RubberBand base class.
  std::cerr << "BrushRubberBand::start: calling setLineWidthInPixels, trail=" << trail << " lineWidth=" << lineWidth << std::endl;
  trail->setLineWidthInPixels(lineWidth);
  std::cerr << "BrushRubberBand::start: calling setLineColor" << std::endl;
  trail->setLineColor(color);

  std::cerr << "BrushRubberBand::start: calling doDashes" << std::endl;
  doDashes(trail);
  std::cerr << "BrushRubberBand::start: calling addItem" << std::endl;
  layer->addItem(trail);
  std::cerr << "BrushRubberBand::start: calling style-start. style=" << style << std::endl;
  style->start(lyr, startPt);	// adds style's CanvasItem to the layer.
  std::cerr << "BrushRubberBand::start: calling addPoint, trail= " << trail << std::endl;
  trail->addPoint(pt);
  std::cerr << "BrushRubberBand::start: done" << std::endl;
}

void BrushRubberBand::setColor(const OOFCanvas::Color &c) {
  std::cerr << "BrushRubberBand::setColor: " << this << " " << c << std::endl;
  this->OOFCanvas::RubberBand::setColor(c);
}

void BrushRubberBand::stop() {
  OOFCanvas::RubberBand::stop();
  style->stop();
  trail = nullptr;
}

void BrushRubberBand::update(const OOFCanvas::Coord &pt) {
  KeyHolder kh(lock);
  RubberBand::update(pt);
  trail->addPoint(currentPt);
  style->update(currentPt);
}

std::string* BrushRubberBand::print() const {
  return new std::string("BrushRubberBand()");
}
