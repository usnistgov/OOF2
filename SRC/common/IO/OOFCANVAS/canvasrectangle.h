// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOF_CANVASRECTANGLE_H
#define OOF_CANVASRECTANGLE_H

#include "canvasshape.h"
#include "utility.h"

namespace OOFCanvas {
  class CanvasRectangle : public CanvasFillableShape {
  protected:
    double xmin, ymin, xmax, ymax;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const;
    virtual bool containsPoint(const CanvasBase*, const Coord&) const;
    Rectangle bbox0;
  public:
    CanvasRectangle(double xmin, double ymin, double xmax, double ymax);
    CanvasRectangle(const Coord&, const Coord&);
    virtual const std::string &classname() const;
    virtual void setLineWidth(double);
    friend std::ostream &operator<<(std::ostream &, const CanvasRectangle&);
    virtual std::string print() const;
  };

  std::ostream &operator<<(std::ostream &, const CanvasRectangle&);
};

#endif // OOF_CANVASRECTANGLE_H
