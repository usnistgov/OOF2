// -*- C++ -*-
// $RCSfile: direction.h,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2012/02/28 22:24:57 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef DIRECTION_H
#define DIRECTION_H

// A Direction is a direction in 3D space, even in 2D OOF2.  In OOF3D
// the Coord class could be used instead.  A direction is *not* an
// Orientation.

class CUnitVectorDirection;
class CAngleDirection;

#include "common/doublevec.h"

class COrientation;
class SmallMatrix;

class CDirection {
public:
  virtual ~CDirection() {}
  // Conversion
  virtual CUnitVectorDirection unitVector() const = 0;
  virtual CAngleDirection angles() const = 0;
  // Matrix multiplication (for rotation).
  virtual CUnitVectorDirection matmult(const SmallMatrix&) const = 0;
  // Components
  virtual double theta() const = 0;
  virtual double phi() const = 0;
};

class CUnitVectorDirection : public CDirection {
private:
  DoubleVec vec;
public:
  CUnitVectorDirection(double x, double y, double z);
  CUnitVectorDirection(const DoubleVec *);
  virtual CUnitVectorDirection unitVector() const { return *this; }
  virtual CAngleDirection angles() const;
  virtual CUnitVectorDirection matmult(const SmallMatrix&) const;
  virtual double theta() const;
  virtual double phi() const;
  double x() const { return vec[0]; }
  double y() const { return vec[1]; }
  double z() const { return vec[2]; }
};

class CAngleDirection : public CDirection {
private:
  double theta_, phi_;
public:
  CAngleDirection(double, double);
  virtual CUnitVectorDirection unitVector() const;
  virtual CAngleDirection angles() const { return *this; }
  virtual CUnitVectorDirection matmult(const SmallMatrix&) const;
  virtual double theta() const { return theta_; }
  virtual double phi() const { return phi_; }
};

CUnitVectorDirection operator*(const SmallMatrix&, const CDirection&);


#endif // DIRECTION_H
