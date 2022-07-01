// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CANVASIMAGE_SWG
#define CANVASIMAGE_SWG

// TODO PYTHON3: How much of this is necessary?

// The CanvasImage and NewCanvasImage typemaps are for returning an
// OOFCanvas::CanvasImage from C++ to Python.  This requires some
// extra work because we can't use %extern "oofcanvas/oofcanvas.swg",
// since that file isn't part of OOF2.  So these typemaps explicitly
// do what would have been done if swig had known about the
// OOFCanvas::CanvasImage class.  The NewCanvasImage* typemap is
// equivalent to %new CanvasImage*.

// These aren't in common/typemaps.swg in order to avoid including
// oofcanvas.h in all swig C++ output files.

%{
  #include <oofcanvas.h>
  typedef OOFCanvas::CanvasImage CanvasImage;
  typedef OOFCanvas::CanvasImage NewCanvasImage;
%}

%typemap(python, out) CanvasImage* {
   // typemap(python, out) CanvasImage*
  $result = $1->pythonObject();

  // TODO PYTHON3: Why was calling pythonObject() not sufficient before?
  
   // static PyObject *canvasImageClass = 0;
   // if(!canvasImageClass) {
   //   PyObject *module = PyImport_ImportModule("oofcanvas");
   //   canvasImageClass = PyObject_GetAttrString(module, "CanvasImage");
   //   Py_XDECREF(module);
   //   if(!canvasImageClass) return 0;
   // }
   // char _ptmp[128];
   // SWIG_MakePtr(_ptmp, (char*) $source, "_CanvasImage_p");
   // PyObject *swigthis = Py_BuildValue("(s)", _ptmp);
   // PyObject *ci = PyObject_CallObject(canvasImageClass, swigthis);
   // Py_XDECREF(swigthis);
   // $target = ci;
}

// TODO PYTHON3: Do we need this?  Why not just use %newobject?

%typemap(python, out) NewCanvasImage* {
   // typemap(python, out) CanvasImage*
  $result = $1->pythonObject();
   // static PyObject *canvasImageClass = 0;
   // static PyObject *pyOne;
   // if(!canvasImageClass) {
   //   PyObject *module = PyImport_ImportModule("oofcanvas");
   //   canvasImageClass = PyObject_GetAttrString(module, "CanvasImage");
   //   Py_XDECREF(module);
   //   if(!canvasImageClass) return 0;
   //   pyOne = PyInt_FromLong(1);
   // }
   // char _ptmp[128];
   // SWIG_MakePtr(_ptmp, (char*) $source, "_CanvasImage_p");
   // PyObject *swigthis = Py_BuildValue("(s)", _ptmp);
   // $target = PyObject_CallObject(canvasImageClass, swigthis);
   // Py_XDECREF(swigthis);
   // // Take ownership
   // PyObject_SetAttrString($target, "thisown", pyOne);
}


#endif // CANVASIMAGE_SWG
