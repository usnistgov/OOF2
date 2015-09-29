// -*- C++ -*-
// $RCSfile: compoundsubproblem.C,v $
// $Revision: 1.8 $
// $Author: langer $
// $Date: 2011/03/04 19:48:12 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include <algorithm>
#include <iterator>

#include "engine/compoundsubproblem.h"

BinarySubproblemPredicate::BinarySubproblemPredicate(CSubProblem *a,
						     CSubProblem *b)
  : subA(a),
    subB(b)
{}

//-------------

bool UnionSBPredicate::operator()(const FEMesh *mesh, const Element *el)
  const
{
  return subA->contains(el) || subB->contains(el);
}

MaterialSet *CUnionSubProblem::getMaterials() const {
  MaterialSet *matlsA = predicate.subA->getMaterials();
  MaterialSet *matlsB = predicate.subB->getMaterials();
  MaterialSet *matls = new MaterialSet();
  std::set_union(matlsA->begin(), matlsA->end(),
		 matlsB->begin(), matlsB->end(),
		 std::insert_iterator<MaterialSet>(*matls, matls->begin()
		 )
    );
  delete matlsA;
  delete matlsB;
  return matls;
}

//-------------

bool IntersectionSBPredicate::operator()(const FEMesh *mesh, const Element *el)
  const
{
  return subA->contains(el) && subB->contains(el);
}

//-------------

bool XorSBPredicate::operator()(const FEMesh *mesh, const Element *el) const {
  // bitwise xor is ok since CSubProblem::contains returns a bool.
  return subA->contains(el) ^ subB->contains(el);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ComplementSBPredicate::ComplementSBPredicate(CSubProblem *comp)
  : complement(comp)
{}

bool ComplementSBPredicate::operator()(const FEMesh *mesh, const Element *el)
  const
{
  return not complement->contains(el);
}
