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

#include "common/burn.h"

class OrientMap;
class LatticeSymmetry;

class COrientationDifferentiator3 : public CPixelDifferentiator3 {
private:
  const OrientMap *orientmap;
  double local_flammability;
  double global_flammability;
  const LatticeSymmetry *lattice;
public:
  COrientationDifferentiator3(const OrientMap*, double, double,
			     const std::string&);
  virtual bool operator()(const ICoord&, const ICoord&, const ICoord&) const;  
};

class COrientationDifferentiator2 : public CPixelDifferentiator2 {
private:
  const OrientMap *orientmap;
  double misorientation;
  const LatticeSymmetry *lattice;
public:
  COrientationDifferentiator2(const OrientMap*, double, const std::string&);
  virtual bool operator()(const ICoord&, const ICoord&) const;
  virtual double distance2(const ICoord&, const ICoord&) const;
};

#endif // PIXELDIFFORIENT_H
