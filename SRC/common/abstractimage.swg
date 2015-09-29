// -*- C++ -*-
// $RCSfile: abstractimage.swg,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:40:15 $


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ABSTRACTIMAGE_SWG
#define ABSTRACTIMAGE_SWG

%module abstractimage
%include "common/typemaps.swg"

%{
#include "common/abstractimage.h"
#include "common/coord.h"
%}

class AbstractImage {
public:
  Coord size();
  ICoord sizeInPixels();
};

#endif // ABSTRACTIMAGE_SWG
