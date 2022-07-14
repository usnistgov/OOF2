// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef SWITCHBOARD_SWG
#define SWITCHBOARD_SWG

%module(package="ooflib.SWIG.common") switchboard

%{
#include "common/switchboard.h"
#include "common/pythonlock.h"
%}

%include "common/typemaps.swg"


void init_switchboard_api(PyObject *pythonCallable); // call this once


class OOFMessage {
public:
  OOFMessage(const std::string&);
  const string &name();
};

%extend OOFMessage {
  int __len__() const {
    return self->nargs();
  }
  PyObject *__getitem__(int which) const {
    if(which >= self->nargs() || which < 0) {
      PYTHON_THREAD_BEGIN_BLOCK;
      PyErr_SetString(PyExc_IndexError,
		      "Not that many arguments in OOFMessage");
      return 0;
    }
    return self->getarg(which);
  }
};

%pythoncode "common/switchboard.spy"

#endif // SWITCHBOARD_SWG
