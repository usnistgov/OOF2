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

#include "common/doublevec.h"
#include "common/ooferror.h"
#include "common/smallmatrix.h"
#include "engine/corientation.h"
#include "engine/fieldindex.h"
#include "engine/ooferror.h"
#include "engine/outputval.h"
#include "engine/properties/elasticity/cijkl.h"
#include "engine/rank3tensor.h"
#include "engine/symeig3.h"
#include <iomanip>
#include <iostream>

Rank3Tensor::Rank3Tensor(const Rank3Tensor& sm)
  : m0(3), m1(3), m2(3), nrows(3)
{
  (*this)=sm;
}
    
Rank3Tensor::~Rank3Tensor() {}

bool Rank3Tensor::operator==(const Rank3Tensor &that) {
  return (m0==that.m0 && m1==that.m1 && m2==that.m2);
}

Rank3Tensor& Rank3Tensor::operator=(const Rank3Tensor& sm) {
  if(&sm != this) {
    m0 = sm.m0;
    m1 = sm.m1;
    m2 = sm.m2;
  }
  return *this;
}

// access

double Rank3Tensor::operator()(unsigned int i, unsigned int j, unsigned int k)
  const
{
  assert(i<nrows && j<nrows && k<nrows && i>=0 && j>=0 && k>=0);
  if(i==0)
    return m0(j,k);
  if(i==1)
    return m1(j,k);
  return m2(j,k);
}

double &Rank3Tensor::operator()(unsigned int i, unsigned int j, unsigned int k)
	 
{
  assert(i<nrows && j<nrows && k<nrows && i>=0 && j>=0 && k>=0);
  if(i==0)
    return m0(j,k);
  if(i==1)
    return m1(j,k);
  return m2(j,k);
}

double &Rank3Tensor::operator()(int i, const SymTensorIndex &jk) {
  return operator()(i, jk.row(), jk.col());
}

double Rank3Tensor::operator()(int i, const SymTensorIndex &jk) const
{
  return operator()(i, jk.row(), jk.col());
}


Rank3Tensor &Rank3Tensor::operator+=(const Rank3Tensor &a) {
  m0 +=a.m0;
  m1 +=a.m1;
  m2 +=a.m2;
  return *this;
}

Rank3Tensor &Rank3Tensor::operator-=(const Rank3Tensor &a) {
  m0 -= a.m0;
  m1 -= a.m1;
  m2 -= a.m2;
  return *this;
}

SymmMatrix operator*(const Rank3Tensor &a, const DoubleVec &x) {
  unsigned int nrows = a.nrows;
  if(x.size() != nrows) 
    throw ErrProgrammingError("Vector has wrong dimension",
			      __FILE__, __LINE__);
  if(x.size() != nrows) abort();
  SymmMatrix result(nrows);
  for(unsigned int i=0; i<nrows; i++) {
    for(unsigned int j=i; j<nrows; j++)
      for(unsigned int k=0; k<nrows;k++)
	result(i,j) += a(k,i,j)*x[k];
  }
  return result;
}

// Compute A^ T (*this) A
Rank3Tensor Rank3Tensor::transform(const COrientation *orient) const {
  SmallMatrix A = orient->rotation();
  assert(A.rows() == nrows);
  // from Nye page 111, equation 5
  // TODO: Use partial sums to speed this up?
  Rank3Tensor result;
  for(unsigned int i=0; i<nrows; i++) {
    for(unsigned int j=0; j<nrows; j++) {
      // Only need to index k starting from j, because each index i
      // corresponds to a SymmMatrix, which automatically increments
      // both off-diagonals.
      for (unsigned int k=j; k<nrows; k++) {
	double &r = result(i, j, k);
	  for(unsigned int l=0; l<nrows; l++)
	    for(unsigned int m=0; m<nrows; m++)
	      for(unsigned int n=0; n<nrows; n++)
		r += A(i, l) * A(j, m) * A(k,n) * (*this)(l, m, n);
      }
    }
  }
  return result;
}

