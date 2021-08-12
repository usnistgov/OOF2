// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFCANVASIMAGE_H
#define OOFCANVASIMAGE_H

#include "canvasitem.h"
#include "utility.h"
#include <string>

#ifdef OOFCANVAS_USE_IMAGEMAGICK
#include <Magick++.h>
#endif // OOFCANVAS_USE_IMAGEMAGICK

namespace OOFCanvas {

  // TODO? Arbitrary rotation.

  class CanvasImage : public CanvasItem {
  protected:
    Coord location;	      // lower-left corner in user coordinates
    Coord size;
    ICoord pixels;
    double opacity;
    bool pixelScaling;
    bool drawPixelByPixel;
    unsigned char *buffer;	// points to data owned by Cairo::ImageSurface
    int stride;
    Cairo::RefPtr<Cairo::ImageSurface> imageSurface;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const;
    virtual bool containsPoint(const OffScreenCanvas*, const Coord&) const;
    void setUp(Cairo::RefPtr<Cairo::ImageSurface>,
	       double, double);	// displayed size
    void setSurface(Cairo::RefPtr<Cairo::ImageSurface>, const ICoord&);
  public:
    CanvasImage(const Coord &pos, const Coord &size, const ICoord &npixels);
    virtual const std::string &classname() const;
    friend std::ostream &operator<<(std::ostream&, const CanvasImage&);
    virtual std::string print() const;

    virtual void pixelExtents(double&, double&, double&, double&) const;

    static CanvasImage *newBlankImage(
			      const Coord&, // position
			      const ICoord&,// no. of pixels
			      const Coord&, // displayed size
			      const Color&);

    static CanvasImage *newFromPNGFile(const Coord&,	   // position
				       const std::string&, // filename
				       const Coord&);	   // displayed size

    // versions with pointer args are used from python
    static CanvasImage *newBlankImage(
			      const Coord*, // position
			      const ICoord*,	 // no. of pixels
			      const Coord*, // displayed size
			      const Color&);

    static CanvasImage *newFromPNGFile(const Coord*,	   // position
				       const std::string&, // filename
				       const Coord*);	   // displayed size
    
#ifdef OOFCANVAS_USE_IMAGEMAGICK
    static CanvasImage *newFromImageMagickFile(const Coord&, // position
					       const std::string&, // filename
					       const Coord&); // disp. size

    static CanvasImage *newFromImageMagickFile(const Coord*, // position
					       const std::string&, // filename
					       const Coord*); // disp. size
    
    static CanvasImage *newFromImageMagick(const Coord&,	// position
					   Magick::Image,
					   const Coord&); // displayed size
#endif // OOFCANVAS_USE_IMAGEMAGICK

    void setPixelSize(); 	// TODO GTK3: get rid of this
    void setDrawIndividualPixels() { drawPixelByPixel = true; }

    // set the color of a single pixel
    void set(const ICoord&, const Color&);
    Color get(const ICoord&) const;

    // overall opacity
    void setOpacity(double alpha) { opacity = alpha; }

  };
  
  std::ostream &operator<<(std::ostream&, const CanvasImage&);

};				// namespace OOFCanvas


#endif // OOFCANVASIMAGE_H
