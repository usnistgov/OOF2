// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONCONSTANT_HEAT_SOURCE_H
#define NONCONSTANT_HEAT_SOURCE_H


#include "common/coord.h"
#include "engine/property.h"
#include "engine/symmmatrix.h"
#include <string>

class Element;
class Material;
class FEMesh;
class OrientationPropBase;
class SmallSystem;
class ScalarField;
class VectorFlux;
class ElementNodeIterator;



class NonconstantHeatSource : public EqnProperty {
public:
  NonconstantHeatSource(const std::string &name, PyObject *registration);
  virtual ~NonconstantHeatSource() {};
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return false; }
  virtual void force_value(const FEMesh*, const Element*, const Equation*,
			   const MasterPosition&, double time, void*,
			   SmallSystem*)
    const;
protected:
  VectorFlux *heat_flux;
  virtual double nonconst_heat_source(const Coord &pt, double time) const = 0;
};


class TestNonconstantHeatSource : public NonconstantHeatSource {
protected:
  int testNo;
  double nonconst_heat_source_1(const Coord &pt, double time) const;
  double nonconst_heat_source_2(const Coord &pt, double time) const;
  double nonconst_heat_source_3(const Coord &pt, double time) const;
  double nonconst_heat_source_4(const Coord &pt, double time) const;
  double nonconst_heat_source_5(const Coord &pt, double time) const;
  double nonconst_heat_source_6(const Coord &pt, double time) const;
  double nonconst_heat_source_7(const Coord &pt, double time) const;
  double nonconst_heat_source_8(const Coord &pt, double time) const;
  virtual double nonconst_heat_source(const Coord &pt, double time) const;
public:
  TestNonconstantHeatSource(const std::string &name, PyObject *registration,
			    int testno)
    : NonconstantHeatSource(name, registration),
      testNo(testno)
  {}
  virtual ~TestNonconstantHeatSource() {}
};

#endif
