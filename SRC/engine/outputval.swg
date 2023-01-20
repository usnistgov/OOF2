// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OUTPUTVAL_SWG
#define OUTPUTVAL_SWG


%module(package="ooflib.SWIG.engine") outputval

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/fieldindex.swg"
#endif // NOSECONDIMPORTS

PYTHONEXPORTABLE(FieldIndex);

%{
#include "engine/outputval.h"
#include "common/tostring.h"
#include <vector>
typedef OutputVal NewOutputVal;
typedef FieldIndex NewFieldIndex;
%}

// The OutputValueVec typemap converts a std::vector of OutputValues
// to a list of PythonExportable OutputVal subclasses, and hands
// ownership of the objects to Python.


%typemap(out) ArithmeticOutputValueVec* {
  // typemap(out) ArithmeticOutputValueVec*
  ArithmeticOutputValueVec::size_type sz = $1->size();
  // assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $result = PyList_New((Py_ssize_t) sz);
  for(ArithmeticOutputValueVec::size_type i=0; i<sz; i++) {
    // Don't use valuePtr() or valueRef() here, because the OutputVals
    // copied into the Python list will outlive the OutputValues that
    // they're copied from.  valueClone() makes an independent copy,
    // and calling pythonObject with own=true gives Python ownership.
    // of it.
    PyObject *obj = (*$1)[i].valueClone()->pythonObject(true);
    if(!obj)
      SWIG_fail;
    PyList_SET_ITEM($result, (Py_ssize_t) i, obj);
  }
}

%typemap(out) NonArithmeticOutputValueVec* {
  // typemap(out) NonArithmeticOutputValueVec*
  NonArithmeticOutputValueVec::size_type sz = $1->size();
  // assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $result = PyList_New((Py_ssize_t) sz);
  for(NonArithmeticOutputValueVec::size_type i=0; i<sz; i++) {
    // Don't use valuePtr() or valueRef() here, because the OutputVals
    // copied into the Python list will outlive the OutputValues that
    // they're copied from.  valueClone() makes an independent copy,
    // and calling pythonObject with own=true gives Python ownership.
    PyObject *obj = (*$1)[i].valueClone()->pythonObject(true);
    if(!obj)
      SWIG_fail;
    PyList_SET_ITEM($result, (Py_ssize_t) i, obj);
  }
}

%typemap(newfree) ArithmeticOutputValueVec* {
  // typemap(newfree) ArithmeticOutputValueVec*
  delete $1;
}

%typemap(newfree) NonArithmeticOutputValueVec* {
  // typemap(newfree) NonArithmeticOutputValueVec*
  delete $1;
}

PYTHONEXPORTABLE(OutputVal);
%nodefaultctor OutputVal;

%rename(c_components) OutputVal::components;

class OutputVal {
public:
  ~OutputVal();
  int dim();
  // IndexP getIndex(char *);
  NewFieldIndex *getIndex(const std::string&) const;
  NewOutputVal *clone();
  NewOutputVal *zero();
  %newobject value_list;
  std::vector<double> *value_list();
  ComponentsP components();
};

%nodefaultctor NonArithmeticOutputVal;

class NonArithmeticOutputVal : public OutputVal {
public:
};

%nodefaultctor ArithmeticOutputVal;

class ArithmeticOutputVal : public OutputVal {
public:
  NewOutputVal *one();
  void component_pow(int);
  void component_square();
  void component_sqrt();
};

%extend ArithmeticOutputVal {
  double __getitem__(const FieldIndex &i) const {
    return (*self)[i];
  }
};

class ScalarOutputVal : public ArithmeticOutputVal {
public:
  ScalarOutputVal(double);
  double value();
};

%extend ScalarOutputVal {
  // Arithmetic operations -- it's convenient to have
  // Python-accessible wrapped versions of the addto/subtractfrom
  // operations, which don't mess up the ownership.  These are not
  // substitutes for __add__, __sub__, etc. -- they're called by
  // them.
  void _add(const ScalarOutputVal &other) {
    (*self) += other;
  }
  void _sub(const ScalarOutputVal &other) {
    (*self) -= other;
  }
  void _mul(double other) {
    (*self) *= other;
  }
  double __float__() const {
    return self->value(); 
  }
  %newobject __repr__;
  const std::string *__repr__() const {
    return new std::string(to_string(self->value()));
  }
};

class VectorOutputVal : public ArithmeticOutputVal {
public:
  int size();
  VectorOutputVal(int);
};

%extend VectorOutputVal {
  %newobject __repr__;
  const std::string *__repr__() {
    std::string *res = new std::string("[");
    *res += to_string( (*self)[0] );
    for(unsigned int i=1; i<self->size(); i++)
      *res += ", " + to_string( (*self)[i] );
    *res += "]";
    return res;
  }
  // Arithmetic operations -- see comment in ScalarOutputVal, above.
  void _add(const VectorOutputVal &other) {
    (*self) += other;
  }
  void _sub(const VectorOutputVal &other) {
    (*self) -= other;
  }
  void _mul(double other) {
    (*self) *= other;
  }
  double __getitem__(const FieldIndex &i) const {
    return (*self)[i];
  }
  void __setitem__(const FieldIndex &i, double x) {
    (*self)[i] = x;
  }
};

ADD_REPR_GENERIC(ListOutputVal);

class ListOutputVal : public NonArithmeticOutputVal {
public:
  ListOutputVal(std::vector<std::string>*);
  int size();
};

%nodefaultctor ListOutputValIndex;

class ListOutputValIndex : public FieldIndex {

};

%extend ListOutputVal {
  double __getitem__(const FieldIndex &i) const {
    return (*self)[i];
  }
  void __setitem__(const FieldIndex &i, double x) {
    (*self)[i] = x;
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

%nodefaultctor OutputValue;

class OutputValue {
public:
  ~OutputValue();
  OutputVal *valuePtr();
  OutputValue(const OutputValue&);
  int dim();
  NewOutputVal *valueClone();
};

%nodefaultctor NonArithmeticOutputValue;

class NonArithmeticOutputValue : public OutputValue {
};

%nodefaultctor ArithmeticOutputValue;

class ArithmeticOutputValue : public OutputValue {
public:
};

%extend ArithmeticOutputValue {
  double __getitem__(const FieldIndex &i) const {
    return (*self)[i];
  }
  void _add(const ArithmeticOutputValue &other) {
    (*self) += other;
  }
  void _mul(double other) {
    (*self) *= other;
  }
};

%pythoncode "engine/outputval.spy"

#endif // OUTPUTVAL_SWG
