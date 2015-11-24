/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef DOUBLEVEC_SWG
#define DOUBLEVEC_SWG

%module doublevec

%{
#include <cstring>
#include "common/doublevec.h"
%}

%pragma(python) include="doublevec.spy"

class DoubleVec {
public:
  DoubleVec(int size, double val=0);
  ~DoubleVec();
  
  int size() const;
  void resize(int size, double val=0);
  void zero();
  void unit();

  double norm() const;

  void axpy(double alpha, const DoubleVec& x);
  void scale(double alpha);
  double dot(const DoubleVec&);

  const std::string str() const;
};

%addmethods DoubleVec {
  %new const std::string* __repr__() {
     return new std::string((*self).str());
  }

  // TODO(lizhong): is this function necessary?
  //void copy_inplace(DoubleVec *x) {
  //  self->data = x->data;
  //}

  %new DoubleVec *clone() {
    return new DoubleVec(*self);
  }

  // TODO(lizhong): is this function necessary?
  // Increment the entry at index i by the amount v.
  // Do not use this too much.
  //void increment(int i, double v) {
  //  self->data[i] += v;
  //}

  void save(const char *filename) {
    save_vec(*self, std::string(filename));
  }

  void load(const char *filename) {
    load_vec(*self, std::string(filename));
  }
}

#endif // DOUBLEVEC_SWG
