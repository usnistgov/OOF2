// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELDIFFERENTIATORI_H
#define PIXELDIFFERENTIATORI_H

#include <oofconfig.h>
#include <vector>
#include <Magick++.h>

#include "common/array.h"
#include "common/burn.h"
#include "common/statgroups.h"

class OOFImage;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class CColorDifferentiator3 : public CPixelDifferentiator3 {
private:
  const OOFImage *image;
  double local_flammability;
  double global_flammability;
  bool useL2norm;
#ifndef USE_SKIMAGE
  const Magick::PixelPacket *rawpixels;
#endif // USE_SKIMAGE
public:
  CColorDifferentiator3(const OOFImage *image, double lf, double gf, bool l2);
  virtual bool operator()(const ICoord&, const ICoord&, const ICoord&) const;
};

class CColorDifferentiator2 : public CPixelDifferentiator2 {
private:
  const OOFImage *image;
  double color_delta;
  bool useL2norm;
#ifndef USE_SKIMAGE
  const Magick::PixelPacket *rawpixels;
#endif // USE_SKIMAGE
public:
  CColorDifferentiator2(const OOFImage *image, double cd, bool l2);
  virtual bool operator()(const ICoord&, const ICoord&) const;
  virtual double distance2(const ICoord&, const ICoord&) const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class ColorPixelDistribution : public PixelDistribution {
protected:
  // Store values as double[3] instead of CColors for easy arithmetic.
  double mean[3];
  double sumsq[3];		// sums of squares of rgb values
  double variance[3]; 		// independent rbg variances,
  double var0;			// variance used when there's only one value
  const OOFImage *image;
#ifndef USE_SKIMAGE
  const Magick::PixelPacket *rawpixels;
#endif // USE_SKIMAGE
  void findVariance();
public:
  ColorPixelDistribution(const ICoord&, const OOFImage*, double);
  ColorPixelDistribution(const std::set<ICoord>&, const OOFImage*, double);
  virtual PixelDistribution *clone(const std::set<ICoord>&) const;
  virtual void add(const ICoord&);
  virtual void merge(const PixelDistribution*);
  virtual double deviation2(const ICoord&) const;
  virtual double deviation2(const PixelDistribution*) const;
#ifdef DEBUG
  virtual std::string stats() const;
  virtual std::string value(const ICoord&) const;
#endif // DEBUG
};

class ColorPixelDistFactory : public PixelDistributionFactory {
protected:
  const OOFImage *image;
  double sigma0;
public:
  ColorPixelDistFactory(const OOFImage *im, double s)
    : image(im), sigma0(s)
  {}
  virtual PixelDistribution *newDistribution(const ICoord&) const;
};

#endif // PIXELDIFFERENTIATORI_H
