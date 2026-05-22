/// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef SMALLTENSOR_H
#define SMALLTENSOR_H

#include <stdlib.h>
#include <string.h>
#include <vector>

class SmallTensor3 {
protected:
  std::vector<double> data;
  int index(int i, int j, int k) const {
    return 9*i + 3*j + k;
  }
public:
  SmallTensor3()
    : data(27, 0.0)
  {}
  SmallTensor3(const SmallTensor3 &other) = default;
  SmallTensor3(SmallTensor3 &&other) = default;
  virtual ~SmallTensor3() {}
  double &operator()(int i, int j, int k) {
    return data[index(i, j, k)];
  }
  double operator()(int i, int j, int k) const {
    return data[index(i, j, k)];
  }
};


class SmallTensor4 {
protected:
  std::vector<double> data;
  int index(int i, int j, int k, int l) const {
    return 27*i + 9*j + 3*k + l;
  }
public:
  SmallTensor4()
    : data(81, 0.0)
  {}
  SmallTensor4(const SmallTensor4 &other) = default;
  SmallTensor4(SmallTensor4 &&other) = default;
  virtual ~SmallTensor4() {}
  double &operator()(int i, int j, int k, int l) {
    return data[index(i, j, k, l)];
  };
  double operator()(int i, int j, int k, int l) const {
    return data[index(i, j, k, l)];
  }
};

#endif
