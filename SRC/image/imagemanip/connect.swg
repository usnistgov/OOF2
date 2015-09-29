// -*- C++ -*-
// $RCSfile: connect.swg,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:41:38 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CONNECT_SWG
#define CONNECT_SWG

%module connect
%include "common/typemaps.swg"

%{
#include "image/imagemanip/connect.h"
%}

class OOFImage;

void makeConnected(OOFImage, double, double, int, int, int, int, int, bool);

#endif // CONNECT_SWG
