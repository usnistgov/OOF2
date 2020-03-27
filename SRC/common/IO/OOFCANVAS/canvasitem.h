// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFCANVASITEM_H
#define OOFCANVASITEM_H

#ifdef OOFCANVAS_USE_PYTHON
#include "common/pythonexportable.h"
#endif

namespace OOFCanvas {
  class CanvasItem;
  class PixelSized;
  class CanvasItemListIterator;
};

#include "canvas.h"
#include "canvaslayer.h"
#include "utility.h"
#include <cairomm/cairomm.h>

namespace OOFCanvas {

  class CanvasItem
#ifdef OOFCANVAS_USE_PYTHON
    : public PythonExportable<CanvasItem>
#endif 
  {
  protected:
    // Bounding box in user space.  Canvas items that can compute this
    // when they're constructed should do so.  Canvas items that can't
    // compute it without knowing the ppu should override
    // CanvasItem::boundingBox().
    Rectangle bbox;
    CanvasLayer *layer;
#ifdef DEBUG
    bool drawBBox;
    double bboxLineWidth;
    Color bboxColor;
#endif // DEBUG
  public:
    CanvasItem();
    virtual ~CanvasItem();
    virtual const std::string &modulename() const;

    // draw() is called by CanvasLayer::draw().  It calls drawItem(),
    // which must be defined in each CanvasItem subclass.
    void draw(Cairo::RefPtr<Cairo::Context>) const;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const = 0;

    // drawBoundingBox is a no-op unless DEBUG is defined.
    void drawBoundingBox(double, const Color&);

    // findBoundingBox() computes the bounding box if it's not already
    // known.  Subclasses that can't compute their bounding boxes
    // unless they know the ppu should override findBoundingBox() and
    // also be derived from PixelSized.  Subclasses that *can* compute
    // their bounding box without knowing ppu should do so in their
    // constructors and in any other methods that affect the bounding
    // box.
    virtual const Rectangle &findBoundingBox(double ppu) { return bbox; }
    // boundingBox() assumes that the bbox is already computed, and
    // just returns it.
    const Rectangle &boundingBox() const { return bbox; }

    virtual bool pixelSized() const { return false; }
    
    // containsPoint computes whether the given point in user
    // coordinates is on the item.  It's used to determine if a mouse
    // click selected the item.  It's called after bounding boxes have
    // been checked, so there's no need for it to check again.
    virtual bool containsPoint(const OffScreenCanvas*, const Coord&) const = 0;

    // Any routine that might change a CanvasItem's size after it's
    // been added to a CanvasLayer needs to call modified().
    void modified();

    virtual std::string print() const = 0;
    std::string *repr() const; // for python wrapping
    friend class CanvasLayer;
  };

  std::ostream &operator<<(std::ostream&, const CanvasItem&);

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // PixelSized is a mix-in subclass for CanvasItems which are
  // drawn differently in user-space units when the ppu (pixels per
  // unit) changes.  Anything whose dimensions are given in pixels
  // (aka device units) needs to be derived from PixelSized.
  
  class PixelSized {
  public:
    virtual bool pixelSized() const { return true; }

    // referencePoint() and pixelExtents() are used when computing the
    // ppu for Canvas::zoomToFill().  referencePoint() returns the
    // position in user space that the CanvasItem would occupy if the
    // ppu were infinite (ie, if the item's size were 0).
    // pixelExtents() gives the number of pixels that the object
    // extends from the referencePoint in each direction.
    virtual Coord referencePoint() const = 0;
    virtual void pixelExtents(double &left, double &right,
			      double &up, double &down) const = 0;

    // findBoundingBox() is used to get the bounding box when the ppu
    // is known, in order to compute the size of the Cairo::Surface or
    // the scroll limits.
    virtual const Rectangle &findBoundingBox(double ppu) = 0;
  };

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  class CanvasItemListIterator {
  private:
    std::vector<CanvasItem*>::iterator end;
    std::vector<CanvasItem*>::iterator iter;
  public:
    CanvasItemListIterator(std::vector<CanvasItem*> *list)
      : end(list->end()),
	iter(list->begin())
    {}
    bool done() { return iter == end; }
    CanvasItem *next_() { assert(!done()); return *iter++; }
  };
};

#endif // OOFCANVASITEM_H

