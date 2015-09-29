// -*- C++ -*-
// $RCSfile: outputval.swg,v $
// $Revision: 1.24 $
// $Author: langer $
// $Date: 2011/07/14 21:19:31 $

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


%module outputval
%include "engine/typemaps.swg"
%extern "engine/fieldindex.swg"

%pragma(python) include="outputval.spy"

%pragma(python) code="from ooflib.SWIG.engine.fieldindex import IndexPPtr"
%pragma(python) code="from ooflib.SWIG.engine.fieldindex import IteratorPPtr"

%{
#include "engine/outputval.h"
#include "common/tostring.h"
%}

%typemap(python, out) OutputVal* {
  // typemap(python, out) OutputVal*
  $target = $source->pythonObject();
  if(!$target)
    return 0;
}

class OutputVal {
public:
  ~OutputVal();
  IndexP getIndex(char *);
  IteratorP getIterator();
  int dim();
  %new OutputVal *clone();
  %new OutputVal *zero();
  %new OutputVal *one();
  void component_pow(int);
  void component_square();
  void component_sqrt();
  %new DoubleList *value_list();
  %addmethods {
    double __getitem__(const IndexP &i) const {
      return (*self)[i];
    }
  }
};

class ScalarOutputVal : public OutputVal {
public:
  ScalarOutputVal(double);
  double value();
  // Arithmetic operations -- it's convenient to have
  // Python-accessible wrapped versions of the addto/subtractfrom
  // operations, which don't mess up the ownership.  These are not
  // substitutes for __add__, __sub__, etc. -- they're called by
  // them.
  %addmethods {
    %new const string *__repr__() const {
      return new std::string(to_string( self->value() ));
    }
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
  }
};

class VectorOutputVal : public OutputVal {
public:
  int size();
  VectorOutputVal(int);
  %addmethods {
    %new const string *__repr__() const {
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
  }
  %addmethods {
    double __getitem__(const IndexP &i) const {
      return (*self)[i];
    }
    void __setitem__(const IndexP &i, double x) {
      (*self)[i] = x;
    }
  }
};

class OutputValue {
public:
  ~OutputValue();
  OutputVal *valuePtr();
  OutputValue(const OutputValue&);
  int dim();
  %new OutputVal *valueClone();
  %addmethods {
     double __getitem__(const IndexP &i) const {
       return (*self)[i];
     }
     void _add(const OutputValue &other) {
       (*self) += other;
     }
     void _mul(double other) {
       (*self) *= other;
     }
  }
};

#endif // OUTPUTVAL_SWG
