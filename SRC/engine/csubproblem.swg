// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef SUBPROBLEM_SWG
#define SUBPROBLEM_SWG

%module(package="ooflib.SWIG.engine") csubproblem

// Because CSubProblem has methods that return these iterators (which
// are lightweight objects) by value and they don't have default
// constructors, we have to make sure that swig uses the value wrapper
// mechanism.  It's supposed to realize that automatically, but
// somehow isn't.  These lines must precede the importation of the
// class definitions.
%feature("valuewrapper") ElementIterator;
%feature("valuewrapper") NodeIterator;
%feature("valuewrapper") FuncNodeIterator;

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/doublevec.swg"
%import "common/lock.swg"
%import "engine/element.swg"
%import "engine/equation.swg"
%import "engine/femesh.swg"
%import "engine/field.swg"
%import "engine/flux.swg"
%import "engine/linearizedsystem.swg"
%import "engine/material.swg"
%import "engine/meshiterator.swg"
%import "engine/node.swg"
#endif // NOSECONDIMPORTS

// %pragma(python) code="from ooflib.SWIG.common.lock import LockPtr"
// %pragma(python) code="from ooflib.SWIG.common.lock import RWLockPtr"
// %pragma(python) code="from ooflib.SWIG.common.doublevec import DoubleVecPtr"
// %pragma(python) code="from ooflib.SWIG.engine.equation import EquationPtr"
// %pragma(python) code="from ooflib.SWIG.engine.femesh import FEMeshPtr"
// %pragma(python) code="from ooflib.SWIG.engine.field import FieldPtr"
// %pragma(python) code="from ooflib.SWIG.engine.linearizedsystem import LinearizedSystemPtr"
// %pragma(python) code="from ooflib.SWIG.engine.meshiterator import ElementIteratorPtr"
// %pragma(python) code="from ooflib.SWIG.engine.meshiterator import FuncNodeIteratorPtr"
// %pragma(python) code="from ooflib.SWIG.engine.meshiterator import NodeIteratorPtr"
// %pragma(python) code="from ooflib.SWIG.engine.nodalequation import NodalEquationPtr"

%{
#include "common/doublevec.h"
#include "engine/cconjugate.h"
#include "engine/csubproblem.h"
#include "engine/femesh.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/meshiterator.h"
#include "engine/sparsemat.h"
#include <vector>
%}

MAKE_LISTVEC_TYPEMAPS(CConjugatePair);
MAKE_LISTVEC_TYPEMAPS(CompoundField);
MAKE_LISTVEC_TYPEMAPS(Equation);
MAKE_LISTVEC_TYPEMAPS(Field);
MAKE_LISTVEC_TYPEMAPS(Flux);

%nodefaultctor CSubProblem; // only derived classes can be constructed

class CSubProblem {
public:
  ~CSubProblem();

  void set_rwlock(RWLock *rw);
  RWLock * get_rwlock();
  void set_femesh(FEMesh*);
  FEMesh *get_mesh();
  void set_nnodes(int);

  int ndof();
  int neqn();

  bool containsNode(Node*);

  Lock precomputeLock;
  bool precomputeRequired;
  void requirePrecompute();
  void redefined();

  ElementIterator element_iterator();
  NodeIterator node_iterator();
  FuncNodeIterator funcnode_iterator();

  %newobject new_linear_system;
  LinearizedSystem *new_linear_system(double);
  void make_linear_system(LinearizedSystem *, CNonlinearSolver*);

  %newobject all_compound_fields;
  CompoundFieldRefVec *all_compound_fields();
  %newobject all_equations;
  EquationSubClassRefVec *all_equations();
  %newobject all_fluxes;
  FluxSubClassRefVec *all_fluxes();

  %newobject getMaterials;
  MaterialSet *getMaterials();


  bool define_field(Field&);
  void undefine_field(Field&);
  bool is_defined_field(Field&);
  void activate_field(Field&);
  void deactivate_field(Field&);
  bool is_active_field(Field&);
  int n_active_fields();
  void acquire_field_data(Field &field, const CSubProblem*);

  bool is_active_flux(Flux&);

  void activate_equation(Equation&);
  void deactivate_equation(Equation&);
  bool is_active_equation(Equation&);
  int n_active_eqns();

  void setStaticStepper(bool);
  bool staticStepper();

  void mapFields();
  bool set_meshdofs(DoubleVec*);
  %newobject get_meshdofs;
  DoubleVec *get_meshdofs();

  void set_slaveDoF(int);
  void clear_slaveDoFs();

  void post_process();

  // for symmetrizing the stiffness matrix, if at all possible
//   void set_trivial_equation_mapping();
  void set_equation_mapping(CConjugatePairVec*);

#ifdef HAVE_MPI
  int GatherNumNodes();
  void set_parallel_mapping();
#endif

  //AMR subproblem
  // SCPatch stuff, which should be encapsulated elsewhere eventually
  void init_scpatches(IntVec*);
  void add_scpatch(int, Material*, int, IntVec*, IntVec*, int);
  %newobject get_elements_from_patch;
  IntVec *get_elements_from_patch(int, Material*);
  %newobject get_nodes_from_patch;
  IntVec *get_nodes_from_patch(int, Material*);
  void init_nodalfluxes();
  void recover_fluxes();
  void report_recovered_fluxes(Element*, Coord *Point);
  double zz_L2_estimate(Element*, Flux*);
  %newobject zz_L2_weights;
  std::vector<double> *zz_L2_weights(Flux*, double, double);
  bool contains(Element*);
};				// class CSubProblem

%extend CSubProblem {
  int __hash__() {
    return self->objectid();
  }
};

long get_globalCSubProblemCount();

%pythoncode "engine/csubproblem.spy"

#endif // SUBPROBLEM_SWG
