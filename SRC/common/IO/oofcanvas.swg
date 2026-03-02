// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// This file duplicates some type information from OOFCanvas.  It is
// here to be %imported into other swig files, but should not be
// directly swigged itself.

// Because this is %imported and not %included, it won't generate any
// code, so the importing files should contain something like this:
// %{
//   #include <oofcanvas.h>
//   typedef OOFCanvas::CanvasColor CanvasColor;
//   typedef OOFCanvas::CanvasCoord CanvasCoord;
// %}

namespace OOFCanvas {
  class CanvasColor {
  public:
    CanvasColor(double, double, double);
    CanvasColor opacity(double);
  };

  class CanvasCoord {};
};

