// -*- C++ -*-
// $RCSfile: doublevec.C,v $
// $Revision: 1.1 $
// $Author: langer $
// $Date: 2012/02/28 18:39:37 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/doublevec.h"
#include "common/vectormath.h"
#include <iostream>

// This file is completely unnecessary except when debugging.  It just
// adds debugging code to the python-wrapped std::vector<double>.

//#define VDEBUG DEBUG

#ifdef VDEBUG 
long DoubleVec::total = 0;
#endif // VDEBUG

DoubleVec::DoubleVec() {}

DoubleVec::DoubleVec(int n)
  : std::vector<double>(n, 0.0)
{
#ifdef VDEBUG
  total += n;
  std::cerr << "DoubleVec allocated: " << this << " "
	    << n << " " << total << std::endl;
#endif // VDEBUG
}

DoubleVec::DoubleVec(int n, double x)
  : std::vector<double>(n, x)
{
#ifdef VDEBUG
  total += n;
  std::cerr << "DoubleVec allocated: " << this << " "
	    << n << " " << total << std::endl;
#endif // VDEBUG
}

DoubleVec::DoubleVec(const std::vector<double> &vec)
  : std::vector<double>(vec)
{
#ifdef VDEBUG
  total += size();
  std::cerr << "DoubleVec copied: " << this << " " 
	    << size() << " " << total << std::endl;
#endif // VDEBUG
}

DoubleVec::DoubleVec(const std::vector<double>::const_iterator &a,
		     const std::vector<double>::const_iterator &b)
  : std::vector<double>(a, b)
{
#ifdef VDEBUG
  total += size();
  std::cerr << "DoubleVec copied from iterators: " << this << " " 
	    << size() << " " << total << std::endl;
#endif // VDEBUG
}

DoubleVec::~DoubleVec() {
#ifdef VDEBUG
  total -= size();
  std::cerr << "DoubleVec deallocated: " << this << " " 
	    << size() << " " << total << std::endl;
#endif // VDEBUG
}

void DoubleVec::resize(int n, double x) {
#ifdef VDEBUG
  int old = size();
#endif	// VDEBUG
  std::vector<double>::resize(n, x);
#ifdef VDEBUG
  total += n - old;
  std::cerr << "DoubleVec resized: " << this << " "
	    << old << "->" << n << " " << total 
	    << std::endl;
#endif // VDEBUG
}


double DoubleVec::norm() const {
  return sqrt(dot(*this, *this));
}
