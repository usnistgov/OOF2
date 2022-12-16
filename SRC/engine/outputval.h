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

#ifndef OUTPUTVAL_H
#define OUTPUTVAL_H

#include "common/pythonexportable.h"
#include "engine/fieldindex.h"

#include <iostream>
#include <math.h>
#include <vector>

class IndexP;

// The OutputVal classes defined here are used to ferry values from
// the finite element mesh out to the Python output machinery. The
// classes give the output machinery the ability to decide what
// further processing is possible (eg computing components or
// invariants).

// OutputVal does not have a template parameter for the output type
// (ie, OutputVal<double>, OutputVal<SymmMatrix3> etc) because the
// templated subclasses would still have to be swigged separately, so
// there wouldn't be much effort saved.

class OutputVal : public PythonExportable<OutputVal> {
private:
  OutputVal(const OutputVal&) = delete;
protected:
  static std::string modulename_;
  int refcount;
public:
  OutputVal();
  virtual ~OutputVal();
  virtual const OutputVal &operator=(const OutputVal&) = 0;
  virtual unsigned int dim() const = 0;
  virtual OutputVal *clone() const = 0;
  virtual OutputVal *zero() const = 0;
  virtual const std::string &modulename() const { return modulename_; }
  // IO ops.
  virtual std::vector<double> *value_list() const = 0;
  virtual void print(std::ostream&) const = 0;
  // getIndex converts the string representation of a component index
  // into an IndexP object that can be used to extract a component.
  virtual IndexP getIndex(const std::string&) const = 0;

  friend class OutputValue;
};

class ArithmeticOutputVal : public OutputVal {
public:
  virtual ArithmeticOutputVal *one() const = 0;
  virtual ArithmeticOutputVal &operator+=(const ArithmeticOutputVal&) = 0;
  virtual ArithmeticOutputVal &operator-=(const ArithmeticOutputVal&) = 0;
  virtual ArithmeticOutputVal &operator*=(double) = 0;
  // Component-wise operations.
  virtual void component_pow(int) = 0;
  virtual void component_square() = 0;
  virtual void component_sqrt() = 0;
  virtual double magnitude() const = 0;
  virtual double operator[](const IndexP&) const = 0;
  virtual double &operator[](const IndexP&) = 0;
};

class NonArithmeticOutputVal : public OutputVal {
public:
};

std::ostream &operator<<(std::ostream &, const OutputVal&);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Subclasses of ArithmeticOutputVal

class ScalarOutputVal : public ArithmeticOutputVal {
private:
  static std::string classname_;
  double val;
public:
  ScalarOutputVal() : val(0.0) {}
  ScalarOutputVal(double x) : val(x) {}
  ScalarOutputVal(const ScalarOutputVal &a) : val(a.val) {}
  const ScalarOutputVal &operator=(const ScalarOutputVal&);
  virtual const ScalarOutputVal &operator=(const OutputVal&);
  virtual unsigned int dim() const { return 1; }
  virtual ScalarOutputVal *clone() const { return new ScalarOutputVal(val); }
  virtual ScalarOutputVal *zero() const { return new ScalarOutputVal(0.0); }
  virtual ScalarOutputVal *one() const { return new ScalarOutputVal(1.0); }
  virtual const std::string &classname() const { return classname_; }
  virtual ArithmeticOutputVal &operator+=(const ArithmeticOutputVal &other) {
    const ScalarOutputVal &another =
      dynamic_cast<const ScalarOutputVal&>(other);
    val += another.val;
    return *this;
  }
  virtual ArithmeticOutputVal &operator-=(const ArithmeticOutputVal &other) {
    const ScalarOutputVal &another =
      dynamic_cast<const ScalarOutputVal&>(other);
    val -= another.val;
    return *this;
  }
  virtual ArithmeticOutputVal &operator*=(double a) {
    val *= a;
    return *this;
  }
  ScalarOutputVal &operator+=(double x) {
    val += x;
    return *this;
  }
  virtual void component_pow(int p) {
    val = pow(val, p);
  }
  virtual void component_square() {
    val *= val;
  }
  virtual void component_sqrt() {
    val = sqrt(val);
  }
  virtual std::vector<double> *value_list() const;
  virtual double magnitude() const { return fabs(val); }
  double value() const { return val; }
  double &value() { return val; }
  virtual double operator[](const IndexP&) const;
  virtual double &operator[](const IndexP&);
  virtual IndexP getIndex(const std::string&) const;
  
  virtual void print(std::ostream&) const;
};

ScalarOutputVal operator+(const ScalarOutputVal&, const ScalarOutputVal&);
ScalarOutputVal operator-(const ScalarOutputVal&, const ScalarOutputVal&);
ScalarOutputVal operator*(const ScalarOutputVal&, double);
ScalarOutputVal operator*(double, const ScalarOutputVal&);
ScalarOutputVal operator/(ScalarOutputVal&, double);

