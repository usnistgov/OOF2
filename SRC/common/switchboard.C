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
#include <string>

#include "common/ooferror.h"
#include "common/pythonlock.h"
#include "common/pyutils.h"
#include "common/switchboard.h"
#include "common/trace.h"

static PyObject *notifier = 0;

void init_switchboard_api(PyObject *pyNotify) {
  // Called just once, passing switchboard.cnotify.
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_XINCREF(pyNotify);
  notifier = pyNotify;
}

void switchboard_notify(const std::string &msg) {
  if(notifier != 0) {
    PYTHON_THREAD_BEGIN_BLOCK;
    PyObject *result = PyObject_CallFunction(notifier, "s", msg.c_str());
    if(!result) {
      pythonErrorRelay();	// raises an exception
    }
    else {
      Py_XDECREF(result);
    }
  }
}

void switchboard_notify(const OOFMessage &msg) {
  if(notifier != 0) {
    PYTHON_THREAD_BEGIN_BLOCK;
    PyObject *pmsg = msg.pythonObject();
    if(!pmsg)
      pythonErrorRelay();
    PyObject *result = PyObject_CallFunction(notifier, "O", pmsg);
    if(!result) {
      pythonErrorRelay();	// raises an exception
    }
    Py_XDECREF(pmsg);
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

const std::string OOFMessage::classname_("OOFMessage");

OOFMessage::OOFMessage(const std::string &msgname)
  : msgname(msgname)
{
}

const std::string &OOFMessage::name() const { return msgname; }

void OOFMessage::addarg(const PythonExportableBase &arggh) {
  PYTHON_THREAD_BEGIN_BLOCK;
  PyObject *arg = arggh.pythonObject();
  if(!arg)
    pythonErrorRelay();
  args.push_back(arg);
}

void OOFMessage::addarg(const std::string &strng) {
  PYTHON_THREAD_BEGIN_BLOCK;
  args.push_back(PyUnicode_FromString(strng.c_str()));
}

void OOFMessage::addarg(int val) {
  PYTHON_THREAD_BEGIN_BLOCK;
  args.push_back(PyLong_FromLong(val));
}

int OOFMessage::nargs() const {
  return args.size();
}

PyObject *OOFMessage::getarg(int i) const {
  return args[i];
}

std::ostream &operator<<(std::ostream &os, const OOFMessage &msg) {
  os << "OOFMessage(" << msg.name();
  return os;
}
