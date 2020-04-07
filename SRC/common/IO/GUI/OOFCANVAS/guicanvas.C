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
#include "guicanvas.h"
#include "rubberband.h"
#include <algorithm>
#include <cassert>
#include <gdk/gdk.h>
#include <iostream>

#ifdef OOFCANVAS_USE_PYTHON
#include <pygobject.h>
#endif 

namespace OOFCanvas {

  GUICanvasBase::GUICanvasBase(double ppu)
    : OffScreenCanvas(ppu),
      layout(nullptr),
      allowMotion(false),
      lastButton(0),
      buttonDown(false),
      rubberBandLayer(this, "rubberbandlayer"),
      rubberBand(nullptr),
      rubberBandBufferFilled(false),
      destroyed(false)
  {}

  void GUICanvasBase::initSignals() {
    // gdk_window_set_events() is called in the "realize" event
    // handler.
    g_signal_connect(G_OBJECT(layout), "realize",
		     G_CALLBACK(GUICanvasBase::realizeCB), this);
    // g_signal_connect(G_OBJECT(layout), "size-allocate",
    // 		     G_CALLBACK(GUICanvasBase::allocateCB), this);

    g_signal_connect(G_OBJECT(layout), "button_press_event",
    		     G_CALLBACK(GUICanvasBase::buttonCB), this);
    g_signal_connect(G_OBJECT(layout), "button_release_event",
    		     G_CALLBACK(GUICanvasBase::buttonCB), this);
    g_signal_connect(G_OBJECT(layout), "motion_notify_event",
    		     G_CALLBACK(GUICanvasBase::motionCB), this);
    g_signal_connect(G_OBJECT(layout), "draw",
    		     G_CALLBACK(GUICanvasBase::drawCB), this);
  }
  
  void GUICanvasBase::show() {
    gtk_widget_show(layout);
  }

  void GUICanvasBase::draw() {
    // This generates a draw event on the drawing area, which causes
    // GUICanvasBase::drawCB to be called.
    gtk_widget_queue_draw(layout);
  }

  void GUICanvasBase::setWidgetSize(int w, int h) {
    gtk_layout_set_size(GTK_LAYOUT(layout), w, h);
  }

  GtkAdjustment *GUICanvasBase::getHAdjustment() const {
    return gtk_scrollable_get_hadjustment(GTK_SCROLLABLE(layout));
  }

  GtkAdjustment *GUICanvasBase::getVAdjustment() const {
    return gtk_scrollable_get_vadjustment(GTK_SCROLLABLE(layout));
  }

  //=\\=//

  // Zooming

  // pixSize computes the size in pixels that the window would have to
  // be at the given ppu in order to contain a bounding box from bbmin
  // to bbmax and a bunch of pixel-sized items at positions refPt with
  // pixel extents pLo and pHi.

