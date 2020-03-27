// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFCANVASCIRCLE_H
#define OOFCANVASCIRCLE_H

#include "canvasshape.h"
#include "utility.h"

namespace OOFCanvas {
  class CanvasCircle : public CanvasFillableShape {
  protected:
    Coord center;
    double radius;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const;
    virtual bool containsPoint(const OffScreenCanvas*, const Coord&) const;
    void setup();
  public:
    CanvasCircle(double cx, double cy, double r);
    CanvasCircle(const Coord &c, double r);
    virtual const std::string &classname() const;
    virtual void setLineWidth(double);
    friend std::ostream &operator<<(std::ostream&, const CanvasCircle&);
    virtual std::string print() const;
  };
  std::ostream &operator<<(std::ostream&, const CanvasCircle&);

  class CanvasEllipse : public CanvasFillableShape {
  protected:
    Coord center;
    // The distances from the center to the edge are radiusX and
    // radiusY in the x and y directions, if the ellipse is not
    // rotated.  If angle!=0, the ellipse is rotated in the
    // counterclockwise direction around its center.
    double r0, r1;
    double angle;		// stored in radians, specified in degrees
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const;
    virtual bool containsPoint(const OffScreenCanvas*, const Coord&) const;
    void setup();
  public:
    CanvasEllipse(double cx, double cy, double r0, double r1, double angle);
    CanvasEllipse(const Coord &c, const Coord &r, double angle);
    virtual const std::string &classname() const;
    virtual void setLineWidth(double);
    friend std::ostream &operator<<(std::ostream&, const CanvasEllipse&);
    virtual std::string print() const;
  };
  std::ostream &operator<<(std::ostream&, const CanvasEllipse&);

  // A dot is a circle whose radius and lineWidth are given in pixels.
  // The size doesn't change when the window is zoomed.  The center is
  // given in user coordinates.
  
  class CanvasDot : public CanvasFillableShape, public PixelSized {
  protected:
    Coord center;
    double radius;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const;
    virtual bool containsPoint(const OffScreenCanvas*, const Coord&) const;
  public:
    CanvasDot(double cx, double cy, double r);
    CanvasDot(const Coord &c, double r);
    virtual const std::string &classname() const;
    friend std::ostream &operator<<(std::ostream&, const CanvasDot&);
    virtual std::string print() const;

    virtual const Rectangle &findBoundingBox(double ppu);
    virtual bool pixelSized() const { return true; }
    virtual Coord referencePoint() const { return center; }
    virtual void pixelExtents(double&, double&, double&, double&) const;
  };
  std::ostream &operator<<(std::ostream&, const CanvasDot&);

}; 				// namespace OOFCanvas

#endif // OOFCANVASCIRCLE_H
