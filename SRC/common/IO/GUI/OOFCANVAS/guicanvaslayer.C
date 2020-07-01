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

  void WindowSizeCanvasLayer::rebuild() {
    GUICanvasBase *cnvs = dynamic_cast<GUICanvasBase*>(canvas);
    int size_x = cnvs->widgetWidth();
    int size_y = cnvs->widgetHeight();
    // makeCairoObjs doesn't do anything if the size hasn't changed.
    makeCairoObjs(size_x, size_y);
  }

  void WindowSizeCanvasLayer::redraw() {
    if(dirty) {
      rebuild();
      clear();
      // A WindowSizeCanvasLayer has the same ppu and orientation as
      // the other canvas layers, but its origin in device coordinates
      // is at the upper left corner of the window.
      GUICanvasBase *cnvs = dynamic_cast<GUICanvasBase*>(canvas);
      double ppu = cnvs->getPixelsPerUnit();
      double hadj, vadj;
      cnvs->getEffectiveAdjustments(hadj, vadj);
      context->set_matrix(cnvs->getTransform());
      // The signs for the x and y translations are different because
      // the y axis is flipped.
      context->translate(-hadj/ppu, vadj/ppu);
      redrawToContext(context);
      dirty = false;
    }
  }

  void WindowSizeCanvasLayer::draw(Cairo::RefPtr<Cairo::Context> ctxt,
				   double, double)
    const
  {
    // Copy this layer to the given ctxt.  ctxt is the Cairo::Context
    // that was provided to the Gtk "draw" event handler.
    if(visible && !items.empty()) {
      // Args are the user-space coordinates in ctxt where the surface
      // origin (upper left corner) should appear.
      ctxt->set_source(surface, 0, 0);
      ctxt->paint_with_alpha(alpha);
    }
  }

};				// namespace OOFCanvas
