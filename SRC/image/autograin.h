// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef AUTOGRAIN_H
#define AUTOGRAIN_H

#include <oofconfig.h>
#include <vector>

#include "common/array.h"

class ActiveArea;
class CMicrostructure;
class ICoord;
class OOFImage;

class CPixelDifferentiator {
public:
  virtual ~CPixelDifferentiator() {}
  virtual bool operator()(const ICoord&, const ICoord&, const ICoord&) const=0;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class CColorDifferentiator : public CPixelDifferentiator {
private:
  const OOFImage *image;
  double local_flammability;
  double global_flammability;
  bool useL2norm;
public:
  CColorDifferentiator(const OOFImage *image, double lf, double gf, bool l2);
  virtual bool operator()(const ICoord&, const ICoord&, const ICoord&) const;
};

std::vector<ICoord> burn(CMicrostructure*,
			 const CPixelDifferentiator&,
			 bool,
			 const ICoord&,
			 const ActiveArea*,
			 SimpleArray2D<bool>&);

const std::string *autograin(CMicrostructure*,
			     const CPixelDifferentiator*,
			     bool,
			     const std::string&);

#endif // AUTOGRAIN_H
