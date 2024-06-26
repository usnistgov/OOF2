/// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/lock.h"
#include "common/progress.h"
#include "common/pythonlock.h"
#include "common/switchboard.h"
#include "common/threadstate.h"
#include "common/tostring.h"
#include <map>
#include <vector>
#include <limits>

int Progress::idcounter(0);
SLock Progress::idlock;
std::map<int, Progress*> idmap;

static const bool verboseLocks = false;

Progress::Progress(const std::string &nm, ThreadState *ts)
  : name_(nm),
    stopped_(false),
    finished_(false),
    threadstate(ts),
    progressbar(0),
    started_(false)
{
  // std::cerr << "Progress::ctor: " << name_ << " " << this << std::endl;
  KeyHolder key(idlock);
  id_ = idcounter++;
  idmap[id_] = this;
}

Progress::~Progress() {
  // std::cerr << "Progress:dtor: " << name_ << " " << this
  // 	    << " finished_=" << finished_ << " started_=" << started_
  // 	    << std::endl;

  // The failure of this assertion often means that a procedure raised
  // an exception and that the call to Progress::finish was never
  // made.  The solution is to ensure that the Progress::finish() is
  // called inside a finally: block in Python or generic catch block
  // in C++.  If that's not done, then this assertion might abort the
  // program before the exception is handled, and the developer will
  // never see the exception.
  assert(finished_ or not started_);
  
  KeyHolder kh(lock, verboseLocks);
  disconnectBar(progressbar);
  KeyHolder key(idlock);
  idmap.erase(id_);
}

DefiniteProgress::~DefiniteProgress() {}

IndefiniteProgress::~IndefiniteProgress() {}

void Progress::finish() {
  {
    KeyHolder kh(lock, verboseLocks);
    finished_ = true;
    started_ = false;
  }
  disconnectBar(progressbar);
}

void Progress::start() {
  if(!started_) {
    {
      KeyHolder kh(lock, verboseLocks);
      started_ = true;
      finished_ = false;
    }
    // Send the "new progress" message to the ActivityViewer window.
    OOFMessage msg("new progress");
    msg.addarg(id());
    switchboard_notify(msg);
  }
}

void Progress::stop() {
  // Stop all Progress objects on the thread on which this Progress
  // object is running.  stop() may be called from another thread, so
  // it can't use findThreadState() to get the ThreadState.
  threadstate->impedeProgress();
}

void Progress::stop1() {
  KeyHolder kh(lock, verboseLocks);
  stopped_ = true;
}

void Progress::setMessage(const std::string &msg) {
  {
    // TODO OPT: This may be slow! Can we avoid locking here?
    KeyHolder kh(lock, verboseLocks);
    message_ = msg;
  }
  start();
}

const std::string *Progress::message() const {
  KeyHolder kh(lock, verboseLocks);
  return new std::string(message_);
}

// void Progress::setFraction(double x) {
//   // This function should be pure virtual, but it's implemented here
//   // to help debug.  Race conditions were leading to calls to
//   // setFraction while a Progress object was partially destructed,
//   // apparently.
//   std::cerr << "*********" << std::endl
// 	    << " 'pure virtual' Progress::setFraction(" << x << ") thread="
// 	    << findThreadNumber() << " id=" << id_ << std::endl
// 	    << "started=" << started_ << " finished=" << finished_
// 	    << " stopped=" << stopped_ << std::endl
// 	    << "message=" << message_
// 	    << std::endl
// 	    << "*********" << std::endl;
//   abort();
// }

// Acquire and release the ThreadState's progressLock.  This prevents
// the ThreadState from deleting the Progress object.

void Progress::acquireThreadLock() {
  threadstate->acquireProgressLock();
}

