// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFGUICANVASLAYER_H
#define OOFGUICANVASLAYER_H

#include "canvaslayer.h"

namespace OOFCanvas {
  // A WindowSizeCanvasLayer is big enough to fill the Canvas's
  // window, which may be bigger or smaller than the bounding box of
  // its contents.
  
  class WindowSizeCanvasLayer : public CanvasLayer {
  public:
    WindowSizeCanvasLayer(OffScreenCanvas*, const std::string&);
    virtual void rebuild();
    virtual void render();
    virtual void copyToCanvas(Cairo::RefPtr<Cairo::Context>, double, double) const;
  };
};

#endif // OOFGUICANVASLAYER_H
