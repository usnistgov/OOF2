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

%typemap(in) PyObject *VERBATIM {
  // typemap(in) PyObject *VERBATIM
  $1 = $input;
 }

%typemap(out) PyObject* {
  // typemap(out) PyObject*
  if($1 == nullptr)
    $result = Py_None;
  else
    $result = $1;
  Py_XINCREF($result);
}

class OOFImage : public AbstractImage {
public:
  OOFImage(char *name, PyObject *VERBATIM);
  ~OOFImage();
  // void save(char *filename);
  const std::string &name();
  void rename(char *);
  %newobject comment;
  std::string *comment();
  void setSize(Coord *Point);
  
  Coord size();
  ICoord sizeInPixels();
  ICoord pixelFromPoint(Coord *Point);
  bool pixelInBounds(ICoord *iPoint);
  %newobject clone;
  OOFImage *clone(char *name, PyObject *VERBATIM);
  PyObject *npImage();
  void setNpImage(PyObject *VERBATIM);

  void setMicrostructure(CMicrostructure*);
  CMicrostructure *getCMicrostructure();
  void removeMicrostructure();

  // void flip(char *axis);
  // void fade(double);
  // void dim(double);
  // void blur(double, double);
  // void contrast(bool);
  void despeckle();
  void edge(double);
  void enhance();
  void equalize();
  void medianFilter(double);
  // void negate(bool);
  void normalize();
  void reduceNoise(double);
  void sharpen(double, double);
  // void gray();
  void evenly_illuminate(int);
  
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

// Parallel image send/recv
#ifdef HAVE_MPI
void _Send_Image(OOFImage*, const std::vector<int>*, int);
%newobject _Recv_Image;
OOFImage *_Recv_Image(int, int);
#endif //HAVE_MPI

BoolArray threshold(DoubleArray,double);

// class ImageMagickError : public ErrError {
// public:
//   ImageMagickError(char *m);
//   ~ImageMagickError();
// };
// WRAP_OOFERROR_CLASS(ImageMagickError);

DoubleArray grayify(const OOFImage& image);
void setFromBool(OOFImage&, const BoolArray&);

%pythoncode "image/oofimage.spy"

#endif // OOFIMAGE_SWG
