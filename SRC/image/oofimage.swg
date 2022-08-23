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

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%include "common/ooferrorwrappers.swg"
%import "common/IO/bitoverlay.swg"
%import "common/abstractimage.swg"
%import "common/boolarray.swg"
%import "common/canvasimage.swg"
%import "common/ccolor.swg"
%import "common/doublearray.swg"
%import "common/ooferror.swg"
%import "common/timestamp.swg"
#endif // NOSECONDIMPORTS

%{
#include "oofcanvas/canvasimage.h"
#include "common/boolarray.h"
#include "common/doublearray.h"
#include "common/ooferror.h"
#include "image/oofimage.h"
%}

// %pragma(python) code="from ooflib.SWIG.common.doublearray import DoubleArrayPtr"
// %pragma(python) code="from ooflib.SWIG.common.boolarray import BoolArrayPtr"
// %pragma(python) code="from ooflib.SWIG.common.boolarray import BoolArrayPtr"
// %pragma(python) code="from ooflib.SWIG.common.ccolor import CColorPtr"
// %pragma(python) code="from ooflib.SWIG.common.timestamp import TimeStampPtr"
// %pragma(python) code="from ooflib.SWIG.common.ooferror import ErrErrorPtr"
// %pragma(python) code="from ooflib.SWIG.common.abstractimage import AbstractImagePtr"

class OOFImage : public AbstractImage {
public:
  OOFImage(char *name, char *filename);
  ~OOFImage();
  void save(char *filename);
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
  OOFImage *clone(char *name);

  void setMicrostructure(CMicrostructure*);
  CMicrostructure *getCMicrostructure();
  void removeMicrostructure();

  %newobject getPixels;
  std::vector<unsigned short> *getPixels();
  void flip(char *axis);
  void fade(double);
  void dim(double);
  void blur(double, double);
  void contrast(bool);
  void despeckle();
  void edge(double);
  void enhance();
  void equalize();
  void medianFilter(double);
  void negate(bool);
  void normalize();
  void reduceNoise(double);
  void sharpen(double, double);
  void gray();
  void evenly_illuminate(int);
  
  bool compare(OOFImage&, double);
  %newobject makeCanvasImage;
  OOFCanvas::CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);

  // getTimeStamp is redefined in oofimage.spy so that it can have optional args
  %rename(_getTimeStamp) getTimeStamp;
  TimeStamp *getTimeStamp();
};

%extend OOFImage {
  CColor __getitem__(ICoord *iPoint) {
    return (*self)[iPoint];
  }
};

%newobject newImageFromData;
OOFImage *newImageFromData(char *name, ICoord *iPoint,
			   const std::vector<unsigned short>*);

// Parallel image send/recv
#ifdef HAVE_MPI
void _Send_Image(OOFImage*, IntVec*, int);
%newobject _Recv_Image;
OOFImage *_Recv_Image(int, int);
#endif //HAVE_MPI

BoolArray threshold(DoubleArray,double);

class ImageMagickError : public ErrError {
public:
  ImageMagickError(char *m);
  ~ImageMagickError();
};
WRAP_OOFERROR_CLASS(ImageMagickError);
ADD_REPR(ImageMagickError, summary);

DoubleArray grayify(const OOFImage& image);
void setFromBool(OOFImage&, const BoolArray&);

%pythoncode "image/oofimage.spy"

#endif // OOFIMAGE_SWG
