// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef STATGROUPS_SWG
#define STATGROUPS_SWG

%module statgroups
%include "common/typemaps.swg"

%{
#include "common/statgroups.h"
#include "common/cmicrostructure.h"
%}

%pragma(python) include="common/statgroups.spy"

class PixelDistributionFactory {};

const string *statgroups(CMicrostructure*,
			 PixelDistributionFactory*,
			 double, double,
			 int,
			 int,
			 char*, bool);

#endif // STATGROUPS_SWG

