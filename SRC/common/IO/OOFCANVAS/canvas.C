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
#include "canvasitem.h"
#include "canvaslayer.h"
#include <iostream>
#include <gdk/gdk.h>
#include <cassert>
#include <algorithm>

#ifdef PYTHON_OOFCANVAS
#include <pygobject.h>
#endif 

// TODO: If the layout size as computed from the bounding box is
// smaller than the window size in one or both directions, the image
// is drawn in the upper left corner of the window.  Can we center it?
	
// TODO: Save visible area or entire canvas to a file (pdf or png).

// TODO? Canvas::setMargin(double) to add some space when zooming to
// fill.  Not the same as the old OOFCanvas::set_margin.

namespace OOFCanvas {

  static double optimalPPU(double, double, double,
			   const std::vector<double>&,
			   const std::vector<double>&,
			   const std::vector<double>&);

  //=\\=//

  CanvasBase::CanvasBase(double ppu)
    : backingLayer(nullptr),
      transform(Cairo::identity_matrix()),
      ppu(ppu),			// pixels per unit
      bgColor(1.0, 1.0, 1.0),
      allowMotion(false),
      lastButton(0),
      mouseInside(false),
      buttonDown(false),
      antialiasing(Cairo::ANTIALIAS_DEFAULT)
  {
    // pixelwidth, pixelheight, and offset are set in realizeHandler.
    // They can't be initialized here because they depend on the
    // window size, which isn't known yet.

  }

  void CanvasBase::initSignals() {
    // gdk_window_set_events() is called in the "realize" event
    // handler.

    g_signal_connect(G_OBJECT(layout), "realize",
		     G_CALLBACK(CanvasBase::realizeCB), this);
    g_signal_connect(G_OBJECT(layout), "size-allocate",
		     G_CALLBACK(CanvasBase::allocateCB), this);

    g_signal_connect(G_OBJECT(layout), "button_press_event",
    		     G_CALLBACK(CanvasBase::buttonCB), this);
    g_signal_connect(G_OBJECT(layout), "button_release_event",
    		     G_CALLBACK(CanvasBase::buttonCB), this);
    g_signal_connect(G_OBJECT(layout), "motion_notify_event",
    		     G_CALLBACK(CanvasBase::motionCB), this);
    g_signal_connect(G_OBJECT(layout), "draw",
    		     G_CALLBACK(CanvasBase::drawCB), this);
    // g_signal_connect(G_OBJECT(layout), "leave_notify_event",
    // 		     G_CALLBACK(CanvasBase::crossingCB), this);
    // g_signal_connect(G_OBJECT(layout), "enter_notify_event",
    // 		     G_CALLBACK(CanvasBase::crossingCB), this);
    // g_signal_connect(G_OBJECT(layout), "focus_in_event",
    // 		     G_CALLBACK(CanvasBase::focusCB), this);
    // g_signal_connect(G_OBJECT(layout), "focus_out_event",
    // 		     G_CALLBACK(CanvasBase::focusCB), this);

  }
  
  void CanvasBase::destroy() {
    if(backingLayer)
      delete backingLayer;
    for(CanvasLayer *layer : layers)
      delete layer;
    layers.clear();
    // Signal handlers are automatically disconnected when the widget
    // is destroyed.
    gtk_widget_destroy(layout);
  }

  
  CanvasBase::~CanvasBase() {
    destroy();
  }

  CanvasLayer *CanvasBase::newLayer(const std::string &name) {
    CanvasLayer *layer = new CanvasLayer(this, name);
    layers.push_back(layer);
    return layer;
  }

  void CanvasBase::deleteLayer(CanvasLayer *layer) {
    auto iter = std::find(layers.begin(), layers.end(), layer);
    if(iter != layers.end())
      layers.erase(iter);
    delete layer;
  }

  void CanvasBase::clear() {
    for(CanvasLayer *layer : layers)
      delete layer;
    layers.clear();
    draw();
  }

  bool CanvasBase::empty() const {
    for(const CanvasLayer* layer : layers)
      if(!layer->empty())
	return false;
    return true;
  }

  int CanvasBase::layerNumber(const CanvasLayer *layer) const {
    for(int i=0; i<layers.size(); i++)
      if(layers[i] == layer)
	return i;
    throw "Layer number out of range."; 
  }

  CanvasLayer *CanvasBase::getLayer(const std::string &nm) const {
    std::cerr << "CanvasLayer::getLayer: nm=" << nm << std::endl;
    for(CanvasLayer *layer : layers)
      if(layer->name == nm)
	return layer;
    throw "Layer not found.";
  }

