// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFCANVAS_SWG
#define OOFCANVAS_SWG

%module oofcanvas

%pragma(python) include="oofcanvas.spy"

%{
#define SWIG_FILE_WITH_INIT
#include "oofcanvas.h"
using namespace OOFCanvas;
using namespace std;

typedef std::vector<CanvasItem*> CanvasItemList;
typedef std::vector<std::string> StringVec;
typedef std::vector<double> DoubleVec;
%}

%typemap(python, out) PyObject* {
  // typemap(python, out) PyObject*				 
  $target = $source;
}

%typemap(python, in) PyObject* {
  $target = $source;
}

%typemap(python, out) CanvasItem* {
  // typemap(python, out) CanvasItem*				   
  $target = $source->pythonObject();
}

%typemap(python, out) string* {
  // typemap(python, out) string*
  $target = PyString_FromString($source->c_str());
}

%typemap(python, newfree) string* {
  // typemap(python, newfree) string*
  delete $source;
}

// Convert a std::vector* of std::strings to a list of Python strings
%typemap(python, out) StringVec* {
  // typemap(python, out) StringVec*
  StringVec::size_type sz = $source->size();
  $target = PyList_New((Py_ssize_t) sz);
  for(StringVec::size_type i=0; i<sz; i++) {
    PyObject *str = PyString_FromString((*$source)[i].c_str());
    PyList_SET_ITEM($target, (Py_ssize_t) i, str); // Steals reference.
  }
}

// Convert a Python list or tuple of doubles to a std::vector<double>
%typemap(python, newfree) StringVec *{
  // typemap(python, newfree) StringVec*
  delete $source;
}


%typemap(python, in) DoubleVec* (DoubleVec vec) {
  if(!PySequence_Check($source)) {
    PyErr_SetString(
	    PyExc_TypeError,
	    "OOFCanvas: Error in vector<double> typemap. Expected a sequence of numbers.");
    return 0;
  }
  DoubleVec::size_type sz = Py_SAFE_DOWNCAST(PySequence_Size($source),
					     Py_ssize_t, DoubleVec::size_type);
  if(sz > 0) {
    vec.resize(sz);
    for(DoubleVec::size_type i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($source, (Py_ssize_t) i);
      if(PyFloat_Check(x))
	vec[i] = PyFloat_AsDouble(x);
      else if(PyInt_Check(x))
	vec[i] = (double) PyInt_AsLong(x);
      else {
	PyErr_SetString(PyExc_TypeError, "OOFCanvas: Error in vector<double> typemap. Expected a sequence of numbers.");
	return 0;
      }
      Py_XDECREF(x);
    }
  }
  $target = &vec;
}

class Color {
public:
  Color(double, double, double);
  Color opacity(double);
};

class Rectangle {
public:
  double xmin();
  double xmax();
  double ymin();
  double ymax();
  %addmethods {
    %new const string *__repr__() {
      return new std::string("[(" +
			     to_string(self->xmin()) + "," +
			     to_string(self->ymin()) + ", (" +
			     to_string(self->xmax()) + "," +
			     to_string(self->ymax()) + ")]");
    }
  }
};

%readonly
Color black, white, red, green, blue, magenta, cyan, yellow, gray;
%readwrite

// Some enums that Cairo defines in C++ need to be accessible from
// Python.  I don't know how this is done in pycairo.  It would be
// convenient if we could just use the pycairo enums, but for now we
// just define constants in C++ for each enum value and expose the
// constants in python as opaque objects.

%{
typedef Cairo::LineCap CairoLineCap;
typedef Cairo::LineJoin CairoLineJoin;
%}

class CairoLineJoin {};
class CairoLineCap {};

%readonly
CairoLineJoin lineJoinMiter;
CairoLineJoin lineJoinRound;
CairoLineJoin lineJoinBevel;
CairoLineCap lineCapButt;
CairoLineCap lineCapRound;
CairoLineCap lineCapSquare;
%readwrite



class CanvasItem {
private:
  CanvasItem();			// private constructor is not swigged
  ~CanvasItem();
public:
  Rectangle boundingBox();
  void drawBoundingBox(double, Color&);
};

