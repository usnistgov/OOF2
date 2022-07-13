// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef AUTOGROUP_SWG
#define AUTOGROUP_SWG

%module autogroup

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/cmicrostructure.swg"
%import "image/oofimage.swg"
#endif // NOSECONDIMPORTS

%{
#include "common/pixelgroup.h"
#include "common/cmicrostructure.h"
#include "image/autogroup.h"
#include "image/oofimage.h"
%}

%newobject autogroup;
std::vector<std::string> *autogroup(CMicrostructure*, OOFImage*, std::string&);

#endif // AUTOGROUP_SWG
