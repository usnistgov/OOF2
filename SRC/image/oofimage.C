// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifdef HAVE_MPI
#include "common/mpitools.h"
#endif ////HAVE_MPI
#include "common/IO/bitoverlay.h"
#include "common/boolarray.h"
#include "common/doublearray.h"
#include "common/ooferror.h"
#include "common/pythonlock.h"
#include "common/pyutils.h"
#include "image/oofimage.h"

#include <oofcanvas.h>

#include <math.h>
#include <set>
#include <iostream>

OOFImage::OOFImage(const std::string &name, PyObject *pyobj)
  : name_(name), npobject(nullptr)
{
  setNpImage(pyobj);
  setup();
  imageChanged();
}

void OOFImage::setNpImage(PyObject *new_npimage) {
  PYTHON_THREAD_BEGIN_BLOCK;
  if(new_npimage != (PyObject*) npobject) {
    Py_XINCREF(new_npimage);
    Py_XDECREF((PyObject*) npobject);
    npobject = (PyArrayObject*) new_npimage;
  }
}

OOFImage::OOFImage(const std::string &name)
  : name_(name), npobject(nullptr)
{}


void OOFImage::setup() {
  npy_intp *dims = PyArray_DIMS(npobject);
  sizeInPixels_ = ICoord(dims[1], dims[0]);
}


OOFImage::~OOFImage() {
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_XDECREF(npobject);
}

// Tolerant comparison -- returns a boolean true if the other image
// is within tolerance of this image, otherwise returns false.
bool OOFImage::compare(const OOFImage &other, double tol) const {
  if (sizeInPixels_ != other.sizeInPixels_) return false;

  for(int i=0;i<sizeInPixels_[0];i++) {
    for(int j=0;j<sizeInPixels_[1];j++) {
      CColor c0 = (*this)[ICoord(i,j)];
      CColor c1 = other[ICoord(i,j)];
      if (!c0.compare(c1, tol))
	return false;
    }
  }
  return true;
}

void OOFImage::setSize(const Coord *sighs) {
  size_ = *sighs;
}

ICoord OOFImage::pixelFromPoint(const Coord *point) const {
  double xx = (*point)[0]/size_[0]*sizeInPixels_[0];
  double yy = (*point)[1]/size_[1]*sizeInPixels_[1];
  if (xx == sizeInPixels_[0])
    xx = sizeInPixels_[0] - 1.0;
  if (yy == sizeInPixels_[1])
    yy = sizeInPixels_[1] - 1.0;

  return ICoord((int) floor(xx), (int) floor(yy));
}

bool OOFImage::pixelInBounds(const ICoord *pxl) const {
  int xx = (*pxl)[0];
  int yy = (*pxl)[1];
  if ( (xx<0) || (xx>=sizeInPixels_[0]) || (yy<0) || (yy>=sizeInPixels_[1]) )
    return false;
  return true;
}

OOFImage *OOFImage::clone(const std::string &nm , PyObject *npobject) const {
  // Clone is always called after copying the numpy image data in
  // python, where it's easier to do.
  OOFImage *copy = new OOFImage(nm, npobject);
  copy->setup();
  copy->size_ = size_;
  copy->setMicrostructure(microstructure);
  return copy;
}

void OOFImage::imageChanged() {
  ++timestamp;			// marks image as changed
  // TODO NUMPY: Is there an equivalent to this?  Copy the image to
  // ensure changes are applied?
  
  //image.modifyImage(); 
}

