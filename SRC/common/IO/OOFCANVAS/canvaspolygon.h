// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOF_CANVASPOLYGON_H
#define OOF_CANVASPOLYGON_H

#include "canvasshape.h"
#include "utility.h"

namespace OOFCanvas {
  class CanvasPolygon : public CanvasFillableShape {
    std::vector<Coord> corners;
    Rectangle bbox0;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const;
    virtual bool containsPoint(const OffScreenCanvas*, const Coord&) const;
  public:
    CanvasPolygon();
    CanvasPolygon(int n);	// preallocates space for n corners
    CanvasPolygon(const std::vector<Coord>&);
    virtual const std::string &classname() const;
    void addPoint(const Coord &);
    void addPoint(const Coord* p) { addPoint(*p); }
    void addPoints(const std::vector<Coord>*);
    void setLineWidth(double);
    std::size_t size() const { return corners.size(); }
    virtual void pixelExtents(double&, double&, double&, double&) const;
    friend std::ostream &operator<<(std::ostream&, const CanvasPolygon&);
    virtual std::string print() const;

    int windingNumber(const Coord&) const;
  };

  std::ostream &operator<<(std::ostream&, const CanvasPolygon&);
};

#endif // OOF_CANVASPOLYGON_H