class VectorOutputVal : public ArithmeticOutputVal {
private:
  unsigned int size_;
  double *data;
  static std::string classname_;
public:
  VectorOutputVal();
  VectorOutputVal(int n);
  VectorOutputVal(const VectorOutputVal&);
  VectorOutputVal(const std::vector<double>&);
  virtual ~VectorOutputVal() { delete [] data; }
  virtual const VectorOutputVal &operator=(const OutputVal&);
  const VectorOutputVal &operator=(const VectorOutputVal&);
  virtual unsigned int dim() const { return size_; }
  virtual VectorOutputVal *clone() const;
  virtual VectorOutputVal *zero() const;
  virtual VectorOutputVal *one() const;
  virtual const std::string &classname() const { return classname_; }
  unsigned int size() const { return size_; }
  virtual ArithmeticOutputVal &operator+=(const ArithmeticOutputVal &other) {
    const VectorOutputVal &another = 
      dynamic_cast<const VectorOutputVal&>(other);
    for(unsigned int i=0; i<size_; i++)
      data[i] += another.data[i];
    return *this;
  }
  virtual ArithmeticOutputVal &operator-=(const ArithmeticOutputVal &other) {
    const VectorOutputVal &another = 
      dynamic_cast<const VectorOutputVal&>(other);
    for(unsigned int i=0; i<size_; i++)
      data[i] -= another.data[i];
    return *this;
  }
  virtual ArithmeticOutputVal &operator*=(double a) {
    for(unsigned int i=0; i<size_; i++)
      data[i] *= a;
    return *this;
  }

  virtual void component_pow(int p) {
    for(unsigned int i=0;i<size_;i++)
      data[i] = pow(data[i],p);
  }
  virtual void component_square() {
    for(unsigned int i=0;i<size_;i++)
      data[i] *= data[i];
  }
  virtual void component_sqrt() {
    for(unsigned int i=0;i<size_;i++)
      data[i] = sqrt(data[i]);
  }

  double dot(const std::vector<double>&) const;

  virtual std::vector<double> *value_list() const;
  double operator[](int i) const { return data[i]; }
  double &operator[](int i) { return data[i]; }
  virtual double operator[](const IndexP &p) const;
  virtual double &operator[](const IndexP &p);
  virtual IndexP getIndex(const std::string&) const;
  virtual double magnitude() const;
  virtual void print(std::ostream&) const;
};

VectorOutputVal operator+(const VectorOutputVal&, const VectorOutputVal&);
VectorOutputVal operator-(const VectorOutputVal&, const VectorOutputVal&);
VectorOutputVal operator*(const VectorOutputVal&, double);
VectorOutputVal operator*(double, const VectorOutputVal&);
VectorOutputVal operator/(VectorOutputVal&, double);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Subclasses of NonArithmeticOutputVal

// ListOutputVal is just a list of values without any specific
// structure, so the labels for its components need to be supplied
// externally.

class ListOutputVal : public NonArithmeticOutputVal {
private:
  unsigned int size_;
  double *data;
  const std::vector<std::string> labels; 
  static std::string classname_;
public:
  ListOutputVal(const std::vector<std::string>*);
  ListOutputVal(const std::vector<std::string>*, const std::vector<double>&);
  ListOutputVal(const ListOutputVal&);
  virtual ~ListOutputVal();
  virtual const std::string &classname() const { return classname_; }  
  virtual const ListOutputVal &operator=(const OutputVal&);
  const ListOutputVal &operator=(const ListOutputVal&);
  virtual unsigned int dim() const { return size_; }
  unsigned int size() const { return size_; }  
  virtual ListOutputVal *zero() const;
  virtual ListOutputVal *clone() const;
  double &operator[](int i) { return data[i]; }
  double operator[](int i) const { return data[i]; }
  virtual double operator[](const IndexP &p) const;
  virtual double &operator[](const IndexP &p);
  virtual IndexP getIndex(const std::string&) const;
  virtual std::vector<double> *value_list() const;
  virtual void print(std::ostream&) const;
  const std::string &label(int i) const { return labels[i]; }
  friend class ListOutputValIndex;
};

// ListOutputValIndex has to be a FieldIndex so that it can be used to
// index ListOutputVal, but it doesn't really belong in FieldIndex
// because the in_plane method doesn't make any sense for it.  We're
// over-using the FieldIndex class.
// TODO PYTHON3: OutputVal should use some other kind of Index, and
// FieldIndex should be derived from that.

