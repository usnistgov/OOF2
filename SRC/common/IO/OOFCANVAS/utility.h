// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFCANVASUTIL_H
#define OOFCANVASUTIL_H

#include <cairomm/cairomm.h>
#include <iostream>
#include <sstream>
#include <pango/pangocairo.h>

namespace OOFCanvas {
  
  class Color {
  public:
    double red, green, blue, alpha;	// 0-1
    Color() : red(0), green(0), blue(0), alpha(1) {}
    Color(double r, double g, double b) 
      : red(r), green(g), blue(b), alpha(1)
    {}
    Color(double r, double g, double b, double a) 
      : red(r), green(g), blue(b), alpha(a)
    {}
    const Color &operator=(const Color &c) {
      red = c.red; green = c.green; blue = c.blue; alpha = c.alpha;
      return *this;
    }
    void set(Cairo::RefPtr<Cairo::Context>) const;
    Color opacity(double) const;
  };

  extern const Color black, white, red, green, blue, gray,
    yellow, magenta, cyan;

  class Coord {
  public:
    double x, y;
    Coord() : x(0.0), y(0.0) {}
    Coord(double x, double y) : x(x), y(y) {}
    Coord(const Coord &p) : x(p.x), y(p.y) {}
    const Coord &operator=(const Coord &p) { x = p.x; y = p.y; return *this; }
    double operator[](int i) const { return i == 0 ? x : y; }
    double &operator[](int i) { return i == 0 ? x : y; }
    Coord &operator*=(double a) { x *= a; y *= a; return *this; }
    Coord &operator/=(double a) { x /= a; y /= a; return *this; }
    Coord &operator+=(const Coord &b) { x += b.x; y += b.y; return *this; }
    Coord &operator-=(const Coord &b) { x -= b.x; y -= b.y; return *this; }
    Coord operator*(double) const;
    Coord operator/(double) const;
    Coord operator+(const Coord&) const;
    Coord operator-(const Coord&) const;
    double operator*(const Coord& b) const { return x*b.x + y*b.y; } // dot prod
    double norm2() const { return x*x + y*y; }
    bool operator==(const Coord&) const;
    bool operator!=(const Coord&) const;
    Coord transform(const Cairo::Matrix&) const;
    
    Coord user_to_device(Cairo::RefPtr<Cairo::Context>) const;
    Coord device_to_user(Cairo::RefPtr<Cairo::Context>) const;
  };

  inline Coord operator*(double a, Coord pt) { return pt*a; }
  double cross(const Coord&, const Coord&);


  std::ostream &operator<<(std::ostream&, const Coord&);

  class ICoord {
  public:
    int x, y;
    ICoord() : x(0), y(0) {}
    ICoord(int x, int y) : x(x), y(y) {}
    ICoord &operator+=(const ICoord &a) { x += a.x; y+= a.y; return *this; }
    ICoord &operator-=(const ICoord &a) { x -= a.x; y-= a.y; return *this; }
    int operator[](int i) const { return i == 0 ? x : y; }
    ICoord operator*(int) const;
    Coord operator*(double) const;
    Coord operator/(double) const;
    ICoord operator+(const ICoord&) const;
    ICoord operator-(const ICoord&) const;
    bool operator==(const ICoord&) const;
    bool operator!=(const ICoord&) const;
  };

  inline Coord operator*(double a, ICoord pt) { return pt*a; }
  inline ICoord operator*(int a, ICoord pt) { return pt*a; }

  Coord operator+(const Coord&, const ICoord&);
  Coord operator+(const ICoord&, const Coord&);
  Coord operator-(const Coord&, const ICoord&);
  Coord operator-(const ICoord&, const Coord&);

  std::ostream &operator<<(std::ostream&, const ICoord&);

  //=\\=//

  class Segment {
  public:
    const Coord p0, p1;
    Segment(double x0, double y0, double x1, double y1)
      : p0(x0, y0), p1(x1, y1)
    {}
    Segment(const Coord &p0, const Coord &p1)
      : p0(p0), p1(p1)
    {}
    // Given a point, compute the normal distance from it to the
    // segment and the relative distance along the segment (0<alpha<1)
    // of its normal projection onto the segment.
    void projection(const Coord&, double &alpha, double &distance) const;

    // angle measured from the x axis, counterclockwise.
    double angle() const;
    Coord interpolate(double) const;
  };

  std::ostream &operator<<(std::ostream&, const Segment&);

  //=\\=//

  // Rectangle is used for bounding boxes.  It's not a rectangle drawn
  // on the canvas. Use CanvasRectangle for that.

  class Rectangle {
  private:
    void setup(double, double, double, double);
  protected:
    Coord pmin, pmax;
    bool initialized_;
  public:
    Rectangle();
    Rectangle(const Coord&, const Coord&);
    Rectangle(double xmin, double ymin, double xmax, double ymax);
    Rectangle(const Rectangle&);
    Rectangle(const PangoRectangle&);
    bool initialized() const { return initialized_; }
    void swallow(const Coord&);
    void swallow(const Rectangle &rect);
    void expand(double);
    void shift(const Coord&);
    void scale(double, double);
    double width() const { return pmax.x - pmin.x; }
    double height() const { return pmax.y - pmin.y; }
    double xmin() const { return pmin.x; }
    double xmax() const { return pmax.x; }
    double ymin() const { return pmin.y; }
    double ymax() const { return pmax.y; }
    double &xmin() { return pmin.x; }
    double &xmax() { return pmax.x; }
    double &ymin() { return pmin.y; }
    double &ymax() { return pmax.y; }
    Coord lowerLeft() const { return pmin; }
    Coord lowerRight() const { return Coord(pmax.x, pmin.y); }
    Coord upperLeft() const { return Coord(pmin.x, pmax.y); }
    Coord upperRight() const { return pmax; }
    Coord center() const;
    const Rectangle &operator=(const Rectangle&);
    bool contains(const Coord&) const;
    void clear() { initialized_ = false; }
    bool operator==(const Rectangle&) const;
    bool operator!=(const Rectangle&) const;

    Rectangle user_to_device(Cairo::RefPtr<Cairo::Context>) const;
    Rectangle device_to_user(Cairo::RefPtr<Cairo::Context>) const;

    friend std::ostream &operator<<(std::ostream&, const Rectangle&);
  };

  std::ostream &operator<<(std::ostream&, const Rectangle&);

  //=\\=//
  
  template <class TYPE>
  std::string to_string(const TYPE &x) {
    std::ostringstream os;
    os << x;
    return os.str();
  }

  std::ostream &operator<<(std::ostream&, const Cairo::Matrix&);
  bool operator==(const Cairo::Matrix&, const Cairo::Matrix&);

  std::ostream &operator<<(std::ostream&, const std::vector<double>&);
};

#endif // OOFCANVASUTIL_H

