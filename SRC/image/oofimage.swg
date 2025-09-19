// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFIMAGE_SWG
#define OOFIMAGE_SWG

%module(package="ooflib.SWIG.image") oofimage

%include "common/typemaps.swg"
%include "common/canvasimage.swg"
%include "common/ooferrorwrappers.swg"
%import "common/IO/bitoverlay.swg"
%import "common/abstractimage.swg"
%import "common/boolarray.swg"
%import "common/ccolor.swg"
%import "common/coord.swg"
%import "common/doublearray.swg"
%import "common/ooferror.swg"
%import "common/timestamp.swg"

%{
#include "oofcanvas/canvasimage.h"
#include "common/boolarray.h"
#include "common/doublearray.h"
#include "common/ooferror.h"
#include "image/oofimage.h"
%}

// The numpy PyArrayObject is "derived" from PyObject, but both are
// just C structs, not real C++ classes.  That's why we need explicit
// C-style casts in these typemaps.

%typemap(in) PyArrayObject*  {
  // typemap(in) PyArrayObject* 
  $1 = (PyArrayObject*) $input;
}

%typemap(out) PyArrayObject* {
  // typemap(out) PyArrayObject*
  if($1 == nullptr)
    $result = Py_None;
  else
    $result = (PyObject*) $1;
  Py_XINCREF($result);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class OOFImage : public AbstractImage {
public:
  OOFImage(char *name, PyArrayObject*, bool);
  ~OOFImage();
  const std::string &name();
  void rename(char *);
  void setSize(Coord *Point);
  bool isGray();
  
  Coord size();
  ICoord sizeInPixels();
  ICoord pixelFromPoint(Coord *Point);
  bool pixelInBounds(ICoord *iPoint);
  %newobject cclone;
  OOFImage *cclone(char *name, PyArrayObject*, bool);
  PyArrayObject *npImage();
  void setNpImage(PyArrayObject*, bool);

  void setMicrostructure(CMicrostructure*);
  CMicrostructure *getCMicrostructure();
  void removeMicrostructure();

  void evenly_illuminate(int);
  void enhance_contrast(PyArrayObject*, PyArrayObject*);
  void reduce_noise(PyArrayObject*, PyArrayObject*);
  
  bool compare(OOFImage&, double);
  CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);

  // getTimeStamp is redefined in oofimage.spy so that it can have optional args
  %rename(_getTimeStamp) getTimeStamp;
  TimeStamp *getTimeStamp();
};

%extend OOFImage {
  CColor __getitem__(ICoord *iPoint) {
    return (*self)[iPoint];
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Parallel image send/recv
#ifdef HAVE_MPI
void _Send_Image(OOFImage*, const std::vector<int>*, int);
%newobject _Recv_Image;
OOFImage *_Recv_Image(int, int);
#endif //HAVE_MPI

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

%pythoncode "image/oofimage.spy"

#endif // OOFIMAGE_SWG
