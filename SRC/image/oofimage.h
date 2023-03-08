// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFIMAGE_H
#define OOFIMAGE_H

#include <oofconfig.h>

#include "common/abstractimage.h"
#include "common/array.h"
#include "common/ccolor.h"
#include "common/colordifference.h"
#include "common/coord.h"
#include "common/ooferror.h"
#include "common/timestamp.h"
#include <string>
#include <vector>

// This value of NPY_NO_DEPRECATED_API suppresses *all* numpy
// deprecation warnings, which is probably not a good idea.  Not
// defining NPY_NO_DEPRECATED_API produces deprecation warnings, and
// the suggestion to set NPY_NO_DEPRECATED_API to NPY_1_7_API_VERSION.
// But with that setting PyArray_NDIM and PyArray_DIMS aren't defined.
#define NPY_NO_DEPRECATED_API NPY_1_1_API_VERSION
#include <numpy/arrayobject.h>

class BitmapOverlay;
class BoolArray;
class DoubleArray;
class CMicrostructure;
class OOFImageIterator;
class ConstOOFImageIterator;
namespace OOFCanvas {
  class CanvasImage;
};

/*----------*/

class OOFImage : public AbstractImage {
protected:
  std::string name_;
  PyArrayObject *npobject;	// numpy python object
  Coord size_; 
  ICoord sizeInPixels_;		// width, height.
  double scale;			// converts from int rgb to doubles in [0,1]
  void setup();
  TimeStamp timestamp;
  CMicrostructure *microstructure;
public:
  OOFImage(const std::string &nm);
  OOFImage(const OOFImage&) = delete;
  OOFImage(const std::string &nm, const std::string &filename);
  OOFImage(const std::string &nm, PyObject *ndarray);
  virtual ~OOFImage();
  // void save(const std::string &filename);
  const std::string &name() const { return name_; }
  void rename(const std::string &nm) { name_ = nm; }
  void setSize(const Coord*);	// Physical size, not pixel size!

  // Get and set the PyObject storing the numpy image data.
  PyObject *npImage() { return (PyObject*) npobject; }
  void setNpImage(PyObject*);

  virtual const Coord &size() const { return size_; }
  virtual const ICoord &sizeInPixels() const { return sizeInPixels_; }
  ICoord pixelFromPoint(const Coord*) const;
  bool pixelInBounds(const ICoord*) const;
  const std::string *comment() const;

  OOFCanvas::CanvasImage *makeCanvasImage(const Coord*, const Coord*) const;

  void setMicrostructure(CMicrostructure *ms) { microstructure = ms; }
  CMicrostructure *getCMicrostructure() const { return microstructure; }
  void removeMicrostructure() { microstructure = 0; }

  typedef OOFImageIterator iterator;
  typedef ConstOOFImageIterator const_iterator;

  iterator begin();
  const_iterator begin() const;
  iterator end();
  const_iterator end() const;

  const CColor operator[](const ICoord &c) const;
  const CColor operator[](const ICoord *c) const { return operator[](*c); }
  // Since OOFImage isn't actually made up of CColors, it's hard to
  // use operator[] to set values.  Use this instead:
  void set(const ICoord&, const CColor&);
  void imageChanged();		// call this when done setting pixels.

  // Convert to an Array of doubles.  f is a function that takes a
  // CColor and returns a double.
  Array<double> convert(double (*f)(const CColor&)) const;
  // Same for ints and bools.
  Array<int> convert(int (*f)(const CColor&)) const;
  Array<bool> convert(bool (*f)(const CColor&)) const;
  // Set pixels in the image to values from an array.  These call imageChanged()
  void set(const Array<double> &array, CColor (*f)(double));
  void set(const Array<int> &array, CColor (*f)(int));
  void set(const Array<bool> &array, CColor (*f)(bool));

  OOFImage *clone(const std::string &name, PyObject *npimage) const;

  void getColorPoints(const CColor &reference,
		      const ColorDifference &diff,
		      BoolArray &selected) const;

  bool compare(const OOFImage&, double) const;

  // void flip(const std::string &axis);
  // void fade(double);
  // void dim(double);

  TimeStamp *getTimeStamp() { return &timestamp; }

  // void blur(double radius, double sigma);
  // void contrast(bool sharpen);
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
  void evenly_illuminate(int windowsize);
};				// class OOFImage

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Parallel image send/recv   -- obsolete?
#ifdef HAVE_MPI
void _Send_Image(OOFImage*, std::vector<int>*, int);
OOFImage *_Recv_Image(int, int);
#endif //HAVE_MPI

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class OOFImageIterator {
private:
  OOFImageIterator(OOFImage &image, int pos)
    : pos(pos), image(image)
  {}
  int pos;
  OOFImage &image;
public:
  void operator++() { pos++; }
  CColor operator*() const { return image[coord()]; }
  ICoord coord() const;
  friend class OOFImage;
  friend bool operator==(const OOFImageIterator&, const OOFImageIterator&);
  friend bool operator!=(const OOFImageIterator&, const OOFImageIterator&);
};

class ConstOOFImageIterator {
private:
  ConstOOFImageIterator(const OOFImage &image, int pos)
    : pos(pos), image(image)
  {}
  int pos;
  const OOFImage &image;
public:
  void operator++() { pos++; }
  const CColor operator*() const { return image[coord()]; }
  ICoord coord() const;
  friend class OOFImage;
  friend bool operator==(const ConstOOFImageIterator&,
			 const ConstOOFImageIterator&);
  friend bool operator!=(const ConstOOFImageIterator&,
			 const ConstOOFImageIterator&);
};

double color2gray(const CColor&);
CColor gray2color(double);
CColor bool2color(bool);
CColor int2color(int);

DoubleArray grayify(const OOFImage& image);
void setFromBool(OOFImage&, const BoolArray&);


BoolArray threshold(const DoubleArray&, double);

#endif // OOFIMAGE_H
