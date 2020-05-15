// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOF_CANVASSEGMENTS_H
#define OOF_CANVASSEGMENTS_H

#include "canvasshape.h"
#include "utility.h"

namespace OOFCanvas {
  class CanvasSegments : public CanvasShape {
  protected:
    std::vector<Segment> segments;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const;
    virtual bool containsPoint(const OffScreenCanvas*, const Coord&) const;
  public:
    CanvasSegments() : CanvasShape(Rectangle()) {}
    CanvasSegments(int n);
    virtual const std::string &classname() const;
    void addSegment(double x0, double y0, double x1, double y1);
    void addSegment(const Coord&, const Coord&);
    void addSegment(const Coord *a, const Coord *b) { addSegment(*a, *b); }
    void setLineWidth(double);
    virtual void pixelExtents(double&, double&, double&, double&) const;
    int size() const { return segments.size(); }
    friend std::ostream &operator<<(std::ostream &, const CanvasSegments&);
    virtual std::string print() const;
  };

  std::ostream &operator<<(std::ostream &, const CanvasSegments&);
};


#endif // OOF_CANVASSEGMENTS_H
