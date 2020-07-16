// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "canvasimage.h"
#include <stdlib.h>

namespace OOFCanvas {

  bool getLittleEndian() {
    int k = 1;
    unsigned char *c = (unsigned char*) &k;
    return *c;
  }

  static bool littleEndian = getLittleEndian();

  CanvasImage::CanvasImage(const Coord &loc, const Coord &sz, const ICoord &pix)
    : CanvasItem(Rectangle(loc, loc+sz)),
      location(loc),	// position of lower left corner in user units
      size(sz),
      pixels(pix),
      opacity(1.0),
      pixelScaling(false),
      drawPixelByPixel(false),
      buffer(nullptr),
      stride(0)
  {}

  const std::string &CanvasImage::classname() const {
    static std::string nm("CanvasImage");
    return nm;
  }

  // The CanvasImage::set methods set the color and opacity of a
  // single pixel.  They probably don't work correctly unless the
  // Cairo image format is FORMAT_ARGB32.
  
  void CanvasImage::set(int x, int y, double r, double g, double b) {
    assert(buffer != nullptr);
    assert(stride != 0);
    unsigned char *addr = buffer + y*stride + 4*x;
    if(littleEndian) {
      *addr++ = b*255;
      *addr++ = g*255;
      *addr++ = r*255;
      *addr = 255;
    }
    else {
      *addr++ = 255;	// alpha
      *addr++ = r*255;
      *addr++ = g*255;
      *addr   = b*255;
    }
    imageSurface->mark_dirty();
    modified();
  }

  void CanvasImage::set(int x, int y, double r, double g, double b, double a) {
    assert(buffer != nullptr);
    assert(stride != 0);
    unsigned char *addr = buffer + y*stride + 4*x;
    if(littleEndian) {
      *addr++ = b*255;
      *addr++ = g*255;
      *addr++ = r*255;
      *addr   = a*255;
    }
    else {
      *addr++ = a*255;	// alpha
      *addr++ = r*255;
      *addr++ = g*255;
      *addr   = b*255;
    }
    imageSurface->mark_dirty();
    modified();
  }


  void CanvasImage::set(int x, int y,
			unsigned char r, unsigned char g, unsigned char b)
  {
    assert(buffer != nullptr);
    assert(stride != 0);
    unsigned char *addr = buffer + y*stride + 4*x;
    if(littleEndian) {
      *addr++ = b;
      *addr++ = g;
      *addr++ = r;
      *addr = 255;
    }
    else {
      *addr++ = 255;
      *addr++ = r;
      *addr++ = g;
      *addr   = b;
    }
    imageSurface->mark_dirty();
    modified();
  }

  void CanvasImage::set(int x, int y,
			unsigned char r, unsigned char g, unsigned char b,
			unsigned char a)
  {
    assert(buffer != nullptr);
    assert(stride != 0);
    unsigned char *addr = buffer + y*stride + 4*x;
    if(littleEndian) {
      *addr++ = b;
      *addr++ = g;
      *addr++ = r;
      *addr   = a;
    }
    else {
      *addr++ = a;
      *addr++ = r;
      *addr++ = g;
      *addr   = b;
    }
    imageSurface->mark_dirty();
    modified();
  }

  Color CanvasImage::get(int x, int y) const {
    assert(buffer != nullptr);
    assert(stride != 0);
    unsigned char *addr = buffer + y*stride + 4*x;
    unsigned char r, g, b, a;
    if(littleEndian) {
      b = *addr++;
      g = *addr++;
      r = *addr++;
      a = *addr;
    }
    else {
      a = *addr++;
      r = *addr++;
      g = *addr++;
      b = *addr;
    }
    return Color(r/255., g/255., b/255., a/255.);
  }

