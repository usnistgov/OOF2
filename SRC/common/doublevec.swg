%module dvec

%include "std_string.i"

%pythoncode %{
  import types
%}

%{
#include <cstring>
#include "doublevec.h"
%}

class DoubleVec {
public:
  DoubleVec() = default;
  DoubleVec(int size, double val=0);
  DoubleVec(const DoubleVec&);
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

  %extend {
    /*
    %new const char* __repr__() {
      std::string s = $self->str();
      char* cs = new char[s.size()+1];
      strcpy(cs, s.c_str());
      return cs;
    }
    */

    %new const char* __repr__() {
      std::string s = $self->str();
      char* cs = new char[s.size()+1];
      strcpy(cs, s.c_str());
      return cs;
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
  }

  %pythoncode %{
    def __len__(self):
        return self.size()
    
    def __add__(self, other):
        result = self.clone()
        result += other
        return result
    
    def __sub__(self, other):
        result = self.clone()
        result -= other
        return result
    
    def __iadd__(self, other):
        if isinstance(other, DoubleVec):
            self.axpy(1.0, other)
            return self
        return NotImplemented
    
    def __isub__(self, other):
        if isinstance(other, DoubleVec):
            self.axpy(-1.0, other)
            return self
        return NotImplemented
    
    def __mul__(self, factor):
        if isinstance(factor, DoubleVec):
            return self.dot(factor)
        # The test for float and int has to be done here, or else
        # vector*matrix leads to an infinite loop, trying to find a
        # suitable __mul__ variant.  Without the test, the __imul__ (*=)
        # invocation below will fail when the rhs is a matrix.  When that
        # happens, python falls back to __mul__, which is this function,
        # which will call __imul__ and so on ad infinitum.
        if type(factor) is types.FloatType or type(factor) is types.IntType:
            result = self.clone()
            result *= factor
            return result
        return NotImplemented
    
    def __rmul__(self, factor):
        if type(factor) is types.FloatType or type(factor) is types.IntType:
            result = self.clone()
            result *= factor
            return result
        return NotImplemented
    
    def __div__(self, factor):
        result = self.clone()
        result /= factor
        return result
    
    def __imul__(self, factor):
        if type(factor) is types.FloatType or type(factor) is types.IntType:
            self.scale(factor)
            return self
        return NotImplemented
    
    def __idiv__(self, factor):
        if type(factor) is types.FloatType or type(factor) is types.IntType:
            self.scale(1./factor)
            return self
        return NotImplemented
    
    def __neg__(self):
        result = self.clone()
        result *= -1.0
        return result
  %}
};

bool save_market_vec(const DoubleVec&, const std::string&);
bool load_market_vec(DoubleVec&, const std::string&);
bool save_vec(const DoubleVec&, const std::string&, int=13);
bool load_vec(DoubleVec&, const std::string&);

