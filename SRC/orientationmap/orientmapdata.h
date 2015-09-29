// -*- C++ -*-
// $RCSfile: orientmapdata.h,v $
// $Revision: 1.6 $
// $Author: langer $
// $Date: 2014/09/27 21:41:40 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef ORIENTMAPDATA_H
#define ORIENTMAPDATA_H

class OrientMap;
class COrientMapReader;

#include "common/abstractimage.h"
#include "common/array.h"
#include "common/corientation.h"
#include "image/oofimage.h"
#include <string>
#include <vector>

class Angle2Color;
class StringImage;

class COrientMapReader {
public:
  virtual ~COrientMapReader() {}
  void set_angle(OrientMap &data, const ICoord*, const COrientation*) const;
  friend class OrientMap;
};

// TODO: It might make sense to for OrientMap to be derived from
// Array<COrientABG>.

class OrientMap {
private:
  Array<COrientABG> angles;
  Coord size_;
  std::string name;
public:
  OrientMap(const ICoord*, const Coord*);
  OrientMap(const OrientMap&);
  ~OrientMap();
  const ICoord &sizeInPixels() const { return angles.size(); }
  const Coord &size() const { return size_; }
  ICoord pixelFromPoint(const Coord *point) const;
  bool pixelInBounds(const ICoord *pxl) const;

  typedef Array<COrientABG>::iterator iterator;
  typedef Array<COrientABG>::const_iterator const_iterator;
  iterator begin() { return angles.begin(); }
  iterator end() { return angles.end(); }
  const_iterator begin() const { return angles.begin(); }
  const_iterator end() const { return angles.end(); }

  const COrientABG &angle(const ICoord *pt) const { return angles[*pt]; }
  const COrientABG &angle(const ICoord pt) const { return angles[pt]; }
  void fillstringimage(StringImage*, const Angle2Color&) const;
  OOFImage *createImage(const std::string&, const Angle2Color&) const;
  friend class COrientMapReader;
  friend void registerOrientMap(const std::string&, OrientMap*);
};

void registerOrientMap(const std::string&, OrientMap*);
void removeOrientMap(const std::string&);
OrientMap *getOrientMap(const std::string&);

// OrientMapImage is used when displaying an OrientaionMap object in
// the graphics window.

class OrientMapImage : public AbstractImage {
private:
  const OrientMap *orientmap;
  const Angle2Color *colorscheme;
public:
  OrientMapImage(const OrientMap*, const Angle2Color*);
  virtual ~OrientMapImage();
  virtual const Coord &size() const;
  virtual const ICoord &sizeInPixels() const;
  virtual void fillstringimage(StringImage*) const;
};

#endif // ORIENTMAPDATA_H
