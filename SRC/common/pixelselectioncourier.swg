// -*- C++ -*-

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

%module(package="ooflib.SWIG.common") pixelselectioncourier

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/coord.swg"
#endif // NOSECONDIMPORTS

%{
#include "common/pixelselectioncourier.h"
#include "common/tostring.h"
%}

%nodefaultctor PixelSelectionCourier;

class PixelSelectionCourier {};

ADD_REPR_GENERIC(PixelSelectionCourier);

class PointSelection : public PixelSelectionCourier {
public:
  PointSelection(CMicrostructure*, Coord *Point);
  ~PointSelection();
};

class BrushSelection : public PixelSelectionCourier {
public:
  BrushSelection(CMicrostructure*, BrushStyle*, std::vector<Coord> *PointList);
  ~BrushSelection();
};

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

#endif // PIXELSELECTIONCOURIER_SWG