OOFCanvas::CanvasImage *OOFImage::makeCanvasImage(const Coord *pos,
						  const Coord *size)
  const
{
  // The OOFImage constructor flips the image so that OOF can access
  // pixels easily in a right handed coordinate system with the origin
  // in the lower left corner of the image.  This has to flip it back.
  
  // { // Debugging block
  //   PYTHON_THREAD_BEGIN_BLOCK;

  //   std::cerr << "OOFImage::makeCanvasImage: npobject=" << npobject
  //     //<< " " << repr((PyObject*)npobject)
  // 	      << " size=" << *size
  // 	      << std::endl;
  //   std::cerr << "OOFImage::makeCanvasImage: shape="
  // 	      << repr(PyObject_GetAttrString((PyObject*) npobject, "shape"))
  // 	      << " dtype="
  // 	      << repr(PyObject_GetAttrString((PyObject*) npobject, "dtype"))
  // 	      << " array(0,0,0)="
  // 	      << *((double*)PyArray_GETPTR3(npobject, 0, 0, 0))
  //     // << " size=" << PyArray_Size(npobject)
  // 	      << std::endl;
  //   // PyArray_Size, PyArray_Min, and PyArray_Max don't seem to work!
  //   // Get min and max the hard way.
  //   double amin = std::numeric_limits<double>::max();
  //   double amax = -amin;
  //   npy_intp *dims = PyArray_DIMS(npobject);
  //   for(int x=0; x<dims[0]; x++) {
  //     for(int y=0; y<dims[1]; y++) {
  // 	for(int c=0; c<dims[2]; c++) {
  // 	  double v = *(double*)PyArray_GETPTR3(npobject, x, y, c);
  // 	  if(v < amin) amin = v;
  // 	  if(v > amax) amax = v;
  // 	}
  //     }
  //   }
  //   std::cerr << "OOFImage::makeCanvasImage: min=" << amin << " max=" << amax
  // 	      << std::endl;
  // } // end debugging

  OOFCanvas::CanvasImage *img =
    OOFCanvas::CanvasImage::newFromNumpy(OOFCANVAS_COORD(*pos),
					 (PyObject*) npobject, true/* flipy*/);
  img->setDrawIndividualPixels(true);
  img->setSize(OOFCANVAS_COORD(*size));
  return img;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

const CColor OOFImage::operator[](const ICoord &coord) const {
  int r = coord(1);		// row
  int c = coord(0);		// column
  double *red = (double*) PyArray_GETPTR3(npobject, r, c, 0);
  double *grn = red + 1;
  double *blu = red + 2; 
  return CColor(*red, *grn, *blu);
}

void OOFImage::set(const ICoord &coord, const CColor &color) {
  int r = coord(1);
  int c = coord(0);
  double *red = (double*) PyArray_GETPTR3(npobject, r, c, 0);
  double *grn = red + 1;
  double *blu = red + 2;
  *red = color.getRed();
  *grn = color.getGreen();
  *blu = color.getBlue();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Conversion to and from arrays of double, int, or bool.  This is not
// an efficient way of getting or setting just a few pixels.  These
// routines all take as an argument a function f which converts from
// CColor to the appropriate type (double, int, or bool) or vice
// versa.

// TODO OPT?: Is it better to make these functions use
// OOFImage::image::write, like OOFImage::getPixels does?  Doing so
// would require allocating another array, so it's not obviously more
// efficient.

// TODO NUMPY: The convert methods are only used to convert to gray
// scale.  We probably can do that better in numpy.

Array<double> OOFImage::convert(double (*f)(const CColor&)) const {
  Array<double> arr(sizeInPixels_[0], sizeInPixels_[1]);
  for(Array<double>::iterator i=arr.begin(); i!=arr.end(); ++i) {
    arr[i] = (*f)((*this)[i.coord()]);
  }
  return arr;
}

Array<int> OOFImage::convert(int (*f)(const CColor&)) const {
  Array<int> arr(sizeInPixels_[0], sizeInPixels_[1]);
  for(Array<int>::iterator i=arr.begin(); i!=arr.end(); ++i) {
    arr[i] = (*f)((*this)[i.coord()]);
  }
  return arr;
}

Array<bool> OOFImage::convert(bool (*f)(const CColor&)) const {
  Array<bool> arr(sizeInPixels_[0], sizeInPixels_[1]);
  for(Array<bool>::iterator i=arr.begin(); i!=arr.end(); ++i) {
    arr[i] = (*f)((*this)[i.coord()]);
  }
  return arr;
}

void OOFImage::set(const Array<double> &array, CColor (*f)(double)) {
  for(Array<double>::const_iterator i=array.begin(); i!=array.end(); ++i) 
    set(i.coord(), (*f)(array[i]));
  imageChanged();
}

void OOFImage::set(const Array<int> &array, CColor (*f)(int)) {
  for(Array<int>::const_iterator i=array.begin(); i!=array.end(); ++i)
    set(i.coord(), (*f)(array[i]));
  imageChanged();
}

void OOFImage::set(const Array<bool> &array, CColor (*f)(bool)) {
  for(Array<bool>::const_iterator i=array.begin(); i!=array.end(); ++i)
    set(i.coord(), (*f)(array[i]));
  imageChanged();
}
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void OOFImage::getColorPoints(const CColor &ref, 
			      const ColorDifference &diff,
			      BoolArray &selected)
const
{
  for(ConstOOFImageIterator i=this->begin(); i!=this->end(); ++i)
    if (diff.contains(ref, *i)) selected[i.coord()] = true;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

OOFImage::iterator OOFImage::begin() {
  return OOFImageIterator(*this, 0);
}

OOFImage::const_iterator OOFImage::begin() const {
  return ConstOOFImageIterator(*this, 0);
}

OOFImage::iterator OOFImage::end() {
  return OOFImageIterator(*this, sizeInPixels_[0]*sizeInPixels_[1]);
}

OOFImage::const_iterator OOFImage::end() const {
  return ConstOOFImageIterator(*this, sizeInPixels_[0]*sizeInPixels_[1]);
}


ICoord OOFImageIterator::coord() const {
  int width = image.sizeInPixels()[0];
  int y = pos/width;
  int x = pos - width*y;
  return ICoord(x, y);
}

ICoord ConstOOFImageIterator::coord() const {
  int width = image.sizeInPixels()[0];
  int y = pos/width;
  int x = pos - width*y;
  return ICoord(x, y);
}

bool operator==(const OOFImageIterator &a, const OOFImageIterator &b) {
  return a.pos == b.pos;
}

bool operator!=(const OOFImageIterator &a, const OOFImageIterator &b) {
  return a.pos != b.pos;
}


bool operator==(const ConstOOFImageIterator &a, const ConstOOFImageIterator &b){
  return a.pos == b.pos;
}

bool operator!=(const ConstOOFImageIterator &a, const ConstOOFImageIterator &b){
  return a.pos != b.pos;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// // Parallel image send/recv
// #ifdef HAVE_MPI

// // This section has not been updated to use scikit-image!  The MPI
// // code hasn't been checked in years.

// std::vector<unsigned short> *OOFImage::getPixels() {
//   // Magick::Image::write isn't const, so this function isn't const either.
//   int n = 3*sizeInPixels_(0)*sizeInPixels_(1);
//   std::vector<unsigned short> *pxls = new std::vector<unsigned short>(n);
//   image.write(0, 0, sizeInPixels_(0), sizeInPixels_(1),
// 	      "RGB", Magick::ShortPixel, &(*pxls)[0]);
//   return pxls;
// }

// void _Send_Image(OOFImage *image, std::vector<int> *destinations, int tag)
// {
//   std::string name = image->name();
//   _Isend_Int(name.size(), destinations, tag);  // size of the name
//   _Isend_String(name, destinations, tag);  // name itself
//   _Isend_Double(image->size()[0], destinations, tag);  // physical size X
//   _Isend_Double(image->size()[1], destinations, tag);  // physical size Y
//   _Isend_Int(image->sizeInPixels()[0], destinations, tag);  // size in pixels X
//   _Isend_Int(image->sizeInPixels()[1], destinations, tag);  // size in pixels Y

//   std::vector<unsigned short> * pixels = image->getPixels();
//   _Isend_Int(pixels->size(), destinations, tag);  // size of pixels vector
//   _Isend_UnsignedShortVec(pixels, destinations, tag);
//   delete pixels;
// }

// OOFImage *_Recv_Image(int origin, int tag)
// {
//   int name_size = _Recv_Int(origin, tag);  // size of the name
//   std::string name = _Recv_String(origin, name_size, tag);  // name itself
//   double px = _Recv_Double(origin, tag);  // physical size X
//   double py = _Recv_Double(origin, tag);  // physical size Y
//   int ix = _Recv_Int(origin, tag);  // size in pixels X
//   int iy = _Recv_Int(origin, tag);  // size in pixels Y
//   int size_pixels = _Recv_Int(origin, tag);  // size of pixels vector
//   std::vector<unsigned short> *pixels = _Recv_UnsignedShortVec(origin,
// 							       size_pixels,
// 							       tag);
//   Coord *psize = new Coord(px, py);
//   ICoord *isize = new ICoord(ix, iy);
  
//   OOFImage *image = newImageFromData(name, isize, pixels);
//   image->setSize(psize);

//   delete psize;
//   delete isize;
//   delete pixels;

//   return image;
// }
// #endif //HAVE_MPI
