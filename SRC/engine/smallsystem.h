// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// Simple system for holding element-specific data during flux and
// equation computations.  Has SmallMatrix slots for the various time
// derivatives.  It's in its own file because both fluxes and
// equations need it.  If it stays small and trivial, it could be
// moved.

// TODO: Have two derived classes, one for fluxes and one for
// equations.  Some data is only used for one or the other, but not
// both.

#include <oofconfig.h>
#include "common/doublevec.h"
#include "common/smallmatrix.h"
#include "engine/elementnodeiterator.h"
#include "engine/field.h"
#include "engine/fieldindex.h"

#include <vector>

// SmallSparseMatrix is actually a dense matrix, but it's meant to be
// used as a step in generating a large sparse matrix.  Since it's
// small, it doesn't matter that it's dense.  It keeps track of which
// of its elements have been modified, so that it doesn't copy the
// zeros when it's merged into the large sparse matrix.

class SmallSparseMatrix : public SmallMatrix {

private:
  // using vector<char> instead of vector<bool>
  // because bit shifting operations of vector<bool> cause
  // many cache misses when access nonzero_ elements.
  std::vector<char> nonzero_;

public:
  SmallSparseMatrix(int, int);

  virtual double &operator()(int row, int col);
  virtual double operator()(int row, int col) const;
  void operator+=(const SmallSparseMatrix&);

  bool nonzero(int, int) const;
};

std::ostream &operator<<(std::ostream&, const SmallSparseMatrix&);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class SmallSystem {

private:
  SmallSystem(const SmallSystem&) = delete;
  DoubleVec fluxVector_, forceVector_, offsetVector_;
  SmallSparseMatrix mMatrix_, cMatrix_, kMatrix_, dfMatrix_;
public:

  SmallSparseMatrix& mMatrix();
  SmallSparseMatrix& cMatrix();
  SmallSparseMatrix& kMatrix();
  SmallSparseMatrix& dfMatrix();
  const SmallSparseMatrix& mMatrix() const;
  const SmallSparseMatrix& cMatrix() const;
  const SmallSparseMatrix& kMatrix() const;
  const SmallSparseMatrix& dfMatrix() const;

  // These booleans keep track of whether or not the various matrices
  // in the smallsystem have been written to.  They're true at
  // construction time, and are set false if any non-const element
  // retrieval function is ever run.
  bool m_clean, c_clean, k_clean, df_clean;
  bool flux_clean, force_clean, offset_clean;

  SmallSystem(int nr,int nc);

  int nrows() const;
  int ncols() const;

  void reset();

  const DoubleVec &fluxVector() const;
  DoubleVec &fluxVector();

  const DoubleVec &forceVector() const;
  DoubleVec &forceVector();

  const DoubleVec &offsetVector() const;
  DoubleVec &offsetVector();

  double &stiffness_matrix_element(const FieldIndex&,
				   const Field*,
				   const FieldIndex&,
				   const ElementFuncNodeIterator&);
  double &stiffness_matrix_element(const FieldIndex&,
				   const Field*,
				   const ElementFuncNodeIterator&);
  double stiffness_matrix_element(const FieldIndex&,
				  const Field*,
				  const FieldIndex&,
				  const ElementFuncNodeIterator&) const;
  double stiffness_matrix_element(const FieldIndex&,
				  const Field*,
				  const ElementFuncNodeIterator&) const;
  
  double &force_deriv_matrix_element(const FieldIndex&,
				     const Field*,
				     const FieldIndex&,
				     const ElementFuncNodeIterator&);
  double &force_deriv_matrix_element(const FieldIndex&,
				     const Field*,
				     const ElementFuncNodeIterator&);
  double force_deriv_matrix_element(const FieldIndex&,
				    const Field*,
				    const FieldIndex&,
				    const ElementFuncNodeIterator&) const;
  double force_deriv_matrix_element(const FieldIndex&,
				    const Field*,
				    const ElementFuncNodeIterator&) const;
  
  double &damping_matrix_element(const FieldIndex&,
				 const Field*,
				 const FieldIndex&,
				 const ElementFuncNodeIterator&);
  double &damping_matrix_element(const FieldIndex&,
				 const Field*,
				 const ElementFuncNodeIterator&);
  double damping_matrix_element(const FieldIndex&,
				const Field*,
				const FieldIndex&,
				const ElementFuncNodeIterator&) const;
  double damping_matrix_element(const FieldIndex&,
				const Field*,
				const ElementFuncNodeIterator&) const;

  double &mass_matrix_element(const FieldIndex&,
			      const Field*,
			      const FieldIndex&,
			      const ElementFuncNodeIterator&);
  double &mass_matrix_element(const FieldIndex&,
			      const Field*,
			      const ElementFuncNodeIterator&);
  double mass_matrix_element(const FieldIndex&,
			     const Field*,
			     const FieldIndex&,
			     const ElementFuncNodeIterator&) const;
  double mass_matrix_element(const FieldIndex&,
			     const Field*,
			     const ElementFuncNodeIterator&) const;

  // It's not necessary to have access methods that take a FieldIndex,
  // because FieldIndex can be converted to int. 
  double &flux_vector_element(int);
  double flux_vector_element(int) const;
  double &force_vector_element(int);
  double force_vector_element(int) const;
  double &offset_vector_element(int);
  double offset_vector_element(int) const;

  friend std::ostream& operator<<(std::ostream &,
				  const SmallSystem&);

  void operator+=(const SmallSystem&);

};
