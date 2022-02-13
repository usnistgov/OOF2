// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef TIMESTAMP_SWG
#define TIMESTAMP_SWG

%module timestamp
%include "common/typemaps.swg"

%{
#include "common/timestamp.h"
#include "common/tostring.h"
%}
%pragma(python) include="timestamp.spy"

class TimeStamp {
public:
  TimeStamp();
  ~TimeStamp();
  void backdate();
  unsigned long time();		// for debugging
  unsigned long epoch();	// for debugging
  TimeStamp clone();
  TimeStamp cloneAndIncrement();
  %addmethods {
    void increment() {
      ++(*self);
    }
    %new const string *__repr__() {
      return new std::string(to_string(*self));
    }
  }
};

bool operator<(const TimeStamp&, const TimeStamp&);
bool operator>(const TimeStamp&, const TimeStamp&);

//double cputime();

%readonly
TimeStamp timeZero;

#endif // TIMESTAMP_SWG
