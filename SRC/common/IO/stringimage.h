// -*- C++ -*-
// $RCSfile: stringimage.h,v $
// $Revision: 1.14 $
// $Author: langer $
// $Date: 2014/09/27 21:40:32 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

// Class for representing an Image as a string, as a step on the way
// to creating a GdkImlibImage.  Putting this class in C++ instead of
// Python allows the C++ BitmapOverlay to be drawn without passing it
// back out to Python.

#ifndef STRINGIMAGE
#define STRINGIMAGE

#include "common/coord.h"
#include "common/ccolor.h"
#include <string>

class BitmapOverlay;
class BoolArray;
class ShapedStringImage;

class StringImage {
protected:
  unsigned char *data;
  ICoord isize_;
  Coord size_;
  int getOffset(const ICoord&) const;
public:
  StringImage(const ICoord *isize,  const Coord *size);
  ~StringImage();
  const ICoord &sizeInPixels() const { return isize_; }
  const Coord &size() const { return size_; }
  void set(const ICoord *where, const CColor *color);
  CColor get(const ICoord *) const;
  const unsigned char *getString() const { return data; }
  const std::string *hexstringimage() const;  //used for pdf output
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class AlphaStringImage {
protected:
  unsigned char *data;
  ICoord isize_;
  Coord size_;
  int getOffset(const ICoord &) const;
public:
  AlphaStringImage(const ICoord *isize, const Coord *size);
  ~AlphaStringImage();
  const ICoord &sizeInPixels() const { return isize_; }
  const Coord &size() const { return size_; }
  void set(const ICoord *where, const CColor *color, unsigned char alpha);
  const unsigned char *getString() const { return data; }
};

#endif // STRINGIMAGE
