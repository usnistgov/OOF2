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
    Color dashColor;
    bool line;
    bool lineWidthInPixels;
    bool dashLengthInPixels;
    bool dashColorSet;
    int dashOffset;
    std::vector<double> dash;
    Cairo::LineJoin lineJoin;
    Cairo::LineCap lineCap;
    double lineWidthInUserUnits(Cairo::RefPtr<Cairo::Context>) const;
    double lineWidthInUserUnits(const OffScreenCanvas*) const;
    std::vector<double> dashLengthInUserUnits(Cairo::RefPtr<Cairo::Context>)
      const;
    // stroke sets line color, width, and dash pattern and draws the
    // lines.
    void stroke(Cairo::RefPtr<Cairo::Context>) const; // virtual?
  public:
    CanvasShape(const Rectangle &rect) :
      CanvasItem(rect),
      lineWidth(0),
      lineColor(black),
      line(false),
      lineWidthInPixels(false),
      dashLengthInPixels(false),
      dashOffset(0),
      lineJoin(Cairo::LineJoin::LINE_JOIN_MITER),
      lineCap(Cairo::LineCap::LINE_CAP_ROUND)
    {}
    virtual ~CanvasShape() {}
    // Subclasses may need to redefine setLineWidth() and
    // setLineWidthInPixels() if it's necessary to recompute the
    // bounding box whenever the line width changes.
    virtual void setLineWidth(double);
    virtual void setLineWidthInPixels(double);  
    virtual void setLineColor(const Color&);
    void setLineJoin(Cairo::LineJoin lj) { lineJoin = lj; }
    void setLineCap(Cairo::LineCap lc) { lineCap = lc; }

    // Calling setDash() makes the lines dashed.  The args are a
    // vector of dash lengths, and an offset into that vector.
    // setDashInPixels() is the same, but the dash lengths are
    // interpreted in pixel units, not physical units.
    void setDash(const std::vector<double>&, int);
    void setDash(const std::vector<double>*, int); // ptr version for swig
    void setDash(double l); // same as setDash(std::vector<double>{l}, 0)
    void setDashInPixels(const std::vector<double>&, int);
    void setDashInPixels(const std::vector<double>*, int);
    void setDashInPixels(double l); // setDashInPixels(std::vector<double>{l},0)
    // If setDashColor() is called, the spaces between dashes will be
    // in the given color.  If it's not called, the spaces will be
    // blank.
    void setDashColor(const Color&);
    void unsetDashes();

    Color getLineColor() const { return lineColor; }
  };

  class CanvasFillableShape : public CanvasShape {
  protected:
    Color fillColor;
    bool fill;
    void fillAndStroke(Cairo::RefPtr<Cairo::Context>) const;
  public:
    CanvasFillableShape(const Rectangle &rect)
      : CanvasShape(rect),
	fillColor(black),
	fill(false)
    {
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
