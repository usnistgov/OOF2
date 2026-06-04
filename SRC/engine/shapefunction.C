// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Shape function evaluation in the wild is complicated.  Values at
// Gauss points are precomputed and stored in each ShapeFunction's
// sftable.  Values that depend explicitly on Elements (ie,
// derivatives in lab space and jacobians) are stored in
// ShapeFunction::sfcache and re-used when possible.

// This is summary of what happens starting from calling
// ElementFuncNodeIterator::shapefunction or
// ElementFuncNodeIterator::dshapefunction in a Property.

// To evaluate shape functions
//
// In Property, given
//   ElementFuncNodeIterator node
//   MasterPosition pt     // could be MasterCoord or GaussPoint
// Call:
//   ElementFuncNodeIterator::shapefunction(MasterPosition)
//      iterator knows element knows master knows shapefunction
//   which calls ShapeFunction::value(n, MasterPosition)
//      n is iterator index from ElementFuncNodeIterator
//   which calls MasterPosition::shapefunction(ShapeFunction, n)
//   which is either
//   --> GaussPoint::shapefunction(ShapeFunction, n)
//       which calls ShapeFunction::value(n, GaussPoint)
//       which returns value from sftable lookup
//   --> MasterCoord::shapefunction(ShapeFunction, n)
//       which calls ShapeFunction::value(n, MasterCoord)
//       which is defined in the derived ShapeFunction class
//
//
// Shape function *derivatives* are more complicated because of the
// jacobian terms when computing derivative terms in lab coordinates.
//
// In Property, given:
//   ElementFuncNodeIterator node;
//   MasterPosition &pt;    // could be MasterCoord or GaussPoint
// Call:
//   ElementFuncNodeIterator::dshapefunction(i, pt)
//     iterator knows element knows master knows shapefunction
//     i is derivative component     
//   which calls ShapeFunction::realderiv(element, n, i, pt)
//   which calls MasterPosition::dshapefunction(element, ShapeFunction, n, i)
//   which is either
//   --> GaussPoint::dshapefunction(Element, ShapeFunction, n, i)
//       calls ShapeFunction.realderiv(Element, n, i, GaussPoint)
//       which tries to retrieve from sfcache or computes and caches the result
//         * if computing, calls
//           ShapeFunction::masterderiv(n, j, GaussPoint)
//              which looks up the result in sftable
//           and Element::Jdmasterdx(i,j, GaussPoint)
//               which calls ElementMapNodeIterator::masterderiv(ii, GaussPoint)
//               which calls ShapeFunction::masterderiv(n, i, GaussPoint)
//               which looks up the result in sftable
//           and Element::det_jacobian(GaussPoint)
//               which calls ShapeFunction::det_jacobian(Element, GaussPoint)
//               which tries to retrieve from sfcache or computes and caches
//                  if computing, calls
//                  Element::jacobian(int, int, GaussPoint)
//                  which calls ElementMapNodeIterator::masterderiv(int,GPt.)
//                  which call ShapeFunction::masterderiv(int, int, GaussPoint)
//                  which looks up the result in sftable
//   --> MasterCoord::dshapefunction
//       which calls ShapeFunction::realderiv(element, n, i, MasterCoord)
//       which calls
//          Element::Jdmasterdx(int, int, MasterCoord)
//             which calls ElementMapNodeIterator::masterderiv(int, MasterCoord)
//             which calls ShapeFunction::masterderiv(int, int, MasterCoord)
//             which is defined in the derived ShapeFunction class
//          and ShapeFunction::masterderiv(int, int, MasterCoord)
//             which is defined in the derived ShapeFunction class 
//          and ShapeFunction::det_jacobian(Element, MasterCoord)
//             which calls Element::jacobian(int, int, MasterCoord)
//             which calls ElementMapNodeIterator::masterderiv(int, MasterCoord)
//             which calls ShapeFunction::masterderiv(int, int, MasterCoord)
//             which is defined in the derived ShapeFunction class



