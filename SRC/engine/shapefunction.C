// -*- C++ -*-
// $RCSfile: shapefunction.C,v $
// $Revision: 1.17 $
// $Author: lnz5 $
// $Date: 2015/07/17 17:53:03 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/tostring.h"
#include "common/trace.h"
#include "common/doublevec.h"
#include "engine/element.h"
#include "engine/masterelement.h"
#include "engine/shapefunction.h"
#include "engine/shapefunctioncache.h"

#if DIM==3
#include "vtk-5.0/vtkMath.h"
#endif 

#ifdef _OPENMP
#include <omp.h>
#endif

class ShapeFunctionTable {
  // Stores values of shape function and its derivatives at a set of
  // Gauss points.
private:
  ShapeFunctionTable(int ngauss, int nnodes);
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

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ShapeFunction::ShapeFunction(int nsf, const MasterElement &master)
  : sftable(master.ngauss_sets()),
    nfunctions(nsf)
{
  for(int i=0; i<master.ngauss_sets(); i++) {
    sftable[i] = new ShapeFunctionTable(master.ngauss(i), nsf);
  }

#ifdef _OPENMP
  // When make_linear_system is running in parallel, each thread
  // has its own shapefunction cache storing calculated results of 
  // ShapeFunction::det_jacobian(..) and ShapeFunction::realderiv(..)
  // functions.

  // Allocate a sfcache for each OpenMP thread
  nthreads = omp_get_max_threads();
  ngauss_sets = master.ngauss_sets();
  sfcache.resize(nthreads * ngauss_sets);
  for (int i = 0; i < nthreads; i++) {
    for (int j = 0; j < ngauss_sets; j++)
      sfcache[i * ngauss_sets + j] = new ShapeFunctionCache(
        master.ngauss(j), nsf);
  }
#else
  sfcache.resize(master.ngauss_sets());
  for (int i = 0; i < master.ngauss_sets(); i++) {
    sfcache[i] = new ShapeFunctionCache(master.ngauss(i), nsf);
  }
#endif
}

ShapeFunction::~ShapeFunction() {
  for(std::vector<ShapeFunctionTable*>::size_type i=0; i<sftable.size(); i++)
    delete sftable[i]; 
  for(std::vector<ShapeFunctionCache*>::size_type i=0; i<sfcache.size(); i++)
    delete sfcache[i];

}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Use double dispatch to evaluate shape functions at Positions, since
// the evaluation is done differently at GaussPoints and MasterCoords

double ShapeFunction::value(ShapeFunctionIndex n, const MasterPosition &p)
  const
{
  //  Trace("ShapeFunction::value p=" + to_string(p.mastercoord()));
  return p.shapefunction(*this, n);
}

double ShapeFunction::masterderiv(ShapeFunctionIndex n, SpaceIndex j,
		 		  const MasterPosition &p)
  const
{
  //  Trace("ShapeFunction::masterderiv sf=" + to_string(n) + " p=" + to_string(p.mastercoord()));
  return p.mdshapefunction(*this, n, j);
}

double ShapeFunction::realderiv(const Element *el, ShapeFunctionIndex n,
				SpaceIndex j, const MasterPosition &p)
  const
{
  //  Trace("ShapeFunction::realderiv sf=" + to_string(n) + " p=" + to_string(p.mastercoord()));
  return p.dshapefunction(el, *this, n, j);
}

// Find the value and derivative at Gauss points by using the lookup tables.

double ShapeFunction::value(ShapeFunctionIndex n, const GaussPoint &g)
  const
{
  return sftable[g.order()]->f_table[g.index()][n];
}

// derivative wrt master coordinates
double ShapeFunction::masterderiv(ShapeFunctionIndex n, SpaceIndex j,
			    const GaussPoint &g) const
{
  //  Trace("ShapeFunction::masterderiv sf=" + to_string(n) + " gpt=" + to_string(g.mastercoord()));
  return sftable[g.order()]->df_table[g.index()][n][j];
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Fill in the lookup tables

void ShapeFunction::precompute(const MasterElement &master) {
  // Use the virtual functions that evaluate the shapefunction at
  // arbitrary points to store its values at the Gauss points.

  // loop over integration orders (sets of gauss points)
  for(int ord=0; ord<master.ngauss_sets(); ord++) {

    const GaussPtTable &gptable = master.gptable(ord);

    sftable[ord] = new ShapeFunctionTable(gptable.size(), nfunctions);
    std::vector<DoubleVec> &f_table = sftable[ord]->f_table;
    std::vector<std::vector<DoubleVec> > &df_table =
      sftable[ord]->df_table;

    // loop over gausspoints
    for(std::vector<GaussPtData>::size_type g=0; g<gptable.size(); g++) {
      MasterCoord mpos = gptable[g].position;
      for(ShapeFunctionIndex n=0; n<nfunctions; ++n) { // loop over sf's
	f_table[g][n] = value(n, mpos);
	DoubleVec &dftemp = df_table[g][n];
	for(SpaceIndex j=0; j<DIM; ++j) // loop over spatial dimensions
	  dftemp[j] = masterderiv(n, j, mpos);
      }
    }
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double ShapeFunction::realderiv(const Element *el,
				ShapeFunctionIndex n, SpaceIndex i,
				const GaussPoint &g) const
{
  //  Trace("ShapeFunction::realderiv 1");
  double result = 0;
  int idx;
#ifdef _OPENMP
  // calculate the index of the sfcache of current OpenMP thread
  idx = omp_get_thread_num() * ngauss_sets + g.order();
#else
  idx = g.order();
#endif

  if(sfcache[idx]->query_dsf(el, n, i, g, result))
    return result;

  // don't be tempted to rewrite this in terms of
  // realderiv(Element*, ..., MasterCoord&) because that one doesn't use
  // the precomputed values of the shape function derivatives!
  for(SpaceIndex j=0; j<DIM; ++j)
    result += el->Jdmasterdx(j, i, g)*masterderiv(n, j, g);
  result /= el->det_jacobian(g);

  sfcache[idx]->store_dsf(el, n, i, g, result);
  return result;
}

double ShapeFunction::realderiv(const Element *el,
				ShapeFunctionIndex n, SpaceIndex i,
				const MasterCoord &mc) const
{
  //  Trace("ShapeFunction::realderiv 2");
  double result = 0;
  for(SpaceIndex j=0; j<DIM; ++j)
    result += el->Jdmasterdx(j, i, mc)*masterderiv(n, j, mc);
  result /= el->det_jacobian(mc);
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double ShapeFunction::det_jacobian(const Element *el, const GaussPoint &g) const
{
  double result;
  int idx;
#ifdef _OPENMP
  // calculate the index of the sfcache of current OpenMP thread
  idx = omp_get_thread_num() * ngauss_sets + g.order();
#else
  idx = g.order();
#endif

  if(sfcache[idx]->query_jac(el, g, result))
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

  sfcache[idx]->store_jac(el, g, result);
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