class ListOutputValIndex : virtual public FieldIndex {
protected:
  int max_;
  int index_;
  const ListOutputVal *ov_;
public:
  ListOutputValIndex(const ListOutputVal *ov)
    : max_(ov->size_), index_(0), ov_(ov)
  {}
  ListOutputValIndex(const ListOutputVal *ov, int i)
    : max_(ov->size_), index_(i), ov_(ov)
  {}
  ListOutputValIndex(const ListOutputValIndex &o)
    : max_(o.max_), index_(o.index_), ov_(o.ov_)
  {}
  virtual const std::string &classname() const;
  virtual FieldIndex *clone() const {
    return new ListOutputValIndex(*this);
  }
  virtual int integer() const { return index_; }
  virtual void set(const std::vector<int>*);
  virtual std::vector<int>* getComponents() const;
  virtual void print(std::ostream &os) const;
  virtual const std::string &shortstring() const;
};


// TODO PYTHON3: Use ComponentIterator?  Do we need this?
// class ListOutputValIterator : public ListOutputValIndex,
// 				   public FieldIterator
// {
// public:
//   ListOutputValIterator(const ListOutputVal *ov)
//     : ListOutputValIndex(ov)
//   {}
//   ListOutputValIterator(const ListOutputValIterator &o)
//     : ListOutputValIndex(o)
//   {}
//   virtual void operator++() { index_++; }
//   virtual bool end() const { return index_ == max_; }
//   virtual void reset() { index_ = 0; }
//   virtual int size() const { return max_; }
//   virtual FieldIterator *cloneIterator() const {
//     return new ListOutputValIterator(*this);
//   }
// };



//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// OutputValue is a generic wrapper for the different OutputVal
// classes.  It takes ownership of the OutputVal that it's initialized
// with, handles the reference counting, and deletes the OutputVal
// when the reference count goes to zero.

class OutputValue {
protected:
  OutputVal *val;
public:
  OutputValue() {}  // Dummy constructor
  OutputValue(OutputVal*);
  OutputValue(const OutputValue&);
  virtual ~OutputValue();

  unsigned int dim() const { return val->dim(); }

  // valueRef and valuePtr do *not* increment the reference count, so
  // it's important to use them only in situations in which the
  // returned reference or pointer cannot possibly outlive the
  // OutputValue.
  const OutputVal &valueRef() const { return *val; }
  const OutputVal *valuePtr() const { return val; } 
  // For situations in which the OutputVal might outlive the
  // OutputValue, use valueClone instead of valueRef or valuePtr.
  // valueClone returns a new copy of the OutputVal.  It's the calling
  // function's responsibility to see that the copy is deleted.
  OutputVal *valueClone() const { return val->clone(); }

  int nrefcount() { return (*val).refcount; } // for debugging
  friend std::ostream &operator<<(std::ostream&, const OutputValue&);
};

class NonArithmeticOutputValue : public OutputValue {
  // This class doesn't do anything that's not already in OutputValue,
  // but all the other ArithmeticOutput* classes have a corresponding
  // NonArithmeticOutput* class, so this one should also.
public:
  NonArithmeticOutputValue() {}
  // NonArithmeticOutputValue(const NonArithmeticOutputVal&);
  NonArithmeticOutputValue(NonArithmeticOutputVal*);
};

class ArithmeticOutputValue : public OutputValue {
public:
  ArithmeticOutputValue() {}
  ArithmeticOutputValue(ArithmeticOutputVal*);
  // ArithmeticOutputValue(const ArithmeticOutputValue&);
  // ~ArithmeticOutputValue();
  
  const ArithmeticOutputValue &operator+=(const ArithmeticOutputValue &other);
  const ArithmeticOutputValue &operator-=(const ArithmeticOutputValue &other);
  const ArithmeticOutputValue &operator *=(double x);

  // In principle, operator[](IndexP) should be defined in the base
  // classes OutputValue and OutputVal.  However, it's a bit of a pain
  // to define them for NonArithmeticOutputVals that are indexed by
  // strings, and they're not needed in C++.  They're defined in
  // Python.
  double operator[](const IndexP &p) const;
  double &operator[](const IndexP &p);
};

ArithmeticOutputValue operator*(double x, const ArithmeticOutputValue &ov);
ArithmeticOutputValue operator*(const ArithmeticOutputValue &ov, double x);
ArithmeticOutputValue operator/(const ArithmeticOutputValue &ov, double x);
ArithmeticOutputValue operator+(const ArithmeticOutputValue &a,
				const ArithmeticOutputValue &b);
ArithmeticOutputValue operator-(const ArithmeticOutputValue &a,
				const ArithmeticOutputValue &b);

std::ostream &operator<<(std::ostream&, const OutputValue&);


// Typedefs used in the swig-generated code.
typedef std::vector<ArithmeticOutputValue> ArithmeticOutputValueVec;
typedef std::vector<NonArithmeticOutputValue> NonArithmeticOutputValueVec;

// TODO: Energies should not be calculated by using the properties
// (each property contributing its part).  Instead, the Fluxes should
// be used.  e += Flux*Grad Field.  Need a better abstract way of
// defining Energies.



#endif // OUTPUTVAL_H
