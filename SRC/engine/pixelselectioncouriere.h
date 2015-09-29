// -*- C++ -*-
// $RCSfile: pixelselectioncouriere.h,v $
// $Revision: 1.6 $
// $Author: langer $
// $Date: 2014/09/27 21:40:50 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef PIXELSELECTIONCOURIERE_H
#define PIXELSELECTIONCOURIERE_H

#include "common/pixelselectioncourier.h"
#include "common/array.h"
#include <vector>

class CMicrostructure;
class CSkeletonElement;
class Coord;
class ICoord;
class Material;

// ElementSelection
class ElementSelection : public PixelSelectionCourier {
private:
  const CSkeletonElement *element;
  const std::vector<ICoord> *selected;
  std::vector<ICoord>::const_iterator sel_iter;
public:
  ElementSelection(const CMicrostructure *ms,
		   const CSkeletonElement *element);
  virtual ~ElementSelection();
  virtual void start();
  virtual ICoord currentPoint() const;
  virtual void next();
  virtual void print(std::ostream &os) const;
};    

// SegmentSelection
class SegmentSelection : public PixelSelectionCourier {
private:
  const Coord n0, n1;
  const std::vector<ICoord> *selected;
  std::vector<ICoord>::const_iterator sel_iter;
public:
  SegmentSelection(const CMicrostructure *ms,
		   const Coord *n0, const Coord *n1);
  virtual ~SegmentSelection();
  virtual void start();
  virtual ICoord currentPoint() const;
  virtual void next();
  virtual void print(std::ostream &os) const;
};

class MaterialSelectionBase : public PixelSelectionCourier {
private:
  Array<PixelAttribute*>::const_iterator iter;
  Array<PixelAttribute*>::const_iterator iterend;
public:
  MaterialSelectionBase(const CMicrostructure*);
  virtual void start();
  virtual ICoord currentPoint() const;
  virtual void next();
  virtual void print(std::ostream&) const = 0;
  virtual bool ok(const Material*) const = 0;
};

class MaterialSelection : public MaterialSelectionBase {
private:
  const Material *material;
public:
  MaterialSelection(const CMicrostructure*, const Material*);
  virtual bool ok(const Material*) const;
  virtual void print(std::ostream&) const;
};

class AnyMaterialSelection : public MaterialSelectionBase  {
public:
  AnyMaterialSelection(const CMicrostructure*);
  virtual bool ok(const Material*) const;
  virtual void print(std::ostream&) const;
};

class NoMaterialSelection : public MaterialSelectionBase {
public:
  NoMaterialSelection(const CMicrostructure*);
  virtual bool ok(const Material*) const;
  virtual void print(std::ostream&) const;
};

#endif // PIXELSELECTIONCOURIERE_H
