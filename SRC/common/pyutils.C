// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/ooferror.h"
#include "common/pythonlock.h"
#include "common/pyutils.h"

// Convert a PyObject* unicode object to a C++ string.  This does
// *not* call the __repr__ -- it assumes that the PyObject is a
// unicode string.  This replaces Python2's PyString_AsString().

std::string pyStringAsString(PyObject *str) {
  PyObject *ustr = PyUnicode_AsEncodedString(str, "UTF-8", "replace");
  if(!ustr)
    pythonErrorRelay();
  char *result = PyBytes_AsString(ustr);
  if(!result)
    pythonErrorRelay();
  Py_XDECREF(ustr);
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Call the __repr__ of the given object.  Use the nolock version in
// situations (such as inside typemaps) where the python global
// interpreter lock does not need to be acquired.

std::string repr_nolock(PyObject *obj) {
  assert(obj != 0);
  PyObject *repr = PyObject_Repr(obj);
  PyObject *ustr = PyUnicode_AsEncodedString(repr, "UTF-8", "replace");
  assert(ustr != 0);
  std::string r(PyBytes_AsString(ustr));
  Py_XDECREF(repr);
  Py_XDECREF(ustr);
  return r;
}

std::string repr(PyObject *obj) {
  PYTHON_THREAD_BEGIN_BLOCK;
  return repr_nolock(obj);
}