Rank3Tensor operator*(double x, const Rank3Tensor &A) {
  Rank3Tensor result(A);
  result.m0 *= x;
  result.m1 *= x;
  result.m2 *= x;
  return result;
}

Rank3Tensor operator*(const Rank3Tensor &A, double x) {
  Rank3Tensor result(A);
  result.m0 *= x;
  result.m1 *= x;
  result.m2 *= x;
  return result;
}


Rank3Tensor &Rank3Tensor::operator*=(double x) {
  m0 *= x;
  m1 *= x;
  m2 *= x;
  return *this;
}

Rank3Tensor &Rank3Tensor::operator/=(double x) {
  return operator*=(1./x);
}

Rank3Tensor operator/(const Rank3Tensor &A, double x) {
  Rank3Tensor result(A);
  result *= 1./x;
  return result;
}



std::string Rank3Tensor::classname_("Rank3Tensor");

SymmMatrix &Rank3Tensor::operator()(unsigned int i) {
  assert(i<nrows && i>=0);
  if(i==0)
    return m0;
  if(i==1)
    return m1;
  return m2;
}

SymmMatrix Rank3Tensor::operator()(unsigned int i) const {
  assert(i<nrows && i>=0);
  if(i==0)
    return m0;
  if(i==1)
    return m1;
  return m2;
}

SymmMatrix Rank3Tensor::operator*(const DoubleVec& E) {

  SymmMatrix result(nrows);
  
  //Perform multiplications
  for(unsigned int i=0;i<nrows; i++)
    for(unsigned int j=i; j<nrows;j++)
      for(unsigned int k=0; k<nrows;k++)
	  result(i,j) += (*this)(k,i,j)*E[k];

  return result;
}


Rank3Tensor operator*(const Cijkl &a, const DoubleVec &x) {
  Rank3Tensor result;
  unsigned int nrows = x.size();
  for(unsigned int i=0; i<nrows; i++) 
    for(unsigned int j=0; j<nrows; j++)
      for(unsigned int k=0; k<=j; k++)
	{
	  double &r = result(i,j,k);
	  for(unsigned int l=0; l<nrows; l++)
	    r += a(l,i,j,k)*x[l];
	}
  return result;
}

Rank3Tensor operator*(const Cijkl& c, const Rank3Tensor& d) 
{
  Rank3Tensor e;
  int nrows = d.nrows;
  for(int i=0; i<nrows;i++)
    for(int j=0; j<nrows;j++)
      for(int k=j; k<nrows;k++) { // e_i is stored as a SymmMatrix
	double &eijk = e(i,j,k);
	for(int l=0; l<nrows;l++)
	  for(int m=0; m<nrows;m++)
	    eijk += d(i,l,m)*c(l,m,j,k);
      }
  return e;
}


std::ostream &operator<<(std::ostream &os, const Rank3Tensor &dd) {
  os.setf(std::ios::scientific, std::ios::floatfield);
  os << "[ ";
  for(unsigned int i=0; i<dd.nrows; i++){
    for(unsigned int j=0;j<dd.nrows;j++) {
      for(unsigned int k=0; k<dd.nrows; k++)
	os << dd(i, j, k) << " ";
      os << std::endl;
    }
    os << std::endl;
  }
   os << "]";
  return os ;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Copy values from a Rank3Tensor, modulus, into a ListOutputVal,
// listdata, given a vector, idxstrs, of strings containing the
// indices of the desired components as one space index 1-3, and one
// Voigt index 1-6.

void copyOutputVals(const Rank3Tensor &modulus, ListOutputVal *listdata,
		    const std::vector<std::string> &idxstrs)
{
  for(unsigned int i=0; i<idxstrs.size(); i++) {
    const std::string &idxpair = idxstrs[i];
    int j = int(idxpair[0]-'1');	    // 1-3
    SymTensorIndex kl(int(idxpair[1]-'1')); // Voigt, 1-6
    (*listdata)[i] = modulus(j, kl);
  }
}
