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

#include "common/ccolor.h"
#include "common/tostring.h"
#include "image/oofimage.h"
#include "image/pixeldifferentiator.h"

#include <set>
#include <algorithm>
#include <math.h>


CColorDifferentiator3::CColorDifferentiator3(const OOFImage *image,
					     double lf, double gf, bool l2)
  : image(image),
    local_flammability(lf),
    global_flammability(gf),
    useL2norm(l2),
    rawpixels(image->pixelPacket())
{}

bool CColorDifferentiator3::operator()(const ICoord &target,
				      const ICoord &local_reference,
				      const ICoord &global_reference)
  const
{
  const CColor trgt = image->getColor(target, rawpixels);
  const CColor lcl = image->getColor(local_reference, rawpixels); 
  const CColor glbl = image->getColor(global_reference, rawpixels);
  
  if(useL2norm) {
    double local_dist = L2dist2(trgt, lcl);
    double global_dist = L2dist2(trgt, glbl);
    return (local_dist < local_flammability*local_flammability &&
	    global_dist < global_flammability*global_flammability);
  }
  else {
    double local_dist = L1dist(trgt, lcl);
    double global_dist = L1dist(trgt, glbl);
    return local_dist < local_flammability && global_dist < global_flammability;
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

CColorDifferentiator2::CColorDifferentiator2(const OOFImage *image,
					     double cd, bool l2)
  : image(image),
    color_delta(cd),
    useL2norm(l2),
    rawpixels(image->pixelPacket())
{}

bool CColorDifferentiator2::operator()(const ICoord &target,
				       const ICoord &reference)
  const
{
  const CColor trgt = image->getColor(target, rawpixels);
  const CColor rfrnc = image->getColor(reference, rawpixels); 
  return distance2(target, reference) < color_delta*color_delta;
}

double CColorDifferentiator2::distance2(const ICoord &p0, const ICoord &p1)
  const
{
  const CColor c0 = image->getColor(p0, rawpixels);
  const CColor c1 = image->getColor(p1, rawpixels);
  if(useL2norm) {
    return L2dist2(c0, c1);
  }
  else {
    double d = L1dist(c0, c1);
    return d*d;
  }
}
					 
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// TODO: Allow user to specify the color space norm?  If we do that,
// do we also have to include the off diagonal terms in the variance
// to make it consistent?  Is this implementation already
// inconsistent?

ColorPixelDistribution::ColorPixelDistribution(const ICoord &pixel,
					       const OOFImage *image,
					       double sigma0)
  : var0(sigma0*sigma0),
    image(image),
    rawpixels(image->pixelPacket())
{
  CColor col = image->getColor(pixel, rawpixels);
  pxls.push_back(pixel);
  mean[0] = col.getRed();
  mean[1] = col.getGreen();
  mean[2] = col.getBlue();
  sumsq[0] = col.getRed()*col.getRed();
  sumsq[1] = col.getGreen()*col.getGreen();
  sumsq[2] = col.getBlue()*col.getBlue();
  variance[0] = var0;
  variance[1] = var0;
  variance[2] = var0;
}

// Initialize with a whole bunch of pixels.
ColorPixelDistribution::ColorPixelDistribution(const std::set<ICoord> &pixels,
					       const OOFImage *image,
					       double sigma0)
  : mean{0.0, 0.0, 0.0},
    sumsq{0.0, 0.0, 0.0},
    var0(sigma0*sigma0),
    image(image),
    rawpixels(image->pixelPacket())
{
  pxls.insert(pxls.begin(), pixels.begin(), pixels.end());
  for(const ICoord &pixel : pxls) {
    CColor col = image->getColor(pixel, rawpixels);
    mean[0] += col.getRed();
    mean[1] += col.getGreen();
    mean[2] += col.getBlue();
    sumsq[0] += col.getRed()*col.getRed();
    sumsq[1] += col.getGreen()*col.getGreen();
    sumsq[2] += col.getBlue()*col.getBlue();
  }
  mean[0] /= npts();
  mean[1] /= npts();
  mean[2] /= npts();

  findVariance();
}

PixelDistribution *ColorPixelDistribution::clone(
					 const std::set<ICoord> &pxls)
  const
{
  ColorPixelDistribution *newpd = new ColorPixelDistribution(pxls, image,
							     sqrt(var0));
  return newpd;
}

void ColorPixelDistribution::add(const ICoord &pixel) {
  int oldN = pxls.size();
  pxls.push_back(pixel);
  int newN = pxls.size();

  CColor col = image->getColor(pixel, rawpixels);
  double r = col.getRed();
  double g = col.getGreen();
  double b = col.getBlue();

  // If the color being added is exactly equal to the mean, don't
  // recompute the mean.  Recomputing it might introduce numerical
  // error, which can make autogrouping fail on an image which has
  // already been segmented (so that the pixel values are piecewise
  // constant).
  if(mean[0] != r)
    mean[0] = (oldN*mean[0] + r)/newN;
  if(mean[1] != g)
    mean[1] = (oldN*mean[1] + g)/newN;
  if(mean[2] != b)
    mean[2] = (oldN*mean[2] + b)/newN;
  
  sumsq[0] += r*r;
  sumsq[1] += g*g;
  sumsq[2] += b*b;
  findVariance();
}

// void ColorPixelDistribution::remove(const ICoord &pixel) {
//   auto iter = std::find(pxls.begin(), pxls.end(), pixel);
//   if(iter == pxls.end())
//     return;
//   int oldN = pxls.size();
//   pxls.erase(iter);
//   int newN = pxls.size();
//   CColor col = (*image)[pixel];
//   mean[0] = (oldN*mean[0] - col.getRed())/newN;
//   mean[1] = (oldN*mean[1] - col.getGreen())/newN;
//   mean[2] = (oldN*mean[2] - col.getBlue())/newN;
//   sumsq[0] -= col.getRed()*col.getRed();
//   sumsq[1] -= col.getGreen()*col.getGreen();
//   sumsq[2] -= col.getBlue()*col.getBlue();
//   findVariance();
// }

void ColorPixelDistribution::merge(const PixelDistribution *othr) {
  unsigned int nOld = npts();
  
  const ColorPixelDistribution *other =
    dynamic_cast<const ColorPixelDistribution*>(othr);

  pxls.insert(pxls.end(), other->pxls.begin(), other->pxls.end());
  unsigned int nNew = npts();

  for(unsigned int i=0; i<3; i++) {
    // See comment in ColorPixelDistribution::add about avoiding
    // numerical error.
    if(mean[i] != other->mean[i])
      mean[i] = (nOld*mean[i] + other->npts()*other->mean[i])/nNew;
    sumsq[i] += other->sumsq[i];
  }
  findVariance();
}

void ColorPixelDistribution::findVariance() {
  unsigned int n = npts();
  for(unsigned int i=0; i<3; i++) {
    variance[i] = sumsq[i]/n - mean[i]*mean[i];
    if(variance[i] < var0)
      variance[i] = var0;
  }
}

double ColorPixelDistribution::deviation2(const ICoord &pixel)
  const
{
  CColor color = image->getColor(pixel, rawpixels);
  double delta[3];
  delta[0] = color.getRed() - mean[0];
  delta[1] = color.getGreen() - mean[1];
  delta[2] = color.getBlue() - mean[2];
  assert(variance[0]!=0 && variance[1]!=0 && variance[2]!=0);  
  return (delta[0]*delta[0]/variance[0] +
	  delta[1]*delta[1]/variance[1] +
	  delta[2]*delta[2]/variance[2]);
}

double ColorPixelDistribution::deviation2(const PixelDistribution *othr)
  const
{
  const ColorPixelDistribution *other =
    dynamic_cast<const ColorPixelDistribution*>(othr);
  double delta[3];
  delta[0] = other->mean[0] - mean[0];
  delta[1] = other->mean[1] - mean[1];
  delta[2] = other->mean[2] - mean[2];
  assert(variance[0]!=0 && variance[1]!=0 && variance[2]!=0);
  double devs = (delta[0]*delta[0]/variance[0] +
	  delta[1]*delta[1]/variance[1] +
	  delta[2]*delta[2]/variance[2]);
  // std::cerr << "ColorPixelDistribution::deviation2: this=" << stats()
  // 	    << "\tother=" << other->stats() << "\tdeviations=" << devs
  // 	    << std::endl;
  return devs;
}
  
#ifdef DEBUG

std::string ColorPixelDistribution::stats() const {
  return "[" + to_string(mean[0], 20) + ", " + to_string(mean[1], 20) + ", "
    + to_string(mean[2], 20) 
    + "] +/- ["
    + to_string(sqrt(variance[0])) + "," + to_string(sqrt(variance[1])) + ","
    +  to_string(sqrt(variance[2])) + "]"
    //    + "  sumsq=[" + to_string(sumsq[0]) + "," + to_string(sumsq[1]) +"," + to_string(sumsq[2]) + "]" + " n=" + to_string(npts())
    ;
}

std::string ColorPixelDistribution::value(const ICoord &pixel) const {
  return to_string(image->getColor(pixel, rawpixels));
}

#endif // DEBUG



PixelDistribution *ColorPixelDistFactory::newDistribution(const ICoord &pixel)
  const
{
  return new ColorPixelDistribution(pixel, image, sigma0);
}
