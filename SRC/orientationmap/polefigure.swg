// -*- C++ -*-

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

%module(package="ooflib.SWIG.orientationmap") polefigure

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/crystalsymmetry.swg"
%import "common/direction.swg"
#endif //NOSECONDIMPORTS

%{
#include "common/direction.h"
#include "orientationmap/polefigure.h"
%}

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

%pythoncode "orientationmap/polefigure.spy"

#endif // POLEFIGURE_SWG


