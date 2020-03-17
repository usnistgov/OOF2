// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFCANVASSHAPE_H
#define OOFCANVASSHAPE_H

#include "canvasitem.h"
#include "utility.h"

namespace OOFCanvas {
  class CanvasShape : public CanvasItem {
  protected:
    double lineWidth;
    Color lineColor;
    bool line;
    bool lineWidthInPixels;
    Cairo::LineJoin lineJoin;
    Cairo::LineCap lineCap;
    double lineWidthInUserUnits(Cairo::RefPtr<Cairo::Context>) const;
  public:
    CanvasShape() :
      lineWidth(0),
      lineColor(black),
      line(false),
      lineWidthInPixels(false),
      lineJoin(Cairo::LineJoin::LINE_JOIN_MITER),
      lineCap(Cairo::LineCap::LINE_CAP_ROUND)
    {}
    virtual ~CanvasShape() {}
    // Subclasses may need to redefine setLineWidth if it's necessary
    // to recompute the bounding box whenever the line width changes.
    virtual void setLineWidth(double);
    void setLineWidthInPixels() { lineWidthInPixels = true; }
    virtual void setLineColor(const Color&);
    void setLineJoin(Cairo::LineJoin lj) { lineJoin = lj; }
    void setLineCap(Cairo::LineCap lc) { lineCap = lc; }

    Color getLineColor() const { return lineColor; }
  };

  class CanvasFillableShape : public CanvasShape {
  protected:
    Color fillColor;
    bool fill;
    void fillAndStroke(Cairo::RefPtr<Cairo::Context>) const;
  public:
    CanvasFillableShape() : fillColor(black), fill(false) {
      line = false;
    }
    virtual ~CanvasFillableShape() {}
    virtual void setFillColor(const Color&); 
  };

  // These are for use from python.  See comment in oofcanvas.swg.
  extern const Cairo::LineCap lineCapButt, lineCapRound, lineCapSquare;
  extern const Cairo::LineJoin lineJoinMiter, lineJoinRound, lineJoinBevel;
  
};				// namespace OOFCanvas





#endif // OOFCANVASSHAPE_H
