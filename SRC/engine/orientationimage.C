// -*- C++ -*-
// $RCSfile: orientationimage.C,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2014/09/27 21:40:48 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/IO/stringimage.h"
#include "common/array.h"
#include "common/cmicrostructure.h"
#include "common/coord.h"
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
  std::cerr << "OrientationImage::size: size=" << microstructure->size() << std::endl;
  return microstructure->size();
}

const ICoord &OrientationImage::sizeInPixels() const {
  return microstructure->sizeInPixels();
}

void OrientationImage::fillstringimage(StringImage *strimg) const {
  const Array<int> &pxls = *microstructure->getCategoryMapRO();
  for(Array<int>::const_iterator i=pxls.begin(); i!=pxls.end(); ++i) {
    ICoord where = i.coord();
    const Material *mat = getMaterialFromPoint(microstructure, &where);
    if(mat) {
      try {
	OrientationPropBase *orientprop =
	  dynamic_cast<OrientationPropBase*>(mat->fetchProperty("Orientation"));
	CColor color((*colorscheme)
		     (*orientprop->orientation(microstructure, where)));
	strimg->set(&where, &color);
      }
      catch (ErrNoSuchProperty &exc) {
	strimg->set(&where, &noOrientation);
      }
    }
    else {			// no material
      strimg->set(&where, &noMaterial);
    }
  }
}
