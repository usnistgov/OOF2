// -*- C++ -*-
// $RCSfile: nonconstant_force_density_example.swg,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2011-02-17 22:44:14 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@ctcms.nist.gov.
 */

#ifndef %HEADER%_SWG
#define %HEADER%_SWG

%module %MODULENAME%

%{
#include "%MODULENAME%.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"
%extern "engine/property/forcedensity/nonconstant/nonconstant_force_density.swg"
%pragma(python) code="from ooflib.SWIG.engine.property.forcedensity.nonconstant.nonconstant_force_density import NonconstantForceDensityPtr"
%pragma(python) include="%MODULENAME%.spy"


class %CLASS% : public NonconstantForceDensity {
public:
  %CLASS%(PyObject *reg, char *name, double parameter1, double parameter2);
};

#endif // %HEADER%_SWG
