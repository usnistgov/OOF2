// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "image/IO/GUI/oofimage.h"

OOFCanvas::CanvasImage *oofImageToCanvasImage(const OOFImage *image,
					      const Coord *pos,
					      const Coord *size)
{
  return new CanvasImage::newFromImageMagick((*pos)[0], (*pos)[1],
					     image->magickImage(),
					     (*size)[0], (*size)[1]);
}
