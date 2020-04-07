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

  void WindowSizeCanvasLayer::clear() {
    GUICanvasBase *cnvs = dynamic_cast<GUICanvasBase*>(canvas);
    int size_x = cnvs->widgetWidth();
    int size_y = cnvs->widgetHeight();
    makeCairoObjs(size_x, size_y);
    // The Cairo::ImageSurface for the WindowSizeCanvasLayer is
    // aligned with the Canvas window, but it needs to have the same
    // ppu as the other CanvasLayers so that things drawn on it can
    // match things drawn on the other layers.  The offset can be
    // different because it can be compensated for when the
    // WindowSizeCanvasLayer is copied to the Canvas.  The offset must
    // put the upperleft corner of the ImageSurface to the lowerleft
    // corner of the window, and vice versa.

    double ppu = cnvs->getPixelsPerUnit();
    int hadj = gtk_adjustment_get_value(cnvs->getHAdjustment());
    int vadj = gtk_adjustment_get_value(cnvs->getVAdjustment());
    
    Coord offset = ppu*cnvs->pixel2user(ICoord(0, size_y)) + Coord(hadj, -vadj);
    Cairo::Matrix mat(ppu, 0.0, 0.0, -ppu, -offset.x, size_y+offset.y);
    context->set_matrix(mat);
  }

  void WindowSizeCanvasLayer::draw(Cairo::RefPtr<Cairo::Context> ctxt,
				   double hadj, double vadj)
    const
  {
    // Copy this layer to the given ctxt.  ctxt is the Cairo::Context
    // that was provided to the Gtk "draw" event handler.  The
    // coordinates in ctxt are pixel coordinates (the transformation
    // matrix is the identity matrix) but may have a non-zero offset.

    if(visible && !items.empty()) {
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
