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

#include "common/IO/bitoverlay.h"
#include "common/trace.h"
#include "common/tostring.h"
#include "oofcanvas/oofcanvas.h"

BitmapOverlay::BitmapOverlay(const Coord *size, const ICoord *isize)
  : fg(CColor(1., 1., 1., 1.)),
    bg(CColor(0., 0., 0., 1.))
{
    resize(size, isize);
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
}

void BitmapOverlay::setColor(const CColor *color) {
  fg = *color;
}

CColor BitmapOverlay::getBG() const {
  return bg;
}

CColor BitmapOverlay::getFG() const {
  return fg;
}

OOFCanvas::CanvasImage *BitmapOverlay::makeCanvasImage(const Coord *position,
						       const Coord *size)
  const
{
  using OOFCanvas::CanvasImage;
  CanvasImage *img = CanvasImage::newBlankImage(
				OOFCANVAS_COORD(*position),
				OOFCANVAS_ICOORD(sizeInPixels_),
				canvasColor(bg).opacity(0.0));
  img->setDrawIndividualPixels(true);
  img->setSize(OOFCANVAS_COORD(*size));
  int ymax = sizeInPixels_[1] - 1;
  for(Array<bool>::const_iterator i=data.begin(); i!=data.end(); ++i) {
    if(data[i]) {
      ICoord p(i.coord());
      img->set(OOFCanvas::ICoord(p[0], ymax-p[1]), canvasColor(fg));
    }
  }
  return img;
}

