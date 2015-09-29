// -*- C++ -*-
// $RCSfile: pixelgroup.h,v $
// $Revision: 1.35 $
// $Author: langer $
// $Date: 2011/03/04 19:48:11 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef PIXELGROUP_H
#define PIXELGROUP_H

#include <Python.h>
#include "common/boolarray.h"
#include "common/coord.h"
#include "common/lock.h"
#include "common/pixelattribute.h"
//#include "common/pythonexportable.h"
#include <string>
#include <vector>

class BitmapOverlay;
class CMicrostructure;

// PixelSet is the base class for PixelGroup.  It keeps track of the
// pixels, but doesn't manipulate the Microstructure's lists of pixel
// groups or categories.

class PixelSet {
private:
  static int ngroups;
  const int id_;
  bool defunct_;
protected:
  // weed() sorts the list of pixels and removes duplicates.  It's
  // const because it only acts on mutable data.  The data is mutable
  // because weeding happens behind the scenes in const functions like
  // len() and members().
  mutable SLock member_lock;
  void weed() const;
  mutable std::vector<ICoord> members_;
  mutable bool weeded;
  ICoord geometry;
  CMicrostructure *microstructure;
public:
  PixelSet(const ICoord *geometry, CMicrostructure *microstructure);
  PixelSet(const PixelSet&);
  virtual ~PixelSet();
  int id() const { return id_; }
  virtual void set_defunct();		// schedule for destruction
  bool is_defunct() const { return defunct_; }
  void resize(const ICoord *newgeom);
  int len() const;
  PixelSet *clone() const { return new PixelSet(*this); }

  CMicrostructure *getCMicrostructure() const { return microstructure; }
  
  virtual void add(const std::vector<ICoord>*);
  virtual void addWithoutCheck(const std::vector<ICoord>*); // ignore actv area
  virtual void add(const ICoord&);
  virtual void remove(const std::vector<ICoord>*);
  virtual void removeWithoutCheck(const std::vector<ICoord>*);
  virtual ICoord pop();
  virtual void clear();

  virtual void setFromBitmap(const BitmapOverlay&);

  const ICoord &operator[](int i) const { return members_[i]; }
  const std::vector<ICoord> *members() const;

  void despeckle(int threshold, BoolArray &selected) const;
#ifndef DIM_3
  void elkcepsed(int threshold, BoolArray &selected) const;
  void expand(double range, BoolArray &selected) const;
  void shrink(double range, BoolArray &selected) const;
#endif // DIM_3
};

class PixelGroup : public PixelSet {
private:
  bool meshable_;
protected:
  std::string name_;
public:
  PixelGroup(const std::string &name, const ICoord *geometry,
	     CMicrostructure *microstructure);
  PixelGroup(const std::string &name, const PixelGroup &othergroup);
  virtual ~PixelGroup();
  bool is_meshable() const { return meshable_; }
  void set_meshable(bool);
  virtual void set_defunct();		// schedule for destruction
  void rename(const std::string &nm) { name_ = nm; }
  virtual void add(const std::vector<ICoord> *pixels);
  virtual void addWithoutCheck(const std::vector<ICoord>*);
  virtual void add(const ICoord&);
  virtual void remove(const std::vector<ICoord> *pixels);
  // virtual ICoord pop();		// removes and returns one pixel
  // virtual void setFromBitmap(const BitmapOverlay&);
  virtual void clear();

  const std::string &name() const { return name_; }
  bool operator<(const PixelGroup &other) const { return name_ < other.name(); }
};

struct PixelGroupCompare {
  bool operator()(const PixelGroup *a, const PixelGroup *b) const {
    return (*a) < (*b);
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class GroupList : public PixelAttribute {
private:
  mutable std::vector<PixelGroup*> data;
  mutable bool sorted;
  static bool groupsorter(const PixelGroup*, const PixelGroup*);
  void sort() const;
public:
  GroupList() : sorted(true) {}
  virtual bool operator<(const PixelAttribute&) const;
  virtual bool strictLessThan(const PixelAttribute&) const;
  void add(PixelGroup *group);
  void remove(PixelGroup *group);
  const std::vector<PixelGroup*> &members() const;
  void resort() { sorted = false; }
  bool contains(const PixelGroup*) const;
  virtual void print(std::ostream&) const;
};

std::vector<std::string> *pixelGroupNames(const CMicrostructure*,
					  const ICoord*);

bool pixelGroupQueryPixel(const CMicrostructure&, const ICoord&,
			  const PixelGroup*);

class PixelGroupAttributeRegistration : public PxlAttributeRegistration {
private:
  static const std::string classname_;
  static const std::string modulename_;
public:
  PixelGroupAttributeRegistration();
  virtual ~PixelGroupAttributeRegistration() {}
  virtual PixelAttribute *createAttribute(const ICoord&) const {
    return new GroupList();
  }
  virtual const std::string &classname() const { return classname_;}
  virtual const std::string &modulename() const { return modulename_; }
};

#endif // PIXELGROUP_H
