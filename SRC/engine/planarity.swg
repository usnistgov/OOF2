// -*- C++ -*-
// $RCSfile: planarity.swg,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2014/09/27 21:40:51 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PLANARITY_SWG
#define PLANARITY_SWG

%module planarity

%include "engine/typemaps.swg"

%{
#include "engine/planarity.h"
%}

enum Planarity {IN_PLANE, OUT_OF_PLANE, ALL_INDICES};

#endif // PLANARITY_SWG
