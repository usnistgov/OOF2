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
  
  CanvasLayer::CanvasLayer(CanvasBase *canvas, const std::string &name) 
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
  
  void CanvasLayer::clear() {
    ICoord size(canvas->boundingBoxSizeInPixels());
    surface = Cairo::RefPtr<Cairo::ImageSurface>(
		 Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32,
					     size.x, size.y));
    cairo_t *ct = cairo_create(surface->cobj());
    context = Cairo::RefPtr<Cairo::Context>(new Cairo::Context(ct, true));
    context->set_matrix(canvas->getTransform());
    context->set_antialias(canvas->antialiasing);

// #ifdef DEBUG
//     {
//       double xmin, ymin, xmax, ymax;
//       context->get_clip_extents(xmin, ymin, xmax, ymax);
//       Rectangle user_clip(xmin, ymin, xmax, ymax);
//       context->user_to_device(xmin, ymin);
//       context->user_to_device(xmax, ymax);
//       Rectangle clip_extents(xmin, ymin, xmax, ymax);
//       std::cerr << "CanvasLayer::clear: " << this
// 		<< " transf=" << canvas->getTransform()
//     		<< " device clip_extents=" << clip_extents
// 		<< " user clip_extents=" << user_clip
//     		<< " surface=(" << surface->get_width() << ", "
//     		<< surface->get_height() << ")"
//     		<< std::endl;
//     }
// #endif // DEBUG
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
    clear();
  }

  Rectangle CanvasLayer::findBoundingBox(double ppu, bool newppu) {
    if(!dirty && !newppu && bbox.initialized())
      return bbox;
    bbox.clear();
    for(CanvasItem *item : items) {
      // Don't recompute bbox unless ppu has changed since it was
      // last computed.
      if(newppu || !item->boundingBox().initialized())
	item->findBoundingBox(ppu);
      bbox.swallow(item->boundingBox());
    }
    return bbox;
  }

  std::vector<CanvasItem*> CanvasLayer::pixelSizedItems() const {
    std::vector<CanvasItem*> result;
    for(CanvasItem *item : items) {
      if(item->pixelSized())
	result.push_back(item);
    }
    return result;
  }

  std::vector<CanvasItem*> CanvasLayer::userSizedItems() const {
    std::vector<CanvasItem*> result;
    for(CanvasItem *item : items) {
      if(!item->pixelSized())
	result.push_back(item);
    }
    return result;
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
      clear();
      // {
      // 	double xmin, ymin, xmax, ymax;
      // 	context->get_clip_extents(xmin, ymin, xmax, ymax);
      // 	Rectangle clip_extents(xmin, ymin, xmax, ymax);
      // 	std::cerr << "CanvasLayer::redraw: clip_extents=" << clip_extents
      // 		  << std::endl;
      // }
      
      for(CanvasItem *item : items) {
	item->draw(context);
      }
      dirty = false;
    }
  }

  // CanvasLayer::draw copies the layer's surface to the Canvas's
  // surface.  The layer's items have already been drawn on its
  // surface.
  void CanvasLayer::draw(Cairo::RefPtr<Cairo::Context> ctxt,
			 double hadj, double vadj)
    const
  {
    // hadj and vadj are pixel offsets, from the scroll bars.
    if(visible && !items.empty()) {
      ctxt->set_source(surface, -hadj, -vadj);

      // {
      // 	static int filecount = 0;
      // 	surface->write_to_png("layer_"+to_string(filecount++)+".png");
      // 	double xmin, ymin, xmax, ymax;
      // 	ctxt->get_clip_extents(xmin, ymin, xmax, ymax);
      // 	Rectangle clip_extents(xmin, ymin, xmax, ymax);
      // 	std::cerr << "CanvasLayer::draw: clip_extents=" << clip_extents
      // 		  << " filecount=" << filecount
      // 		  << std::endl;

      // }
      if(alpha == 1.0)
	ctxt->paint();
      else
	ctxt->paint_with_alpha(alpha);
    }
  }

  Coord CanvasLayer::pixel2user(const ICoord &pt) const {
    assert(context);
    double x = pt.x;
    double y = pt.y;
    context->device_to_user(x, y);
    return Coord(x, y);
  }

  ICoord CanvasLayer::user2pixel(const Coord &pt) const {
    assert(context);
    double x = pt.x;
    double y = pt.y;
    context->user_to_device(x, y);
    return ICoord(x, y);
  }

  // TODO: Do we want to support different scales in the x and y
  // directions?
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
      if(item->boundingBox().contains(pt) && item->containsPoint(canvas, pt)) {
	clickeditems.push_back(item);
      }
    }
  }

  void CanvasLayer::allItems(std::vector<CanvasItem*> &itemlist) const {
    itemlist.insert(itemlist.end(), items.begin(), items.end());
  }
};				// namespace OOFCanvas
