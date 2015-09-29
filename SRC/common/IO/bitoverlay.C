// -*- C++ -*-
// $RCSfile: bitoverlay.C,v $
// $Revision: 1.24 $
// $Author: langer $
// $Date: 2011/07/21 15:26:48 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/IO/bitoverlay.h"
#include "common/trace.h"
#include "common/tostring.h"
#include "common/IO/stringimage.h"

BitmapOverlay::BitmapOverlay(const Coord *size, const ICoord *isize)
  : fg(CColor(1., 1., 1.)),
    bg(CColor(0., 0., 0.))
{
    resize(size, isize);
		tintAlpha = 1.0;
		voxelAlpha = 1.0;
}

BitmapOverlay::~BitmapOverlay() {}

void BitmapOverlay::resize(const Coord *size, const ICoord *isize) {
  size_ = *size;
  sizeInPixels_ = *isize;
  clear();
}

void BitmapOverlay::clear() {
  data.resize(sizeInPixels_);
  data.clear(false);
  ++timestamp;
}

void BitmapOverlay::invert() {
  data.invert();
}

void BitmapOverlay::set(const ICoord *pixel) {
  data.set(pixel);
  ++timestamp;
}

void BitmapOverlay::set(const std::vector<ICoord> *pixels) {
  for(std::vector<ICoord>::const_iterator i=pixels->begin();i<pixels->end();++i)
    if(data.contains(*i))
      data.set(&*i);
  ++timestamp;
}

void BitmapOverlay::reset(const std::vector<ICoord> *pixels) {
  for(std::vector<ICoord>::const_iterator i=pixels->begin();i<pixels->end();++i)
    if(data.contains(*i))
      data.reset(&*i);
  ++timestamp;
}

void BitmapOverlay::reset(const ICoord *pixel) {
  data.reset(pixel);
  ++timestamp;
}

void BitmapOverlay::toggle(const ICoord *pixel) {
  data.toggle(pixel);
  ++timestamp;
}

void BitmapOverlay::toggle(const std::vector<ICoord> *pixels) {
  for(std::vector<ICoord>::const_iterator i=pixels->begin();i<pixels->end();++i)
    if(data.contains(*i))
      data.toggle(&*i);
  ++timestamp;
}

bool BitmapOverlay::get(const ICoord *pixel) const {
  if(data.contains(*pixel))
    return data.get(*pixel);
  return false;
}

void BitmapOverlay::copy(const BitmapOverlay *other) {
  data = other->data.clone();
  // avoid taking address of temporary
  CColor x(other->getFG());
  setColor(&x);
  tintAlpha = other->getTintAlpha();
  voxelAlpha = other->getVoxelAlpha();
}

void BitmapOverlay::setColor(const CColor *color) {
  // TODO:  A comment here would be nice.  What is this doing?
  fg = *color;
  if(fg.getRed() == 0.0) {
    bg.setRed(1.0);
    bg.setGreen(1.0);
    bg.setBlue(1.0);
  }
  else {
    bg.setRed(0.0); 
    bg.setBlue(0.0);
    bg.setGreen(0.0);
  }
}

CColor BitmapOverlay::getBG() const {
  return bg;
}

CColor BitmapOverlay::getFG() const {
  return fg;
}

// Construct a string representation of the image, for making a gdk
// pixbuf.

void BitmapOverlay::fillstringimage(StringImage *stringimage) const {
  for(Array<bool>::const_iterator i=data.begin(); i!=data.end(); ++i) {
    if(data[i])
      stringimage->set(&i.coord(), &fg);
    else
      stringimage->set(&i.coord(), &bg);
  }
}

void BitmapOverlay::fillalphastringimage(AlphaStringImage *stringimage) const
{
  CColor black(0., 0., 0.);
  for(Array<bool>::const_iterator i=data.begin(); i!=data.end(); ++i) {
    if(data[i])
      stringimage->set(&i.coord(), &fg, (unsigned char)(255*tintAlpha));
    else
      stringimage->set(&i.coord(), &black, 0);
  }
}
