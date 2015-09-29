// -*- C++ -*-
// $RCSfile: polefigure.h,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2012/04/18 20:26:13 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef POLEFIGURE_H
#define POLEFIGURE_H

class PoleFigure;

#include "common/array.h"
#include "engine/crystalsymmetry.h"
#include <vector>

class CMicrostructure;
class CDirection;
class PixelSet;
class RotationSet;

class PoleFigure {
private:
  int nBins;
  int totalCounts;
  double binSize;
  double rProj;
  SimpleArray2D<double> counts;
  double minVal, maxVal;
  int processPixel(const ICoord&, const RotationSet*,
		   const CDirection*,
		   const CMicrostructure*);
public:
  PoleFigure(const CMicrostructure*, 
	     const PixelSet*,
	     const AnisoCrystalSymmetry*,
	     const CDirection *pole, 
	     int nBins,
	     bool hemisphere);
  double getValue(int i, int j) const { return counts(i, j); }
  int nCounts() const { return totalCounts; }
  double maxValue() const { return maxVal; }
  double minValue() const { return minVal; }
  double getBinSize() const { return binSize; }
  bool inside(int, int) const;
};

#endif // POLEFIGURE_H