  void CanvasBase::raiseLayer(int which, int howfar) {
    assert(howfar >= 0);
    assert(which >= 0 && which < layers.size());
    CanvasLayer *moved = layers[which];
    int maxlayer = which + howfar; // highest layer that will be moved
    if(maxlayer >= layers.size())
      maxlayer = layers.size() - 1;
    for(int i=which; i < maxlayer; i++)
      layers[i] = layers[i+1];
    layers[maxlayer] = moved;
    draw();
  }
  
  void CanvasBase::lowerLayer(int which, int howfar) {
    std::cerr << "CanvasBase::lowerLayer: howfar=" << howfar << std::endl;
    assert(howfar >= 0);
    assert(which >= 0 && which < layers.size());
    CanvasLayer *moved = layers[which];
    int minlayer = which - howfar; // lowest layer that will be moved
    if(minlayer < 0)
      minlayer = 0;
    for(int i=which; i > minlayer; i--)
      layers[i] = layers[i-1];
    layers[minlayer] = moved;
    draw();
  }

  void CanvasBase::raiseLayerToTop(int which) {
    CanvasLayer *moved = layers[which];
    for(int i=which; i<layers.size()-1; i++)
      layers[i] = layers[i+1];
    layers[layers.size()-1] = moved;
    draw();
  }

  void CanvasBase::lowerLayerToBottom(int which) {
    CanvasLayer *moved = layers[which];
    for(int i=which; i>0; i--) 
      layers[i] = layers[i-1];
    layers[0] = moved;
    draw();
  }
  
  void CanvasBase::draw() {
    // This generates an draw event on the drawing area, which
    // causes CanvasBase::drawCB to be called.
    gtk_widget_queue_draw(layout);
  }

  void CanvasBase::redraw() {
    // Force all layers to be redrawn
    for(CanvasLayer *layer : layers)
      layer->dirty = true;
    draw();
  }

  void CanvasBase::setBackgroundColor(double r, double g, double b) {
    bgColor = Color(r, g, b);
  }

  void CanvasBase::antialias(bool aa) {
    if(aa && antialiasing != Cairo::ANTIALIAS_DEFAULT) {
      antialiasing = Cairo::ANTIALIAS_DEFAULT;
      redraw();
    }
    else if(!aa && antialiasing != Cairo::ANTIALIAS_NONE) {
      antialiasing = Cairo::ANTIALIAS_NONE;
      redraw();
    }
  }

  void CanvasBase::show() {
    gtk_widget_show(layout);
  }

  //=\\=//

  // CanvasBase::transform is a Cairo::Matrix that converts from user
  // coordinates to device coordinates in the CanvasLayers'
  // Cairo::Contexts. It is *not* the transform that maps the
  // CanvasLayers to the gtk Layout, nor does it have anything to do
  // with scrolling.

  void CanvasBase::setTransform(double scale) {

    // If no layers are dirty and ppu hasn't changed, don't do anything.
    bool newppu = (scale != ppu);
    bool layersChanged = false;
    if(!newppu) {
      for(CanvasLayer *layer : layers) {
	if(!layer->empty() && layer->dirty) {
	  layersChanged = true;
	  break;
	}
      }
    }
    if(!newppu && !layersChanged)
      return;
    
    // Find the bounding box of all drawn objects at the new scale
    Rectangle bbox;
    for(CanvasLayer *layer : layers) {
      if(!layer->empty()) {
	Rectangle rect = layer->findBoundingBox(scale, newppu);
	if(rect.initialized())
	  bbox.swallow(rect);
      }
    }
    
    if(!bbox.initialized()) {
      // Nothing is drawn.
      transform = Cairo::identity_matrix();
    }
    else {
      if(newppu  || !boundingBox.initialized() || bbox != boundingBox) {
	boundingBox = bbox;
	ppu = scale;
	guint w = ppu*boundingBox.width();
	guint h = ppu*boundingBox.height();

	gtk_layout_set_size(GTK_LAYOUT(layout), w, h);
	Coord offset = ppu*boundingBox.lowerLeft();
	transform = Cairo::Matrix(ppu, 0, 0, -ppu, -offset.x, h+offset.y);

	// Force layers to be redrawn
	for(CanvasLayer *layer : layers) {
	  layer->dirty = true; 
	}
      }
    }
    backingLayer->clear();

  } // CanvasBase::setTransform

  //=\\=//

