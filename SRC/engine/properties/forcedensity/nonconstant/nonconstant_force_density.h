// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONCONSTANT_FORCE_DENSITY_H
#define NONCONSTANT_FORCE_DENSITY_H

#include <oofconfig.h>
#include "engine/property.h"
#include "engine/smallsystem.h"
#include <string>

class CSubProblem;
class Element;
class Equation;
class Flux;
class Material;
class FEMesh;
class Position;
class TwoVectorField;
class SymmetricTensorFlux;
class ElementNodeIterator;
class DoubleVec;


class NonconstantForceDensity : public EqnProperty {
public:
  NonconstantForceDensity(const std::string &name, PyObject *reg);
  virtual ~NonconstantForceDensity() {}
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return false; }
  virtual void precompute(FEMesh*);
  virtual void force_value(const FEMesh*, const Element*, const Equation*,
			   const MasterPosition&, double time, void*, 
			   SmallSystem*) const;
protected:
  TwoVectorField *displacement;
  SymmetricTensorFlux *stress_flux;

  virtual DoubleVec nonconst_force_density(const Coord &pt, double time) const = 0;
};


class TestNonconstantForceDensity : public NonconstantForceDensity {
protected:
  int testNo;
  DoubleVec nonconst_force_density_1(const Coord &pt, double time)
    const;
  DoubleVec nonconst_force_density_2(const Coord &pt, double time)
    const;
  DoubleVec nonconst_force_density_3(const Coord &pt, double time)
    const;
  DoubleVec nonconst_force_density_4(const Coord &pt, double time)
    const;
  DoubleVec nonconst_force_density_5(const Coord &pt, double time)
    const;
  DoubleVec nonconst_force_density(const Coord &pt, double time) const;
public:
  TestNonconstantForceDensity(const std::string &name, PyObject *registration,
			      int testno)
    : NonconstantForceDensity(name, registration),
      testNo(testno)
  {}
  virtual ~TestNonconstantForceDensity() {}
};

#endif
