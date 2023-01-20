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
#include "common/pythonexportable.h"
#include "common/pythonlock.h"
#include "common/pyutils.h"

// Convert a PyObject* unicode object to a C++ string.  This does
// *not* call the __repr__ -- it assumes that the PyObject is a
// unicode string.  This replaces Python2's PyString_AsString().

std::string pyStringAsString(PyObject *str) {
  assert(PyUnicode_Check(str));
  PyObject *ustr = PyUnicode_AsEncodedString(str, "UTF-8", "replace");
  if(!ustr)
    pythonErrorRelay();
  char *r = PyBytes_AsString(ustr);
  if(!r)
    pythonErrorRelay();
  std::string result(r);
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
  if(!repr)
    pythonErrorRelay();
  PyObject *ustr = PyUnicode_AsEncodedString(repr, "UTF-8", "replace");
  if(!ustr)
    pythonErrorRelay();
  char *r = PyBytes_AsString(ustr);
  if(!r)
    pythonErrorRelay();
  std::string result(r);
  Py_XDECREF(repr);
  Py_XDECREF(ustr);
  return result;
}

std::string repr(PyObject *obj) {
  PYTHON_THREAD_BEGIN_BLOCK;
  return repr_nolock(obj);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const PythonExportableBase &peb) {
  os << "PythonExportableBase(" << &peb << ")";
  return os;
}