  void CanvasImage::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {

    // The native Cairo image drawing method antialiases each pixel --
    // maybe that's not the right term for it, but each pixel is
    // blurry if you zoom way in.  This may be what you want if you're
    // showing pictures from your vacation, but if the pixels are
    // individual data points that you are examining, you don't want
    // to antialias them.  If drawPixelByPixel is false, then the
    // native Cairo rendering is used.  If it's true, then the pixels
    // are drawn as individual filled rectangles.

    // Drawing the individual rectangles has three possible drawbacks.
    // First, it might be slow (but I haven't actually timed it).
    // Second, it can lead to aliasing problems in which adjacent
    // image pixels don't actually meet when drawn on the screen,
    // producing a stripe of the background color across the image.
    // This can often be fixed by scaling the whole image by a factor
    // very close to one.  Third, when converted to pdf or some other
    // printable format, the boundaries between the image pixels can
    // sometimes be seen.

    // The default behavior of CanvasImage is to use the Cairo
    // rendering and not draw the individual pixels.  To change it,
    // call CanvasImage::setDrawIndividualPixels().
    
    if(!drawPixelByPixel) {
      // Scaling the context to change the image size also changes the
      // location, so convert the location to device units before
      // scaling, then convert back afterwards.
      double posX, posY;
      if(!pixelScaling) {
	posX = location.x;
	posY = location.y + size.y;
	ctxt->user_to_device(posX, posY);
	ctxt->scale(size.x/pixels.x, -size.y/pixels.y);
	ctxt->device_to_user(posX, posY);
      }
      else {
	// Given size is in device pixels
	// Find the size (dx, dy) of a pixel in user coordinates
	double dx = 1.0;		
	double dy = 1.0;
	ctxt->device_to_user_distance(dx, dy);
	// dy is negative now.

	// Get the desired display position in device coordinates
	posX = location.x;
	posY = location.y;
	ctxt->user_to_device(posX, posY);

	// Scaling x by dx would make image pixels correspond to device
	// pixels, so scale by dx*size.x/pixels.x to make the image fit
	// into size.x device pixels.
	ctxt->scale(dx*size.x/pixels.x, dy*size.y/pixels.y);
	posY -= size.y;
      
	// Convert the display position back to user coordinates
	ctxt->device_to_user(posX, posY);
      }
      ctxt->set_source(imageSurface, posX, posY);
      if(opacity == 1.0)
	ctxt->paint();
      else
	ctxt->paint_with_alpha(opacity);
    }
    else {
      // drawPixelByPixel==true
      ctxt->save();
      ctxt->set_antialias(Cairo::ANTIALIAS_NONE);
      double dx = size.x/pixels.x;
      double dy = size.y/pixels.y;
      if(pixelScaling) {
	ctxt->device_to_user_distance(dx, dy); // changes sign of dy
	dy *= -1;
      }

      for(unsigned int j=0; j<pixels.y; j++) {
	for(unsigned int i=0; i<pixels.x; i++) {
	  Color clr = get(i, pixels.y-j-1);
	  clr.set(ctxt);
	  ctxt->move_to(location.x + i*dx, location.y+j*dy);
	  ctxt->rel_line_to(dx, 0);
	  ctxt->rel_line_to(0, dy);
	  ctxt->rel_line_to(-dx, 0);
	  ctxt->close_path();
	  ctxt->fill();
	}
      }
      ctxt->restore();

    }
  }

  void CanvasImage::setPixelSize() {
    // Change from user units to pixel units.
    pixelScaling = true;
    // The "bare" bounding box is just a point.
    bbox = Rectangle(location, location);
    modified();
  }

  void CanvasImage::pixelExtents(double &left, double &right,
				 double &up, double &down)
    const
  {
    left = 0.0;
    down = 0.0;
    if(pixelScaling) {
      right = size.x;
      up = size.y;
    }
    else {
      right = 0.0;
      up = 0.0;
    }
  }

  bool CanvasImage::containsPoint(const OffScreenCanvas*, const Coord&) const {
    // This isn't called unless the point is within the bounding box,
    // and images fill their bounding boxes, so there's nothing to do
    // here.
    // TODO: That's not necessarily true if we allow images to be
    // rotated by arbitrary angles.
    return true;
  }

  std::string CanvasImage::print() const {
    return to_string(*this);
  }
  
