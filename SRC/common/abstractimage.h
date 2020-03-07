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

#ifndef ABSTRACTIMAGE_H
#define ABSTRACTIMAGE_H

class Coord;
class ICoord;
class StringImage;
class AlphaStringImage;

class AbstractImage {
public:
  virtual ~AbstractImage() {}
  virtual const Coord &size() const = 0;
  virtual const ICoord &sizeInPixels() const = 0;
  virtual CanvasImage makeCanvasImage(const Coord *pos, const Coord *size)
    const = 0;
};

#endif // ABSTRACTIMAGE_H
