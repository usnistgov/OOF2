// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "guicanvas.h"
#include "guicanvaslayer.h"

namespace OOFCanvas {

  WindowSizeCanvasLayer::WindowSizeCanvasLayer(OffScreenCanvas *cb,
					       const std::string &name)
    : CanvasLayer(cb, name)
  {}

  bool WindowSizeCanvasLayer::rebuild() {

    // TODO GTK3: Why is this being called on every mouse event
    // instead of only when the window size changes or when zoomed?
    
    GUICanvasBase *cnvs = dynamic_cast<GUICanvasBase*>(canvas);
    int size_x = cnvs->widgetWidth();
    int size_y = cnvs->widgetHeight();
    bool rebuilt = makeCairoObjs(size_x, size_y);
    // The Cairo::ImageSurface for the WindowSizeCanvasLayer is
    // aligned with the Canvas window, but it needs to have the same
    // ppu as the other CanvasLayers so that things drawn on it can
    // match things drawn on the other layers.  The offset can be
    // different because it can be compensated for when the
    // WindowSizeCanvasLayer is copied to the Canvas.  The offset must
    // map the upperleft corner of the ImageSurface to the lowerleft
    // corner of the window, and vice versa.

    // double ppu = cnvs->getPixelsPerUnit();
    // int hadj = gtk_adjustment_get_value(cnvs->getHAdjustment());
    // int vadj = gtk_adjustment_get_value(cnvs->getVAdjustment());

    // There are three coordinate systems:

    // * Window coords are the device coordinates in this layer.  The
    //   origin is at the upper left corner of the window.

    // * Bitmap coords are the device coordinates of CanvasLayers that
    //   aren't WindowSizeCanvasLayers.  They're offset from Window
    //   coords by (hadj, vadj).

    // * User coords are what the user is using.

    // The transformation matrix for this layer's context converts
    // from user coordinates to window coordinates.  We already know
    // how to convert from user coordinates to bitmap coordinates, so
    // just subtract (hadj, vadj) from the offset.  The offset can be
    // found by converting the origin.


    // Cairo::Matrix mat = cnvs->getTransform();
    // context->set_matrix(mat);
    // context->translate(ppu*hadj, ppu*vadj);
    
    // ICoord offset = cnvs->user2pixel(Coord(0.0, 0.0)) - ICoord(hadj, vadj);
    // Cairo::Matrix mat(ppu, 0.0, 0.0, -ppu, offset.x, offset.y);

    // Coord offset = ppu*cnvs->pixel2user(ICoord(0, size_y)) + Coord(hadj, -vadj);
    // Cairo::Matrix mat(ppu, 0.0, 0.0, -ppu, -offset.x, size_y+offset.y);

    // context->set_matrix(mat);

    // std::cerr << "WindowSizeCanvasLayer::rebuild:"
    // 	      << " size=" << size_x << "," << size_y
    // 	      << " adj=" << hadj << "," << vadj
    // 	      // << " mat=" << mat
    // 	      // << " offset=" << offset
    // 	      << " canvas origin=" << cnvs->user2pixel(Coord(0,0))
    // 	      << " layer origin=" << user2pixel(Coord(0, 0))
    // 	      << std::endl;

    return rebuilt;
  }

  void WindowSizeCanvasLayer::redraw() {
    if(dirty) {
      if(!rebuild())
	clear();
      GUICanvasBase *cnvs = dynamic_cast<GUICanvasBase*>(canvas);
      double ppu = cnvs->getPixelsPerUnit();
      int hadj = gtk_adjustment_get_value(cnvs->getHAdjustment());
      int vadj = gtk_adjustment_get_value(cnvs->getVAdjustment());
      context->set_matrix(cnvs->getTransform());
      context->translate(hadj/ppu, vadj/ppu);
      std::cerr << "WindowSizeCanvasLayer::redraw: mat="
		<< context->get_matrix()
		<< " ppu=" << ppu
		<< " adj=" << hadj << "," << vadj
		<< " canvas origin=" << cnvs->user2pixel(Coord(0,0))
		<< " layer origin=" << user2pixel(Coord(0,0))
		<< std::endl;
      for(CanvasItem *item : items)
	item->draw(context);
      dirty = false;
    }
  }

  void WindowSizeCanvasLayer::draw(Cairo::RefPtr<Cairo::Context> ctxt,
				   double hadj, double vadj)
    const
  {
    // Copy this layer to the given ctxt.  ctxt is the Cairo::Context
    // that was provided to the Gtk "draw" event handler.
    if(visible && !items.empty()) {
      // Args are the user-space coordinates in ctxt where the surface
      // origin (upper left corner) should appear.
      ctxt->set_source(surface, 0, 0);
	
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
