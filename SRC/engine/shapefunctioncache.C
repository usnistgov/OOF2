// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Store the values of the derivatives of a shapefunction and the
// determinant of the jacobian at gauss points. This differs from the
// precomputed values stored in the ShapeFunctionTable class, because
// those values only depend on the master element geometry. These
// values depend on the real space geometry.  We don't want to
// precompute and store the shapefunctions for each element
// individually, because that would take too much memory. But we don't
// want to recompute shape functions when computing all the different
// Properties of a single element.

#include <oofconfig.h>
#include "gausspoint.h"
#include "shapefunctioncache.h"

#include <iostream>

ShapeFunctionCache::ShapeFunctionCache(int ngauss, int nsf)
  : det_jac(new std::vector<SFCValue>(ngauss)),
    df(new std::vector<std::vector<std::vector<SFCValue> > >
       (ngauss,
	std::vector<std::vector<SFCValue> >(nsf,
					     std::vector<SFCValue>(DIM)))),
    cached_element(nullptr)
{}

ShapeFunctionCache::~ShapeFunctionCache() {
  delete det_jac;
  delete df;
}

// is the cache usable?
bool ShapeFunctionCache::current(const Element *el) const {
  return cached_element == el;
}

void ShapeFunctionCache::reset(const Element *el) {
  if(!current(el)) {
    reset();
  }
  cached_element = el;
}

void ShapeFunctionCache::reset() {
  for(std::vector<SFCValue>::size_type i=0; i<det_jac->size(); i++)
    (*det_jac)[i].computed = false;
  for(auto i=0; i<df->size(); i++)
    for(auto j=0; j<(*df)[i].size(); j++)
      for(auto k=0; k<(*df)[i][j].size(); k++)
	(*df)[i][j][k].computed = false;
  cached_element = nullptr;
}

bool ShapeFunctionCache::query_dsf(const Element *el, int i, int j,
				   const GaussPoint &g, double &value)
  const
{
#ifdef OOF2_SHAPEFUNCTION_CACHE
  if(!current(el)) return false; // cached element is different
  SFCValue &v = (*df)[g.index()][i][j];
  
  if(v.computed) {
    value = v.value;
    return true;
  }
  return false;
#else // not using OOF2_SHAPEFUNCTION_CACHE
  return false;
#endif // OOF2_SHAPEFUNCTION_CACHE
}

bool ShapeFunctionCache::query_jac(const Element *el, const GaussPoint &g,
				   double &value) const
{
#ifdef OOF2_SHAPEFUNCTION_CACHE
  if(!current(el)) return false;
  SFCValue &v = (*det_jac)[g.index()];
  if(v.computed) {
    value = v.value;
    return true;
  }
  return false;
#else // not using OOF2_SHAPEFUNCTION_CACHE
  return false;
#endif // OOF2_SHAPEFUNCTION_CACHE
}

void ShapeFunctionCache::store_dsf(const Element *el, int i, int j,
				   const GaussPoint &g, double value)
{
#ifdef OOF2_SHAPEFUNCTION_CACHE
  reset(el);
  
  SFCValue &v = (*df)[g.index()][i][j];
  v.value = value;
  v.computed = true;
#endif // OOF2_SHAPEFUNCTION_CACHE
}

void ShapeFunctionCache::store_jac(const Element *el, const GaussPoint &g,
				   double value)
{
#ifdef OOF2_SHAPEFUNCTION_CACHE
  reset(el);
  SFCValue &v = (*det_jac)[g.index()];
  v.value = value;
  v.computed = true;
#endif // OOF2_SHAPEFUNCTION_CACHE
}

