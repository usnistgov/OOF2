// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef %MODULENAME%_SWG
#define %MODULENAME%_SWG

%module %MODULENAME%

%{
#include "%MODULENAME%.h"
%}

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/nonlinear/general_nonlinear_elasticity.swg"

class %CLASS% : public GeneralNonlinearElasticity {
public:
  %CLASS%(std::string &name, PyObject *reg, double param1, double param2);
};

%pythoncode "%MODULENAME%.spy"

#endif // %MODULENAME%_SWG
