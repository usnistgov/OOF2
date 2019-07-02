// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELDIFFORIENT_H
#define PIXELDIFFORIENT_H

#include "image/autograin.h"

class OrientMap;
class LatticeSymmetry;

class COrientationDifferentiator : public CPixelDifferentiator {
private:
  const OrientMap *orientmap;
  double local_flammability;
  double global_flammability;
  const LatticeSymmetry *lattice;
public:
  COrientationDifferentiator(const OrientMap*, double, double,
			     const std::string&);
  virtual bool operator()(const ICoord&, const ICoord&, const ICoord&) const;  
};

#endif // PIXELDIFFORIENT_H