  void CanvasBase::zoomToFill() {
    // This is tricky, because some objects have fixed sizes in device
    // units, and therefore change their size in user units when the
    // ppu is changed.  It's not possible to simply compute the
    // bounding box in user units and scale it to fit the window.

    std::vector<CanvasItem*> pixelSizedItems;
    for(CanvasLayer *layer : layers) {
      std::vector<CanvasItem*> layeritems(layer->pixelSizedItems());
      if(!layeritems.empty())
	pixelSizedItems.insert(pixelSizedItems.end(),
			       layeritems.begin(), layeritems.end());
    }

    double ppu_x = -1;	// to be determined
    double ppu_y = -1;	// to be determined
    
    if(pixelSizedItems.empty()) {
      // Compute ppu in the x and y directions, and choose the smaller
      // one, so that the image fits in both directions.

      // TODO: This assumes that boundingbox has already been
      // computed, which is only done when setTransform is called.  Is
      // that a bad assumption?
      assert(boundingBox.initialized());
      double fudge = 0.97;	// a little extra space
      ppu_x = fudge*widthInPixels()/boundingBox.width();
      ppu_y = fudge*heightInPixels()/boundingBox.height();
    }
    
    else {
      // The Canvas contains some CanvasItems whose user-space size
      // changes when the ppu changes.
      Rectangle bboxInf;   // user-space bbox if the ppu were infinite
      unsigned int nPixSized = pixelSizedItems.size();
      // pixel extents of each item from its reference point
      std::vector<double> pLeft(nPixSized), pRight(nPixSized);
      std::vector<double> pUp(nPixSized), pDown(nPixSized);
      // user coordinates of the reference points of each object
      std::vector<double> xRef(nPixSized), yRef(nPixSized);
      // Get the bounding box of the items defined in user coordinates.
      int nUserSizedItems = 0;
      for(CanvasLayer *layer : layers) {
	std::vector<CanvasItem*> items(layer->userSizedItems());
	nUserSizedItems += items.size();
	for(CanvasItem *item : items)
	  bboxInf.swallow(item->boundingBox());
      }
      // Expand the bounding box to include the reference points of
      // the items defined in device coordinates, and accumulate some
      // additional data while looping.
      for(unsigned int i=0; i<nPixSized; i++) {
	PixelSized *psitem = dynamic_cast<PixelSized*>(pixelSizedItems[i]);
	assert(psitem != nullptr);
	Coord refPt = psitem->referencePoint();
	xRef[i] = refPt.x;
	yRef[i] = refPt.y;
	bboxInf.swallow(refPt);
	psitem->pixelExtents(pLeft[i], pRight[i], pUp[i], pDown[i]);
      }

      // bboxInf is now the smallest possible bounding box.  As ppu
      // decreases from infinity, some of the CanvasItems will grow,
      // and may protrude through the sides of bboxInf.  We need to
      // find the smallest ppu such that the expanded bbox fits inside
      // a rectangle of (size widthInPixels(), heightInPixels()).
      
      // The distance in device units that an item i protrudes through
      // the right side of bboxInf is
      // max( pRight[i]-ppu*(bboxInf.xmax()-xRef[i]), 0)
      // On the left side, it's
      // max( pLeft[i]-ppu*(xRef[i]-bboxInf.xmin()), 0)

      // The total width of the window is ppu*bboxInf.width() plus the
      // max (over i) or the two protrusions.  The left and right
      // maxes can occur for different i.  The total width is a
      // piecewise-linear function of ppu.

      if(bboxInf.width() == 0.0) {
	// There are no CanvasItems with non-zero user-space size, and
	// all the CanvasItems with sizes in pixels have the same
	// reference point.
	ppu_x = std::numeric_limits<double>::max();
      }
      else {
	ppu_x = optimalPPU(widthInPixels(), bboxInf.xmin(), bboxInf.xmax(),
			   pLeft, pRight, xRef);
      }

      if(bboxInf.height() == 0.0) {
	ppu_y = std::numeric_limits<double>::max();
      }
      else {
	ppu_y = optimalPPU(heightInPixels(), bboxInf.ymin(), bboxInf.ymax(),
			   pDown, pUp, yRef);
      }
      
    } // end if there are some pixel-sized canvas items
    
    // Pick the smaller of ppu_x and ppu_y, so that the entire image
    // is visible in both directions.
    double newppu = ppu_x < ppu_y ? ppu_x : ppu_y;
    if(newppu < std::numeric_limits<double>::max()) {
      setTransform(newppu);
    }
    else {
      // No ppu was established.  This can only happen if all of the
      // CanvasItems have sizes set in device units and all of their
      // reference points coincide.  In that case, the user units are
      // irrelevant, so any ppu will do.
      setTransform(1.0);
    }
      // Put the center of the scaled image in the center of the window.
    center();
  }

  // pixSize computes the size in pixels that the window would have to
  // be at the given ppu in order to contain a bounding box from bbmin
  // to bbmax and a bunch of pixel-sized items at positions refPt with
  // pixel extents pLo and pHi.

