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
#include "engine/smallsystem.h"
#include <vector>

// Default constructor clears all the objects.
SmallSystem::SmallSystem(int nr, int nc) :
  fluxVector_(nr, 0.0), forceVector_(nr, 0.0), offsetVector_(nr, 0.0),
  mMatrix_(nr,nc), cMatrix_(nr,nc), kMatrix_(nr,nc), dfMatrix_(nr,nc),
  m_clean(true), c_clean(true), k_clean(true), df_clean(true),
  flux_clean(true), force_clean(true), offset_clean(true)
{
  mMatrix_.clear();
  cMatrix_.clear();
  kMatrix_.clear();
  dfMatrix_.clear();
}

void SmallSystem::reset() {
  mMatrix_.clear();
  cMatrix_.clear();
  kMatrix_.clear();
  dfMatrix_.clear();
  fluxVector_.zero();
  forceVector_.zero();
  offsetVector_.zero();
  m_clean = true;
  c_clean = true;
  k_clean = true;
  df_clean = true;
  flux_clean = true;
  force_clean = true;
  offset_clean = true;
}

int SmallSystem::nrows() const {
  return mMatrix_.rows();
}

int SmallSystem::ncols() const {
  return mMatrix_.cols();
}

const DoubleVec &SmallSystem::fluxVector() const {
  return fluxVector_;
}

DoubleVec &SmallSystem::fluxVector() {
  flux_clean = false;
  return fluxVector_;
}

const DoubleVec &SmallSystem::forceVector() const {
  return forceVector_;
}

DoubleVec &SmallSystem::forceVector() {
  force_clean = false;
  return forceVector_;
}

const DoubleVec &SmallSystem::offsetVector() const {
  return offsetVector_;
}

DoubleVec &SmallSystem::offsetVector() {
  offset_clean = false;
  return offsetVector_;
}

SmallSparseMatrix& SmallSystem::mMatrix() {
  m_clean = false;
  return mMatrix_;
}

const SmallSparseMatrix& SmallSystem::mMatrix() const {
  return mMatrix_;
}

SmallSparseMatrix& SmallSystem::cMatrix() {
  c_clean = false;
  return cMatrix_;
}

const SmallSparseMatrix& SmallSystem::cMatrix() const {
  return cMatrix_;
}

SmallSparseMatrix& SmallSystem::kMatrix() {
  k_clean = false;
  return kMatrix_;
}

const SmallSparseMatrix& SmallSystem::kMatrix() const {
  return kMatrix_;
}

SmallSparseMatrix& SmallSystem::dfMatrix() {
  df_clean = false;
  return dfMatrix_;
}

