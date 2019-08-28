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

#include "common/array.h"
#include "common/burn.h"
#include "common/statgroups.h"
#include "engine/corientation.h"

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

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class OrientationPixelDistribution : public PixelDistribution {
protected:
  double var0;			// variance used when there's only one value
  double variance;
  COrientAxis mean;
  const LatticeSymmetry *lattice;
  const OrientMap *orientmap;
  void findVariance();
public:
  OrientationPixelDistribution(const ICoord&, const OrientMap*, double, 
			       const LatticeSymmetry*);
  OrientationPixelDistribution(const std::set<ICoord>&, const OrientMap*, 
			       double, const LatticeSymmetry*);
  virtual PixelDistribution *clone(const std::set<ICoord>&) const;
  virtual void add(const ICoord&);
  virtual void merge(const PixelDistribution*);
  virtual double deviation2(const ICoord&) const;
  virtual double deviation2(const PixelDistribution*) const;
#ifdef DEBUG
  virtual std::string stats() const;
  virtual std::string value(const ICoord&) const;
#endif // DEBUG
};

class OrientationPixelDistFactory : public PixelDistributionFactory {
protected:
  const OrientMap *orientmap;
  double sigma0;
  const LatticeSymmetry *lattice;
public:
  OrientationPixelDistFactory(const OrientMap*, double, const std::string&);
  virtual PixelDistribution *newDistribution(const ICoord&) const;
};

#endif // PIXELDIFFORIENT_H
