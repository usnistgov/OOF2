// -*- C++ -*-
// $RCSfile: segmenter.swg,v $
// $Revision: 1.12 $
// $Author: langer $
// $Date: 2014/09/27 21:41:36 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef SEGMENTER_SWG
#define SEGMENTER_SWG

%module segmenter
%include "common/typemaps.swg"

%{
#include "image/oofimage.h"
#include "common/doublearray.h"
  %}
%pragma(python) include="segmenter.spy"

#endif // SEGMENTER_SWG
