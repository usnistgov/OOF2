// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef FORCEDENSITY_H
#define FORCEDENSITY_H

#include <oofconfig.h>
#include "engine/property.h"
#include <string>

class CSubProblem;
class Element;
class Equation;
class FEMesh;
class SmallSystem;

class ForceDensity : public EqnProperty {
private:
  double gx, gy;
#if DIM==3
  double gz;
#endif
public:
#if DIM==2
  ForceDensity(PyObject *reg, const std::string &name, double x, double y);
#elif DIM==3
  ForceDensity(PyObject *reg, const std::string &name, double x, double y, double z);
#endif
  virtual ~ForceDensity() {}
  virtual void force_value(const FEMesh*, const Element*, const Equation*,
			   const MasterPosition&, double time, SmallSystem*) const;
  virtual int integration_order(const CSubProblem*, const Element*) const;
  double fdensity_x() const { return gx; }
  double fdensity_y() const { return gy; }
#if DIM==3
  double fdensity_z() const { return gz; }
#endif

  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);
};

#endif
