// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOF_CANVASTEXT_H
#define OOF_CANVASTEXT_H

#include "canvasitem.h"
#include "utility.h"
#include <vector>
#include <string>

namespace OOFCanvas {
  class CanvasText : public CanvasItem, public PixelSized {
  protected:
    const Coord location;
    const std::string text;
    double angle;
    Color color;
    std::string fontName;
    bool sizeInPixels;

    bool antiAlias;
    virtual void drawItem(Cairo::RefPtr<Cairo::Context>) const;
    virtual bool containsPoint(const OffScreenCanvas*, const Coord&) const;
    PangoLayout *getLayout(Cairo::RefPtr<Cairo::Context>) const;
    Rectangle findBoundingBox_(double) const;
  public:
    CanvasText(double, double, const std::string &text);
    ~CanvasText();
    virtual const std::string &classname() const;
    void setFillColor(const Color&);
    void setFont(const std::string&, bool);
    void rotate(double);	// in degrees

    virtual const Rectangle &findBoundingBox(double ppu);
    virtual bool pixelSized() const { return sizeInPixels; }
    virtual Coord referencePoint() const { return location; }
    virtual void pixelExtents(double&, double&, double&, double&) const;

    // Antialiasing is turned on by default.  Use this to turn it off.
    void setAntiAlias(bool v) { antiAlias = v; }
    friend std::ostream &operator<<(std::ostream&, const CanvasText&);
    virtual std::string print() const;
  };

  std::vector<std::string> *list_fonts();

  std::ostream &operator<<(std::ostream&, const CanvasText&);

};


#endif // OOF_CANVASTEXT_H
