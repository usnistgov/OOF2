// -*- C++ -*-
// $RCSfile: lock.swg,v $
// $Revision: 1.19 $
// $Author: langer $
// $Date: 2011/03/30 14:32:49 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef LOCK_SWG
#define LOCK_SWG

%module lock
%include "common/typemaps.swg"
%{
#include "common/lock.h"
%}
%pragma(python) include="lock.spy"

class Lock {
public:
  Lock();
  ~Lock();
  void acquire();
  void release();
};

class SLock : public Lock {
public:
  SLock();
  ~SLock();
  void acquire();
  void release();
};

class Condition {
public:
  Condition(Lock*);
  ~Condition();
  void wait();
  void signal();
  void broadcast();
};

class RWLock {
public:
  RWLock();
  ~RWLock();
  void read_acquire();
  void read_release();

  void write_acquire();
  void write_release();

  void write_pause();
  void write_resume();
  int nReaders();		// for debugging
};

void enable_all();
bool disable_all();

#endif // LOCK_SWG
