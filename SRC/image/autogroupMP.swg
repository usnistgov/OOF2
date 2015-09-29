// -*- C++ -*-
// $RCSfile: autogroupMP.swg,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2011/07/14 21:19:33 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef AUTOGROUPMP_SWG
#define AUTOGROUPMP_SWG

%module autogroup
%include "common/typemaps.swg"

%{
#include "common/pixelgroup.h"
#include "common/cmicrostructure.h"
#include "image/autogroupMP.h"
#include "image/oofimage.h"
%}

const string *autogroup(CMicrostructure*, OOFImage*, char*);

#endif // AUTOGROUPMP_SWG
