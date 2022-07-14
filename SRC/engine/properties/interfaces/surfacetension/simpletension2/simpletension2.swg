// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef SIMPLETENSION2_SWG
#define SIMPLETENSION2_SWG

%module(package="ooflib.SWIG.engine.properties.interfaces.surfacetension.simpletension2") simpletension2

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/properties/interfaces/surfacetension/simpletension2/simpletension2.h"
%}

class SimpleTension2 : public Property
{
public:
  SimpleTension2(PyObject *self, char *, double, double, double, double);
};

%pythoncode "engine/properties/interfaces/surfacetension/simpletension2/simpletension2.spy"

#endif // SIMPLETENSION2_SWG
