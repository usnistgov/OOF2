// -*- C++ -*-
// $RCSfile: polefigure.swg,v $
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

#ifndef POLEFIGURE_SWG
#define POLEFIGURE_SWG

%module polefigure
%include "common/typemaps.swg"
%extern "engine/crystalsymmetry.swg"
%extern "common/direction.swg"

%{
#include "orientationmap/polefigure.h"
%}

%pragma(python) include = "polefigure.spy"

class PoleFigure {
public:
  PoleFigure(CMicrostructure*, PixelSet*, AnisoCrystalSymmetry*,
	     CDirection*, int, bool);

  double getValue(int, int);
  bool inside(int, int) const;
  double getBinSize();
  int nCounts();
  double minValue();
  double maxValue();
};

#endif // POLEFIGURE_SWG


