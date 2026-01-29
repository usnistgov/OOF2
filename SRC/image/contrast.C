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

// OOFImage::enhance_contrast() performs the same operation as
// skimage.filters.rank.enhance_contrast().  

// The skimage documentation says "This replaces each pixel by the
// local maximum if the pixel gray value is closer to the local
// maximum than the local minimum. Otherwise it is replaced by the
// local minimum."

// The differences are that our version doesn't require that the image
// bit depth be reduced to 8, and can be applied to either all
// channels or just the hsv value via @adapt_rgb.

#include "image/oofimage.h"
#include "common/cdebug.h"

PyArrayObject* OOFImage::enhance_contrast(PyArrayObject *mask,
					  PyArrayObject *newimage)
  const
{

  // Check that image and newimage have the same shape.
  int imagedim = PyArray_NDIM(npobject);
  const npy_intp* imageshape = PyArray_SHAPE(npobject);
  int newdim = PyArray_NDIM(newimage);
  const npy_intp* newshape = PyArray_SHAPE(newimage);
#ifdef DEBUG
  assert(PyArray_TYPE(newimage) == NPY_DOUBLE);
  assert(newdim == imagedim);
  for(int i=i; i<newdim; i++)
    assert(newshape[i] == imageshape[i]);
#endif // DEBUG

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

  int kmax = isgray_ ? 1 : imageshape[2];

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
	m0min = -d0;
      if(m0max + d0 > imageshape[0])
	m0max = imageshape[0] - d0;
      if(m1min + d1 < 0)
	m1min = -d1;
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
	    if(*(char*) PyArray_GETPTR2(mask, m0, m1)) { // inside the mask
	      double val = isgray_ ?
		*(double*) PyArray_GETPTR2(npobject, m0+d0, m1+d1) :
		*(double*) PyArray_GETPTR3(npobject, m0+d0, m1+d1, k);
	      if(val < minimum)
		minimum = val;
	      if(val > maximum)
		maximum = val;
	    }
	  }
	} // end loop over mask

	// This is where the contrast is done.
	if(isgray_) {
	  double pval = *(double*) PyArray_GETPTR2(npobject, p0, p1);
	  double newval = (pval - minimum < maximum - pval) ? minimum : maximum;
	  *(double*) PyArray_GETPTR2(newimage, p0, p1) = newval;
	}
	else {
	  double pval = *(double*) PyArray_GETPTR3(npobject, p0, p1, k);
	  double newval = (pval - minimum < maximum - pval) ? minimum : maximum;
	  *(double*) PyArray_GETPTR3(newimage, p0, p1, k) = newval;
	}
      } // end loop over channels
    }
  } // end loop over pixels in the image
  return newimage;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Version that acts on a single channel image and is suitable for use
// with skimage.color.adapt_rgb.

void enhance_contrast1(PyArrayObject* image,
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

  // Get the center of the mask in mask coordinates.  The shape of the
  // mask is (2*mc0+1, 2*mc1+1).  The lengths of the edges of masks
  // created by skimage.morphology.disk are always odd.  TODO: Check
  // that this works with other mask shapes that might have even
  // lengths.
  int mc0 = maskshape[0]/2;	// integer division
  int mc1 = maskshape[1]/2;	// integer division

  // dump("MASK size= " + tostring(maskshape[0]) + ", " + tostring(maskshape[1]));
  // dump("MASK  center=" + tostring(mc0) + ", " + tostring(mc1));
  // for(int m0=0; m0<maskshape[0]; m0++) {
  //   std::string row;
  //   for(int m1=0; m1<maskshape[1]; m1++) {
  //     row += tostring(int(*(char*)PyArray_GETPTR2(mask, m0, m1))) + " ";
  //   }
  //   dump(row);
  // }
  // dump("-----------");

  // Loop over pixels in the image
  for(int p0=0; p0<imageshape[0]; p0++) {
    for(int p1=0; p1<imageshape[1]; p1++) {
      // bool verbose = p0==0 && p1==7; 

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

      // if(verbose)
      // 	dump("p0min=" + tostring(p0min) + " p0max=" + tostring(p0max)
      // 	     + " p1min=" + tostring(p1min) + " p1max=" + tostring(p1max));

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
	  // if(verbose)
	  //   dump("pp0=" + tostring(pp0) + " pp1=" + tostring(pp1) +
	  // 	 " mm0=" + tostring(mm0) + " mm1=" + tostring(mm1));
	  if(*(char*) PyArray_GETPTR2(mask, mm0, mm1)) { // is point masked?
	    double val = *(double*) PyArray_GETPTR2(image, pp0, pp1);
	    // if(verbose)
	    //   dump("   in mask, val=" + tostring(val));
	    if(val < minimum) {
	      // if(verbose)
	      // 	dump("minimum=" + tostring(minimum) + " val<minimum");
	      minimum = val;
	    }
	    if(val > maximum)
	      // if(verbose)
	      // 	dump("maximum=" + tostring(maximum) + " val>maximum");
	      maximum = val;
	  } // point is masked
	}   // loop over pixels pp1
      }	    // loop over pixels pp0
      
      assert(minimum != std::numeric_limits<double>::max());
      assert(maximum != -std::numeric_limits<double>::max());

      // Choose a new value for the central pixel
      double pval = *(double*) PyArray_GETPTR2(image, p0, p1);
      double newval = (pval - minimum < maximum - pval) ? minimum : maximum;
      // dump(tostring(p0) + "," + tostring(p1) +
      // 	   ": old=" + tostring(pval) +
      // 	   " min=" + tostring(minimum) + " max=" + tostring(maximum) +
      // 	   " diffs=" + tostring(pval - minimum) + " " + tostring(maximum-pval) +
      // 	   " new=" + tostring(newval)
      // 	   );

      *(double*) PyArray_GETPTR2(newimage, p0, p1) = newval;


    } // end loop over p1
  } // end loop over p0
}