  double pixSize(double ppu,
		 double bbmin, double bbmax,
		 const std::vector<double> &pLo,
		 const std::vector<double> &pHi,
		 const std::vector<double> &refPt)
  {
    // * protrudeLow is the maximum distance in pixels that the
    //   pixel-sized items protrude on the low end of the bounding
    //   box.
    // * refPt[i] is the refernce point for the i^th item, in user
    //   units.
    // * pLo[i] is the distance in pixels that the i^th item extends
    //   below its reference point.

    // The total size is
    //    ppu*(bbmax - bbmin)
    //    + max(pHi_i - ppu*(bbmax-refPt_i))
    //    + max(pLo_i - ppu*(refPt_i - bbmin))
    // where the maxes are over i, and truncated below at 0.
    
    double protrudeLow = 0.0;
    double protrudeHigh = 0.0;
    for(unsigned int i=0; i<pLo.size(); i++) {
      double p = pLo[i] - (refPt[i] - bbmin)*ppu;
      if(p > protrudeLow)
	protrudeLow = p;
      p = pHi[i] - (bbmax - refPt[i])*ppu;
      if(p > protrudeHigh)
	protrudeHigh = p;
    }
    return ppu*(bbmax-bbmin) + protrudeHigh + protrudeLow;
  }
    
  // optimalPPU computes the ppu in one direction for zoomToFill()
  // when the Canvas contains CanvasItems whose size is given in
  // pixels.

  double optimalPPU(double totalPixels,		// size of window, device coords
		    double bbmin, double bbmax, // minimal bounding box, user
		    const std::vector<double> &pLo, // pixel extents
		    const std::vector<double> &pHi, // pixel extents
		    const std::vector<double> &refPt) // item coords, user
  {
    // The span (bbmin, bbmax) contains CanvasItems at user-space
    // reference points refPt[i].  The items extend below refPt[i] by
    // pLo[i] pixels, and above by pHi[i] pixels.

    // The optimal ppu is the one for which pixSize() returns
    // totalPixels.  pixSize() is a piecewise linear function of ppu,
    // so we could find all the pieces and solve for ppu in each
    // piece.
    
    // Find the ppu values at which pixSize(ppu) might change slope.
    // These are the points at which a canvas item starts to protrude
    // through the original bounding box, or where two items (with
    // different refPts) protrude equally.

    std::vector<double> criticalPPUs(1, 0.0);
    unsigned int n = pLo.size();
    for(unsigned int i=0; i<n; i++) {
      if(refPt[i] < bbmax) {
	// ppu at which item i extends up to bbmax exactly
	double ppui = pHi[i]/(bbmax - refPt[i]);
	criticalPPUs.push_back(ppui);
	// ppus at which item i extends up as far as item j
	for(unsigned int j=0; j<i; j++) {
	  double ppuj = pHi[j]/(bbmax - refPt[j]);
	  if((ppuj < ppui && pHi[j] > pHi[i]) ||
	     (ppuj > ppui && pHi[j] < pHi[i])) {
	    double ppuij = ppui*ppuj*(pHi[i] - pHi[j]) /
	      (pHi[i]*ppuj - pHi[j] - ppui);
	    criticalPPUs.push_back(ppuij);
	  }
	} // loop over items j != i
      }	// end if item i has a refPt below bbmax

      if(refPt[i] > bbmin) {
	// ppu at which item i extends down to bbmin exactly
	double ppui = pLo[i]/(refPt[i] - bbmin);
	criticalPPUs.push_back(ppui);
	// ppus at which item i extends down as far as item j
	for(unsigned int j=0; j<i; j++) {
	  double ppuj = pLo[j]/(refPt[j] - bbmin);
	  if((ppuj < ppui && pLo[j] > pLo[i]) ||
	     (ppuj > ppui && pLo[j] < pLo[i])) {
	    double ppuij = ppui*ppuj*(pLo[i] - pLo[j]) /
	      (pLo[i]*ppuj - pLo[j] - ppui);
	    criticalPPUs.push_back(ppuij);
	  } // end if one item actually overtakes the other
	} // loop over items j!=i
      }	// end if item i has a refPt above bbmin
    } // loop over fixed size items i

    std::sort(criticalPPUs.begin(), criticalPPUs.end());

    // Examine each interval between slope changes and find the ppu
    // that gives the desired total number of pixels.  There can be
    // more than one, but we want the largest, so just keep track of
    // it.
    double ppuMax = 0;		// maximum ppu found that gives a solution
    for(unsigned int i=0; i<criticalPPUs.size()-1; i++) {
      double ppu0 = criticalPPUs[i];
      double ppu1 = criticalPPUs[i+1];
      double pix0 = pixSize(ppu0, bbmin, bbmax, pLo, pHi, refPt);
      double pix1 = pixSize(ppu1, bbmin, bbmax, pLo, pHi, refPt);
      if((pix0 - totalPixels)*(pix1-totalPixels) <= 0) {
	// ppu at which this segment gives the desired number of pixels
	double ppu = ppu0 + (totalPixels - pix0)*(ppu1 - ppu0)/(pix1 - pix0);
	if(ppu >= ppu0 && ppu <= ppu1 && ppu > ppuMax)
	  ppuMax = ppu;
      }
    }
    // The segment from the largest crossing to ppu=infinity has to be
    // handled separately.
    double ppu0 = criticalPPUs.back();
    double pix0 = pixSize(ppu0, bbmin, bbmax, pLo, pHi, refPt);
    if(pix0 <= totalPixels) {
      double offset = pix0 - ppu0*(bbmax - bbmin);
      double ppu = (totalPixels - offset)/(bbmax - bbmin);
      if(ppu > ppuMax)
	ppuMax = ppu;
    }
    return ppuMax;
  }
    
