// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef LATTICESYSTEM_H
#define LATTICESYSTEM_H

#include <oofconfig.h>
#include <vector>

#include "common/smallmatrix.h"

class LatticeSystem {
protected:
  const std::vector<const SmallMatrix3x3> matrices_;
  const std::string name_;
public:
  LatticeSystem(const std::string&,
		std::initializer_list<const SmallMatrix3x3>);
  ~LatticeSystem() {}
  int size() const { return matrices_.size(); }
  virtual const std::vector<const SmallMatrix3x3> &matrices() const {
    return matrices_;
  }
};

class TriclinicLatticeSystem : public LatticeSystem {
public:
  TriclinicLatticeSystem();
};

class MonoclinicLatticeSystem : LatticeSystem {
public:
  MonoclinicLatticeSystem();
};

class OrthorhombicLatticeSystem : public LatticeSystem {
public:
  OrthorhombicLatticeSystem();
};

class TetragonalLatticeSystem : public LatticeSystem {
public:
  TetragonalLatticeSystem();
};

class TrigonalLatticeSystem : public LatticeSystem {
public:
  TrigonalLatticeSystem();
};

class RhombohedralLatticeSystem : public LatticeSystem {
public:
  RhombohedralLatticeSystem();
};

class HexagonalLatticeSystem : public LatticeSystem {
public:
  HexagonalLatticeSystem();
};

class CubicLatticeSystem : public LatticeSystem {
public:
  CubicLatticeSystem();
};

const LatticeSystem *getLatticeSystem(const std::string&);

#endif // LATTICESYSTEM_H
