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
    makeCairoObjs(size.x, size.y);
    context->set_matrix(canvas->getTransform());

// #ifdef DEBUG
//     {
//       double xmin, ymin, xmax, ymax;
//       context->get_clip_extents(xmin, ymin, xmax, ymax);
//       Rectangle user_clip(xmin, ymin, xmax, ymax);
//       context->user_to_device(xmin, ymin);
//       context->user_to_device(xmax, ymax);
//       Rectangle clip_extents(xmin, ymin, xmax, ymax);
//       std::cerr << "CanvasLayer::clear: " << name << " " << this
// 		<< "\ttransf=" << canvas->getTransform()
//     		<< " device clip_extents=" << clip_extents
// 		<< " user clip_extents=" << user_clip
//     		<< " surface=(" << surface->get_width() << ", "
//     		<< surface->get_height() << ")"
//     		<< std::endl;
//     }
// #endif // DEBUG
  }

  void CanvasLayer::makeCairoObjs(int x, int y) {
    surface = Cairo::RefPtr<Cairo::ImageSurface>(
      Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32, x, y));
    cairo_t *ct = cairo_create(surface->cobj());
    context = Cairo::RefPtr<Cairo::Context>(new Cairo::Context(ct, true));
    context->set_antialias(canvas->antialiasing);
  }

  void CanvasLayer::clear(const Color &color) {
    clear();
    context->set_source_rgb(color.red, color.green, color.blue);
    context->paint();
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
  // surface, via the Canvas' context, passed in as an argument.  The
  // layer's items have already been drawn on its surface.
  
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

  std::ostream &operator<<(std::ostream &os, const CanvasLayer &layer) {
    os << "CanvasLayer(\"" << layer.name << "\")";
    return os;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  WindowSizeCanvasLayer::WindowSizeCanvasLayer(CanvasBase *cb,
					       const std::string &name)
    : CanvasLayer(cb, name)
  {}

  void WindowSizeCanvasLayer::clear() {
    int size_x = canvas->widthInPixels();
    int size_y = canvas->heightInPixels();
    makeCairoObjs(size_x, size_y);
    // The Cairo::ImageSurface for the WindowSizeCanvasLayer is
    // aligned with the Canvas window, but it needs to have the same
    // ppu as the other CanvasLayers so that things drawn on it can
    // match things drawn on the other layers.  The offset can be
    // different because it can be compensated for when the
    // WindowSizeCanvasLayer is copied to the Canvas.  The offset must
    // put the upperleft corner of the ImageSurface to the lowerleft
    // corner of the window, and vice versa.

    double ppu = canvas->getPixelsPerUnit();
    int h = canvas->heightInPixels();
    int hadj = gtk_adjustment_get_value(canvas->getHAdjustment());
    int vadj = gtk_adjustment_get_value(canvas->getVAdjustment());
    
    Coord offset = ppu*canvas->pixel2user(ICoord(0, h)) + Coord(hadj, -vadj);
    Cairo::Matrix mat(ppu, 0.0, 0.0, -ppu, -offset.x, h+offset.y);
    context->set_matrix(mat);

  }

  void WindowSizeCanvasLayer::draw(Cairo::RefPtr<Cairo::Context> ctxt,
				   double hadj, double vadj)
    const
  {
    // ctxt is the Cairo::Context that was provided to the Gtk "draw"
    // event handler.  The coordinates in ctxt are pixel coordinates
    // (the transformation matrix is the identity matrix) but may have
    // a non-zero offset.

    if(visible && !items.empty()) {
      double ppu = canvas->getPixelsPerUnit();
      // The latter two arguments to set_source are the user
      // coordinates in the destination context of upper left corner
      // of the source surface.
      // Coord upleft(canvas->pixel2user(ICoord(hadj, vadj)));
      // ICoord origin(canvas->user2pixel(Coord(0, 0)));
      // ctxt->set_source(surface, upleft.x, upleft.y);

      Coord offset = (ICoord(hadj, vadj) + canvas->user2pixel(Coord(0, 0)))/ppu;
      ctxt->set_source(surface, offset.x, offset.y);
	
      if(alpha == 1.0)
	ctxt->paint();
      else
	ctxt->paint_with_alpha(alpha);
    }
  }

  // void WindowSizeCanvasLayer::redraw() { // Just for debugging
  //   if(dirty) {
  //     clear();
  //     context->set_source_rgb(0.2, 0.1, 0.1);
  //     context->paint_with_alpha(0.5);
  //     // double x0, y0, x1, y1;
  //     // context->get_clip_extents(x0, y0, x1, y1);
  //     // std::cerr << "WindowSizeCanvasLayer::redraw: clip extents = "
  //     // 		<< x0 << " " << y0 << " " << x1 << " " << y1 << std::endl;
  //     for(CanvasItem *item : items)
  // 	item->draw(context);
  //     dirty = false;
  //   }
  // }

  

  
};				// namespace OOFCanvas
