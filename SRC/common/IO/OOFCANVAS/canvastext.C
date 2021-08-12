// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "canvastext.h"
#include <math.h>
#include <pango/pangocairo.h>

// TODO: Currently it's not possible to tell if a given point is on a
// CanvasText item, so text items aren't selectable by the mouse.  It
// is possible to tell if a point is inside a text item's bounding
// box, so text could be selected if nearby clicks are acceptable.
// However, it might be possible to render the text to an otherwise
// empty surface and check the color of the selected point on the
// surface.

namespace OOFCanvas {

  // The constructor passes the wrong bbox to the CanvasItem
  // constructor, but that's ok because the CanvasText item can't be
  // used unless setFont is called, and setFont computes the actual
  // bounding box.

  CanvasText::CanvasText(const Coord &location, const std::string &txt)
    : CanvasItem(Rectangle()),
      location(location),
      text(txt),
      angle(0),
      color(black),
      fontName(""),
      sizeInPixels(false)
  {}

  CanvasText::CanvasText(const Coord *location, const std::string &txt)
    : CanvasItem(Rectangle()),
      location(*location),
      text(txt),
      angle(0),
      color(black),
      fontName(""),
      sizeInPixels(false)
  {}
  
  CanvasText::~CanvasText() {}
    

  const std::string &CanvasText::classname() const {
    static const std::string name("CanvasText");
    return name;
  }

  void CanvasText::rotate(double ang) {
    angle = M_PI/180.*ang;
    findBoundingBox_();
    modified();
  }

  void CanvasText::setFillColor(const Color &c) {
    color = c;
    modified();
  }

  void CanvasText::setFont(const std::string &name, bool inPixels) {
    sizeInPixels = inPixels;
    fontName = name;
    bbox.clear();
    modified();
    findBoundingBox_();

    // TODO: Check to see if the name specifies a size in pixels.  If
    // it is, do something appropriate.
    
    // fontDesc = pango_font_description_from_string(name.c_str());
    // std::cerr << "CanvasText::setFont: '" << name
    // 	      << "' absolute="
    // 	      << pango_font_description_get_size_is_absolute(fontDesc)
    // 	      << " size=" << pango_font_description_get_size(fontDesc)
    // 	      << std::endl;
  }

  PangoLayout *CanvasText::getLayout(Cairo::RefPtr<Cairo::Context> ctxt) const {
    // Create a PangoLayout for the given text at the given size,
    // using the given Cairo Context.
    PangoLayout *layout = pango_cairo_create_layout(ctxt->cobj());
    pango_layout_set_text(layout, text.c_str(), -1);

    PangoFontDescription *pfd =
      pango_font_description_from_string(fontName.c_str());
    // If the size is in device units, scale it by the Context's ppu.
    if(sizeInPixels) {
      double dx = 1.0;
      double dy = 1.0;
      ctxt->device_to_user_distance(dx, dy);
      int size = pango_font_description_get_size(pfd);
      pango_font_description_set_size(pfd, size*dx);
    }
      
    pango_layout_set_font_description(layout, pfd);
    // std::cerr << "CanvasText::getLayout: font_desc="
    // 	      << pango_font_description_to_string(pfd) << std::endl;

    pango_font_description_free(pfd);
    return layout;
  }
  
  void CanvasText::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    color.set(ctxt);
    PangoLayout *layout = getLayout(ctxt);
    double baseline = pango_layout_get_baseline(layout)/double(PANGO_SCALE);
    ctxt->rotate(angle);
    ctxt->move_to(location.x, location.y+baseline);
    ctxt->scale(1.0, -1.0); // flip y, because fonts still think y goes down
    pango_layout_context_changed(layout);
    pango_cairo_show_layout(ctxt->cobj(), layout);
    g_object_unref(layout);
  }

  void CanvasText::findBoundingBox_() {
    if(fontName == "")
      return;
    Rectangle bb;
    // To get the bounding box, we need to have a Cairo::Context, but
    // we need the bounding box to figure out the dimensions of the
    // Cairo::Surface, from which we get the Context.  So create a
    // dummy Surface and Context here.
    // Ths size of the Surface doesn't matter.  We need it to create
    // the Context, but the Context doesn't seem to need the Surface
    // to get the text size.
    auto surface = Cairo::RefPtr<Cairo::ImageSurface>(
	      Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32, 10, 10));
    cairo_t *ct = cairo_create(surface->cobj());
    auto ctxt = Cairo::RefPtr<Cairo::Context>(new Cairo::Context(ct, true));

    // Although the size of the dummy Surface doesn't seem to matter,
    // the transformation matrix does.  If the ppu is too small, on
    // Linux (but not Mac) the width (but not the height?) of the
    // rectangle computed by pango_layout_get_extents will be wrong.
    // The size seems to converge as the ppu increases, until
    // something else goes wrong at large ppu.  (Mac is using pango
    // 1.42.4.  Linux has 1.40.14.)

    double ppu = 1.0;
    Cairo::Matrix transf(Cairo::scaling_matrix(ppu, ppu));
    ctxt->set_matrix(transf);

    // Compute bounding box in the text's coordinates
    PangoLayout *layout = getLayout(ctxt);
    try {
      PangoRectangle pango_rect;
      pango_layout_get_extents(layout, nullptr, &pango_rect);
      bb = Rectangle(pango_rect);
      bb.scale(1./PANGO_SCALE, 1./PANGO_SCALE);
    
      if(angle != 0.0) {
	// Find the Rectangle that contains the rotated bounding box,
	// before translating.
	Cairo::Matrix rot(Cairo::rotation_matrix(-angle));
	Rectangle rotatedBBox(bb.lowerRight().transform(rot),
			      bb.upperRight().transform(rot));
	rotatedBBox.swallow(bb.upperLeft().transform(rot));
	rotatedBBox.swallow(bb.lowerLeft().transform(rot));
	bb = rotatedBBox;
      }
    
      bb.scale(1.0, -1.0);
      bb.shift(location);
    }
    catch (...) {
      g_object_unref(layout);
      throw;
    }
    g_object_unref(layout);

    if(sizeInPixels) {
      bbox = Rectangle(location, location);
      pixelBBox = bb;
    }
    else {
      bbox = bb;
    }
  }

  void CanvasText::pixelExtents(double &left, double &right,
				double &up, double &down)
    const
  {
    // When ppu=1, the user-space and device-space bounding boxes are
    // the same.
    left = location.x - pixelBBox.xmin();
    right = pixelBBox.xmax() - location.x;
    // down and up seem to be reversed because our definition of "up"
    // and pango's definition differ.
    down = location.y - pixelBBox.ymax();
    up = pixelBBox.ymin() - location.y;
  }

  bool CanvasText::containsPoint(const OffScreenCanvas*, const Coord&) const {
    return false;
  }

  std::string CanvasText::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasText &text) {
    os << "CanvasText(\"" << text.text << "\")";
    return os;
  }

  std::vector<std::string> *list_fonts() {
    std::vector<std::string> *result = new std::vector<std::string>;
    PangoFontFamily **families;
    int n;
    PangoFontMap *fontmap = pango_cairo_font_map_get_default();
    pango_font_map_list_families(fontmap, &families, &n);
    for(int i=0; i<n; i++) {
      const char *family_name = pango_font_family_get_name(families[i]);
      result->emplace_back(family_name);
    }
    g_free(families);
    return result;
  }


};				// namespace OOFCanvas
