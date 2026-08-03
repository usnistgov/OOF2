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

// contrast() performs the same operation as
// skimage.filters.rank.enhance_contrast(), more or less.

// The scikit-image documentation says "This replaces each pixel by the
// local maximum if the pixel gray value is closer to the local
// maximum than the local minimum. Otherwise it is replaced by the
// local minimum."

// The differences are that our version doesn't require that the image
// bit depth be reduced to 8, and can be applied to either all
// channels or just the hsv value via scikit-image's @adapt_rgb
// decorator.

// enhance_contrast is *not* an OOFImage method because it's easier to
// use it with @adapt_rgb if it's a function that takes a
// PyArrayObject* image argument.

#include "image/oofimage.h"


void enhance_contrast(PyArrayObject* image,
		      PyArrayObject* mask,
		      PyArrayObject *newimage)
{
  int imagedims = PyArray_NDIM(image);
  int maskdims = PyArray_NDIM(mask);
  int newdims = PyArray_NDIM(newimage);
  assert(imagedims==2 && maskdims==2 && newdims==2);
  const npy_intp* imageshape = PyArray_SHAPE(image);
  const npy_intp* maskshape = PyArray_SHAPE(mask);
  const npy_intp* newshape = PyArray_SHAPE(newimage);
  assert(newshape[0]==imageshape[0] && newshape[1]==imageshape[1]);

  // Get the center of the mask in mask coordinates.  If the size of
  // the mask is even, then the 'center' is between two pixels, and
  // will be rounded down.  The final result may be skewed.  If this
  // is a problem, ensure that the height and width are odd.
  //
  // The shape of the mask is (2*mc0+1, 2*mc1+1) if the height and
  // width are odd.
  int mc0 = maskshape[0]/2;	// integer division
  int mc1 = maskshape[1]/2;	// integer division

  // Loop over pixels in the image
  for(int p0=0; p0<imageshape[0]; p0++) {
    for(int p1=0; p1<imageshape[1]; p1++) {

      // Difference between image and mask coordinates.  Both start at
      // edges.  The mask is centered at (p0,p1) in image coordinates.
      int d0 = p0 - mc0;	// maskcoord + d = imagecoord
      int d1 = p1 - mc1;

      double minimum = std::numeric_limits<double>::max();
      double maximum = -minimum;

      // Find the pixel coordinates of the edges of the mask
      int p0min = d0;
      int p1min = d1;
      int p0max = p0min + maskshape[0];
      int p1max = p1min + maskshape[1];
      // Clip the masked region to the limits of the image
      if(p0min < 0) p0min = 0;
      if(p1min < 0) p1min = 0;
      if(p0max > imageshape[0]) p0max = imageshape[0];
      if(p1max > imageshape[1]) p1max = imageshape[1];

      // TODO? Is it better to convert the mask to a list of pixels
      // (x,y), offset the members of a copy of the list by the
      // position of the center pixel, then loop over the list instead
      // of looping over the mask?  Better would be to not copy the
      // list, but compute the offset from the last position.  It's
      // still necessary to check for mask pixels that are outside the
      // image, so this doesn't eliminate all if-statements inside the
      // loop.

      // Loop over the masked pixels
      for(int pp0=p0min; pp0<p0max; pp0++) {
	int mm0 = pp0 - d0;
	for(int pp1=p1min; pp1<p1max; pp1++) {
	  int mm1 = pp1 - d1;
	  if(*(char*) PyArray_GETPTR2(mask, mm0, mm1)) { // is point masked?
	    double val = *(double*) PyArray_GETPTR2(image, pp0, pp1);
	    if(val < minimum) {
	      minimum = val;
	    }
	    if(val > maximum)
	      maximum = val;
	  } // point is masked
	}   // loop over pixels pp1
      }	    // loop over pixels pp0
      
      assert(minimum != std::numeric_limits<double>::max());
      assert(maximum != -std::numeric_limits<double>::max());

      // Choose a new value for the central pixel
      double pval = *(double*) PyArray_GETPTR2(image, p0, p1);
      double newval = (pval - minimum < maximum - pval) ? minimum : maximum;

      *(double*) PyArray_GETPTR2(newimage, p0, p1) = newval;

    } // end loop over p1
  } // end loop over p0
}
