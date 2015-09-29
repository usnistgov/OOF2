// -*- C++ -*-
// $RCSfile: tostring.h,v $
// $Revision: 1.6 $
// $Author: langer $
// $Date: 2014/09/27 21:40:28 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

// Convert anything to a string, as long as operator<< is defined.

#ifndef TOSTRING_H
#define TOSTRING_H

#include <string>

// convert anything to a string

#ifndef HAVE_SSTREAM	// old fashioned version

#include <strstream.h>
template <class TYPE> 
std::string to_string(const TYPE &x) {
  std::ostrstream os;
  os << x << std::ends;
  return os.str();
}

#else  // modern version

#include <sstream>
template <class TYPE> 
std::string to_string(const TYPE &x) {
  std::ostringstream os;
  os << x;
  return os.str();
}

#endif // HAVE_SSTREAM

#endif // TOSTRING_H


