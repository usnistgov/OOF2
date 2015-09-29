// -*- C++ -*-
// $RCSfile: oofimage3d.swg,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2014/09/27 21:41:27 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFIMAGE3D_SWG
#define OOFIMAGE3D_SWG
%module oofimage3d
%include "common/typemaps.swg"
%{
#include "image/oofimage3d.h"
#include "common/ooferror.h"
#include <oofconfig.h>
#include "common/doublearray.h"
#include "common/boolarray.h"
%}

%pragma(python) include="oofimage3d.spy"
%extern "common/IO/bitoverlay.swg"
%extern "common/ccolor.swg"
%extern "common/timestamp.swg"
%extern "common/ooferror.swg"
//%extern "common/abstractimage.swg"
%extern "common/IO/stringimage.swg"

%extern "common/doublearray.swg"
%pragma(python) code="from ooflib.SWIG.common.doublearray import DoubleArrayPtr"
%extern "common/boolarray.swg"
%pragma(python) code="from ooflib.SWIG.common.boolarray import BoolArrayPtr"
%pragma(python) code="from ooflib.SWIG.common.boolarray import BoolArrayPtr"
%pragma(python) code="from ooflib.SWIG.common.ccolor import CColorPtr"
%pragma(python) code="from ooflib.SWIG.common.timestamp import TimeStampPtr"
%pragma(python) code="from ooflib.SWIG.common.ooferror import ErrErrorPtr"
%pragma(python) code="from ooflib.SWIG.common.abstractimage import AbstractImagePtr"

// To pass vtk objects from c++ to python and vice versa, all we have
// to do is use the builtin vtkPythonUtil class and make passed back
// type a pyObject.  It's that easy!


class OOFImage3D { //: public AbstractImage {
public:
  OOFImage3D(char *name, char *firstimage, char *filepattern, int numfiles);
  ~OOFImage3D();

  string name();
  void rename(char *);

  void setSize(Coord *Point);
  Coord size();
  ICoord sizeInPixels();

  void setMicrostructure(CMicrostructure*);
  CMicrostructure *getCMicrostructure();
  void removeMicrostructure();

  bool compare(OOFImage3D&, double);

	void save(char *filepattern);

  OOFImage3D *clone(char *name);

  // getTimeStamp is redefined in oofimage.spy so that it can have optional args
  %name(_getTimeStamp) TimeStamp *getTimeStamp();
  %addmethods {
    CColor __getitem__(ICoord *iPoint) {
      return (*self)[iPoint];
    }
  }

	PyObject *getVolumeActor();
	//void addImageToPicker(PyObject*);
	PyObject *getImageData();

  %new ShortVec *getPixels();

  void gray();
  void threshold(double T);
  void blur(double radius, double sigma);
	void dim(double factor);
	void fade(double factor);
	void negate(double dummy);
	void medianFilter(int radius);
	void normalize();
	void flip(char *axis);


};


%new OOFImage3D *newImageFromData(char *name, ICoord *iPoint, ShortVec*);

#endif // OOFIMAGE3D_SWG
