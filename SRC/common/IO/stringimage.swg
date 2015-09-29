// -*- C++ -*-
// $RCSfile: stringimage.swg,v $
// $Revision: 1.12 $
// $Author: langer $
// $Date: 2014/09/27 21:40:32 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef STRINGIMAGE_SWG
#define STRINGIMAGE_SWG

%module stringimage

%include "common/typemaps.swg"
%{
#include "common/IO/stringimage.h"
%}

class StringImage {
public:
  StringImage(ICoord *iPoint, Coord *Point);
  ~StringImage();
  void set(ICoord *iPoint, CColor*);
  CColor get(ICoord *iPoint);
  %new string *hexstringimage();
};

class AlphaStringImage {
};

#endif // STRINGIMAGE_SWG