class CanvasShape : public CanvasItem {
public:
  void setLineWidth(double);
  void setLineWidthInPixels();
  void setLineColor(Color&);
  void setLineJoin(CairoLineJoin);
  void setLineCap(CairoLineCap);
};

class CanvasFillableShape : public CanvasShape {
public:
  void setFillColor(Color&);
};

class CanvasRectangle : public CanvasFillableShape {
public:
  CanvasRectangle(double, double, double, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasSegment : public CanvasShape {
public:
  CanvasSegment(double, double, double, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasSegments : public CanvasShape {
public:
  CanvasSegments();
  void addSegment(double, double, double, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasPolygon : public CanvasFillableShape {
public:
  CanvasPolygon();
  void addPoint(double, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasCircle : public CanvasFillableShape {
public:
  CanvasCircle(double, double, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasEllipse : public CanvasFillableShape {
public:
  CanvasEllipse(double, double, double, double, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasDot : public CanvasFillableShape {
public:
  CanvasDot(double, double, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasArrowhead : public CanvasItem {
public:
  CanvasArrowhead(CanvasSegment*, double, double, double);
  void setReversed();
  void setPixelSize();
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasText : public CanvasItem {
public:
  CanvasText(double, double, char*);
  void setFillColor(Color);
  void setFont(char*, bool);
  void rotate(double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasImage : public CanvasItem {
public:
  void setOpacity(double);
  void setPixelSize();
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }

  %new static CanvasImage *newBlankImage(double, double, int, int,
					 double, double,
					 double, double, double, double);
  %new static CanvasImage *newFromPNGFile(double, double, char*,
					  double, double);
  %new static CanvasImage *newFromImageMagickFile(double, double, char*,
						  double, double);
};


class CanvasLayer {
private:
  CanvasLayer();		// private constructor is not swigged
public:
  ~CanvasLayer();
  void addItem(CanvasItem*);
  void removeAllItems();
  void clear();
  void redraw();
  void setClickable(bool);
  void setOpacity(double);
  void show();
  void hide();
  void raiseBy(int);
  void lowerBy(int);
  void raiseToTop();
  void lowerToBottom();
  %addmethods {
    const char *name() {
      return self->name.c_str();
    }
  }
};

class CanvasItemList {
  // CanvasItemList is just a typedef for std::vector<CanvasItem*>,
  // but swig doesn't need to know that.
public:
  ~CanvasItemList();
  %addmethods {
    int __len__() { return self->size(); }
    %new CanvasItemListIterator *getiter() {
      return new CanvasItemListIterator(self);
    }
  }
};


class RubberBand {
public:
  void setLineWidth(double);
  void setColor(Color);
};

class LineRubberBand : public RubberBand {
public:
  LineRubberBand();
};

class RectangleRubberBand : public RubberBand {
public:
  RectangleRubberBand();
};

class CircleRubberBand : public RubberBand {
public:
  CircleRubberBand();
};

class EllipseRubberBand : public RubberBand {
public:
  EllipseRubberBand();
};

class SpiderRubberBand : public RubberBand {
public:
  SpiderRubberBand(DoubleVec*);
};

class CanvasItemListIterator {
public:
  CanvasItem *next_();
  bool done();
};

class OffScreenCanvas {
public:
  OffScreenCanvas(double);
  ~OffScreenCanvas();
  CanvasLayer *newLayer(char*);
  CanvasLayer *getLayer(int);
  %name(getLayerByName) CanvasLayer *getLayer(char*);
  int nLayers();
  bool empty();
  void raiseLayer(int, int);
  void lowerLayer(int, int);
  void lowerLayerToBottom(int);
  void raiseLayerToTop(int);
  void clear();
  void draw();
  double getPixelsPerUnit();
  void antialias(bool);
  void setBackgroundColor(double, double, double);
  %name(clickedItems) %new CanvasItemList* clickedItems_new(double, double);
  %name(allItems) %new CanvasItemList* allItems_new();
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

%new StringVec *list_fonts();


%typemap(python, in) PyObject*;
%typemap(python, out) PyObject*;
%typemap(python, out) StringVec*;
%typemap(python, newfree) StringVec*;

#endif // OOFCANVAS_SWG
