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

#ifndef ORIENTATION_H
#define ORIENTATION_H

#include "engine/corientation.h"
#include "engine/property.h"
#include <string>

class CMicrostructure;
class Element;
class ICoord;
class FEMesh;
class MasterPosition;

class OrientationPropBase : public AuxiliaryProperty {
public:
  OrientationPropBase(const std::string &name, PyObject *registration)
    : AuxiliaryProperty(name, registration)
  {}
  virtual const COrientation *orientation() const = 0;
  virtual const COrientation *orientation(const FEMesh*, const Element*,
					  const MasterPosition&) const = 0;
  virtual const COrientation *orientation(const CMicrostructure*, const ICoord&)
    const = 0;
};

class OrientationProp : public OrientationPropBase {
private:
  const COrientation *orient;
public:
  OrientationProp(const std::string &name, PyObject *registration, 
		  const COrientation *orient);
  ~OrientationProp();
  virtual const COrientation *orientation() const { return orient; }
  virtual const COrientation *orientation(const FEMesh*, const Element*,
				    const MasterPosition&) const;
  virtual const COrientation *orientation(const CMicrostructure*, const ICoord&)
    const;
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);
};

#endif
