// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Despeckle and Elkcepsed methods for the PixelSet class.

#include <oofconfig.h>
#include "common/pixelgroup.h"
#include "common/boolarray.h"

static ICoord north(0,1);
static ICoord east(1,0);
static ICoord northeast(1,1);
static ICoord northwest(-1, 1);

// Count number of selected neighbors.
static int Nnbrs(const ICoord &pxl, const BoolArray &sel) {
  int w = sel.width() - 1;
  int h = sel.height() - 1;
  int x = pxl(0);
  int y = pxl(1);
  int howmany = 0;	// number of neighbors selected
  if(x > 0) if(sel[pxl - east]) howmany++;
  if(x < w) if(sel[pxl + east]) howmany++;
  if(y > 0) if(sel[pxl - north]) howmany++;
  if(y < h) if(sel[pxl + north]) howmany++;
  if(x > 0 && y > 0) if(sel[pxl - northeast]) howmany++;
  if(x < w && y < h) if(sel[pxl + northeast]) howmany++;
  if(x < w && y > 0) if(sel[pxl - northwest]) howmany++;
  if(x > 0 && y < h) if(sel[pxl + northwest]) howmany++;
  return howmany;
}

static inline bool isUnselected(const ICoord &pxl, const BoolArray &sel) {
  return !sel[pxl];
}

static inline bool isSelected(const ICoord &pxl, const BoolArray &sel) {
  return sel[pxl];
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

static void addnbrs_unsel(const ICoord &pxl, const BoolArray &sel,
			  PixelSet &grp)
{
  int w = sel.width() - 1;
  int h = sel.height() - 1;
  int x = pxl(0);
  int y = pxl(1);
  if(x > 0) if(isUnselected(pxl-east, sel)) grp.add(pxl-east);
  if(x < w) if(isUnselected(pxl+east, sel)) grp.add(pxl+east);
  if(y > 0) if(isUnselected(pxl-north, sel)) grp.add(pxl-north);
  if(y < h) if(isUnselected(pxl+north, sel)) grp.add(pxl+north);
  if(x > 0 && y > 0)
    if(isUnselected(pxl-northeast, sel)) grp.add(pxl-northeast);
  if(x < w && y < h)
    if(isUnselected(pxl+northeast, sel)) grp.add(pxl+northeast);
  if(x < w && y > 0)
    if(isUnselected(pxl-northwest, sel)) grp.add(pxl-northwest);
  if(x > 0 && y < h)
    if(isUnselected(pxl+northwest, sel)) grp.add(pxl+northwest);
}

static void addnbrs_sel(const ICoord &pxl, const BoolArray &sel,
			PixelSet &grp)
{
  int w = sel.width() - 1;
  int h = sel.height() - 1;
  int x = pxl(0);
  int y = pxl(1);
  if(x > 0) if(isSelected(pxl-east, sel)) grp.add(pxl-east);
  if(x < w) if(isSelected(pxl+east, sel)) grp.add(pxl+east);
  if(y > 0) if(isSelected(pxl-north, sel)) grp.add(pxl-north);
  if(y < h) if(isSelected(pxl+north, sel)) grp.add(pxl+north);
  if(x > 0 && y > 0)
    if(isSelected(pxl-northeast, sel)) grp.add(pxl-northeast);
  if(x < w && y < h)
    if(isSelected(pxl+northeast, sel)) grp.add(pxl+northeast);
  if(x < w && y > 0)
    if(isSelected(pxl-northwest, sel)) grp.add(pxl-northwest);
  if(x > 0 && y < h)
    if(isSelected(pxl+northwest, sel)) grp.add(pxl+northwest);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void PixelSet::despeckle(int nbr_threshold,
			   BoolArray &selected) const {
  // array of selected pixels
  BoolArray sel(geometry);
  for(std::vector<ICoord>::size_type i=0; i<members_.size(); i++)
    sel[members_[i]] = true;
  // Unselected neighbors are stored in a PixelSet 
  PixelSet unselnbrs(&geometry, microstructure);
  // Find unselected neighbors by looping over sel
  for(BoolArray::iterator i=sel.begin(); i!=sel.end(); ++i)
    if(*i)			// pixel is selected
      addnbrs_unsel(i.coord(), sel, unselnbrs);
  unselnbrs.weed();

//   std::vector<ICoord> *newpixels = new std::vector<ICoord>;
  while(unselnbrs.len() > 0) {
    // Remove last pixel from the unselected neighbor list.
    ICoord candidate(unselnbrs.pop());
    if(Nnbrs(candidate, sel) >= nbr_threshold) {
      sel[candidate] = true;
      addnbrs_unsel(candidate, sel, unselnbrs);
//       newpixels->push_back(candidate);
      selected[candidate] = true;
    }
  }
//   return newpixels;
}

void PixelSet::elkcepsed(int nbr_threshold,
			   BoolArray &selected) const {
  // array of selected pixels
  BoolArray sel(geometry);
  for(std::vector<ICoord>::size_type i=0; i<members_.size(); i++)
    sel[members_[i]] = true;
  // Group of candidates for unselecting
  PixelSet candidates(*this); // weeded copy of self

//   // Pixels removed from the group
//   std::vector<ICoord> *removed = new std::vector<ICoord>;
  // Examine pixels in group, 
  while(candidates.len() > 0) {
    ICoord candidate(candidates.pop());
    // A candidate may appear more than once in the list, so check to
    // see that it's still selected before doing anything.
    if(sel[candidate] && Nnbrs(candidate, sel) < nbr_threshold) {
      sel[candidate] = false;
      // add selected neighbors of this pixel to the list of pxls to be examined
      addnbrs_sel(candidate, sel, candidates);
//       removed->push_back(candidate);
      selected[candidate] = true;
    }
  }
//   return removed;
}
