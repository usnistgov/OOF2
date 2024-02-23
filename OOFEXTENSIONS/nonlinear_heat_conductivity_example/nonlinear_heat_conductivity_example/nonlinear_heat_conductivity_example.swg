// -*- C++ -*-
// $RCSfile: nonlinear_heat_conductivity_example.swg,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2011-02-18 19:32:26 $


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef %HEADER%_SWG
#define %HEADER%_SWG

%module %MODULENAME%

%{
#include "%MODULENAME%.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"
%extern "engine/property/heatconductivity/nonlinear/nonlinear_heat_conductivity.swg"
%pragma(python) code="from ooflib.SWIG.engine.property.heatconductivity.nonlinear.nonlinear_heat_conductivity import NonlinearHeatConductivityPtr"
%pragma(python) include="%MODULENAME%.spy"


class %CLASS% : public NonlinearHeatConductivity {
public:
  %CLASS%(PyObject *reg, char *name, double param1, double param2);
};

#endif 
