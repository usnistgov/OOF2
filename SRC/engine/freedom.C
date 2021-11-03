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
#include "common/tostring.h"
#include "engine/femesh.h"
#include "engine/freedom.h"
#include <string>

#ifdef HAVE_OPENMP
#include <omp.h>
#include <unordered_map>
#include "engine/csubproblem.h"
using DirtyDofs = std::unordered_map<int, double>;
#endif

DegreeOfFreedom::DegreeOfFreedom(int ind)
  : index_(ind)
{
}

// Making DegreeOfFreedom::value inline in freedom.h causes horrible
// #include loops.

double DegreeOfFreedom::value(const FEMesh *mesh) const {
#ifdef HAVE_OPENMP
  CSubProblem *pSubProb = mesh->getCurrentSubProblem();
  if ( (pSubProb != NULL) && !(pSubProb->dirty_dof_zone.empty()) ) {
    // dirty_dof_zone is used since this function is called 
    // from the parallel region of make_linear_system of a
    // nonlinear solver
    int tdn = omp_get_thread_num();
    DirtyDofs& dirty_dofs = pSubProb->dirty_dof_zone[tdn];
    auto it = dirty_dofs.find(index_);
    if (it == dirty_dofs.end()) {
      double val = (*mesh->dofvalues)[index_];
      dirty_dofs.insert(DirtyDofs::value_type(index_, val));
      return val;
    }
    return it->second;
  }
  else {
    return (*mesh->dofvalues)[index_];
  } 
#else
  return (*mesh->dofvalues)[index_];
#endif
}

double &DegreeOfFreedom::value(FEMesh *mesh) const {
#ifdef HAVE_OPENMP
  CSubProblem *pSubProb = mesh->getCurrentSubProblem();
  if ( (pSubProb != NULL) && !(pSubProb->dirty_dof_zone.empty()) ) {
    // dirty_dof_zone is used since this function is called 
    // from the parallel region of make_linear_system of a
    // nonlinear solver
    int tdn = omp_get_thread_num();
    DirtyDofs& dirty_dofs = pSubProb->dirty_dof_zone[tdn];
    auto it = dirty_dofs.find(index_);
    if (it == dirty_dofs.end()) {
      double val = (*mesh->dofvalues)[index_];
      dirty_dofs.insert(DirtyDofs::value_type(index_, val));
      return val;
    }
    return it->second;
  }
  else {
    return (*mesh->dofvalues)[index_];
  } 
#else
  return (*mesh->dofvalues)[index_];
#endif
}

void DegreeOfFreedom::setValue(const FEMesh *mesh, double newValue)
{
#ifdef HAVE_OPENMP
  CSubProblem *pSubProb = mesh->getCurrentSubProblem();
  if ( (pSubProb != NULL) && !(pSubProb->dirty_dof_zone.empty()) ) {
    // dirty_dof_zone is used since this function is called 
    // from the parallel region of make_linear_system of a
    // nonlinear solver
    int tdn = omp_get_thread_num();
    DirtyDofs& dirty_dofs = pSubProb->dirty_dof_zone[tdn];
    dirty_dofs[index_] = newValue;
  }
  else {
    (*mesh->dofvalues)[index_] = newValue;
  }
#else
  (*mesh->dofvalues)[index_] = newValue;
#endif
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const DegreeOfFreedom &dof) {
  return os << "[" << dof.dofindex() << "]";
}
