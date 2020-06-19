// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFGUICANVAS_SWG
#define OOFGUICANVAS_SWG

%module oofcanvasgui
%include "common/typemaps.swg"

%pragma(python) include="oofcanvasgui.spy"

%pragma(python) code="from ooflib.SWIG.common.IO.OOFCANVAS.oofcanvas import OffScreenCanvasPtr"
%pragma(python) code="from ooflib.SWIG.common.IO.OOFCANVAS.oofcanvas import RectanglePtr"
%extern "common/IO/OOFCANVAS/oofcanvas.swg"
  
%{
#define SWIG_FILE_WITH_INIT
#include "common/IO/GUI/OOFCANVAS/guicanvas.h"
using namespace OOFCanvas;
typedef std::vector<CanvasItem*> CanvasItemList;
%}

%typemap(python, in) PyObject* {
  $target = $source;
}

void initializePyGTK();

%name(Canvas) class PythonCanvas : public OffScreenCanvas {
public:
  %name(Canvas) PythonCanvas(PyObject*, double ppu);
  %name(Canvas) ~PythonCanvas();
  void destroy();
  int widgetWidth();
  int widgetHeight();
  void show();
  void zoom(double);
  void zoomAbout(double, double, double);
  void zoomToFill();
  void center();
  Rectangle visibleRegion();
  void setMouseCallback(PyObject*, PyObject*);
  void setResizeCallback(PyObject*, PyObject*);
  void allowMotionEvents(bool);
  void setRubberBand(RubberBand*);
  void removeRubberBand();
};



#endif // OOFGUICANVAS_SWG