void Progress::releaseThreadLock() {
  threadstate->releaseProgressLock();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// If new Progress subclasses are created, remember to update the
// factory function ThreadState::getProgress.

const std::string DefiniteProgress::classname_("DefiniteProgress");
const std::string LogDefiniteProgress::classname_("LogDefiniteProgress");
const std::string IndefiniteProgress::classname_("IndefiniteProgress");

DefiniteProgress::DefiniteProgress(const std::string &name, ThreadState *ts)
  : Progress(name, ts),
    fraction_(0.0)
{}

void DefiniteProgress::setFraction(double x) {
  {
    KeyHolder kh(lock, verboseLocks);
    fraction_ = x;
  }
  start();
}

IndefiniteProgress::IndefiniteProgress(const std::string &name, ThreadState *ts)
  : Progress(name, ts),
    count_(0)
{}

void IndefiniteProgress::pulse() {
  {
    KeyHolder kh(lock, verboseLocks);
    if(count_ == std::numeric_limits<unsigned long>::max())
      count_ = 0;
    ++count_;
  }
  start();
}

LogDefiniteProgress::LogDefiniteProgress(const std::string &name,
					 ThreadState *ts)
  : DefiniteProgress(name, ts)
{}

void LogDefiniteProgress::setRange(double initialVal, double targetVal) {
  assert(initialVal >= targetVal);
  initialValue = initialVal;
  targetValue = targetVal;
  log_init_over_targ = log(initialValue/targetValue);
}

void LogDefiniteProgress::setFraction(double x) {
  {
    KeyHolder kh(lock, verboseLocks);
    if(x > initialValue)
      fraction_ = 0.0;
    else if(x < targetValue)
      fraction_ = 1.0;
    else {
      fraction_ = 1.0 - log(x/targetValue)/log_init_over_targ;
    }
  }
  start();
}
		       

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// GUI progress bar interface

// disconnect_hook is called by a Progress object when it wants to
// disconnect from its GUI progress bar. progressGUI.C sets the hook.

void (*Progress::disconnect_hook)(PyObject*) = 0;

// setProgressBar is called by the GUI when it creates a
// GUIProgressBar object.  If progressbar is set, we can assume that
// the GUI is running.

void Progress::setProgressBar(PyObject *bar) {
  PYTHON_THREAD_BEGIN_BLOCK;
  progressbar = bar;
  Py_XINCREF(progressbar);
}

bool Progress::hasProgressBar() const {
  return progressbar != 0;
}

void Progress::disconnectBar(PyObject *pbar) {
  // Because ProgressBar destruction and disconnection are separate
  // processes, but each one calls the other and either one can come
  // first, it's necessary to do something to prevent annihilation
  // loops. This can be done here by setting the local progressbar
  // pointer to zero before disconnecting it.  However, if
  // ProgressBars are being created and destroyed too quickly, it's
  // possible that a new pointer one will be assigned before the old
  // ProgressBar is completely destroyed.  Therefore disconnectBar is
  // called with an explicit ProgressBar pointer and this routine
  // doesn't do anything unless the given bar is the current one.
  if(progressbar == pbar && progressbar != 0) {
    progressbar = 0;
    // disconnect_hook is non-zero if the GUI has been loaded.
    if(disconnect_hook) {
      (*disconnect_hook)(pbar);	// decrefs its argument.
    }
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// getProgress creates a new Progress object and returns it, unless
// there's an existing object with the given name, in which case it
// returns that one instead.
Progress *getProgress(const std::string &name, ProgressType ptype) {
  ThreadState *ts = findThreadState();
  return ts->getProgress(name, ptype);
}

// findProgress returns the existing Progress object with the given
// name.  It raises an exception if there isn't one.
Progress *findProgress(const std::string &name) {
  ThreadState *ts = findThreadState();
  return ts->findProgress(name);
}

// findProgressByID is used by the ActivityViewer window and possibly
// other cases in which the Progress object might have been created on
// a different thread than the one trying to use it.
Progress *findProgressByID(int id) {
  std::map<int, Progress*>::iterator i = idmap.find(id);
  if(i == idmap.end())
    return 0;
  return (*i).second;
}
