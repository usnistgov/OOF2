// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "canvas.h"
#include "canvasitem.h"
#include "canvaslayer.h"
#include <iostream>

namespace OOFCanvas {

  CanvasItem::CanvasItem()
    : layer(nullptr)
#ifdef DEBUG
    , drawBBox(false)
#endif // DEBUG
  {}
  
  CanvasItem::~CanvasItem() {}

  const std::string &CanvasItem::modulename() const {
    static const std::string name("oofcanvas");
    return name;
  }

  void CanvasItem::draw(Cairo::RefPtr<Cairo::Context> ctxt) const {
    ctxt->save();
    try {
      drawItem(ctxt);
#ifdef DEBUG
      if(drawBBox) {
	ctxt->restore();
	ctxt->save();
	ctxt->set_line_width(bboxLineWidth);
	bboxColor.set(ctxt);
	ctxt->move_to(bbox.xmin(), bbox.ymin());
	ctxt->line_to(bbox.xmax(), bbox.ymin());
	ctxt->line_to(bbox.xmax(), bbox.ymax());
	ctxt->line_to(bbox.xmin(), bbox.ymax());
	ctxt->close_path();
	ctxt->stroke();
      }
#endif // DEBUG

    }
    catch (...) {
      ctxt->restore();
      throw;
    }
    ctxt->restore();
  }

  void CanvasItem::modified() {
    if(layer != nullptr)
      layer->dirty = true;
  }

  void CanvasItem::drawBoundingBox(double lineWidth, const Color &color) {
#ifdef DEBUG
    bboxLineWidth = lineWidth;
    bboxColor = color;
    drawBBox = true;
#endif // DEBUG
  }

  std::ostream &operator<<(std::ostream &os, const CanvasItem &item) {
    // Call print() the in derived class, which calls operator<< for
    // the derived class.
    os << item.print();		
    return os;
  }

  std::string *CanvasItem::repr() const { // for calling from Python
    return new std::string(print());
  }
  
}; 				// namespace OOFCanvas
