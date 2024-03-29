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

#ifndef PRINTVEC_H
#define PRINTVEC_H

// std::vector<> doesn't have an output operator...

#include <iostream>
#include <iomanip>
#include <set>
#include <vector>

template <class VEC>
void print(const VEC &vec, std::ostream &os) {
  if(vec.size() == 0) return;
  os << vec[0];
  for(std::size_t i=1; i<vec.size(); i++) {
    os << " " << vec[i];
  }
}

template <class TYPE>
std::ostream &operator<<(std::ostream &os, const std::vector<TYPE> &vec) {
  if(vec.size() > 0) {
    std::streamsize prec = os.precision();
    os << std::setprecision(20) << vec[0];
    for(std::size_t i=1; i<vec.size(); i++)
      os << " " << vec[i];
    os.precision(prec);
    // os << std::setprecision(prec);
  }
  return os;
}

template <class TYPE>
std::ostream &operator<<(std::ostream &os, const std::set<TYPE> &set) {
  if(!set.empty()) {
    bool first = true;
    for(auto &x : set) {
      if(!first)
	os << " ";
      os << x;
      first = false;
    }
  }
  return os;
}

#endif
