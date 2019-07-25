// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef STATGROUPS_H
#define STATGROUPS_H

#include <oofconfig.h>

#include <set>
#include <vector>

class CMicrostructure;
class ICoord;

// For this to be useful, we need to be able to compute the mean and
// deviation of a set of orientations, even though adding two
// orientations isn't defined.

// Given two orientations Q1 and Q2.  Let Q2 = R Q1, where R is the
// misorientation orientation (computed taking crystal symmetry into
// account).  Express R in angle-axis representation, R = A(X, theta)
// for axis X.  Then sqrt(R) is A(X, theta/2), and the mean of Q1 and
// Q2 is reasonably defined as sqrt(R) Q1.

// The weighted average of two orientations is
// w*Q1 + (1-w)*Q2 = A(X, (1-w)theta)*Q1



// What do we need to do?

// Ask if a pixel's value is likely to be from a distribution
//    How many sigmas is it from the mean?
//    How far is it in VALUE space?
// Add a pixel to a distribution and update the mean
// Create a new distribution with a single pixel
// Return a list of pixels in a distribution

// Should PixelDistribution subclasses cache the pixel value at the
// last ICoord used?

class PixelDistribution {
protected:
  // mean and deviation aren't stored here because we don't know their types.
  std::vector<ICoord> pxls;	// TODO: Use std::set for easy removal?
public:
  PixelDistribution() {}
  virtual ~PixelDistribution() {}
  unsigned int npts() const { return pxls.size(); }

  // Add a pixel and update the mean and variance.
  virtual void add(const ICoord&) = 0;
  virtual void remove(const ICoord&) = 0;
  // Add without updating the mean and variance
  void add_noupdate(const ICoord &pt) { pxls.push_back(pt); }
  void remove_noupdate(const ICoord &pt);
  void clear_noupdate() { pxls.clear(); }

  // How many deviations squared from the mean is the value at the
  // given point?
  virtual double deviation2(const ICoord&) const = 0;

  // How many deviations squared from this mean is the mean of the
  // other distribution?
  virtual double deviation2(const PixelDistribution*) const = 0;

  // Merge the given group PixelDistribution into this one. 
  virtual void merge(const PixelDistribution*) = 0;

  // Make a new PixelDistribution of the same subclass using the given
  // set of pixels.
  virtual PixelDistribution *clone(const std::set<ICoord>&) const = 0;

  const std::vector<ICoord> &pixels() const { return pxls; }

  std::vector<std::set<ICoord>> contiguousPixels() const;

#ifdef DEBUG
  virtual std::string stats() const = 0;
  virtual std::string value(const ICoord&) const = 0;
#endif // DEBUG
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class PixelDistributionFactory {
public:
  virtual ~PixelDistributionFactory() {}
  virtual PixelDistribution *newDistribution(const ICoord&) const = 0;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

const std::string *statgroups(CMicrostructure*, const PixelDistributionFactory*,
			      double, double,
			      int minsize,
			      const std::string&, bool);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// DummyDistribution is used as a placeholder in lists of
// PixelDistribution.

class DummyDistribution : public PixelDistribution {
public:
  DummyDistribution() {}
  virtual void add(const ICoord&) {}
  virtual void remove(const ICoord&) {}
  virtual double deviation2(const ICoord&) const { return 0.0; }
  virtual double deviation2(const PixelDistribution*) const { return 0.0; }
  virtual void merge(const PixelDistribution*) {}
  PixelDistribution *clone(const std::set<ICoord>&) const { 
    return new DummyDistribution(); 
  }
#ifdef DEBUG
  virtual std::string stats() const { return "dummy"; }
  virtual std::string value(const ICoord&) const { return "dummy value"; }
#endif // DEBUG
};

#endif // STATGROUPS_H
