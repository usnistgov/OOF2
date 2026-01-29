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

// reduce_noise() is an attempt to reproduce the ImageMagick
// reduceNoise() routine, which the IM docs describe as "Smooth the
// contours of an image while still preserving edge information. The
// algorithm works by replacing each pixel with its neighbor closest
// in value.  The neighbors of a pixel are defined as those pixels
// within the given radius".
//
// What that description is missing is that the replacement is only
// done if the pixel value is a minimum or maximum within the window.
// Maybe. See https://imagemagick.org/script/command-line-options.php.

// This method certainly doesn't do what the ImageMagick function
// does.  I don't know if there is a bug here or if the ImageMagick
// routine doesn't do what it says it does.  I suspect that both are
// true.  Until this is fixed, the 'secret' flag in the ReduceNoise
// registration in denoise.py should be True.

static double pixelmag(PyArrayObject* npobject, int i, int j) {
  double mag = 0.0;
  for(int k=0; k<PyArray_SHAPE(npobject)[2]; k++) {
    double v = *(double*) PyArray_GETPTR3(npobject, i, j, k);
    mag += v*v;
  }
  return mag;
}

PyArrayObject* OOFImage::reduce_noise(PyArrayObject *mask,
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
  // around with it now.  TODO MAYBE: Fix this.  
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

  int nreplaced = 0;

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

      double target[3];
      for(int k=0; k<imageshape[2]; k++)
	target[k] = *(double*) PyArray_GETPTR3(npobject, p0, p1, k);
      
      double targetmag = pixelmag(npobject, p0, p1);
      bool targethi = true; // is target pixel mag greater than all nbrs?
      bool targetlo = true; // is target pixel mag less than all nbrs?
	
      double closest[3]; // neighbor color that's closest to the target color
      double mindist2 = std::numeric_limits<double>::max();
      
      // Loop over the mask, finding the closest color to the target
      // pixel.
      for(int m0=m0min; m0<m0max; m0++) {
	assert(m0 + d0 >= 0 && m0 + d0 < imageshape[0]);
	for(int m1=m1min; m1<m1max; m1++) {
	  assert(m1 + d1 >= 0 && m1 + d1 < imageshape[1]);
	  if(*(char*) PyArray_GETPTR2(mask, m0, m1)) { // apply the mask
	    // The mask pixel is at (m0+d0, m1+d1) in image coordinates.
	    if(!(m0+d0 == p0 && m1+d1 == p1)) {	      // skip the target pixel
	      double dist2 = 0;	// squared color distance to target pixel
	      double nbrmag = pixelmag(npobject, m0+d0, m1+d1);
	      targethi &= nbrmag < targetmag;
	      targetlo &= nbrmag > targetmag;
	      // if(nbrmag > targetmag) targethi = false;
	      // if(nbrmag < targetmag) targetlo = false;
	      if(!(targethi || targetlo))
		break;
	      // Loop over channels
	      double nbrcolor[3];
	      for(int k=0; k<imageshape[2]; k++) {
		double val = *(double*) PyArray_GETPTR3(npobject,
							m0+d0, m1+d1, k);
		double diff = val - target[k];
		dist2 += diff*diff;
		nbrcolor[k] = val;
	      }	// end loop over channels
	      
	      if(dist2 < mindist2) {
		mindist2 = dist2;
		for(int k=0; k<imageshape[2]; k++)
		  closest[k] = nbrcolor[k];
	      }
	    } // end if not at the target
	  }   // end if in the mask
	  
	} // end inner loop over mask
	if(!(targethi || targetlo))
	  break;
      }	// end outer loop over mask
      
      if(targethi || targetlo) {
	for(int k=0; k<imageshape[2]; k++) {
	  double *vk = (double*) PyArray_GETPTR3(newimage, p0, p1, k);
	  *vk = closest[k];
	}
	nreplaced++;
      }
      else {
	// TODO NUMPY: Copying here is probably inefficient. newimage
	// should be initialized with a copy of the original image.
	for(int k=0; k<imageshape[2]; k++)
	  *(double*) PyArray_GETPTR3(newimage, p0, p1, k) =
	    *(double*) PyArray_GETPTR3(npobject, p0, p1, k);
      }
      
    } // end inner loop over pixels in the image
  } // end outer loop over pixels in the image

  std::cerr << "OOFImage::reduce_noise: replaced " << nreplaced << "/"
	    << imageshape[0]*imageshape[1] << " pixels" << std::endl;
  return newimage;
}
