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

// Routines used to catch C++ signals and dump the current Python
// stack before bailing out.

#include <Python.h>
#include <string>
#include <signal.h>
#include <pthread.h>
#include <unistd.h>
#include <iostream>
#include "cdebug.h"

#include "common/pythonlock.h"
#include "common/ooferror.h"

static PyObject *python_dumper;

static void handler(int sig) {
  std::string msg;
  if(sig == SIGBUS)
    msg = "Bus Error";
  else if(sig == SIGSEGV)
    msg = "Segmentation Fault";
  else if(sig == SIGINT)
    msg = "Interrupted";
  
  PyGILState_STATE pystate = acquirePyLock();
  PyObject *result = PyObject_CallFunction(python_dumper, "(s)", msg.c_str());
  Py_DECREF(result);
  releasePyLock(pystate);
  std::cerr << "cdebug.C: " << msg << ": aborting" << std::endl;
  abort();
}

void initDebug(PyObject *pydump) {
  python_dumper = pydump;
  Py_XINCREF(python_dumper);
}

// installSignals and restoreSignals are called by the 'except'
// directive in typemaps.swg.

typedef void (*sighandler)(int);

// Signal handlers called due to internal segfaults (i.e. actual
// pointer-dereference problems, as opposed to "kill -11" from the
// command line) appear to be run on the segfaulting thread, resulting
// in the stack dump being correct.

// Experiments with test programs imply that successive "signal" calls
// override the main handler.  Since we actually only have one
// handler, and we want it to be in place whenever any thread is in
// C++ code, the right thing to do is to count up the handlers in a
// thread-safe way, and not restore until you're all the way out.

sighandler bushandler;
sighandler inthandler;
sighandler segvhandler;

static pthread_mutex_t signal_handler_count_lock=PTHREAD_MUTEX_INITIALIZER;
static int signal_handler_count=0;

void installSignals_() {
  pthread_mutex_lock(&signal_handler_count_lock);
  if (signal_handler_count==0) {
    bushandler = signal(SIGBUS, handler);
    inthandler = signal(SIGINT, handler);
    segvhandler = signal(SIGSEGV, handler);
  }
  signal_handler_count++;
  pthread_mutex_unlock(&signal_handler_count_lock);
}

void restoreSignals_() {
  pthread_mutex_lock(&signal_handler_count_lock);
  signal_handler_count--;
  if (signal_handler_count==0) {
    signal(SIGBUS, bushandler);
    signal(SIGINT, inthandler);
    signal(SIGSEGV, segvhandler);
  }
  pthread_mutex_unlock(&signal_handler_count_lock);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The following functions are for testing the error handling
// facilities.  

void segfault(int delay) {
  // raise(SIGSEGV);
  sleep(delay);
  void (*f)() = 0;
  f();
}

void throwException() {
  // The third argument ErrProgrammingError is usually __LINE__, but
  // in this case that's dangerous, because editing anything in this
  // file above here might change __LINE__ here, and that would cause
  // tests that expect a certain error text to fail.  Since this
  // routine is only used to test error handling, we use a fixed
  // integer value instead of __LINE__.  The value is the one that was
  // in the test files at the time that this glitch was
  // discovered. (See TEST/GUI/04100/log.py, for example.)
  throw ErrProgrammingError("Somebody made a mistake!", __FILE__, 124);
}

// A C++ function that can be called from Python, and which calls a
// Python "function" that raises a Python exception.

void throwPythonException() {
  PyGILState_STATE pystate = acquirePyLock();
  try {
    PyObject *result = PyObject_GetAttrString(Py_None, (char*) "say what?");
    if(!result)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
  catch(...) {
    releasePyLock(pystate);
    throw;
  }
  releasePyLock(pystate);
}

// A C++ function that can be called from Python, and which calls a
// Python function that throws a C++ exception.

void throwPythonCException() {
  PyGILState_STATE pystate = acquirePyLock();
  try {
    PyObject *module = PyImport_ImportModule((char*) 
					     "ooflib.SWIG.common.cdebug");
    PyObject *func = PyObject_GetAttrString(module, (char*) "throwException");
    Py_XDECREF(module);
    PyObject *result = PyObject_CallFunction(func, NULL);
    Py_XDECREF(args);
    if(!result)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
  catch (...) {
    releasePyLock(pystate);
    throw;
  }
  releasePyLock(pystate);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// For testing progress bars

// TODO: Copy this to OOF2 and see if it has the same problem.

#include <math.h>
#include "common/tostring.h"
#include "common/progress.h"

void spinCycle(int nCycles) {
  DefiniteProgress *progress = dynamic_cast<DefiniteProgress*>(
				       getProgress("SpinCycle", DEFINITE));

  double x;
  for(int i=0; i<nCycles && !progress->stopped(); i++) {
    x = cos(x);
    progress->setMessage(to_string(i) + "/" + to_string(nCycles));
    progress->setFraction((float) i/nCycles);
  }
  progress->finish();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


// Call out to the python utils.memusage() method

void memusage(const std::string &comment) {
  static PyObject *memfunc = nullptr;
  PyGILState_STATE pystate = acquirePyLock();
  try {
    if(!memfunc) {
      PyObject *utils = PyImport_ImportModule((char*) "ooflib.common.utils");
      memfunc = PyObject_GetAttrString(utils, (char*) "memusage");
      Py_XDECREF(utils);
    }
    PyObject *arg = Py_BuildValue((char *) "(s)", comment.c_str());
    PyObject *result = PyObject_CallObject(memfunc, arg);
    Py_XDECREF(arg);
    if(!result)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
  catch (...) {
    releasePyLock(pystate);
    throw;
  }
  releasePyLock(pystate);
}

					
