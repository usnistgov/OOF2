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
#include "canvaslayer.h"
#include "canvasitem.h"


namespace OOFCanvas {
  
  CanvasLayer::CanvasLayer(OffScreenCanvas *canvas, const std::string &name) 
    : canvas(canvas),
      alpha(1.0),
      visible(true),
      clickable(false),
      dirty(false),
      name(name)
  {}

  CanvasLayer::~CanvasLayer() {
    for(CanvasItem *item : items)
      delete item;
  }

  void CanvasLayer::destroy() {
    // CanvasLayer::destroy is provided as a slightly easier way to
    // delete a layer when a pointer to the Canvas isn't easily
    // available.  Canvas::deleteLayer calls the CanvasLayer
    // destructor.  Don't do anthing else here.
    canvas->deleteLayer(this);
  }

  void CanvasLayer::rebuild() {
    ICoord size(canvas->desiredBitmapSize());
    makeCairoObjs(size.x, size.y);
    context->set_matrix(canvas->getTransform());
    dirty = !empty();
  }

  void CanvasLayer::makeCairoObjs(int x, int y) {
    if(!surface || surface->get_width() != x || surface->get_height() != y) {
      surface = Cairo::RefPtr<Cairo::ImageSurface>(
		   Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32, x, y));
      cairo_t *ct = cairo_create(surface->cobj());
      context = Cairo::RefPtr<Cairo::Context>(new Cairo::Context(ct, true));
      dirty = true;
    }
    if(context->get_antialias() != canvas->antialiasing) {
      context->set_antialias(canvas->antialiasing);
      dirty = true;
    }
  }

  ICoord CanvasLayer::bitmapSize() const {
    if(surface)
      return ICoord(surface->get_width(), surface->get_height());
    return ICoord(0,0);
  }

  void CanvasLayer::clear() {
    if(surface) {
      context->save();
      context->set_operator(Cairo::OPERATOR_CLEAR);
      context->paint();
      context->restore();
      dirty = true;
    }
  }

  void CanvasLayer::clear(const Color &color) {
    context->save();
    context->set_source_rgb(color.red, color.green, color.blue);
    context->set_operator(Cairo::OPERATOR_SOURCE);
    context->paint();
    context->restore();
    dirty = true;
  }

  void CanvasLayer::writeToPNG(const std::string &filename) const {
    surface->write_to_png(filename);
  }

  void CanvasLayer::addItem(CanvasItem *item) {
    assert(item->layer == nullptr);
    item->layer = this;
    items.push_back(item);
    dirty = true;
  }

  void CanvasLayer::removeAllItems() {
    for(CanvasItem *item : items)
      delete item;
    items.clear();
    dirty = true;
  }

  Rectangle CanvasLayer::findBoundingBox(double ppu, bool newppu) {
    if(!dirty && !newppu && bbox.initialized())
      return bbox;
    bbox = findBoundingBox(ppu);
    return bbox;
  }

  Rectangle CanvasLayer::findBoundingBox(double ppu) const {
    Rectangle bb;
    for(CanvasItem *item : items)
      bb.swallow(item->findBoundingBox(ppu));
    return bb;
  }

  bool CanvasLayer::empty() const {
    return items.empty();
  }

  void CanvasLayer::show() {
    visible = true;
  }

  void CanvasLayer::hide() {
    visible = false;
  }

  // raiseBy and lowerBy aren't called "raise" and "lower" because
  // "raise" is a Python keyword.
  
  void CanvasLayer::raiseBy(int howfar) const {
    canvas->raiseLayer(canvas->layerNumber(this), howfar);
  };

  void CanvasLayer::lowerBy(int howfar) const {
    canvas->lowerLayer(canvas->layerNumber(this), howfar);
  }

  void CanvasLayer::raiseToTop() const {
    canvas->raiseLayerToTop(canvas->layerNumber(this));
  }

  void CanvasLayer::lowerToBottom() const {
    canvas->lowerLayerToBottom(canvas->layerNumber(this));
  }
  
  void CanvasLayer::redraw() {
    if(dirty) {
      rebuild();
      clear();		    // paints background color over everything
      redrawToContext(context);	// draws all items
      dirty = false;
    }
  }

  
  void CanvasLayer::redrawToContext(Cairo::RefPtr<Cairo::Context> ctxt) const {
    for(CanvasItem *item : items) {
      item->draw(ctxt);
    }
  }

  // CanvasLayer::draw copies the layer's surface to the Canvas's
  // surface, via the Canvas' context, which is passed in as an
  // argument.  The layer's items have already been drawn on its
  // surface.
  
  void CanvasLayer::draw(Cairo::RefPtr<Cairo::Context> ctxt,
			 double hadj, double vadj)
    const
  {
    // hadj and vadj are pixel offsets, from the scroll bars.
    if(visible && !items.empty()) {
      ctxt->set_source(surface, -hadj, -vadj);
      ctxt->paint_with_alpha(alpha);
    }
  }

  Coord CanvasLayer::pixel2user(const ICoord &pt) const {
    assert(context);
    Coord pp = pt + canvas->centerOffset;
    context->device_to_user(pp.x, pp.y);
    return pp;
  }

  Coord *CanvasLayer::pixel2user(double x, double y) const {
    // GdkEvents give pixel coords as floats, so this version is useful.
    assert(context);
    Coord *pp = new Coord(x, y);
    *pp += canvas->centerOffset;
    context->device_to_user(pp->x, pp->y);
    return pp;
  }

  ICoord CanvasLayer::user2pixel(const Coord &pt) const {
    assert(context);
    Coord pp = pt - canvas->centerOffset/canvas->getPixelsPerUnit();
    context->user_to_device(pp.x, pp.y);
    return ICoord(pp.x, pp.y);
  }

  double CanvasLayer::pixel2user(double d) const {
    assert(context);
    double dummy = 0;
    context->device_to_user_distance(d, dummy);
    return d;
  }

  double CanvasLayer::user2pixel(double d) const {
    assert(context);
    double dummy = 0;
    context->user_to_device_distance(d, dummy);
    return d;
  }

  void CanvasLayer::clickedItems(const Coord &pt,
				 std::vector<CanvasItem*> &clickeditems)
    const
  {
    // TODO? Use an R-tree for efficient search.
    for(CanvasItem *item : items) {
      if(item->findBoundingBox(canvas->getPixelsPerUnit()).contains(pt) &&
	 item->containsPoint(canvas, pt))
	{
	  clickeditems.push_back(item);
	}
    }
  }

  void CanvasLayer::allItems(std::vector<CanvasItem*> &itemlist) const {
    itemlist.insert(itemlist.end(), items.begin(), items.end());
  }

  std::ostream &operator<<(std::ostream &os, const CanvasLayer &layer) {
    os << "CanvasLayer(\"" << layer.name << "\")";
    return os;
  }

};				// namespace OOFCanvas