  static double pixSize(double ppu,
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

  static double optimalPPU(
		   double totalPixels, // size of window, device coords
		   double bbmin, double bbmax, // minimal bounding box, user
		   const std::vector<double> &pLo, // pixel extents
		   const std::vector<double> &pHi, // pixel extents
		   const std::vector<double> &refPt) // item coords, user
  {
    // bbmin and bbmax are the lower and upper limits of the bounding
    // box in the direction (x or y) under consideration.  The span
    // (bbmin, bbmax) contains CanvasItems at user-space reference
    // points refPt[i].  Item i extends below refPt[i] by pLo[i]
    // pixels, and above by pHi[i] pixels.

    // The optimal ppu is the one for which pixSize() returns
    // totalPixels.  pixSize() is a piecewise linear function of ppu,
    // so we need to find all the linear pieces and solve for ppu in
    // each piece.
    
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
  } // optimalPPU

  void GUICanvasBase::zoomToFill() {
    // This is tricky, because some objects have fixed sizes in device
    // units, and therefore change their size in user units when the
    // ppu is changed.  It's not possible to simply compute the
    // bounding box in user units and scale it to fit the window.

    if(empty())
      return;

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

      // The bounding box may not have been initialized yet, if the
      // canvas hasn't been drawn and setTransform hasn't been called.
      if(!boundingBox.initialized()) {
	setTransform(ppu);
      }
      double fudge = 0.97;	// a little extra space
      ppu_x = fudge*widgetWidth()/boundingBox.width();
      ppu_y = fudge*widgetHeight()/boundingBox.height();
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
      // a rectangle of (size widgetWidth(), widgetHeight()).
      
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
	ppu_x = optimalPPU(widgetWidth(), bboxInf.xmin(), bboxInf.xmax(),
			   pLeft, pRight, xRef);
      }

      if(bboxInf.height() == 0.0) {
	ppu_y = std::numeric_limits<double>::max();
      }
      else {
	ppu_y = optimalPPU(widgetHeight(), bboxInf.ymin(), bboxInf.ymax(),
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
  } // GUICanvasBase::zoomToFill

  static void centerAdj(GtkAdjustment *adj) {
    // Set a Gtk Adjustment to its center value.
    double l = gtk_adjustment_get_lower(adj);
    double u = gtk_adjustment_get_upper(adj);
    double p = gtk_adjustment_get_page_size(adj);
    double v = l + 0.5*(u - p  - l);
    gtk_adjustment_set_value(adj, v);
  }
  
  void GUICanvasBase::center() {
    // Move the center of the image to the center of the window,
    // without changing scale.
    centerAdj(getHAdjustment());
    centerAdj(getVAdjustment());
    draw();
  }

  void GUICanvasBase::zoomAbout(const Coord &fixedPt, double factor) {
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
  
  void GUICanvasBase::zoomAbout(double x, double y, double factor) {
    zoomAbout(Coord(x, y), factor);
  };

  void GUICanvasBase::zoom(double factor) {
    int w2 = 0.5*widgetWidth();
    int h2 = 0.5*widgetHeight();
    double xadj = gtk_adjustment_get_value(getHAdjustment());
    double yadj = gtk_adjustment_get_value(getVAdjustment());
    Coord cntr = pixel2user(ICoord(xadj + w2, yadj + h2));
    zoomAbout(cntr, factor);
  }

  //=\\=//

  // widgetHeight and widgetWidth return the size of the visible part
  // of the canvas, ie, the size of the window comtaining the canvas.
  // layoutSize returns the size of the bitmap, which may be larger or
  // smaller than the visible size.

  int GUICanvasBase::widgetHeight() const {
    return gtk_widget_get_allocated_height(layout);
  }

  int GUICanvasBase::widgetWidth() const {
    return gtk_widget_get_allocated_width(layout);
  }

  ICoord GUICanvasBase::layoutSize() const {
    guint w, h;
    gtk_layout_get_size(GTK_LAYOUT(layout), &w, &h);
    return ICoord(w, h);
  }

    //=\\=//

  void GUICanvasBase::setRubberBand(RubberBand *rb) {
    rubberBand = rb;
  }

  void GUICanvasBase::removeRubberBand() {
    rubberBand = nullptr;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Callback routines for gdk events

  // realizeCB is called once, when the Canvas's gtk object is
  // "realized", whatever that means.  It's not as if the Canvas has
  // any existence other than as a pattern of bits.

  void GUICanvasBase::realizeCB(GtkWidget*, gpointer data) {
    ((Canvas*) data)->realizeHandler();
  }

  void GUICanvasBase::realizeHandler() {
    // Set the initial size of the virtual window to be the same as
    // the size the actual window.
    gtk_layout_set_size(GTK_LAYOUT(layout), widgetWidth(), widgetHeight());
    
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
    // size.  So it's done here, instead of in the Canvas constructor.
    backingLayer = new CanvasLayer(this, "<backinglayer>");
    backingLayer->setClickable(false);
  }

  //=\\=//

  // TODO: Why is drawCB called so often?  This only happens on a Mac.
  // If the canvas's app has mouse focus, then drawCB is called
  // whenever the mouse crosses into or out of a Mac terminal window,
  // but not an emacs window.  The scrollbar in the canvas changes
  // color when this happens.

  void GUICanvasBase::drawCB(GtkWidget*, Cairo::Context::cobject *ctxt,
			  gpointer data)
  {
    ((GUICanvasBase*) data)->drawHandler(
	  Cairo::RefPtr<Cairo::Context>(new Cairo::Context(ctxt, false)));
  }

  void GUICanvasBase::drawHandler(Cairo::RefPtr<Cairo::Context> context) {
    // From the gtk2->gtk3 conversion notes: "The cairo context is
    // being set up so that the origin at (0, 0) coincides with the
    // upper left corner of the widget, and is properly clipped."
    // (https://developer.gnome.org/gtk3/stable/ch26s02.html)

    double hadj = gtk_adjustment_get_value(getHAdjustment());
    double vadj = gtk_adjustment_get_value(getVAdjustment());

    setTransform(ppu);

    // If the only thing that's changed is the rubberband, make sure
    // that we don't update more than is necessary.  The rubberband
    // needs to be redrawn quickly and often.

    // If there's no rubberband, just update all layers and copy them
    // to the device's context.

    // If there is a rubberband, and if the rubberband buffer is up to
    // date, copy the rubberband buffer and the rubberband to the
    // device.  TODO: Limit the copying to the bounding boxes of the
    // previous and current rubberbands.

    // If there is a rubberband, but the rubberband buffer is out of
    // date, copy the layers to the rubberband buffer and then copy it
    // and the rubberband to the device.

    if(rubberBand && rubberBand->active()) {

      if(rubberBandBufferFilled) {
	// Are any non-rubberband layers dirty?
	bool dirty = false;
	for(unsigned int i=0; i<layers.size(); i++)
	  if(layers[i]->dirty) {
	    dirty = true;
	    break;
	  }
	if(!dirty) {
	  // No layers other than the rubberband have changed.  Copy the
	  // rubberBandBuffer, which already contains the other layers,
	  // to the destination, and draw the rubberband on top of that.
	  // TODO: set and use rubberBandBBox
	  // background
	  context->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
	  context->paint();

	  // all non-rubberband layers
	  context->set_source(rubberBandBuffer, 0, 0);
	  context->paint();

	  // rubberband
	  rubberBandLayer.redraw();
	  rubberBandLayer.draw(context, hadj, vadj);
	  return;
	}
      }

      // Recreate rubberBandBuffer, which contains all the layers
      // *other* than the rubberBandLayer.

      ICoord size = boundingBoxSizeInPixels();
      rubberBandBuffer = Cairo::RefPtr<Cairo::ImageSurface>(
			    Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32,
							size.x, size.y));
      cairo_t *rbctxt = cairo_create(rubberBandBuffer->cobj());
      Cairo::RefPtr<Cairo::Context> rbContext =
	Cairo::RefPtr<Cairo::Context>(new Cairo::Context(rbctxt, true));
      rbContext->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
      rbContext->paint();

      // Draw all other layers to the rubberBandBuffer.
      for(CanvasLayer *layer : layers) {
	layer->redraw();
	layer->draw(rbContext, hadj, vadj);
      }
      rubberBandBufferFilled = true;

      context->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
      context->paint();

      context->set_source(rubberBandBuffer, 0, 0);
      context->paint();

      rubberBandLayer.redraw();	
      rubberBandLayer.draw(context, hadj, vadj);
      return;
    }

    // There's no rubberband, just draw.

    // TODO? Extract the clipping region from the context using
    // Cairo::Context::get_clip_extents, and only redraw CanvasItems
    // whose bounding boxes intersect the clipping region.  If the
    // items are stored in an R-tree this might be fast.

    context->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
    context->paint();

    for(CanvasLayer *layer : layers) {
      layer->redraw();			// only redraws dirty layers
      layer->draw(context, hadj, vadj); // copies layers to canvas
    }
  } // GUICanvasBase::drawHandler

  //=\\=//

  void GUICanvasBase::buttonCB(GtkWidget*, GdkEventButton *event, gpointer data)
  {
    ((GUICanvasBase*) data)->mouseButtonHandler(event);
  }

  void GUICanvasBase::mouseButtonHandler(GdkEventButton *event) {
    if(empty())
      return;
    ICoord pixel(event->x, event->y);
    Coord userpt(pixel2user(pixel));
    
    std::string eventtype;
    if(event->type == GDK_BUTTON_PRESS) {
      eventtype = "down";
      buttonDown = true;
      mouseDownPt = userpt;
    }
    else {
      eventtype = "up";
      buttonDown = false;
      if(rubberBand && rubberBand->active()) {
	rubberBand->stop();
      }
    }
    lastButton = event->button;
    doCallback(eventtype, userpt, lastButton,
	       event->state & GDK_SHIFT_MASK,   
	       event->state & GDK_CONTROL_MASK);
    allowMotion = (eventtype == "down");
  }

  //=\\=//
  
  void GUICanvasBase::motionCB(GtkWidget*, GdkEventMotion *event, gpointer data)
  {
    ((Canvas*) data)->mouseMotionHandler(event);
  }

  void GUICanvasBase::mouseMotionHandler(GdkEventMotion *event) {
    if(!allowMotion)
      return;
    ICoord pixel(event->x, event->y);
    Coord userpt(pixel2user(pixel));
    if(rubberBand) {
      rubberBandLayer.removeAllItems();
      if(!rubberBand->active()) {
	rubberBandBufferFilled = false;
	rubberBand->start(&rubberBandLayer, mouseDownPt.x, mouseDownPt.y);
      }
      rubberBand->draw(userpt.x, userpt.y);
    }
    doCallback("move", userpt, lastButton,
	       event->state & GDK_SHIFT_MASK,
	       event->state & GDK_CONTROL_MASK);
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // The classes derived from GUICanvasBase, Canvas and PythonCanvas,
  // differ in how the GtkLayout is created and in how the callback
  // functions are set up.  PythonCanvas assumes that they all come
  // from Python.  The PythonCanvas class is called "Canvas" in
  // Python.


  // Derived class to be used when the Canvas is created and used in
  // C++ with a Gtk GUI.  The mouse callback must be a C++ function.
  // A gtk layout is created by the constructor and can be retrieved
  // by calling Canvas::gtk().

  Canvas::Canvas(double ppu)
    : GUICanvasBase(ppu),
      mouseCallback(nullptr),
      mouseCallbackData(nullptr)
  {
    layout = gtk_layout_new(NULL, NULL);
    initSignals();
  }

  Canvas::~Canvas() {
    destroy();
  }

  void Canvas::destroy() {
    // Signal handlers are automatically disconnected when the widget
    // is destroyed.
    if(destroyed)
      return;
    destroyed = true;
    // Actually destroy the gtk widget, since we created it.
    gtk_widget_destroy(layout);
  }


  void Canvas::setMouseCallback(MouseCallback mcb, void *data) {
    mouseCallback = mcb;
    mouseCallbackData = data;
  }

  void Canvas::doCallback(const std::string &eventtype, const Coord &userpt,
			  int button, bool shift, bool ctrl)
  {
    if(mouseCallback != nullptr) {
      (*mouseCallback)(eventtype, userpt.x, userpt.y, button, shift, ctrl);
      draw();
    }
  }
  
#ifdef OOFCANVAS_USE_PYTHON

  // Derived class to be used when the Canvas is created in Python.  A
  // Gtk.Layout must be created and passed in to the constructor.  The
  // mouse callback must be a Python function.  All other public
  // methods are available in C++ and Python.

  // TODO: Do we really need to store pyCanvas?  It's not explicitly
  // used after the constructor finishes, but perhaps storing a
  // reference to it is important.  It's probably not harmful, at
  // least.

  PythonCanvas::PythonCanvas(PyObject *pycan, double ppu)
    : GUICanvasBase(ppu),
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

  PythonCanvas::~PythonCanvas() {
    destroy();
  }

  void PythonCanvas::destroy() {
    if(destroyed)
      return;
    destroyed = true;
    // Dereference, but don't destroy the widget, since we didn't create it.
    g_object_unref(layout);
    PyGILState_STATE pystate = PyGILState_Ensure();
    try {
      if(mouseCallback != nullptr)
	Py_DECREF(mouseCallback);
      if(resizeCallback != nullptr)
	Py_DECREF(resizeCallback);
      Py_DECREF(mouseCallbackData);
      Py_DECREF(resizeCallbackData);
      Py_DECREF(pyCanvas);
    }
    catch(...) {
      PyGILState_Release(pystate);
      throw;
    }
    PyGILState_Release(pystate);
  }

  void PythonCanvas::doCallback(const std::string &eventtype,
				const Coord &userpt,
				int button, bool shift, bool ctrl)
  {
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
      draw();
    }

  }
  
  void PythonCanvas::setMouseCallback(PyObject *pymcb, PyObject *pydata) {
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

  void PythonCanvas::setResizeCallback(PyObject *rscb, PyObject *pydata) {
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

  void PythonCanvas::allocateHandler() {
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

#endif // OOFCANVAS_USE_PYTHON

  
  

};				// namespace OOFCanvas