#include <oofconfig.h>
#include "common/tostring.h"
#include "common/trace.h"
#include "common/doublevec.h"
#include "engine/element.h"
#include "engine/masterelement.h"
#include "engine/shapefunction.h"
#include "engine/shapefunctioncache.h"

// TODO: Tests for shapefunction evaluation

#ifdef HAVE_OPENMP
#include <omp.h>
#endif

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// ShapeFunctionTable stores values of shape function and its
// derivatives at a set of Gauss points.

class ShapeFunctionTable {
public:
  ShapeFunctionTable(int ngauss, int nnodes);
private:
  // f[i][j] = f(gausspoint i, node j)
  std::vector<DoubleVec> f_table;
  // df[i][j][k] = df(gausspoint i, node j)/dx_k
  std::vector<std::vector<DoubleVec> > df_table;
  friend class ShapeFunction;
};

ShapeFunctionTable::ShapeFunctionTable(int ngauss, int nsf)
  : f_table(ngauss, DoubleVec(nsf)),
    df_table(ngauss, std::vector<DoubleVec>(nsf, DoubleVec(DIM)))
{
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ShapeFunction::ShapeFunction(int nsf, const MasterElement &master)
  : nfunctions(nsf)
{
  sftable.reserve(master.ngauss_sets());
  for(int i=0; i<master.ngauss_sets(); i++) {
    sftable.emplace_back(master.ngauss(i), nsf);
  }

#ifdef HAVE_OPENMP
  // When make_linear_system is running in parallel, each thread
  // has its own shapefunction cache storing calculated results of 
  // ShapeFunction::det_jacobian(..) and ShapeFunction::realderiv(..)
  // functions.

  // Allocate a sfcache for each OpenMP thread
  nthreads = omp_get_max_threads();
  ngauss_sets = master.ngauss_sets();
  sfcache.reserve(nthreads*ngauss_sets);
  for(int i=0; i<nthreads; i++) {
    for(int j=0; j<ngauss_sets; j++) {
      sfcache.emplace_back(master.ngauss(j), nsf);
    }
  }
#else
  sfcache.reserve(master.ngauss_sets());
  for(int i=0; i<master.ngauss_sets(); i++) {
    sfcache.emplace_back(master.ngauss(i), nsf);
  }
#endif
}

ShapeFunction::~ShapeFunction() {}

void ShapeFunction::reset_cache() {
  for(ShapeFunctionCache &sfc : sfcache)
    sfc.reset();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Use double dispatch to evaluate shape functions at Positions, since
// the evaluation is done differently at GaussPoints and MasterCoords.

double ShapeFunction::value(int n, const MasterPosition &p) const {
  //  Trace("ShapeFunction::value p=" + tostring(p.mastercoord()));
  return p.shapefunction(*this, n);
}

double ShapeFunction::masterderiv(int n, int j, const MasterPosition &p) const {
  //  Trace("ShapeFunction::masterderiv sf=" + tostring(n) + " p=" + tostring(p.mastercoord()));
  return p.mdshapefunction(*this, n, j);
}

double ShapeFunction::realderiv(const Element *el, int n,
				int j, const MasterPosition &p)
  const
{
  //  Trace("ShapeFunction::realderiv sf=" + tostring(n) + " p=" + tostring(p.mastercoord()));
  return p.dshapefunction(el, *this, n, j);
}

// Find the value and derivative at Gauss points by using the lookup tables.

double ShapeFunction::value(int n, const GaussPoint &g) const {
  return sftable[g.order()].f_table[g.index()][n];
}

// derivative wrt master coordinates
double ShapeFunction::masterderiv(int n, int j, const GaussPoint &g) const {
  //  Trace("ShapeFunction::masterderiv sf=" + tostring(n) + " gpt=" + tostring(g.mastercoord()));
  return sftable[g.order()].df_table[g.index()][n][j];
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Fill in the lookup tables

void ShapeFunction::precompute(const MasterElement &master) {
  // Use the functions that evaluate the shapefunction at arbitrary
  // points to store its values at the Gauss points.  This must be
  // called from the constructor in each ShapeFunction derived
  // class. It can't be called from the base class, because it uses
  // the virtual methods value() and masterderiv().

  // loop over integration orders (sets of gauss points)
  for(int ord=0; ord<master.ngauss_sets(); ord++) {

    const GaussPtTable &gptable = master.gptable(ord);

    std::vector<DoubleVec> &f_table = sftable[ord].f_table;
    std::vector<std::vector<DoubleVec> > &df_table =
      sftable[ord].df_table;

    // loop over gausspoints
    for(std::vector<GaussPtData>::size_type g=0; g<gptable.size(); g++) {
      MasterCoord mpos = gptable[g].position;
      for(int n=0; n<nfunctions; ++n) { // loop over sf's
	f_table[g][n] = value(n, mpos);
	DoubleVec &dftemp = df_table[g][n];
	for(int j=0; j<DIM; ++j) // loop over spatial dimensions
	  dftemp[j] = masterderiv(n, j, mpos);
      }
    }
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double ShapeFunction::realderiv(const Element *el, int n, int i,
				const GaussPoint &g)
  const
{
  //  Trace("ShapeFunction::realderiv 1");
  double result = 0;
  int idx;
#ifdef HAVE_OPENMP
  // calculate the index of the sfcache of current OpenMP thread
  idx = omp_get_thread_num() * ngauss_sets + g.order();
#else
  idx = g.order();
#endif

  if(sfcache[idx].query_dsf(el, n, i, g, result))
    return result;

  // don't be tempted to rewrite this in terms of
  // realderiv(Element*, ..., MasterCoord&) because that one doesn't use
  // the precomputed values of the shape function derivatives!
  for(int j=0; j<DIM; ++j)
    result += el->Jdmasterdx(j, i, g)*masterderiv(n, j, g);
  result /= el->det_jacobian(g);

  sfcache[idx].store_dsf(el, n, i, g, result);
  return result;
}

double ShapeFunction::realderiv(const Element *el, int n, int i,
				const MasterCoord &mc)
  const
{
  //  Trace("ShapeFunction::realderiv 2");
  double result = 0;
  for(int j=0; j<DIM; ++j)
    result += el->Jdmasterdx(j, i, mc)*masterderiv(n, j, mc);
  result /= el->det_jacobian(mc);
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double ShapeFunction::det_jacobian(const Element *el, const GaussPoint &g) const
{
  double result;
  int idx;
#ifdef HAVE_OPENMP
  // calculate the index of the sfcache of current OpenMP thread
  idx = omp_get_thread_num() * ngauss_sets + g.order();
#else
  idx = g.order();
#endif

  if(sfcache[idx].query_jac(el, g, result))
    return result;

  // don't be tempted to rewrite this in terms of
  // det_jacobian(Element*, MasterCoord&) because that one doesn't use
  // the precomputed values of the shape function derivatives!
#if DIM==2
  result = el->jacobian(0, 0, g) * el->jacobian(1, 1, g) -
    el->jacobian(0, 1, g) * el->jacobian(1, 0, g);
#elif DIM==3

  // typing out a closed form in code is messy for 3d
  double m[DIM][DIM]; 
  int ii, jj;
  for(ii=0; ii<DIM; ++ii) {
    for(jj=0; jj<DIM; ++jj) {
      m[ii][jj] = el->jacobian(ii,jj,g);
    }
  }
  result = vtkMath::Determinant3x3(m);

#endif

  sfcache[idx].store_jac(el, g, result);
  return result;
}

double ShapeFunction::det_jacobian(const Element *el, const MasterCoord &mc)
  const
{
#if DIM==2
  return el->jacobian(0, 0, mc) * el->jacobian(1, 1, mc) -
    el->jacobian(0, 1, mc) * el->jacobian(1, 0, mc);
#elif DIM==3

  // typing out a closed form in code is messy for 3d
  double m[DIM][DIM]; 
  int ii, jj;
  for(ii=0; ii<DIM; ++ii) {
    for(jj=0; jj<DIM; ++jj) {
      m[ii][jj] = el->jacobian(ii,jj,mc);
    }
  }
  return vtkMath::Determinant3x3(m);

#endif
}


