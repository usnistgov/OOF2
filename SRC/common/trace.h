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

// Declare a Trace object at the entry point to a function, and the
// given string will be printed when the function is called.

#ifndef TRACE_H
#define TRACE_H

#include <string>

// To keep swig and python happy, the Trace_t class is defined even if
// it's not used.  The Trace_t class is never instantiated if DEBUG is
// not defined.

class Trace_t {
private:
  static int depth;
  static bool enabled;
public:
  Trace_t(const std::string &);
  ~Trace_t();
  void msg(const std::string&) const;
  static void disable() { enabled = false; }
  static void enable() { enabled = true; }
};

#ifdef DEBUG

#define Trace(x) Trace_t trace_var_name_that_ought_to_be_unique(x)
#define TraceMsg(str) trace_var_name_that_ought_to_be_unique.msg(str)

#else  // !DEBUG

#define Trace(x) ; 
#define TraceMsg(x) ;

#endif // !DEBUG


#endif
