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

#include "image/oofimage.h"
#include "common/doublearray.h"
#include "common/pyutils.h"


PyArrayObject* OOFImage::enhance_contrast(PyArrayObject *mask,
					  PyArrayObject *newimage)
{

  // Check that image and newimage have the same shape.
  int imagedim = PyArray_NDIM(npobject);
  const npy_intp* imageshape = PyArray_SHAPE(npobject);
  int newdim = PyArray_NDIM(newimage);
  const npy_intp* newshape = PyArray_SHAPE(newimage);
  assert(PyArray_TYPE(newimage) == NPY_DOUBLE);
  assert(newdim == imagedim);
  for(int i=i; i<newdim; i++)
    assert(newshape[i] == imageshape[i]);

  // For some reason, creating the new image here, instead of creating
  // it in Python and passing it in, is failing. I'm not going to mess
  // around with it now.  TODO: Fix this.  
  // PyArrayObject *newimage = (PyArrayObject*) PyArray_EMPTY(imagedim, imageshape,
  // 							   NPY_DOUBLE, 0);
  // Py_XINCREF((PyObject*)newimage);

  int maskdim = PyArray_NDIM(mask);
  assert(maskdim == 2);
  const npy_intp* maskshape = PyArray_SHAPE(mask);
  assert(maskshape[0] > 1 && maskshape[1] > 1);

  // Get the center of the mask in mask coordinates.  The shape of the
  // mask is (2*mc0+1, 2*mc1+1).  The lengths of the edges of masks
  // created by skimage.morphology.disk are always odd.  TODO: Check
  // that this works with other mask shapes that might have even
  // lengths.
  int mc0 = maskshape[0]/2;	// integer division
  int mc1 = maskshape[1]/2;	// integer division

  // Loop over pixels in the image
  for(int p0=0; p0<imageshape[0]; p0++) {
    for(int p1=0; p1<imageshape[1]; p1++) {
      // Difference between image and mask coordinates.  Both start at
      // edges.  The mask is centered at (p0,p1).
      int d0 = p0 - mc0;	// maskcoord + d = imagecoord
      int d1 = p1 - mc1;
      // Start and end positions for looping over the mask in mask
      // coordinates.
      int m0min = 0;
      int m0max = maskshape[0];
      int m1min = 0;
      int m1max = maskshape[1];
      // The mask is centered on a pixel that may be close to the edge
      // of the image.  Make sure the edges of the mask are within the
      // image.  If not, trim the mask by adjusting the loop range.
      if(m0min + d0 < 0)
	m0min = mc0 - p0;
      if(m0max + d0 > imageshape[0])
	m0max = imageshape[0] - d0;
      if(m1min + d1 < 1)
	m1min = mc1 - p1;
      if(m1max + d1 > imageshape[1])
	m1max = imageshape[1] - d1;

      // Loop over channels
      for(int k=0; k<imageshape[2]; k++) {
	double minimum = std::numeric_limits<double>::max();
	double maximum = -minimum;
	// Loop over the mask, finding the min and max values of the
	// channel in the corresponding pixels of the image.
	for(int m0=m0min; m0<m0max; m0++) {
	  assert(m0 + d0 >= 0 && m0 + d0 < imageshape[0]);
	  for(int m1=m1min; m1<m1max; m1++) {
	    assert(m1 + d1 >= 0 && m1 + d1 < imageshape[1]);
	    if(*(int*) PyArray_GETPTR2(mask, m0, m1)) { // apply the mask
	      double val = *(double*) PyArray_GETPTR3(npobject,
						      m0+d0, m1+d1, k);
	      if(val < minimum)
		minimum = val;
	      if(val > maximum)
		maximum = val;
	    }
	  }
	} // end loop over mask

	// This is where the contrast is done.
	double pval = *(double*) PyArray_GETPTR3(npobject, p0, p1, k);
	double newval = pval - minimum < maximum - pval ? minimum : maximum;
	*(double*) PyArray_GETPTR3(newimage, p0, p1, k) = newval;
      } // end loop over channels
    }
  } // end loop over pixels in the image
  std::cerr << "OOFImage::enhance_contrast: done" << std::endl;
  return newimage;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The old version here uses more OOF2 classes and has the circular
// mask hard coded.  It was just slightly faster than the more general
// OOF-independent version above.

#ifdef OLDVERSION

static double closest(double x, double mn, double mx) {
  if(x-mn < mx-x)
    return mn;
  return mx;
}

void OOFImage::enhance_contrast(int radius) {
  DoubleArray rmax(sizeInPixels_), rmin(sizeInPixels_);
  DoubleArray gmax(sizeInPixels_), gmin(sizeInPixels_);
  DoubleArray bmax(sizeInPixels_), bmin(sizeInPixels_);

  double r2 = radius*radius;
  ICoord diagonalUR(radius+1, radius+1);
  ICoord diagonalLL(-radius, -radius);

  // Loop over pixels in the image, finding the min and max rgb
  // values in a neighborhood around each pixel.
  for(DoubleArray::iterator i=rmax.begin(); i!=rmax.end(); ++i) {
    ICoord pixel = i.coord();
    // window is a square subarray centered on the pixel.  It's used
    // only to get pixel coordinates, not pixel values, so it doesn't
    // matter which of the full sized arrays is used.  Here we use rmax.
    DoubleArray window(rmax.subarray(pixel+diagonalLL, pixel+diagonalUR));
    double wrmin = std::numeric_limits<double>::max();
    double wgmin = wrmin;
    double wbmin = wrmin;
    double wrmax = std::numeric_limits<double>::min();
    double wgmax = wrmax;
    double wbmax = wrmax;
    for(DoubleArray::iterator j=window.begin(); j!=window.end(); ++j) {
      ICoord nbr = j.coord();
      if(norm2(nbr-pixel) <= r2) {	// Use a circular window
	// Using CColor here to retrieve the rgb values is very
	// slightly slower than retrieving them directly using
	// PyArray_GETPTR3(npobject, ...), but is less likely to break
	// if we ever change the data type for the nparray.
	// TODO NUMPY: Is it possible in C++ to get the numpy data
	// type, and call an appropriate templated version of this
	// function?)

	CColor nbrcolor = operator[](nbr);
	double r = nbrcolor.getRed();
	double g = nbrcolor.getGreen();
	double b = nbrcolor.getBlue();
	
	// // This version of the above doesn't use CColor.
	// double* rptr = (double*) PyArray_GETPTR3(npobject,nbr[1],nbr[0],0);
	// double r = *rptr;
	// double g = *(rptr + 1);
	// double b = *(rptr + 2);
	
	if(r < wrmin) wrmin = r;
	if(r > wrmax) wrmax = r;
	if(g < wgmin) wgmin = g;
	if(g > wgmax) wgmax = g;
	if(b < wbmin) wbmin = b;
	if(b > wbmax) wbmax = b;
      }
    }
    rmax[i] = wrmax;
    rmin[i] = wrmin;
    gmax[i] = wgmax;
    gmin[i] = wgmin;
    bmax[i] = wbmax;
    bmin[i] = wbmin;
  }

  // Replace pixels in the original image with either the min or max
  // value from its window, depending on which is closer.
  for(DoubleArray::iterator i=rmax.begin(); i!=rmax.end(); ++i) {
    ICoord pixel = i.coord();
    CColor clr = operator[](pixel);
    double r = closest(clr.getRed(), rmin[i], rmax[i]);
    double g = closest(clr.getGreen(), gmin[i], gmax[i]);
    double b = closest(clr.getBlue(), bmin[i], bmax[i]);    
    set(pixel, CColor(r,g,b));

    // // See comment above re not using CColor.
    // double* rptr = (double*) PyArray_GETPTR3(npobject, pixel[1], pixel[0], 0);
    // *rptr = closest(*rptr, rmin[i], rmax[i]);
    // *(rptr+1) = closest(*(rptr + 1), gmin[i], gmax[i]);
    // *(rptr+2) = closest(*(rptr + 2), bmin[i], bmax[i]);
    
  }
}

#endif // OLDVERSION
