// -*- C++ -*-
// $RCSfile: expandgrp.C,v $
// $Revision: 1.14 $
// $Author: langer $
// $Date: 2014/09/27 21:40:20 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

// Expand and Shrink methods for the PixelSet class.

#include "common/pixelgroup.h"
#include "common/boolarray.h"
#include "common/bitmask.h"
#include "common/printvec.h"
#include <math.h>


static BitMask makeMask(double range) {
  int irange = (int) ceil(range);
  BitMask mask(ICoord(2*irange+1, 2*irange+1), // size
	       ICoord(irange, irange));	// center
  double rr = range*range;
  for(BitMask::iterator i = mask.raw_begin(); i!= mask.end(); i.raw_incr())
    if(norm2(i.coord()) <= rr)
      *i = true;
  return mask;
}

// Create a list of pixels not in the group that are within a distance
// 'range' of pixels that are in the group.  Adding pixels in this
// list to the group will expand the group.

void PixelSet::expand(double range, BoolArray &selected) const {
  weed();
  const BitMask mask(makeMask(range)); // all pixels within range of (0,0)
  PixelSet newpixels(&geometry, microstructure); // new pixels to be added
  ICRectangle bounds(ICoord(0,0), geometry);
  // loop over group members
  for(std::vector<ICoord>::size_type i=0; i<members_.size(); i++) {
    ICoord pxl = members_[i];
    // loop over pixels in mask
     for(BitMask::const_iterator j=mask.begin(); j!=mask.end(); ++j) {
       // location of mask pixel for mask centered at group pixel
       ICoord newpxl = pxl + j.coord();
       if(bounds.contains(newpxl)) { 
	 newpixels.add(newpxl);
       }
     }
  }
  newpixels.remove(&members_);
  const std::vector<ICoord> &pxls(*newpixels.members());
  for(std::vector<ICoord>::size_type i=0; i<pxls.size(); i++) 
    selected[pxls[i]] = true;
}

// Create a list of pixels in the group that are within a distance
// 'range' of pixels that aren't in the group.  Removing pixels in
// this list will shrink the group.

void PixelSet::shrink(double range,
			 BoolArray &selected) const {
  weed();
  const BitMask mask(makeMask(range)); // all pixels within range of (0,0)
  // pixels to be removed from the group
//   std::vector<ICoord> *oldpixels = new std::vector<ICoord>;

  BoolArray grouparray(geometry, false); // array of pixels in the group
  for(std::vector<ICoord>::size_type i=0; i<members_.size(); i++)
    grouparray[members_[i]] = true;

  ICRectangle bounds(ICoord(0,0), geometry);
  for(std::vector<ICoord>::size_type i=0; i<members_.size(); i++) {
    const ICoord &pxl = members_[i];
    for(BitMask::const_iterator j=mask.begin(); j!=mask.end(); ++j) {
      ICoord testpt(j.coord() + pxl);
      if(bounds.contains(testpt) && !grouparray[testpt]) {
	// A pixel that is not in the group is within range of pxl
// 	oldpixels->push_back(pxl);
	selected[pxl] = true;
	break;
      }
    }
  }
}
