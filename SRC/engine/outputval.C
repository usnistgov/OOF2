// -*- C++ -*-
// $RCSfile: outputval.C,v $
// $Revision: 1.18 $
// $Author: langer $
// $Date: 2012/02/28 18:39:42 $

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
#include "engine/fieldindex.h"
#include "engine/outputval.h"
#include <math.h>
#include <string.h>		// for memcpy

std::string OutputVal::modulename_("ooflib.SWIG.engine.outputval");
std::string ScalarOutputVal::classname_("ScalarOutputVal");
std::string VectorOutputVal::classname_("VectorOutputVal");

OutputValue::OutputValue(OutputVal *v)
  : val(v)
{
  ++val->refcount;
}

OutputValue::OutputValue(const OutputValue &other)
  : val(other.val)
{
  ++val->refcount;
}

OutputValue::~OutputValue() {
  if(--val->refcount == 0) {
    delete val;
  }
}

OutputValue operator*(double x, const OutputValue &ov) {
  OutputValue result(ov);
  result *= x;
  return result;
}

OutputValue operator*(const OutputValue &ov, double x) {
  OutputValue result(ov);
  result *= x;
  return result;
}

OutputValue operator/(const OutputValue &ov, double x) {
  OutputValue result(ov);
  result *= 1./x;
  return result;
}

OutputValue operator+(const OutputValue &a, const OutputValue &b) {
  OutputValue result(a);
  result += b;
  return result;
}

OutputValue operator-(const OutputValue &a, const OutputValue &b) {
  OutputValue result(a);
  result -= b;
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// These are here just so that debugging lines can be added if needed.

OutputVal::OutputVal() : refcount(0) {}

OutputVal::~OutputVal() {}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double ScalarOutputVal::operator[](const IndexP&) const {
  return val;
}

double &ScalarOutputVal::operator[](const IndexP&) {
  return val;
}

DoubleVec *ScalarOutputVal::value_list() const {
  return new DoubleVec(1, val);
  // DoubleVec *res = new DoubleVec(0);
  // res->reserve(1);
  // res->push_back(val);
  // return res;
}


IndexP ScalarOutputVal::getIndex(const std::string&) const {
  return IndexP(new ScalarFieldIndex());
}

IteratorP ScalarOutputVal::getIterator() const {
  return IteratorP(new ScalarFieldIterator());
}

ScalarOutputVal operator+(const ScalarOutputVal &a, const ScalarOutputVal &b) {
  ScalarOutputVal result(a);
  result += b;
  return result;
}

ScalarOutputVal operator-(const ScalarOutputVal &a, const ScalarOutputVal &b) {
  ScalarOutputVal result(a);
  result -= b;
  return result;
}

ScalarOutputVal operator*(const ScalarOutputVal &a, double b) {
  ScalarOutputVal result(a);
  result *= b;
  return result;
}

ScalarOutputVal operator*(double b, const ScalarOutputVal &a) {
  ScalarOutputVal result(a);
  result *= b;
  return result;
}

ScalarOutputVal operator/(const ScalarOutputVal &a, double b) {
  ScalarOutputVal result(a);
  result *= (1./b);
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

VectorOutputVal::VectorOutputVal(int n)
  : size_(n),
    data(new double[n])
{
  for(int i=0; i<n; i++)
    data[i] = 0.0;
}

VectorOutputVal::VectorOutputVal(const VectorOutputVal &other)
  : size_(other.size_),
    data(new double[other.size_])
{
  (void) memcpy(data, other.data, size_*sizeof(double));
}

VectorOutputVal::VectorOutputVal(const DoubleVec &vec)
  : size_(vec.size()),
    data(new double[vec.size()])
{
  (void) memcpy(data, &vec[0], size_*sizeof(double));
}

DoubleVec *VectorOutputVal::value_list() const {
  DoubleVec *res = new DoubleVec(0);
  res->reserve(size_);
  for(unsigned int i=0;i<size_;i++)
    res->push_back(data[i]);
  return res;
}

OutputVal *VectorOutputVal::clone() const {
  return new VectorOutputVal(*this);
}

OutputVal *VectorOutputVal::zero() const {
  return new VectorOutputVal(size());
}

OutputVal *VectorOutputVal::one() const {
  VectorOutputVal *won = new VectorOutputVal(size());
  for(unsigned int i=0; i<size(); i++)
    won->data[i] = 1.0;
  return won;
}

double VectorOutputVal::dot(const DoubleVec &other) const {
  assert(size() == other.size());
  double sum = 0;
  for(unsigned int i=0; i<size(); i++)
    sum += data[i]*other[i];
  return sum;
}

double VectorOutputVal::operator[](const IndexP &p) const {
  return data[p.integer()];
}
  
double &VectorOutputVal::operator[](const IndexP &p) {
  return data[p.integer()];
}

IndexP VectorOutputVal::getIndex(const std::string &str) const {
  // str must be "x", "y", or "z"
  return IndexP(new VectorFieldIndex(str[0] - 'x'));
}

IteratorP VectorOutputVal::getIterator() const {
  return IteratorP(new VectorFieldIterator(0, size_));
}

double VectorOutputVal::magnitude() const {
  double sum = 0.0;
  for(unsigned int i=0; i<size_; i++) {
    double x = data[i];
    sum += x*x;
  }
  return sqrt(sum);
}

VectorOutputVal operator+(const VectorOutputVal &a, const VectorOutputVal &b) {
  VectorOutputVal result(a);
  result += b;
  return result;
}

VectorOutputVal operator-(const VectorOutputVal &a, const VectorOutputVal &b) {
  VectorOutputVal result(a);
  result -= b;
  return result;
}

VectorOutputVal operator*(const VectorOutputVal &a, double b) {
  VectorOutputVal result(a);
  result *= b;
  return result;
}

VectorOutputVal operator*(double b, const VectorOutputVal &a) {
  VectorOutputVal result(a);
  result *= b;
  return result;
}

VectorOutputVal operator/(const VectorOutputVal &a, double b) {
  VectorOutputVal result(a);
  result *= (1./b);
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const OutputVal &ov) {
  ov.print(os);
  return os;
}

std::ostream &operator<<(std::ostream &os, const OutputValue &value) {
  return os << *value.val;
}

void ScalarOutputVal::print(std::ostream &os) const {
  os << "ScalarOutputVal(" << val << ")";
}

void VectorOutputVal::print(std::ostream &os) const {
  os << "VectorOutputVal(" << data[0];
  for(unsigned int i=1; i<size_; i++) {
    os << ", " << data[i];
  }
  os << ")";
}