  static void centerAdj(GtkAdjustment *adj) {
    // Set a Gtk Adjustment to its center value.
    double l = gtk_adjustment_get_lower(adj);
    double u = gtk_adjustment_get_upper(adj);
    double p = gtk_adjustment_get_page_size(adj);
    double v = l + 0.5*(u - p  - l);
    gtk_adjustment_set_value(adj, v);
  }
  
  void CanvasBase::center() {
    // Move the center of the image to the center of the window,
    // without changing scale.
    centerAdj(getHAdjustment());
    centerAdj(getVAdjustment());
    draw();
  }

  void CanvasBase::zoomAbout(double factor, const Coord &fixedPt) {
    // Zoom by factor while keeping the device-space coordinates of
    // the user-space fixedPt fixed.
    // The visible window size is fixed, but the virtual window isn't.

    GtkAdjustment *hadj = getHAdjustment();
    GtkAdjustment *vadj = getVAdjustment();

    // Find the device coordinates of the fixedPt
    ICoord devPt = user2pixel(fixedPt);
    double xadj = gtk_adjustment_get_value(hadj);
    double yadj = gtk_adjustment_get_value(vadj);
    int xdev = devPt.x - xadj;
    int ydev = devPt.y - yadj;

    // Zoom
    setTransform(factor*ppu);

    // Adjust scrollbars so that fixedPt is back where it was in
    // device space.
    devPt = user2pixel(fixedPt);
    xadj = devPt.x - xdev;
    yadj = devPt.y - ydev;
    gtk_adjustment_set_value(hadj, xadj);
    gtk_adjustment_set_value(vadj, yadj);

    draw();
  }
  
  void CanvasBase::zoom(double factor) {
    int w2 = 0.5*widthInPixels();
    int h2 = 0.5*heightInPixels();
    double xadj = gtk_adjustment_get_value(getHAdjustment());
    double yadj = gtk_adjustment_get_value(getVAdjustment());
    Coord cntr = pixel2user(ICoord(xadj + w2, yadj + w2));
    zoomAbout(factor, cntr);
  }

  void CanvasBase::zoomAbout(double x, double y, double factor) {
    zoomAbout(factor, Coord(x, y));
  };

  ICoord CanvasBase::user2pixel(const Coord &pt) const {
    assert(backingLayer != nullptr);
    return backingLayer->user2pixel(pt);
  }

  Coord CanvasBase::pixel2user(const ICoord &pt) const {
    assert(backingLayer != nullptr);
    return backingLayer->pixel2user(pt);
  }

  double CanvasBase::user2pixel(double d) const {
    assert(backingLayer != nullptr);
    return backingLayer->user2pixel(d);
  }

  double CanvasBase::pixel2user(double d) const {
    assert(backingLayer != nullptr);
    return backingLayer->pixel2user(d);
  }

  int CanvasBase::heightInPixels() const {
    return gtk_widget_get_allocated_height(layout);
  }

  int CanvasBase::widthInPixels() const {
    return gtk_widget_get_allocated_width(layout);
  }

  ICoord CanvasBase::layoutSize() const {
    guint w, h;
    gtk_layout_get_size(GTK_LAYOUT(layout), &w, &h);
    return ICoord(w, h);
  }

  ICoord CanvasBase::boundingBoxSizeInPixels() const {
    return ICoord(ppu*boundingBox.width(), ppu*boundingBox.height());
  }

  GtkAdjustment *CanvasBase::getHAdjustment() const {
    return gtk_scrollable_get_hadjustment(GTK_SCROLLABLE(layout));
  }

  GtkAdjustment *CanvasBase::getVAdjustment() const {
    return gtk_scrollable_get_vadjustment(GTK_SCROLLABLE(layout));
  }

  //=\\=//

  // realizeCB is called once, when the Canvas's gtk object is
  // "realized", whatever that means.  It's not as if the Canvas has
  // any existence other than as a pattern of bits.

