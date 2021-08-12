// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// TODO GTK3: This assumes that users are using the same version of
// swig that we are, which is almost certainly not true.  Should all
// of PythonCanvas be moved out of OOFCanvas and into OOF2?  

#ifndef OOFCANVAS_SWG
#define OOFCANVAS_SWG

%module oofcanvas

%pragma(python) include="oofcanvas.spy"

%{
#include "oofcanvas.h"
using namespace OOFCanvas;
using namespace std;

typedef std::vector<CanvasItem*> CanvasItemList;
typedef std::vector<CanvasLayer*> CanvasLayerList;
typedef std::vector<std::string> OOFCanvasStringVec;
typedef std::vector<OOFCanvas::Coord> CanvasCoordVec;
typedef std::vector<double> CanvasDoubleVec;
typedef OOFCanvas::Coord CanvasCoord;
typedef OOFCanvas::ICoord CanvasICoord;
%}

%typemap(python, out) PyObject* {
  // typemap(python, out) PyObject*				 
  $target = $source;
}

%typemap(python, in) PyObject* {
  // typemap(python, in) PyObject*
  $target = $source;
}

%typemap(python, out) CanvasItem* {
  // typemap(python, out) CanvasItem*				   
  $target = $source->pythonObject();
}

// Convert a std::vector<CanvasItem*> to a Python list.
%typemap(python, out) CanvasItemList* {
  // typemap(python, out) CanvasItemList*
  CanvasItemList::size_type sz = $source->size();
  $target = PyList_New((Py_ssize_t) sz);
  for(std::vector<CanvasItem*>::size_type i=0; i<sz; i++) {
    // pythonObject returns a new reference and PyList_SET_ITEM steals it
    PyObject *item = (*$source)[i]->pythonObject();
    if(!item)
      return nullptr;
    PyList_SET_ITEM($target, (Py_ssize_t) i, item);
  }
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
%typemap(python, out) OOFCanvasStringVec* {
  // typemap(python, out) OOFCanvasStringVec*
  OOFCanvasStringVec::size_type sz = $source->size();
  $target = PyList_New((Py_ssize_t) sz);
  for(OOFCanvasStringVec::size_type i=0; i<sz; i++) {
    PyObject *str = PyString_FromString((*$source)[i].c_str());
    PyList_SET_ITEM($target, (Py_ssize_t) i, str); // Steals reference.
  }
}

// Convert a list of swigged CanvasLayer*s to a std::vector<CanvasLayer*>
%typemap(python, in) CanvasLayerList* (CanvasLayerList vec) {
  // typemap(python, in) CanvasLayerList*
  if(!PyList_Check($source)) {
    PyErr_SetString(PyExc_TypeError, "Type error in CanvasLayerList* typemap.  Python list CanvasLayers expected.");
    return nullptr;
  }
  CanvasLayerList::size_type sz =
    Py_SAFE_DOWNCAST(PyList_Size($source),
		     Py_ssize_t, CanvasLayerList::size_type);
  vec.resize(sz);
  for(CanvasLayerList::size_type i=0; i<sz; i++) {
    PyObject *strobj = PyObject_GetAttrString(PyList_GET_ITEM($source,
							      (Py_ssize_t) i),
					      "this");
    if(!strobj)
      return nullptr;
    char *str = PyString_AsString(strobj);
    Py_XDECREF(strobj);
    CanvasLayer *layer;
    SWIG_GetPtr(str, (void**) &layer, "_CanvasLayer_p");
    vec[i] = layer;
  }
  $target = &vec;
}

%typemap(python, newfree) OOFCanvasStringVec *{
  // typemap(python, newfree) OOFCanvasStringVec*
  delete $source;
}

// Convert any Python object that supports __getitem__ 
// to a OOFCanvas::Coord.  OOFCanvas::Coord itself is not
// swigged.  TODO: Should it be?

%typemap(python, in) CanvasCoord* (CanvasCoord pt) {
  // typemap(python, in) CanvasCoord*
  static PyObject *zero = nullptr;
  static PyObject *one = nullptr;
  if(!zero) {
    zero = PyInt_FromLong(0);
    one = PyInt_FromLong(1);
    Py_INCREF(zero);
    Py_INCREF(one);
  }
  PyObject *x = PyObject_GetItem($source, zero);
  PyObject *y = PyObject_GetItem($source, one);
  if(x == nullptr || y == nullptr) {
    PyErr_SetString(PyExc_TypeError, "Type error in CanvasCoord typemap");
    return nullptr;
  }
  pt.x = PyFloat_AsDouble(x);
  pt.y = PyFloat_AsDouble(y);
  Py_XDECREF(x);
  Py_XDECREF(y);
  $target = &pt;
}

%typemap(python, out) CanvasCoord* {
  // typemap(python, out) CanvasCoord*
  // Convert an OOFCanvas::Coord to a tuple
  $target = Py_BuildValue("dd", $source->x, $source->y);
}

%typemap(python, newfree) CanvasCoord *{
  // typemap(python, newfree) CanvasCoord*
  delete $source;
}

%typemap(python, in) CanvasICoord* (CanvasICoord pt) {
  // typemap(python, in) CanvasICoord*
  static PyObject *zero = nullptr;
  static PyObject *one = nullptr;
  if(!zero) {
    zero = PyInt_FromLong(0);
    one = PyInt_FromLong(1);
    Py_INCREF(zero);
    Py_INCREF(one);
  }
  PyObject *x = PyObject_GetItem($source, zero);
  PyObject *y = PyObject_GetItem($source, one);
  if(x == nullptr || y == nullptr) {
    PyErr_SetString(PyExc_TypeError, "Type error in CanvasICoord typemap");
    return nullptr;
  }
  pt.x = PyInt_AsLong(x);
  pt.y = PyInt_AsLong(y);
  Py_XDECREF(x);
  Py_XDECREF(y);
  $target = &pt;
}

%typemap(python, out) CanvasICoord* {
  // typemap(python, out) CanvasICoord*
  $target = Py_BuildValue("dd", $source->x, $source->y);
}

%typemap(python, newfree) CanvasICoord* {
  delete $source;
}

// Create a vector of Coords from any iterable object whose contents
// have a __getitem__ that returns x (0) and y (1) components.

%typemap(python, in) CanvasCoordVec* (CanvasCoordVec vec) {
  // typemap(python, in) CanvasCoordVec*
  if(!PySequence_Check($source)) {
    PyErr_SetString(PyExc_TypeError,
    "Type error in CanvasCoordVec typemap.  Python sequence expected.");
    return nullptr;
  }
  static PyObject *zero = nullptr;
  static PyObject *one = nullptr;
  if(!zero) {
    zero = PyInt_FromLong(0);
    one = PyInt_FromLong(1);
    Py_INCREF(zero);
    Py_INCREF(one);
  }
  CanvasCoordVec::size_type sz =
    Py_SAFE_DOWNCAST(PySequence_Size($source), Py_ssize_t,
		     CanvasCoordVec::size_type);
  vec.resize(sz);
  for(CanvasCoordVec::size_type i=0; i<sz; i++) {
    PyObject *item = PySequence_GetItem($source, (Py_ssize_t) i);
    PyObject *x = PyObject_GetItem(item, zero);
    PyObject *y = PyObject_GetItem(item, one);
    if(x == nullptr || y == nullptr) {
      return nullptr;
    }
    vec[i].x = PyFloat_AsDouble(x);
    vec[i].y = PyFloat_AsDouble(y);
    Py_XDECREF(x);
    Py_XDECREF(y);
  }
  $target = &vec;
}

// Convert a Python sequence of numbers to a C++ vector of floats.

%typemap(python, in) CanvasDoubleVec* (CanvasDoubleVec vec) {
  // typemap(python, in) DoubleList*
  if(!PySequence_Check($source)) {
    PyErr_SetString(PyExc_TypeError,
		    "Error in CanvasDoubleVec typemap, expected a sequence of numbers.");
    return nullptr;
  }
  CanvasDoubleVec::size_type sz = Py_SAFE_DOWNCAST(PySequence_Size($source),
						   Py_ssize_t,
						   CanvasDoubleVec::size_type);
  if(sz > 0) {
    vec.resize(sz);
    for(CanvasDoubleVec::size_type i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($source, (Py_ssize_t) i);
      if(PyFloat_Check(x))
	vec[i] = PyFloat_AsDouble(x);
      else if(PyInt_Check(x))
	vec[i] = PyInt_AsLong(x);
      else {
	PyErr_SetString(PyExc_TypeError,
			"Error in CanvasDoubleVec typemap.  Expected a sequence of numbers.");
	return nullptr;
      }
      Py_XDECREF(x);
    }
  }
  $target = &vec;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

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
  // The destructor is not swigged, so destroying a CanvasItem wrapper
  // in Python does not destry the C++ object.  C++ CanvasItems are
  // owned by their CanvasLayer and are destroyed when removed from
  // the layer.
  ~CanvasItem();
public:
  void drawBoundingBox(double, Color);
};

class CanvasShape : public CanvasItem {
public:
  void setLineWidth(double);
  void setLineWidthInPixels(double);
  void setLineColor(Color);
  void setLineJoin(CairoLineJoin);
  void setLineCap(CairoLineCap);
  void setDash(CanvasDoubleVec*, int); 
  void setDashInPixels(CanvasDoubleVec*, int);
  void setDashColor(Color);
};

class CanvasFillableShape : public CanvasShape {
public:
  void setFillColor(Color);
};

class CanvasRectangle : public CanvasFillableShape {
public:
  CanvasRectangle(CanvasCoord*, CanvasCoord*);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasSegment : public CanvasShape {
public:
  CanvasSegment(CanvasCoord*, CanvasCoord*);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasSegments : public CanvasShape {
public:
  CanvasSegments();
  void addSegment(CanvasCoord*, CanvasCoord*);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasCurve : public CanvasShape {
public:
  CanvasCurve();
  void addPoint(CanvasCoord*);
  void addPoints(CanvasCoordVec*);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasPolygon : public CanvasFillableShape {
public:
  CanvasPolygon();
  void addPoint(CanvasCoord*);
  void addPoints(CanvasCoordVec*);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasCircle : public CanvasFillableShape {
public:
  CanvasCircle(CanvasCoord*, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasEllipse : public CanvasFillableShape {
public:
  CanvasEllipse(CanvasCoord*, CanvasCoord*, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasDot : public CanvasFillableShape {
public:
  CanvasDot(CanvasCoord*, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasArrowhead : public CanvasItem {
public:
  CanvasArrowhead(CanvasSegment*, double, bool);
  void setSize(double, double);
  void setSizeInPixels(double, double);
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }
};

class CanvasText : public CanvasItem {
public:
  CanvasText(CanvasCoord*, char*);
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
  void setSize(CanvasCoord*);
  void setSizeInPixels(CanvasCoord*);
  void setDrawIndividualPixels(bool);
  
  %addmethods {
    %new const string *__repr__() {
      return self->repr();
    }
  }

  %new static CanvasImage *newBlankImage(CanvasCoord*, CanvasICoord*, Color);
  %new static CanvasImage *newFromPNGFile(CanvasCoord*, char*);
  %new static CanvasImage *newFromImageMagickFile(CanvasCoord*, char*);
};


class CanvasLayer {
private:
  CanvasLayer();		// private constructor is not swigged
public:
  ~CanvasLayer();
  bool empty();
  void destroy();
  void addItem(CanvasItem*);
  void removeAllItems();
  void rebuild();
  void clear();
  void markDirty();
  void render();
  void setClickable(bool);
  void setOpacity(double);
  void show();
  void hide();
  void raiseBy(int);
  void lowerBy(int);
  void raiseToTop();
  void lowerToBottom();
  void writeToPNG(char*);
  %addmethods {
    const char *name() {
      return self->name.c_str();
    }
  }
};

class OffScreenCanvas {
public:
  OffScreenCanvas(double);
  ~OffScreenCanvas();
  CanvasLayer *newLayer(char*);
  void deleteLayer(CanvasLayer*);
  CanvasLayer *getLayer(int);
  %name(getLayerByName) CanvasLayer *getLayer(char*);
  int nLayers();
  bool empty();
  void raiseLayer(int, int);
  void lowerLayer(int, int);
  void lowerLayerToBottom(int);
  void raiseLayerToTop(int);
  void reorderLayers(CanvasLayerList*);
  void clear();
  void draw();
  double getPixelsPerUnit();
  void setAntialias(bool);
  void setMargin(double);
  void setBackgroundColor(Color);
  %name(clickedItems) %new CanvasItemList* clickedItems_new(CanvasCoord*);
  %name(allItems) %new CanvasItemList* allItems_new();
  bool saveAsPDF(char*, int, bool);
  bool saveAsPNG(char*, int, bool);
  bool saveRegionAsPDF(char*, int, bool, CanvasCoord*, CanvasCoord*);
  bool saveRegionAsPNG(char*, int, bool, CanvasCoord*, CanvasCoord*);

  %new CanvasCoord *pixel2user(int, int);
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

%new OOFCanvasStringVec *list_fonts();


%typemap(python, in) PyObject*;
%typemap(python, out) PyObject*;
%typemap(python, out) OOFCanvasStringVec*;
%typemap(python, newfree) OOFCanvasStringVec*;
// TODO GTK3: Complete this list?
%typemap(python, out) CanvasItem*;

#endif // OOFCANVAS_SWG
