// -*- C++ -*-
// $RCSfile: lock.h,v $
// $Revision: 1.22 $
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

#include <oofconfig.h>

#ifndef LOCK_H
#define LOCK_H


#include <sys/types.h>
#include <pthread.h>

// Simple wrapper for a mutex lock.
class Lock {
protected:
  pthread_mutex_t lock;
public:
  Lock();
  virtual ~Lock();
  virtual void acquire();
  virtual void release();
  friend class Condition;
};

// Silent lock, has no instrumentation. 
class SLock : public Lock {
public:
  SLock() {}
  virtual ~SLock() {}
  virtual void acquire();
};

class Condition {
protected:
  pthread_cond_t condition;
  Lock *lock;
public:
  Condition(Lock*);
  virtual ~Condition();
  // wait() releases the lock, and blocks until signal() or
  // broadcast() is called in another thread, at which time wait()
  // reacquires the lock and returns.
  void wait();	
  // Use broadcast instead of signal if it's possible that more than
  // one thread is waiting.
  void signal();
  void broadcast();
};


// Wrapper for the custom RWLock.  Having a custom class means not
// having to cope with architecture-dependent implementations, or the
// even-more-inconvenient absence thereof.
class RWLock {
protected:
  int r, w, p;			// read, write, pause
  pthread_mutex_t local_lock;
  // Condition signalled when r=w=0 becomes true.
  pthread_cond_t rw_zero;
public:
  RWLock();
  ~RWLock();
  void write_acquire();
  void write_release();

  void read_acquire();
  void read_release();

  void write_pause();
  void write_resume();

  int nReaders() const { return r; }
};


// Uninstrumented RWLock -- used where RWLock protection is required,
// but main thread access is required.  This should be quite rare.
class SRWLock : public RWLock {
public:
  SRWLock() {};
  virtual ~SRWLock() {};
  virtual void write_acquire();
  
  virtual void read_acquire();
};

// The KeyHolder is a wrapper for a mutex lock.  The constructor
// acquires the lock and the destructor releases it.  Creating a
// KeyHolder object in a function allows the lock to be held
// throughout the scope of the function, that is, until just before
// the function returns.

class KeyHolder {
private:
  Lock  *lock;
  bool verbose;
public:
  KeyHolder(Lock &other_lock, bool verbose=false);
  ~KeyHolder();
};

// enable_all and disable_all override all instances of Lock and
// RWLock.  They're used to prevent deadlocks when running in
// unthreaded mode.

void enable_all();
bool disable_all();

#endif // LOCK_H
