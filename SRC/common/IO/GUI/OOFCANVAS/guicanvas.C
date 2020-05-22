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

#include "common/printvec.h"

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
      nonRubberBandBufferFilled(false),
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

  // pixSize() computes the size in pixels that the window would have
  // to be at the given ppu in order to contain a bounding box from
  // bbmin to bbmax and a bunch of objects spanning user coords from
  // refLo to refHi with pixel extensions pLo and pHi.  X and Y are
  // handled separately. pixSize() just does one of them at a time.

  static double pixSize(double ppu,
			const std::vector<double> &pLo,
			const std::vector<double> &refLo,
			const std::vector<double> &pHi,
			const std::vector<double> &refHi)
  {
    // CanvasItem i extends from refLo[i] to refHi[i] in physical
    // units, but extends past that by pLo[i] and pHi[i] in pixel
    // units.
    // The total size is
    //    max(ppu*refHi_i + pHi_i) - min(ppu*refLo_i - pLo_i)
    double maxHi = -std::numeric_limits<double>::max();
    double minLo = std::numeric_limits<double>::max();
    int iHi = -1;
    int iLo = -1;
    for(unsigned int i=0; i<pLo.size(); i++) {
      double xHi = ppu*refHi[i] + pHi[i];
      if(xHi > maxHi) {
	maxHi = xHi;
	iHi = i;
      }
      double xLo = ppu*refLo[i] - pLo[i];
      if(xLo < minLo) {
	minLo = xLo;
	iLo = i;
      }
    }
    return maxHi - minLo;
  }
      
  // zoomToFill() uses optimalPPU() to compute the ppu in one
  // direction.

  static double optimalPPU(
		   double w0, 
		   const std::vector<double> &pLo,
		   const std::vector<double> &refLo, 
		   const std::vector<double> &pHi,
		   const std::vector<double> &refHi)
  {
    // Item i extends from
    //     xLo[i] = ppu*(refLo[i]-C) - pLo[i]
    // to
    //     xHi[i] = ppu*(refHi[i]-C) + pHi[i]
    // where the origin C is arbitrary and ignored.
    // The total width is 
    //     w(ppu) = max(xHi[i]) - min(xLo[i])
    // We need to solve w(ppu) = w0.
    // w is a piecewise linear function of ppu, so we find the
    // critical ppu values at which it changes slope, and look for a
    // solution in each interval.

    assert(pLo.size() == refLo.size() &&
	   pHi.size() == refHi.size() &&
	   pLo.size() == pHi.size());
    unsigned int n = pLo.size();

    double maxRefHi = -std::numeric_limits<double>::max();
    double minRefLo = std::numeric_limits<double>::max();
    int iMax, iMin;
    
    // ppus at which the slope of max(ppu*xmax+pmax) or
    // min(ppu*xmin-pmin) changes.
    std::vector<double> criticalPPUs;
    criticalPPUs.reserve(2*n*(n-1));
    criticalPPUs.push_back(0.0);

    // TODO: Is there a way to do this that isn't o(N^2)?
    
    for(unsigned int i=0; i<n; i++) {
      if(refHi[i] > maxRefHi) {
	maxRefHi = refHi[i];
	iMax = i;
      }
      if(refLo[i] < minRefLo) {
	minRefLo = refLo[i];
	iMin = i; 
      }
      for(unsigned int j=i+1; j<n; j++) {
	// Find the ppu at which items i and j extend equally far down.
	// ppu*refLo[i] - pLo[i] = ppu*refLo[j] - pLo[j]
	if(refLo[i] != refLo[j]) {
	  double ppu = (pLo[i] - pLo[j])/(refLo[i] - refLo[j]);
	  if(ppu > 0)
	    criticalPPUs.push_back(ppu);
	}
	// Find the ppu at which items i and j extend equally far up.
	// ppu*refHi[i] + pHi[i] = ppu*refHi[j] + pHi[j]
	if(refHi[i] != refHi[j]) {
	  double ppu = (pHi[j] - pHi[i])/(refHi[i] - refHi[j]);
	  if(ppu > 0)
	    criticalPPUs.push_back(ppu);
	}
      }
    }

    std::sort(criticalPPUs.begin(), criticalPPUs.end());

    double ppuMax = 0.0;	// maximum ppu that gives a solution
    for(unsigned int i=0; i<criticalPPUs.size()-1; i++) {
      // Interval in which W is a linear function of ppu
      double ppuA = criticalPPUs[i];
      double ppuB = criticalPPUs[i+1];
      if(ppuA != ppuB) {
	// Find value of ppu that gives width W = totalPixels
	double wA = pixSize(ppuA, pLo, refLo, pHi, refHi);
	double wB = pixSize(ppuB, pLo, refLo, pHi, refHi);
	if((wA - w0) * (wB - w0) <= 0.0) {
	  double ppu = ppuA + (w0 - wA)*(ppuB - ppuA)/(wB - wA);
	  if(ppuA <= ppu && ppu <= ppuB && ppu > ppuMax) {
	    ppuMax = ppu;
	  }
	}
      }
    }

    // The interval from the largest criticalPPU to infinity has to be
    // examined too.  As ppu goes to infinity, only the largest refHi
    // and smallest refLo contribute.
    // w0 = (ppu*refHi[iMax] + pHi[iMax]) - (ppu*refLo[iMin] - pLo[iMin])
    double ppu = (w0 - pHi[iMax] - pLo[iMin])/(refHi[iMax] - refLo[iMin]);
    if(ppu > criticalPPUs.back() && ppu > ppuMax)
      ppuMax = ppu;
    
    return ppuMax;
  } // optimalPPU

  //=\\=//

  void GUICanvasBase::zoomToFill() {
    // This is tricky, because some objects have fixed sizes in device
    // units, and therefore change their size in user units when the
    // ppu is changed.  It's not possible to simply compute the
    // bounding box in user units and scale it to fit the window.

    if(empty())
      return;

    Rectangle bboxInf;   // user-space bbox if the ppu were infinite

    int n = 0;
    for(CanvasLayer *layer : layers)
      if(layer->visible) {
	n += layer->size();
      }
    if(n == 0)
      return;
    
    // Pixel extents of each item from its reference point.
    std::vector<double> pxLo, pxHi, pyLo, pyHi;
    // User coordinates of the upper and lower reference points of
    // each object in each direction.
    std::vector<double> xLo, yLo, xHi, yHi;
    pxLo.reserve(n);
    pxHi.reserve(n);
    pyLo.reserve(n);
    pyHi.reserve(n);
    xLo.reserve(n);
    xHi.reserve(n);
    yLo.reserve(n);
    yHi.reserve(n);

    for(CanvasLayer *layer : layers) {
      if(layer->visible) {
	for(CanvasItem *item : layer->items) {
	  const Rectangle &bbox0 = item->findBareBoundingBox();
	  bboxInf.swallow(bbox0);
	  xHi.push_back(bbox0.xmax());
	  xLo.push_back(bbox0.xmin());
	  yHi.push_back(bbox0.ymax());
	  yLo.push_back(bbox0.ymin());
	  double pxlo, pxhi, pylo, pyhi;
	  item->pixelExtents(pxlo, pxhi, pyhi, pylo);
	  pxLo.push_back(pxlo);
	  pxHi.push_back(pxhi);
	  pyHi.push_back(pyhi);
	  pyLo.push_back(pylo);
	}
      }
    }
    double ppu_x = optimalPPU(widgetWidth()/(1+margin), pxLo, xLo, pxHi, xHi);
    double ppu_y = optimalPPU(widgetHeight()/(1+margin), pyLo, yLo, pyHi, yHi);
    // Pick the smaller of ppu_x and ppu_y, so that the entire image
    // is visible in both directions.
    double newppu = ppu_x < ppu_y ? ppu_x : ppu_y;
    if(newppu < std::numeric_limits<double>::max())
      setTransform(newppu);
    else {
      // No ppu was established.  This can only happen if all of the
      // CanvasItems have sizes set in device units and all of their
      // reference points coincide.  In that case, the user units are
      // irrelevant, so any ppu will do.
      setTransform(1.0);
    }
    center();
  } // GUICanvasBase::zoomToFill

  //=\\=//

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
  // bitmapSize returns the desired size of the bitmap, which may be larger or
  // smaller than the visible size.

  int GUICanvasBase::widgetHeight() const {
    return gtk_widget_get_allocated_height(layout);
  }

  int GUICanvasBase::widgetWidth() const {
    return gtk_widget_get_allocated_width(layout);
  }

  ICoord GUICanvasBase::bitmapSize() const {
    ICoord bbsize(OffScreenCanvas::bitmapSize());
    // The bitmap must be at least as large as the window so that the
    // drawing can be centered in the window when it's smaller than
    // the window.
    int w = widgetWidth();
    int h = widgetHeight();
    return ICoord(w > bbsize.x ? w : bbsize.x,
		  h > bbsize.y ? h : bbsize.y);
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

      if(nonRubberBandBufferFilled) {
	// Are any non-rubberband layers dirty?
	bool dirty = false;
	for(unsigned int i=0; i<layers.size(); i++)
	  if(layers[i]->dirty) {
	    dirty = true;
	    break;
	  }
	if(!dirty) {
	  // No layers other than the rubberband have changed.  Copy the
	  // nonRubberBandBuffer, which already contains the other layers,
	  // to the destination, and draw the rubberband on top of that.
	  // TODO: set and use rubberBandBBox
	  // background
	  context->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
	  context->paint();

	  // all non-rubberband layers
	  context->set_source(nonRubberBandBuffer, 0, 0);
	  context->paint();

	  // rubberband
	  rubberBandLayer.redraw();
	  // rubberBandLayer.draw(context, hadj, vadj);
	  rubberBandLayer.draw(context, 0, 0);
	  return;
	}
      }

      // Recreate nonRubberBandBuffer, which contains all the layers
      // *other* than the rubberBandLayer.

      ICoord size = bitmapSize();
      nonRubberBandBuffer = Cairo::RefPtr<Cairo::ImageSurface>(
			       Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32,
							   size.x, size.y));
      cairo_t *rbctxt = cairo_create(nonRubberBandBuffer->cobj());
      Cairo::RefPtr<Cairo::Context> rbContext =
	Cairo::RefPtr<Cairo::Context>(new Cairo::Context(rbctxt, true));
      rbContext->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
      rbContext->paint();

      // Draw all other layers to the nonRubberBandBuffer.
      for(CanvasLayer *layer : layers) {
	layer->redraw();
	layer->draw(rbContext, hadj, vadj);
      }
      nonRubberBandBufferFilled = true;

      context->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
      context->paint();

      context->set_source(nonRubberBandBuffer, 0, 0);
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
	nonRubberBandBufferFilled = false;
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
