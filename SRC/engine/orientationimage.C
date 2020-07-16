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
#include "common/array.h"
#include "common/cmicrostructure.h"
#include "common/coord.h"
#include "common/IO/OOFCANVAS/canvasimage.h"
#include "engine/angle2color.h"
#include "engine/material.h"
#include "engine/ooferror.h"
#include "engine/orientationimage.h"
#include "engine/property/orientation/orientation.h"

OrientationImage::OrientationImage(CMicrostructure *microstructure,
				   const Angle2Color *colorscheme,
				   const CColor *noMaterial,
				   const CColor *noOrientation)
  : microstructure(microstructure),
    noMaterial(*noMaterial),
    noOrientation(*noOrientation),
    colorscheme(colorscheme->clone())
{}

OrientationImage::~OrientationImage() {
  delete colorscheme;
}

const Coord &OrientationImage::size()  const {
  return microstructure->size();
}

const ICoord &OrientationImage::sizeInPixels() const {
  return microstructure->sizeInPixels();
}

OOFCanvas::CanvasImage *OrientationImage::makeCanvasImage(const Coord *position,
							  const Coord *dispsize)
  const
{
  OOFCanvas::CanvasImage *img = OOFCanvas::CanvasImage::newBlankImage(
					 (*position)[0], (*position)[1],
					 sizeInPixels()[0], sizeInPixels()[1],
					 (*dispsize)[0], (*dispsize)[1],
					 0.0, 0.0, 0.0, 1.0);
  img->setDrawIndividualPixels();
  const Array<int> &pxls = *microstructure->getCategoryMapRO();
  for(Array<int>::const_iterator i=pxls.begin(); i!=pxls.end(); ++i) {
    ICoord where = i.coord();
    const Material *mat = getMaterialFromPoint(microstructure, &where);
    CColor color;
    if(mat) {
      try {
	OrientationPropBase *orientprop =
	  dynamic_cast<OrientationPropBase*>(mat->fetchProperty("Orientation"));
	color = (*colorscheme)(*orientprop->orientation(microstructure, where));
      }
      catch(ErrNoSuchProperty &exc) { // no orientation property
	color = noOrientation;
      }
    }
    else {			// no material
      color = noOrientation;
    }
    img->set(where[0], where[1],
	     color.getRed(), color.getGreen(), color.getBlue());
  }
  return img;
}

