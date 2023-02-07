// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef THREADSTATE_SWG
#define THREADSTATE_SWG

%module(package="ooflib.SWIG.common") threadstate

%include "common/typemaps.swg"
%import "common/progress.swg"

%{
#include "common/threadstate.h"
#include "common/progress.h"
#include "common/tostring.h"
%}

ADD_REPR(ThreadID, get_IDstr);

class ThreadID {
public:
  ThreadID();
};

%extend ThreadID {
  bool __eq__(ThreadID &right) {
    return operator==(*self,right);
  }
};

class ThreadState {
 public:
  ThreadState();
  ~ThreadState();
  const ThreadID & get_thread_ID();
  int id();
  %newobject getProgressNames;
  std::vector<std::string> *getProgressNames();
  Progress *getProgress(char*, ProgressType);
  Progress *findProgress(char*);
  void impedeProgress();
  void acquireProgressLock();
  void releaseProgressLock();
};

%extend ThreadState {
  int __eq__(ThreadState &right) {
    return operator==(*self,right);
  }
};

void initThreadState();
int findThreadNumber();
ThreadState *findThreadState();
bool mainthread_query();
void mainthread_delete();
int nThreadStates();

bool threading_enabled;


void cancelThread(ThreadState &tobecancelled); 
/*
  Handle with care!! cancelThread WILL stop a thread without any regard to 
  any cleanup that must be done.
*/

void testcancel();

Progress *getProgress(char *name, ProgressType);

%pythoncode %{
  initThreadState()
%}

#endif // THREADSTATE_SWG

  
