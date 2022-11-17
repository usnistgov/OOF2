// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef GFXBRUSHSTYLE_SWG
#define GFXBRUSHSTYLE_SWG

%module(package="ooflib.SWIG.common.IO.GUI") gfxbrushstyle

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/brushstyle.swg"
#endif // NOSECONDIMPORTS

%{
#include "common/IO/GUI/gfxbrushstyle.h"
%}


%nodefaultctor GfxBrushStyle;

class GfxBrushStyle {
public:
  ~GfxBrushStyle();
};

class GfxCircleBrush : public GfxBrushStyle, public CircleBrush {
public:
  GfxCircleBrush(double);
};

class GfxSquareBrush : public GfxBrushStyle, public SquareBrush {
public:
  GfxSquareBrush(double);
};

//%pythoncode "common/IO/GUI/gfxbrushstyle.spy"

%pythoncode %{

# When the GUI is loaded, the Registrations for the BrushStyles should
# create GfxBrushStyles instead of the non-GUI BrushStyles that were
# registered in brushstyle.py.  Here we sneakily replace the
# registered classes with the GUI versions.
from ooflib.SWIG.common import brushstyle
brushstyle.circleReg.substituteClass(GfxCircleBrush)
brushstyle.squareReg.substituteClass(GfxSquareBrush)

%}
#endif // GFXBRUSHSTYLE_SWG