  std::ostream &operator<<(std::ostream &os, const CanvasImage &canvasImage) {
    os << "CanvasImage(pixels=" << canvasImage.pixels
       << ", size=" << canvasImage.size
       << ", position=" << canvasImage.location
       << ")";
    return os;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Utility functions used when creating CanvasImages

  // If an image's physical (displayed) size has one or more negative
  // components, the actual value of that component is inferred from
  // the size in pixels, assuming that pixels are square.

  static Coord imageSize(double width, double height,
			 double pixWidth, double pixHeight)
  {
    if(width <= 0 && height <=0)
      return Coord(pixWidth, pixHeight); // assume pixels are 1x1 
    if(height <= 0)
      return Coord(width, width*pixHeight/pixWidth); // assume square pixels
    if(width <= 0)
      return Coord(height*pixWidth/pixHeight, height); // assume square pixels
    return Coord(width, height);
  }

  void CanvasImage::setSurface(Cairo::RefPtr<Cairo::ImageSurface> surf,
			       int width)
  {
    imageSurface = surf;
    buffer = surf->get_data();
    stride = Cairo::ImageSurface::format_stride_for_width(surf->get_format(),
							  width);
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Factory methods for creating CanvasImages from different sources

  // static
  CanvasImage *CanvasImage::newBlankImage(
			  double x, double y, // position
			  int w, int h,	      // size in pixels of image data
			  double width, double height, // size in display units
			  double r, double g, double b, // color
			  double a)			// opacity
  {
    CanvasImage *canvasImage = new CanvasImage(Coord(x, y),
					       imageSize(width, height, w, h),
					       ICoord(w, h));
    Cairo::RefPtr<Cairo::ImageSurface> surf =
      Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32, w, h);
    canvasImage->setSurface(surf, w);

    int stride = canvasImage->stride;
    unsigned char *buffer = canvasImage->buffer;
    if(littleEndian) {
      for(int j=0; j<h; j++) {
	unsigned char *rowaddr = buffer + j*stride;
	for(int i=0; i<w; i++) {
	  unsigned char *addr = rowaddr + 4*i;
	  *addr++ = b*255;
	  *addr++ = g*255;
	  *addr++ = r*255;
	  *addr =   a*255;
	}
      }
    }
    else {			// big-endian
      for(int j=0; j<h; j++) {
	unsigned char *rowaddr = buffer + j*stride;
	for(int i=0; i<w; i++) {
	  unsigned char *addr = rowaddr + 4*i;
	  *addr++ = a*255;
	  *addr++ = r*255;
	  *addr++ = g*255;
	  *addr++ = b*255;
	}
      }

    }
    canvasImage->imageSurface->mark_dirty();
    return canvasImage;
  }

  // static
  CanvasImage *CanvasImage::newFromPNGFile(double x, double y,
					   const std::string &filename,
					   double width, double height)
  {
    // Read the file first, to get the size in pixels.
    Cairo::RefPtr<Cairo::ImageSurface> surf =
      Cairo::ImageSurface::create_from_png(filename);
    int w = surf->get_width();	// pixel sizes
    int h = surf->get_height();
    CanvasImage *canvasImage = new CanvasImage(
				       Coord(x,y),
				       imageSize(width, height, w, h),
				       ICoord(w, h));
    canvasImage->setSurface(surf, w);
    return canvasImage;
  }

#ifdef OOFCANVAS_USE_IMAGEMAGICK

  // static
  CanvasImage *CanvasImage::newFromImageMagickFile(double x, double y,
						   const std::string &filename,
						   double width, double height)
  {
    Magick::Image image;	// reference counted
    image.read(filename);
    return CanvasImage::newFromImageMagick(x, y, image, width, height);
  }

  // static
  CanvasImage *CanvasImage::newFromImageMagick(double x, double y,
					       Magick::Image image,
					       double width, double height)
  {
    Magick::Geometry sz = image.size();
    int w = sz.width();
    int h = sz.height();
    CanvasImage *canvasImage = new CanvasImage(Coord(x,y),
					       imageSize(width, height, w, h),
					       ICoord(w, h));
    Cairo::RefPtr<Cairo::ImageSurface> surf =
      Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32, w, h);
    canvasImage->setSurface(surf, w);

    // Copy pixel data from ImageMagick to the Cairo buffer.
    // Cairo uses libpixman for image storage.  There is no
    // documentation for libpixman.

    // See _cairo_format_from_pixman_format() in cairo-image-surface.c
    // in the Cairo source for the correspondence between pixman and
    // Cairo formats.  Cairo::FORMAT_ARGB32 corresponds to
    // PIXMAN_a8r8g8b8.

    // From https://afrantzis.com/pixel-format-guide/pixman.html:
    // The pixel is represented by a 32-bit value, with A in bits
    // 24-31, R in bits 16-23, G in bits 8-15 and B in bits 0-7.
    // On little-endian systems the pixel is stored in memory as the
    // bytes B, G, R, A (B at the lowest address, A at the highest).
    // On big-endian systems the pixel is stored in memory as the
    // bytes A, R, G, B (A at the lowest address, B at the highest).
    
    unsigned char *buffer = canvasImage->buffer;
    using namespace Magick;	// Magick::QuantumRange doesn't work?
    double scale = 255./QuantumRange;
    Magick::PixelPacket *pixpax = image.getPixels(0, 0, w, h);
    int stride = canvasImage->stride;
    if(littleEndian) {
      for(int j=0; j<h; j++) {
	unsigned char *rowaddr = buffer + j*stride;
	for(int i=0; i<w; i++) {
	  const Magick::PixelPacket *pp = pixpax + (i + j*w);
	  unsigned char *addr = rowaddr + 4*i;
	  *addr++ = pp->blue*scale;
	  *addr++ = pp->green*scale;
	  *addr++ = pp->red*scale;
	  *addr   = 255;	// alpha
	}
      }
    }
    else {			// big endian
      for(int j=0; j<h; j++) {
	unsigned char *rowaddr = buffer + j*stride;
	for(int i=0; i<w; i++) {
	  const Magick::PixelPacket *pp = pixpax + i + j*w;
	  unsigned char *addr = rowaddr + 4*i;
	  *addr++ = 255;	// alpha
	  *addr++ = pp->red*scale;
	  *addr++ = pp->green*scale;
	  *addr   = pp->blue*scale;
	}
      }
    }
    canvasImage->imageSurface->mark_dirty();

    return canvasImage;
  }
  
#endif // OOFCANVAS_USE_IMAGEMAGICK
  
};				// namespace OOFCanvas
