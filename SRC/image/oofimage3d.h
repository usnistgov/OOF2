// -*- C++ -*-
// $RCSfile: oofimage3d.h,v $
// $Revision: 1.6 $
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

#include <oofconfig.h>

#ifndef OOFIMAGE3D_H
#define OOFIMAGE3D_H

#include <Python.h>
//#include "common/abstractimage.h"
#include "common/array.h"
#include "common/ccolor.h"
#include "common/colordifference.h"
#include "common/coord.h"
#include "common/ooferror.h"
#include "common/timestamp.h"
#include <string>
#include <vector>
#include "vtk-5.0/vtkImageData.h"
#include "vtk-5.0/vtkVolume.h"
#include "vtk-5.0/vtkPythonUtil.h"
#include "vtk-5.0/vtkObject.h"
#include "vtk-5.0/vtkObjectBase.h"
#include "vtk-5.0/vtkImageAlgorithm.h"
#include "vtk-5.0/vtkAlgorithm.h"
#include "vtk-5.0/vtkSmartPointer.h"

//class BitmapOverlay;
class BoolArray;
//class DoubleArray;
class CMicrostructure;
//class StringImage;
// class OOFImage3DIterator;
// class ConstOOFImage3DIterator;

/*----------*/

typedef std::vector<vtkImageAlgorithm *> pipeline_vector;

class OOFImage3D {
protected:
  std::string name_;
  vtkImageData *image;
  pipeline_vector pipeline;
  Coord size_; 
  ICoord sizeInPixels_;  // width, height, depth.
  double scale;			// converts from int rgb to doubles in [0,1]
  void setup();
  TimeStamp timestamp;
  CMicrostructure *microstructure;

public:
  OOFImage3D(const std::string &nm);
  OOFImage3D(const std::string &name, const std::string &type, const std::string &filepattern, int numfiles);
	OOFImage3D(const std::string &name, const ICoord &isize, const std::vector<unsigned short> *data);
	virtual ~OOFImage3D();

  const std::string &name() const { return name_; }
  void rename(const std::string &nm) { name_ = nm; }
	void setSize(const Coord*);

  virtual const Coord &size() const { return size_; }
  virtual const ICoord &sizeInPixels() const { return sizeInPixels_; };

  void setMicrostructure(CMicrostructure *ms) { microstructure = ms; }
  CMicrostructure *getCMicrostructure() const { return microstructure; }
  void removeMicrostructure() { microstructure = 0; }

  OOFImage3D *clone(const std::string &name) const;

  void getColorPoints(const CColor &reference,
		      const ColorDifference &diff,
		      BoolArray &selected) const;

  TimeStamp *getTimeStamp() { return &timestamp; }

  void save(const std::string &filepattern);

//   typedef OOFImage3DIterator iterator;
//   typedef ConstOOFImage3DIterator const_iterator;

//   iterator begin();
//   const_iterator begin() const;
//   iterator end();
//   const_iterator end() const;

  const CColor operator[](const ICoord &c) const;
  // Version taking ICoord* arg is provided for use in SWIG typemaps.
  const CColor operator[](const ICoord *c) const { return operator[](*c); }

  bool compare(const OOFImage3D&, double) const;

  std::vector<unsigned short> *getPixels();
  
  void padImage(int amount);
  // 	vtkImageData* makeAlphaChannel();
  vtkImageData* getRGB();
  vtkImageData* getRGBA();
  vtkImageData* getAlpha();
  void combineChannels(vtkImageData *color, vtkImageData *alpha);
  
  PyObject* getVolumeActor();
  // We need this for the python based canvas for now.
  PyObject* getImageData() {return vtkPythonGetObjectFromPointer(image); };
  void addImageToPicker(PyObject*);
  
  void imageChanged();		// call this when done setting pixels.
  
  void gray();
  void threshold(double T);
  void blur(double radius, double sigma);
  void dim(double factor);
  void fade(double factor);
  void negate(double dummy);
  void medianFilter(int radius);
  void normalize();
  void flip(const std::string &axis);


};

OOFImage3D *newImageFromData(const std::string &name,
			   const ICoord *isize,
			   const std::vector<unsigned short> *data);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// class OOFImage3DIterator {
// private:
//   OOFImage3DIterator(OOFImage3D &image, int pos)
//     : pos(pos), image(image)
//   {}
//   int pos;
//   OOFImage3D &image;
// public:
//   void operator++() { pos++; }
//   CColor operator*() const { return image[coord()]; }
//   ICoord coord() const;
//   friend class OOFImage;
//   friend bool operator==(const OOFImage3DIterator&, const OOFImage3DIterator&);
//   friend bool operator!=(const OOFImage3DIterator&, const OOFImage3DIterator&);
// };

// class ConstOOFImage3DIterator {
// private:
//   ConstOOFImage3DIterator(const OOFImage3D &image, int pos)
//     : pos(pos), image(image)
//   {}
//   int pos;
//   const OOFImage3D &image;
// public:
//   void operator++() { pos++; }
//   const CColor operator*() const { return image[coord()]; }
//   ICoord coord() const;
//   friend class OOFImage;
//   friend bool operator==(const ConstOOFImage3DIterator&,
// 			 const ConstOOFImage3DIterator&);
//   friend bool operator!=(const ConstOOFImage3DIterator&,
// 			 const ConstOOFImage3DIterator&);
// };

#endif // OOFIMAGE3D_H
