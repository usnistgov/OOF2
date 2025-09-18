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
// #include "common/doublearray.h"
// #include "common/pyutils.h"

// OOFImage::enhance_contrast() performs the same operation as
// skimage.filters.rank.enhance_contrast().  

// The skimage documentation says "This replaces each pixel by the
// local maximum if the pixel gray value is closer to the local
// maximum than the local minimum. Otherwise it is replaced by the
// local minimum."

// The difference is that our version operates on each RGB channel
// separately and doesn't require that the image bit depth be reduced
// to 8.

PyArrayObject* OOFImage::enhance_contrast(PyArrayObject *mask,
					  PyArrayObject *newimage)
  const
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
  // around with it now.  TODO: Fix this.  Use PyArray_NewLikeArray,
  // probably.
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

  int kmax = imagedim == 3 ? imageshape[2] : 1;

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
      for(int k=0; k<kmax; k++) {
	double minimum = std::numeric_limits<double>::max();
	double maximum = -minimum;
	// Loop over the mask, finding the min and max values of the
	// channel in the corresponding pixels of the image.
	for(int m0=m0min; m0<m0max; m0++) {
	  assert(m0 + d0 >= 0 && m0 + d0 < imageshape[0]);
	  for(int m1=m1min; m1<m1max; m1++) {
	    assert(m1 + d1 >= 0 && m1 + d1 < imageshape[1]);
	    if(*(int*) PyArray_GETPTR2(mask, m0, m1)) { // inside the mask
	      // TODO NUMPY: Can this be done without checking imagedim?
	      double val =
		(imagedim == 3 ?
		 *(double*) PyArray_GETPTR3(npobject, m0+d0, m1+d1, k) :
		 *(double*) PyArray_GETPTR2(npobject, m0+d0, m1+d1));
	      if(val < minimum)
		minimum = val;
	      if(val > maximum)
		maximum = val;
	    }
	  }
	} // end loop over mask

	// This is where the contrast is done.
	// TODO NUMPY: Can this be done without checking imagedim?
	if(imagedim == 3) {
	  double pval = *(double*) PyArray_GETPTR3(npobject, p0, p1, k);
	  double newval = (pval - minimum < maximum - pval) ? minimum : maximum;
	  *(double*) PyArray_GETPTR3(newimage, p0, p1, k) = newval;
	}
	else {
	  double pval = *(double*) PyArray_GETPTR2(npobject, p0, p1);
	  double newval = (pval - minimum < maximum - pval) ? minimum : maximum;
	  *(double*) PyArray_GETPTR2(newimage, p0, p1) = newval;
	}
	
      } // end loop over channels
    }
  } // end loop over pixels in the image
  return newimage;
}

