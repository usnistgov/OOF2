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
    // bbox is the "bare" bounding box in user space coordinates.
    // This is the bounding box that the object would have if the
    // pixels were infinitesimal.  Canvas items that can compute this
    // when they're constructed should do so.  If they can't, they
    // need to redefine findBareBoundingBox().
    Rectangle bbox;
    CanvasLayer *layer;
#ifdef DEBUG
    bool drawBBox;
    double bboxLineWidth;
    Color bboxColor;
#endif // DEBUG
  public:
    CanvasItem(const Rectangle&); // arg is the bare bounding box
    virtual ~CanvasItem();
    virtual const std::string &modulename() const;

    // draw() is called by CanvasLayer::draw().  It calls drawItem(),
    // which must be defined in each CanvasItem subclass.
    void draw(Cairo::RefPtr<Cairo::Context>) const;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const = 0;

    // drawBoundingBox is a no-op unless DEBUG is defined.
    void drawBoundingBox(double, const Color&);

    // findBareBoundingBox() returns the what the item's bounding box
    // in user space units would be if the ppu were infinite.  That
    // is, it's the bounding box when so that any pixel-sized
    // components of the item have been shrunk to zero.  Most
    // subclasses can set CanvasItem::bbox in their constructors and
    // don't need to redefine findBareBoundingBox().
    virtual const Rectangle& findBareBoundingBox() const { return bbox; }

    // pixelExtents returns the distances, in pixel units, that the
    // object extends beyond its bare bounding box.  The default
    // implementation returns zeroes.
    virtual void pixelExtents(double &left, double &right,
			      double &up, double &down) const;
    

    // findBoundingBox() computes the actual bounding box, including
    // pixel-sized components, given a value for the pixels per unit.
    // The default implementation uses findBareBoundingBox and
    // pixelExtents.
    Rectangle findBoundingBox(double ppu) const;

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

