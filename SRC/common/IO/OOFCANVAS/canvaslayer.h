// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFCANVASLAYER_H
#define OOFCANVASLAYER_H

#include <cairomm/cairomm.h>

namespace OOFCanvas {
  class GUICanvasBase;
  class OffScreenCanvas;
  class CanvasLayer;
};

#include "canvasitem.h"
#include "utility.h"

namespace OOFCanvas {
  
  class CanvasLayer {
  protected:
    Cairo::RefPtr<Cairo::ImageSurface> surface;
    Cairo::RefPtr<Cairo::Context> context;
    OffScreenCanvas *canvas;
    std::vector<CanvasItem*> items;
    double alpha;
    bool visible;
    bool clickable;
    bool dirty;		// Is the surface or bounding box out of date?
    Rectangle bbox;	// Cached bounding box of all contained items
    void makeCairoObjs(int, int);
  public:
    CanvasLayer(OffScreenCanvas*, const std::string&);
    virtual ~CanvasLayer();
    const std::string name;
    // clear() recreates the surface using the current size of the Canvas.
    virtual void clear();
    // clear(Color) is like clear(), but also sets a background color.
    void clear(const Color&);
    // addItem adds an item to the list and draws to the local
    // surface.  The CanvasLayer takes ownership of the item.
    void addItem(CanvasItem*);
    void removeAllItems();
    // redraw redraws all items to the local surface
    virtual void redraw();
    // draw() draws the surface to the given context (probably the Canvas)
    virtual void draw(Cairo::RefPtr<Cairo::Context>, double hadj, double vadj)
      const;

    void show();
    void hide();

    // Given the ppu, compute and cache the bounding box.
    Rectangle findBoundingBox(double, bool);

    // Get a list of all items whose size is given in device units.
    std::vector<CanvasItem*> pixelSizedItems() const;
    std::vector<CanvasItem*> userSizedItems() const;
    
    ICoord user2pixel(const Coord&) const;
    Coord pixel2user(const ICoord&) const;
    double user2pixel(double) const;
    double pixel2user(double) const;

    void setClickable(bool f) { clickable = f; }
    void clickedItems(const Coord&, std::vector<CanvasItem*>&) const;

    void setOpacity(double alph) { alpha = alph; }

    void allItems(std::vector<CanvasItem*>&) const;
    bool empty() const;

    void raiseBy(int) const;
    void lowerBy(int) const;
    void raiseToTop() const;
    void lowerToBottom() const;

    void writeToPNG(const std::string &) const;

    Cairo::RefPtr<Cairo::Context> getContext() const { return context; }
    
    friend class CanvasItem;
    friend class GUICanvasBase;
    friend class OffScreenCanvas;
  };

  std::ostream &operator<<(std::ostream&, const CanvasLayer&);

};

#endif // OOFCANVASLAYER_H