const SmallSparseMatrix& SmallSystem::dfMatrix() const {
  return dfMatrix_;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

#define SET_INDEX(i, j, fluxindex, field, fieldindex, nodeiter)	\
  int i = fluxindex.integer(); \
  int j = nodeiter.localindex(*field, &fieldindex);

double &SmallSystem::stiffness_matrix_element(
				      const FieldIndex &fi,
				      const Field *field,
				      const FieldIndex &fieldindex,
				      const ElementFuncNodeIterator &efi)
{
  k_clean = false;
  SET_INDEX(i, j, fi, field, fieldindex, efi);
  return kMatrix_(i, j);
}

double &SmallSystem::stiffness_matrix_element(
				      const FieldIndex &fi,
				      const Field *field,
				      const ElementFuncNodeIterator &efi)
{
  k_clean = false;
  ScalarFieldIndex sfi;
  SET_INDEX(i, j, fi, field, sfi, efi);
  return kMatrix_(i, j);
}

double SmallSystem::stiffness_matrix_element(const FieldIndex &fi,
					     const Field *field,
					     const FieldIndex &fieldindex,
					     const ElementFuncNodeIterator &efi)
  const
{
  SET_INDEX(i, j, fi, field, fieldindex, efi);
  return kMatrix_(i, j);
}

double SmallSystem::stiffness_matrix_element(const FieldIndex &fi,
					     const Field *field,
					     const ElementFuncNodeIterator &efi)
  const
{
  ScalarFieldIndex sfi;
  SET_INDEX(i, j, fi, field, sfi, efi);
  return kMatrix_(i, j);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double &SmallSystem::force_deriv_matrix_element(
					const FieldIndex &fi,
					const Field *field,
					const FieldIndex &fieldindex,
					const ElementFuncNodeIterator &efi)
{
  df_clean = false;
  SET_INDEX(i, j, fi, field, fieldindex, efi);
  return dfMatrix_(i, j);
}

double &SmallSystem::force_deriv_matrix_element(
					const FieldIndex &fi,
					const Field *field,
					const ElementFuncNodeIterator &efi)

{
  df_clean = false;
  ScalarFieldIndex sfi;
  SET_INDEX(i, j, fi, field, sfi, efi);
  return dfMatrix_(i, j);
}

double SmallSystem::force_deriv_matrix_element(
				       const FieldIndex &fi,
				       const Field *field,
				       const FieldIndex &fieldindex,
				       const ElementFuncNodeIterator &efi)
  const
{
  SET_INDEX(i, j, fi, field, fieldindex, efi);
  return dfMatrix_(i, j);
}

double SmallSystem::force_deriv_matrix_element(
				       const FieldIndex &fi,
				       const Field *field,
				       const ElementFuncNodeIterator &efi)
  const
{
  ScalarFieldIndex sfi;
  SET_INDEX(i, j, fi, field, sfi, efi);
  return dfMatrix_(i, j);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double &SmallSystem::damping_matrix_element(const FieldIndex &fi,
					    const Field *field,
					    const FieldIndex &fieldindex,
					    const ElementFuncNodeIterator &efi)
{
  c_clean = false;
  SET_INDEX(i, j, fi, field, fieldindex, efi);
  return cMatrix_(i, j);
}

double &SmallSystem::damping_matrix_element(const FieldIndex &fi,
					    const Field *field,
					    const ElementFuncNodeIterator &efi)
{
  c_clean = false;
  ScalarFieldIndex sfi;
  SET_INDEX(i, j, fi, field, sfi, efi);
  return cMatrix_(i, j);
}

double SmallSystem::damping_matrix_element(const FieldIndex &fi,
					   const Field *field,
					   const FieldIndex &fieldindex,
					   const ElementFuncNodeIterator &efi)
  const
{
  SET_INDEX(i, j, fi, field, fieldindex, efi);
  return cMatrix_(i, j);
}

double SmallSystem::damping_matrix_element(const FieldIndex &fi,
					   const Field *field,
					   const ElementFuncNodeIterator &efi)
  const
{
  ScalarFieldIndex sfi;
  SET_INDEX(i, j, fi, field, sfi, efi);
  return cMatrix_(i, j);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double &SmallSystem::mass_matrix_element(const FieldIndex &fi,
					 const Field *field,
					 const FieldIndex &fieldindex,
					 const ElementFuncNodeIterator &efi)
{
  m_clean = false;
  SET_INDEX(i, j, fi, field, fieldindex, efi);
  return mMatrix_(i, j);
}

double &SmallSystem::mass_matrix_element(const FieldIndex &fi,
					 const Field *field,
					 const ElementFuncNodeIterator &efi)
{
  m_clean = false;
  ScalarFieldIndex sfi;
  SET_INDEX(i, j, fi, field, sfi, efi);
  return mMatrix_(i, j);
}

double SmallSystem::mass_matrix_element(const FieldIndex &fi,
					const Field *field,
					const FieldIndex &fieldindex,
					const ElementFuncNodeIterator &efi)
  const
{
  SET_INDEX(i, j, fi, field, fieldindex, efi);
  return mMatrix_(i, j);
}

double SmallSystem::mass_matrix_element(const FieldIndex &fi,
					const Field *field,
					const ElementFuncNodeIterator &efi)
  const
{
  ScalarFieldIndex sfi;
  SET_INDEX(i, j, fi, field, sfi, efi);
  return mMatrix_(i, j);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double& SmallSystem::flux_vector_element(int fi) {
  flux_clean = false;
  return fluxVector_[fi];
}

double SmallSystem::flux_vector_element(int fi) const {
  return fluxVector_[fi];
}

double& SmallSystem::force_vector_element(int fi) {
  force_clean = false;
  return forceVector_[fi];
}

double SmallSystem::force_vector_element(int fi) const {
  return forceVector_[fi];
}

double& SmallSystem::offset_vector_element(int fi) {
  offset_clean = false;
  return offsetVector_[fi];
}

double SmallSystem::offset_vector_element(int fi) const {
  return offsetVector_[fi];
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream& operator<<(std::ostream &os, const SmallSystem &ss) {
  os << ss.kMatrix_;
  return os;
}

void SmallSystem::operator+=(const SmallSystem &other)
{
  mMatrix_  += other.mMatrix_;
  cMatrix_  += other.cMatrix_;
  kMatrix_  += other.kMatrix_;
  dfMatrix_ += other.dfMatrix_;

  fluxVector_   += other.fluxVector_;
  forceVector_  += other.forceVector_;
  offsetVector_ += other.offsetVector_;

  m_clean  &= other.m_clean;
  c_clean  &= other.c_clean;
  k_clean  &= other.k_clean;
  df_clean &= other.df_clean;
  flux_clean   &= other.flux_clean;
  force_clean  &= other.force_clean;
  offset_clean &= other.offset_clean;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

SmallSparseMatrix::SmallSparseMatrix(int r, int c)
  : SmallMatrix(r, c),
    nonzero_(r*c, false)
{}

double &SmallSparseMatrix::operator()(int row, int col) {
  nonzero_[row*cols()+col] = true;
  return SmallMatrix::operator()(row, col);
}

double SmallSparseMatrix::operator()(int row, int col) const {
  return SmallMatrix::operator()(row, col);
}

bool SmallSparseMatrix::nonzero(int row, int col) const {
  return nonzero_[row*cols() + col];
}

void SmallSparseMatrix::operator+=(const SmallSparseMatrix &other) {
  data += other.data;
  for(unsigned int i=0; i<nonzero_.size(); i++)
    nonzero_[i] = nonzero_[i] || other.nonzero_[i];
}

std::ostream& operator<<(std::ostream& os, const SmallSparseMatrix& mat) {
  bool first = true;
  os << "[";
  for(int i=0; i<mat.rows(); i++) {
    for(int j=0; j<mat.cols(); j++) {
      if(mat.nonzero(i,j)) {
	if(!first) os << ", ";
	first = false;
	os << "(" << i << "," << j << "," << mat(i,j) << ")";
      }
    }
  }
  os << "]";
  return os;
}
