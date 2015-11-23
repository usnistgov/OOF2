/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef SPARSEMAT_SWG
#define SPARSEMAT_SWG

%module sparsemat

%include "std_string.i"
%extern "doublevec.i"

%{
#define SWIG_FILE_WITH_INIT
#include "engine/sparsemat.h"
#include "engine/dofmap.h"
#include <string>
#include <cstring>
%} 

%pythoncode %{
import types
%}

class SparseMat {
public:
  SparseMat() = default;
  SparseMat(unsigned int nr, unsigned int nc);
  //SparseMat(const SparseMat&, const DoFMap&, const DoFMap&);
  SparseMat(const SparseMat&) = default;
  ~SparseMat() = default;
  SparseMat clone() const;

  // TODO(lizhong): inline possible methods

  /* Matrix property methods */

  int nrows() const;
  int ncols() const;
  int nnonzeros() const;
  void resize(int nr, int nc);
  void reserve(int size);
  void insert(int ir, int ic, double val);
  bool empty() const;
  bool is_nonempty_row(unsigned int) const;
  bool is_nonempty_col(unsigned int) const;
  SparseMat lower() const;
  SparseMat unit_lower() const;
  SparseMat upper() const;
  SparseMat unit_upper() const;

  /* Arithmetic operations */

  double norm() const;
  SparseMat transpose() const;

  SparseMat& operator*=(double);
  SparseMat& operator/=(double);

  SparseMat& operator+=(const SparseMat&);
  SparseMat& operator-=(const SparseMat&);
  SparseMat operator*(const SparseMat&) const;
  DoubleVec operator*(const DoubleVec&) const;

  SparseMat &add(double, const SparseMat&); // scale and add
  DoubleVec trans_mult(const DoubleVec&) const;

  // In-place matrix vector multiplication, ala blas.
  void axpy(double alpha, const DoubleVec &x, DoubleVec &y) const;
  void axpy_trans(double alpha, const DoubleVec &x, DoubleVec &y) const;

  // Triangular solvers.
  void solve_lower_triangle(const DoubleVec&, DoubleVec&) const;
  void solve_lower_triangle_unitd(const DoubleVec&, DoubleVec&) const;
  void solve_lower_triangle_trans(const DoubleVec&, DoubleVec&) const;
  void solve_lower_triangle_trans_unitd(const DoubleVec&, DoubleVec&) const;
  void solve_upper_triangle(const DoubleVec&, DoubleVec&) const;
  void solve_upper_triangle_trans(const DoubleVec&, DoubleVec&) const;

  /* Iterators */

  /*
  typedef SparseMatConstIterator const_iterator;
  const_iterator begin() const;
  const_iterator end() const;

  typedef SparseMatIterator iterator;
  iterator begin();
  iterator end();
  */

  /* Debugging routines. */

  bool is_lower_triangular(bool diag) const;
  bool is_upper_triangular(bool diag) const;
  bool is_symmetric(double tolerance) const;
  /*
  bool unique_indices() const;
  DoubleVec inefficient_get_column(unsigned int) const;
  //void merge(const std::vector<SparseMat>& ms);
  //void tile(unsigned int i, unsigned int j, const SparseMat &other);
  */

  const std::string str() const;

  %extend {
    void scale(double a) { *self *= a; }
    SparseMat matrixmultiply(SparseMat &m) { return (*self)*m; }

    %new const char* __repr__() {
      std::string s = $self->str();
      char* cs = new char[s.size()+1];
      strcpy(cs, s.c_str());
      return cs;
    }
  }

  %pythoncode %{
    def size(self):
        return (self.nrows(), self.ncols())

    def __iadd__(self, other):
        if isinstance(other, SparseMat):
            self.add(1.0, other)
            return self
        return NotImplemented
    
    def __add__(self, other):
        result = self.clone()
        result += other
        return result
    
    def __isub__(self, other):
        if isinstance(other, SparseMat):
            self.add(-1.0, other)
            return self
        return NotImplemented
    
    def __sub__(self, other):
        result = self.clone()
        result -= other
        return result
    
    def __mul__(self, x):
        if isinstance(x, SparseMat):
            return self.matrixmultiply(x)
        if isinstance(x, DoubleVec):
            result = DoubleVec(self.nrows())
            self.axpy(1.0, x, result)
            return result
        result = self.clone()
        result *= x
        return result
    
    def __rmul__(self, x):
        if isinstance(x, DoubleVec):
            result = DoubleVec(self.nrows())
            self.axpy_trans(1.0, x, result)
            return result
        result = self.clone()
        result *= x
        return result
    
    def __imul__(self, x):
        if type(x) is types.FloatType or type(x) is types.IntType:
            self.scale(x)
            return self
        return NotImplemented

    def __idiv__(self, x):
        if type(x) is types.FloatType or type(x) is types.IntType:
            self.scale(1./x)
            return self
        return NotImplemented
    
    def __div__(self, x):
        result = self.clone()
        result /= x
        return result
  %}
};

bool save_market_mat(const SparseMat&, const std::string&, int=0);
bool load_market_mat(SparseMat&, const std::string&);
bool save_mat(const SparseMat&, const std::string&, int=13, int=0);
bool load_mat(SparseMat&, const std::string&);

#endif // SPARSEMAT_SWG
