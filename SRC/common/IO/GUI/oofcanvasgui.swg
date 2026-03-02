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
// TODO: OOFCanvas should install swig files into
// <prefix>/share/oof2/swig where OOF2 could find them.

%import "common/IO/oofcanvas.swg"

// This block needs to be explicitly inserted into the swig file that
// imports this one. TODO: That's ugly.  Perhaps this file should be
// %included, and not %imported, but itself should contain only the
// C++ block, and then %import the rest.

%{
  #include <oofcanvas.h>
  typedef OOFCanvas::CanvasColor CanvasColor;
  typedef OOFCanvas::CanvasCoord CanvasCoord;
  typedef OOFCanvas::RubberBand RubberBand;
%}

%rename(CanvasColor) OOFCanvas::CanvasColor;

%nodefaultctor RubberBand;

class RubberBand {
public:
  ~RubberBand();
  void setLineWidth(double);
  void setColor(const CanvasColor*);
  void setDashed(bool);
  void setDashLength(double);
  void setDashColor(const CanvasColor*);
  void update(const CanvasCoord*);
};