  void CanvasBase::realizeCB(GtkWidget*, gpointer data) {
    ((Canvas*) data)->realizeHandler();
  }

  void CanvasBase::realizeHandler() {
    // Set the initial size of the virtual window to be the same as
    // the size the actual window.
    gtk_layout_set_size(GTK_LAYOUT(layout), widthInPixels(), heightInPixels());
    
    GdkWindow *bin_window = gtk_layout_get_bin_window(GTK_LAYOUT(layout));

    gdk_window_set_events(bin_window,
			  (GdkEventMask) (gdk_window_get_events(bin_window)
					  | GDK_EXPOSURE_MASK
					  | GDK_BUTTON_PRESS_MASK
					  | GDK_BUTTON_RELEASE_MASK
					  | GDK_POINTER_MOTION_MASK
					  | GDK_KEY_PRESS_MASK
					  | GDK_KEY_RELEASE_MASK
					  | GDK_ENTER_NOTIFY_MASK
					  | GDK_LEAVE_NOTIFY_MASK
					  | GDK_FOCUS_CHANGE_MASK
					  ));
    // The backingLayer is a CanvasLayer that exists just so that the
    // canvas transforms can be defined even when nothing is
    // drawn. This allows pixel2user and user2pixel to work in all
    // circumstances. The backingLayer can't be created until the
    // layout is created, however, because it needs to know the window
    // size.  So it's done here instead of in the Canvas constructor.
    backingLayer = new CanvasLayer(this, "<backinglayer>");
    backingLayer->setClickable(false);
  }

  //=\\=//

  void CanvasBase::allocateCB(GtkWidget*, GdkRectangle*, gpointer data) {
    ((Canvas*) data)->allocateHandler();
  }

  void CanvasBase::allocateHandler() {
    // Called whenever the widget size changes.
    if(backingLayer)
      backingLayer->clear();	// forces it to resize itself
  }
  
   //=\\=//  
  
  // TODO: Why is drawCB called so often?  This only happens on a Mac.
  // If the canvas's app has mouse focus, then drawCB is called
  // whenever the mouse crosses into or out of a Mac terminal window,
  // but not an emacs window.  The scrollbar in the canvas changes
  // color when this happens.

  void CanvasBase::drawCB(GtkWidget*, Cairo::Context::cobject *ctxt,
			  gpointer data)
  {
    ((Canvas*) data)->drawHandler(
	  Cairo::RefPtr<Cairo::Context>(new Cairo::Context(ctxt, false)));
  }

  void CanvasBase::drawHandler(Cairo::RefPtr<Cairo::Context> context) {
    // From the gtk2->gtk3 conversion notes: "The cairo context is
    // being set up so that the origin at (0, 0) coincides with the
    // upper left corner of the widget, and is properly clipped."
    // (https://developer.gnome.org/gtk3/stable/ch26s02.html)

    // static int count = 0;
    // std::cerr << "CanvasBase::drawHandler: " << count++ << " " 
    // 	      << allItems().size() << std::endl;


    context->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
    context->paint();

    // TODO? Extract the clipping region from the context using
    // Cairo::Context::get_clip_extents, and only redraw CanvasItems
    // whose bounding boxes intersect the clipping region.  If the
    // items are stored in an R-tree this might be fast.

    // {
    //   double xmin, ymin, xmax, ymax;
    //   context->get_clip_extents(xmin, ymin, xmax, ymax);
    //   Rectangle clip_extents(xmin, ymin, xmax, ymax);
    //   std::cerr << "CanvasBase::drawHandler: clip_extents=" << clip_extents
    // 		<< std::endl;
    // }

    double hadj = gtk_adjustment_get_value(getHAdjustment());
    double vadj = gtk_adjustment_get_value(getVAdjustment());

    setTransform(ppu);
    
    for(CanvasLayer *layer : layers) {
      layer->redraw();			// only redraws dirty layers
      layer->draw(context, hadj, vadj); // copies layers to canvas
    }
  }

  //=\\=//

  void CanvasBase::buttonCB(GtkWidget*, GdkEventButton *event, gpointer data) {
    ((Canvas*) data)->mouseButtonHandler(event);
  }

  void CanvasBase::mouseButtonHandler(GdkEventButton *event) {
    std::string eventtype;
    if(event->type == GDK_BUTTON_PRESS) {
      eventtype = "down";
      buttonDown = true;
    }
    else {
      eventtype = "up";
      buttonDown = false;
    }
    lastButton = event->button;

    doCallback(eventtype, event->x, event->y, lastButton,
	       event->state & GDK_SHIFT_MASK,   
	       event->state & GDK_CONTROL_MASK);
    allowMotion = (eventtype == "down");
  }

