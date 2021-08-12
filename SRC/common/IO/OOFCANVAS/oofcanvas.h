// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// This file can be included in code that uses OOFCanvas.  It's not
// used within OOFCanvas itself.

#ifndef ALL_OOFCANVAS_H
#define ALL_OOFCANVAS_H

#include "canvas.h"
#include "canvascircle.h"
#include "canvasimage.h"
#include "canvaslayer.h"
#include "canvaspolygon.h"
#include "canvasrectangle.h"
#include "canvassegment.h"
#include "canvassegments.h"
#include "canvastext.h"

// Handy macros to convert different coordinate classes to OOFCanvas
// coordinates, when passing arguments to OOFCanvas methods.

#define OOFCANVAS_COORD(obj) OOFCanvas::Coord((obj)[0], (obj)[1])
#define OOFCANVAS_ICOORD(obj) OOFCanvas::ICoord((obj)[0], (obj)[1])

#endif // ALL_OOFCANVAS_H
