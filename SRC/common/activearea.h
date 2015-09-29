// -*- C++ -*-
// $RCSfile: activearea.h,v $
// $Revision: 1.9 $
// $Author: langer $
// $Date: 2014/09/27 21:40:15 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef ACTIVEAREA_H
#define ACTIVEAREA_H

#include <list>
#include <string>
#include <vector>
#include "common/cpixelselection.h"
#include "common/pixelattribute.h"

class ActiveArea : public CPixelSelection {
  bool override_;
public:
  ActiveArea(const ICoord *pxlsize, const Coord *size,
	      CMicrostructure *ms)
    : CPixelSelection(pxlsize, size, ms), override_(false)
  {}
  virtual ~ActiveArea();
  ActiveArea *clone() const { return new ActiveArea(*this); }
  bool isActive(const ICoord *pxl) const {
    return override_ || !isSelected(pxl);
  }
  bool isActive(const ICoord &pxl) const {
    return override_ || !isSelected(&pxl);
  }
  void override(bool val) { 
    override_ = val; }
  bool getOverride() const { return override_; }

  void add_pixels(std::vector<ICoord>*);

// This function doesn't exist, because PixelGroup::nonmembers()
// doesn't exist.  It would be an expensive function to compute, so
// it's probably better to avoid needing a list of active pixels.
//
//   const std::vector<ICoord> *activePixels() const {
//     return getPixelGroup()->nonmembers();
//   }

};



// Pixels in the microstructure can be members of named active areas.
// Note that being a member of an active area means that this pixel is
// *inactive* when the active area in question is current.


class ActiveAreasAttributeRegistration: public PxlAttributeRegistration {
private:
  static const std::string classname_;
  static const std::string modulename_;
public:
  ActiveAreasAttributeRegistration();
  virtual ~ActiveAreasAttributeRegistration() {}
  virtual PixelAttribute* createAttribute(const ICoord&) const;
  virtual const std::string &classname() const { return classname_;}
  virtual const std::string &modulename() const { return modulename_;}
};


class ActiveAreaList : public PixelAttribute {
private:
  static ActiveAreasAttributeRegistration* reg;
  std::list<std::string> areas; // List of names of active areas.
public:
  ActiveAreaList() {}
  void add(const std::string&);
  void remove(const std::string&);
  std::vector<std::string>* getNames() const;
  virtual bool operator<(const PixelAttribute&) const;
  virtual bool strictLessThan(const PixelAttribute&) const;
  virtual void print(std::ostream&) const;
  // These two need access to the "reg" datum.
  friend class ActiveAreasAttributeRegistration;
  friend ActiveAreaList *areaListFromPixel(const CMicrostructure*,
					   const ICoord*);
};
  
// Utility function for geting the AAList object from a particular pixel.

ActiveAreaList *areaListFromPixel(const CMicrostructure*, const ICoord*);

#endif // ACTIVEAREA_H
