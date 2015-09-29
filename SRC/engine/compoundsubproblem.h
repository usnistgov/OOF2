// -*- C++ -*-
// $RCSfile: compoundsubproblem.h,v $
// $Revision: 1.9 $
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

#ifndef COMPOUNDSUBPROBLEM_H
#define COMPOUNDSUBPROBLEM_H

#include "engine/predicatesubproblem.h"
#include <iostream>

class BinarySubproblemPredicate {
public:
  BinarySubproblemPredicate(CSubProblem*, CSubProblem*);
  virtual ~BinarySubproblemPredicate() {}
  virtual bool operator()(const FEMesh*, const Element*) const = 0;
  CSubProblem *subA;
  CSubProblem *subB;
};

class UnionSBPredicate: public BinarySubproblemPredicate {
public:
  UnionSBPredicate(CSubProblem *a, CSubProblem *b)
    : BinarySubproblemPredicate(a, b)
  {}
  virtual bool operator()(const FEMesh*, const Element*) const;
};

class CUnionSubProblem: public PredicateSubProblem<UnionSBPredicate> {
public:
  CUnionSubProblem(CSubProblem *a, CSubProblem *b)
    : PredicateSubProblem<UnionSBPredicate>(UnionSBPredicate(a, b))
  {}
  virtual MaterialSet *getMaterials() const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class IntersectionSBPredicate: public BinarySubproblemPredicate {
public:
  IntersectionSBPredicate(CSubProblem *a, CSubProblem *b)
    : BinarySubproblemPredicate(a, b)
  {}
  virtual bool operator()(const FEMesh*, const Element*) const;
};

class CIntersectionSubProblem:
  public PredicateSubProblem<IntersectionSBPredicate>
{
public:
  CIntersectionSubProblem(CSubProblem *a, CSubProblem *b)
    : PredicateSubProblem<IntersectionSBPredicate>(IntersectionSBPredicate(a,b))
  {}
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class XorSBPredicate: public BinarySubproblemPredicate {
public:
  XorSBPredicate(CSubProblem *a, CSubProblem *b)
    : BinarySubproblemPredicate(a, b)
  {}
  virtual bool operator()(const FEMesh*, const Element*) const;
};

class CXorSubProblem:
  public PredicateSubProblem<XorSBPredicate>
{
public:
  CXorSubProblem(CSubProblem *a, CSubProblem *b)
    : PredicateSubProblem<XorSBPredicate>(XorSBPredicate(a,b))
  {}
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class ComplementSBPredicate {
protected:
  CSubProblem *complement;
public:
  ComplementSBPredicate(CSubProblem*);
  bool operator()(const FEMesh*, const Element*) const;
};

class CComplementSubProblem: public PredicateSubProblem<ComplementSBPredicate> {
public:
  CComplementSubProblem(CSubProblem *comp)
    : PredicateSubProblem<ComplementSBPredicate>(ComplementSBPredicate(comp))
  {}
};

#endif // COMPOUNDSUBPROBLEM_H
