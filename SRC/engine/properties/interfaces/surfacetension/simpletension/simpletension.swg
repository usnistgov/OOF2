// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef SIMPLETENSION_SWG
#define SIMPLETENSION_SWG

%module simpletension

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/properties.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/property/interfaces/surfacetension/simpletension/simpletension.h"
%}

class SimpleTension : public Property
{
public:
  SimpleTension(PyObject *self, char *, double, double);
};

%pythoncode "engine/property/interfaces/surfacetension/simpletension/simpletension.spy"

#endif // SIMPLETENSION_SWG
