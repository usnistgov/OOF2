// -*- C++ -*-
// $RCSfile: pixelselectioncourier.swg,v $
// $Revision: 1.15 $
// $Author: langer $
// $Date: 2014/09/27 21:40:27 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELSELECTIONCOURIER_SWG
#define PIXELSELECTIONCOURIER_SWG

%module pixelselectioncourier

%include "common/typemaps.swg"
%extern "common/coord.swg"

%{
#include "common/pixelselectioncourier.h"
#include "common/tostring.h"
%}

class PixelSelectionCourier {
public:
  %addmethods {
    %new const string *repr() {	// for debugging
      return new std::string(to_string(*self));
    }
  }
};

class PointSelection : public PixelSelectionCourier {
public:
  PointSelection(CMicrostructure*, Coord *Point);
  ~PointSelection();
};

#ifndef DIM_3
class BrushSelection : public PixelSelectionCourier {
public:
  BrushSelection(CMicrostructure*, BrushStyle*, PointVec *PointList);
  ~BrushSelection();
};
#endif

class RectangleSelection : public PixelSelectionCourier {
public:
  RectangleSelection(CMicrostructure*, Coord *Point, Coord *Point);
  ~RectangleSelection();
};

class CircleSelection : public PixelSelectionCourier {
public:
  CircleSelection(CMicrostructure*, Coord *Point, double,
		  Coord *Point, Coord *Point);
  ~CircleSelection();
};

class EllipseSelection : public PixelSelectionCourier {
public:
  EllipseSelection(CMicrostructure*, Coord *Point, Coord *Point);
  ~EllipseSelection();
};

class GroupSelection : public PixelSelectionCourier {
public:
  GroupSelection(CMicrostructure*, PixelSet*);
  ~GroupSelection();
};

class IntersectSelection : public PixelSelectionCourier {
public:
  IntersectSelection(CMicrostructure*, PixelSet*, PixelSet*);
  ~IntersectSelection();
};

#ifndef DIM_3
class DespeckleSelection : public PixelSelectionCourier {
public:
  DespeckleSelection(CMicrostructure*, PixelSet*, int);
  ~DespeckleSelection();
};

class ElkcepsedSelection : public PixelSelectionCourier {
public:
  ElkcepsedSelection(CMicrostructure*, PixelSet*, int);
  ~ElkcepsedSelection();
};

class ExpandSelection : public PixelSelectionCourier {
public:
  ExpandSelection(CMicrostructure*, PixelSet*, double);
  ~ExpandSelection();
};

class ShrinkSelection : public PixelSelectionCourier {
public:
  ShrinkSelection(CMicrostructure*, PixelSet*, double);
  ~ShrinkSelection();
};
#endif // DIM_3

#endif // PIXELSELECTIONCOURIER_SWG
