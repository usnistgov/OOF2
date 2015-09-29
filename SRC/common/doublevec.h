// -*- C++ -*-
// $RCSfile: doublevec.h,v $
// $Revision: 1.1 $
// $Author: langer $
// $Date: 2012/02/28 18:39:38 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef DOUBLEVEC_H
#define DOUBLEVEC_H

// DoubleVec is just a trivial wrapper for std::vector<double>.  It
// allows std::vector<double> to be swigged, and allows debugging code
// to be attached to methods that aren't easily accessible in the base
// class.  

#include <vector>

class DoubleVec: public std::vector<double> {
#ifdef DEBUG
private:
  static long total;
#endif // DEBUG
public:
  DoubleVec();
  DoubleVec(int);
  DoubleVec(int, double);
  DoubleVec(const std::vector<double>&);
  DoubleVec(const std::vector<double>::const_iterator&,
	    const std::vector<double>::const_iterator&);
  ~DoubleVec();
  void resize(int n, double x=0);
  double norm() const;
};

#endif // DOUBLEVEC_H