  //=\\=//

  // void CanvasBase::crossingCB(GtkWidget*, GdkEventCrossing *event,
  // 			      gpointer data)
  // {
  //   ((Canvas*) data)->crossingEventHandler(event);
  // }

  // void CanvasBase::crossingEventHandler(GdkEventCrossing *event) {
  //   std::cerr << "CanvasBase::crossingEventHandler: " << event->type
  // 	      << std::endl;
  //   if(event->type == GDK_ENTER_NOTIFY)
  //     mouseInside = true;
  //   else if(event->type == GDK_LEAVE_NOTIFY)
  //     mouseInside = false;
  // }

  // void CanvasBase::focusCB(GtkWidget*, GdkEventFocus *event, gpointer data) {
  //   std::cerr << "CanvasBase::focusCB: " << event->in << std::endl;
  // }

  //=\\=//
  
  void CanvasBase::motionCB(GtkWidget*, GdkEventMotion *event, gpointer data) {
    ((Canvas*) data)->mouseMotionHandler(event);
  }

  void CanvasBase::mouseMotionHandler(GdkEventMotion *event) {
    if(!allowMotion)
      return;
    doCallback("move", event->x, event->y, lastButton,
	       event->state & GDK_SHIFT_MASK,
	       event->state & GDK_CONTROL_MASK);
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Routines that can be called from a mouse callback to retrieve the
  // CanvasItem(s) at a given user coordinate.
  
  std::vector<CanvasItem*> CanvasBase::clickedItems(double x, double y) const {
    Coord where(x,y);
    std::vector<CanvasItem*> items;
    for(const CanvasLayer *layer : layers) {
      if(layer->clickable) 
	layer->clickedItems(where, items);
    }
    return items;
  }

  std::vector<CanvasItem*> CanvasBase::allItems() const {
    std::vector<CanvasItem*> items;
    for(const CanvasLayer *layer : layers)
      layer->allItems(items);
    return items;
  }

  // The _new versions of clickedItems and allItems return their
  // results in a new vector, because swig works better that way.  If
  // we instead swig the above versions, without using new, swig will
  // make an extra copy of the vectors.
  std::vector<CanvasItem*> *CanvasBase::clickedItems_new(double x, double y)
    const
  {
    Coord where(x,y);
    std::vector<CanvasItem*> *items = new std::vector<CanvasItem*>;
    for(const CanvasLayer *layer : layers) 
      if(layer->clickable)
	layer->clickedItems(where, *items);
    return items;
  }

  std::vector<CanvasItem*> *CanvasBase::allItems_new() const {
    std::vector<CanvasItem*> *items = new std::vector<CanvasItem*>;
    for(const CanvasLayer *layer : layers)
      layer->allItems(*items);
    return items;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Derived class to be used when the Canvas is created and used in
  // C++.  The mouse callback must be a C++ function.  A gtk layout is
  // created by the constructor and can be retrieved by calling
  // Canvas::gtk().

  Canvas::Canvas(double ppu)
    : CanvasBase(ppu),
      mouseCallback(nullptr),
      mouseCallbackData(nullptr)
  {
    layout = gtk_layout_new(NULL, NULL);
    initSignals();
  }

  void Canvas::destroy() {
    CanvasBase::destroy();
  }


  void Canvas::setMouseCallback(MouseCallback mcb, void *data) {
    mouseCallback = mcb;
    mouseCallbackData = data;
  }
  
  void Canvas::doCallback(const std::string &eventtype,
			  int x, int y, int button, bool shift, bool ctrl)
    const
  {
    ICoord pixel(x, y);
    Coord userpt(pixel2user(pixel));
    if(mouseCallback != nullptr)
      (*mouseCallback)(eventtype, userpt.x, userpt.y, button, shift, ctrl);
  }
  
  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Derived class to be used when the Canvas is created in Python.  A
  // Gtk.Layout must be created and passed in to the constructor.  The
  // mouse callback must be a Python function.  All other public
  // methods are available in C++ and Python.

#ifdef PYTHON_OOFCANVAS

  // TODO: Do we really need to store pyCanvas?  It's not explicitly
  // used after the constructor finishes, but perhaps storing a
  // reference to it is important.  It's probably not harmful, at
  // least.

  CanvasPython::CanvasPython(PyObject *pycan, double ppu)
    : CanvasBase(ppu),
      pyCanvas(pycan),
      mouseCallback(nullptr),
      mouseCallbackData(Py_None),
      resizeCallback(nullptr),
      resizeCallbackData(Py_None)
  {
    PyGILState_STATE pystate = PyGILState_Ensure();
    try {
      // The initial value of the data to be passed to the python mouse
      // callback is None. Since we're storing it, we need to incref it.
      Py_INCREF(mouseCallbackData);
      Py_INCREF(resizeCallbackData);
      Py_INCREF(pyCanvas);

      // Extract the GtkLayout from the passed-in PyObject*, which
      // is a Gtk.Layout.
      PyObject *capsule = PyObject_GetAttrString(pyCanvas, "__gpointer__");
      if(!PyCapsule_CheckExact(capsule)) {
	throw "Canvas constructor: capsule is not a PyCapsule!";
      }
      const char *capsuleName = PyCapsule_GetName(capsule);
      if(!PyCapsule_IsValid(capsule, capsuleName)) {
	throw "Canvas constructor: capsule is not a valid pyCapsule!";
      }
      layout = (GtkWidget*) PyCapsule_GetPointer(capsule, capsuleName);
      g_object_ref(layout);
      Py_DECREF(capsule);
    }
    catch(...) {
      PyGILState_Release(pystate);
      throw;
    }
    PyGILState_Release(pystate);

    initSignals();
  }

  void CanvasPython::destroy() {
    Py_DECREF(pyCanvas);
    g_object_unref(layout);
    CanvasBase::destroy();
  }

  void CanvasPython::doCallback(const std::string &eventtype,
			  int x, int y, int button, bool shift, bool ctrl)
    const
  {
    ICoord pixel(x, y);
    Coord userpt(pixel2user(pixel));

    if(mouseCallback != nullptr) {
      PyGILState_STATE pystate = PyGILState_Ensure();
      try {
	PyObject *args = Py_BuildValue("sddiiiO", eventtype.c_str(),
				       userpt.x, userpt.y,
				       button, shift, ctrl,
				       mouseCallbackData);
	PyObject *result = PyObject_CallObject(mouseCallback, args);
	if(result == nullptr) {
	  PyErr_Print();
	  PyErr_Clear();
	}
	Py_XDECREF(args);
	Py_XDECREF(result);
      }
      catch (...) {
	PyGILState_Release(pystate);
	throw;
      }
      PyGILState_Release(pystate);
    }

  }
  
  void CanvasPython::setMouseCallback(PyObject *pymcb, PyObject *pydata) {
    PyGILState_STATE pystate = PyGILState_Ensure();
    try {
      if(mouseCallback) {
	Py_DECREF(mouseCallback);
	mouseCallback = nullptr;
      }
      if(mouseCallbackData) {
	Py_DECREF(mouseCallbackData);
      }
    
      mouseCallback = pymcb;
      Py_INCREF(mouseCallback);
      if(pydata != nullptr) {
	mouseCallbackData = pydata;
      }
      else {
	mouseCallbackData = Py_None;
      }
      Py_INCREF(mouseCallbackData);
    }
    catch (...) {
      PyGILState_Release(pystate);
      throw;
    }
    PyGILState_Release(pystate);
  }

  void CanvasPython::setResizeCallback(PyObject *rscb, PyObject *pydata) {
    PyGILState_STATE pystate = PyGILState_Ensure();
    try {
      if(resizeCallback) {
	Py_DECREF(resizeCallback);
	resizeCallback = nullptr;
      }
      if(resizeCallbackData) {
	Py_DECREF(resizeCallbackData);
      }
    
      resizeCallback = rscb;
      Py_INCREF(resizeCallback);
      if(pydata != nullptr) {
	resizeCallbackData = pydata;
      }
      else {
	resizeCallbackData = Py_None;
      }
      Py_INCREF(resizeCallbackData);
    }
    catch (...) {
      PyGILState_Release(pystate);
      throw;
    }
    PyGILState_Release(pystate);
  }

  void CanvasPython::allocateHandler() {
    if(resizeCallback) {
      PyGILState_STATE pystate = PyGILState_Ensure();
      try {
	PyObject *args = Py_BuildValue("(O)", resizeCallbackData);
	PyObject *result = PyObject_CallObject(resizeCallback, args);
	if(result == nullptr) {
	  PyErr_Print();
	  PyErr_Clear();
	}
	Py_XDECREF(args);
	Py_XDECREF(result);
      }
      catch (...) {
	PyGILState_Release(pystate);
	throw;
      }
      PyGILState_Release(pystate);
    }
  }

  void initializePyGTK() {
    static bool initialized = false;
    if(!initialized) {
      initialized = true;
      gtk_init(0, nullptr);
      PyGILState_STATE pystate = PyGILState_Ensure();
      try {
	if(!pygobject_init(-1, -1, -1))
	  throw "Cannot initialize pygobject!";
      }
      catch (...) {
	PyGILState_Release(pystate);
	throw;
      }
      PyGILState_Release(pystate);
    }
  }

#endif // PYTHON_OOFCANVAS

};				// namespace OOFCanvas


