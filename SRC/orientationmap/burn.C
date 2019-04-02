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

#include "orientationmap/burn.h"
#include "common/latticesystem.h"

template class Burner<COrientABG, OrientMap>;

OrientationBurner::OrientationBurner(double lcl, double glbl,
				     const std::string &schoenflies, bool nn)
    : Burner(nn),
      local_flammability(lcl),
      global_flammability(glbl),
      lattice(getLatticeSymmetry(schoenflies)) 
  {}

bool OrientationBurner::spread(const COrientABG &from, const COrientABG &to)
  const
{
  double local_dist = from.misorientation(to, *lattice);
  double global_dist = startvalue.misorientation(to, *lattice);
  return local_dist < local_flammability && global_dist < global_flammability;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

OrientBurnSelection::OrientBurnSelection(const CMicrostructure *ms,
					 OrientationBurner *burner,
					 OrientMap *orientmap,
					 const ICoord *pt)
  : PixelSelectionCourier(ms),
    burner(burner),
    orientmap(orientmap),
    spark(*pt),
    selected(ms->sizeInPixels(), false),
    sel_iter(selected.begin())
{}

void OrientBurnSelection::start() {
  burner->burn(*orientmap, &spark, selected);
  if(!*sel_iter) next();
}

ICoord OrientBurnSelection::currentPoint() const {
  return sel_iter.coord();
}

void OrientBurnSelection::advance() {
  if(sel_iter.done())
    done_ = true;
  else
    ++sel_iter;
}

void OrientBurnSelection::next() {
  advance();
  while(!*sel_iter && !done_)
    advance();
}

void OrientBurnSelection::print(std::ostream &os) const {
  os << "OrientBurnSelection()";
}
