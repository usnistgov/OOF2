// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef FEMESH_H
#define FEMESH_H

#include <oofconfig.h>

class FEMesh;

#include "engine/equation.h"
#include "engine/field.h"
#include "engine/fieldeqnlist.h"
#include "engine/materialset.h"
#include "engine/meshiterator.h"
#include <map>
#include <set>
#include <string>
#include <vector>

class CMicrostructure;
class Coord;
class DegreeOfFreedom;
class DoFMap;
class DoubleVec;
class Element;
class Equation;
class Field;
class FuncNode;
class FuncNodeIterator;
struct DoFCompare;
struct NodalEqnCompare;
class MasterCoord;
class NodalEquation;
class Node;
class NodeIterator;
class RWLock;
class InterfaceElement;


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

#ifdef HAVE_MPI
class CNodeShareInfo
{
public:
  CNodeShareInfo(std::vector<int>* procs,
		 std::vector<int>* indices, int index);
  ~CNodeShareInfo();
   // index inherited from the skeleton nodes sharing information
  int inheritedindex,nextindex;
  //the rank of the process
  int localprocrank,nextrank;
  // Des this process own the node? It does if the process is the
  // lowest ranked among those that share this node.
  // (This may now vary or get passed to the next process during a solve step.)
  bool owns;
  // Same as owns but this ownership flag should not change once created.
  bool _owns0;
  // Set to true if the sharenode is part of a subproblem element in the process
  // as determined during the solve step.
  bool hasElement;
  // list of processes (rank numbers) that share this node:
  std::vector<int> remoteproclist;
  // list of indices of this node corresponding to the other processes
  // listed in remoteproclist:
  std::vector<int> remoteindexlist;
  // The following four vectors should have the same length.  These
  // get filled up in set_equation_mapping.
  // list of indices of the free DoFs within this node:
  std::vector<int> localdofindexlist;
  // list of indices of the independent NodalEqns within this node:
  std::vector<int> localeqnindexlist;
  // list of indices into the (probably) symmetrized stiffness matrix
  // of the free DoFs:
  std::vector<int> symmatrixdofindexlist;
  // list of indices into the (probably) symmetrized stiffness matrix
  // of the independent NodalEqns:
  std::vector<int> symmatrixeqnindexlist;
};
// Then construct a mapping of the indices in the symmatrixdofindexlist to the
//  combined/global/"uber" linear system.
// Also need a list of the localdofsizes [dofsize0,dofsize1,...]

#endif // HAVE_MPI

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class FEMesh { 
private:
  CMicrostructure * microstructure;
  RWLock *rwlock;
  static long globalFEMeshCount;
  std::vector<double> *dofvalues;
  double time;		       // max time attained by all subproblems
  CSubProblem *currentSubProblem_;
public:
  FEMesh(CMicrostructure *);
  virtual ~FEMesh();
  CMicrostructure *get_microstructure() const { return microstructure; }

  VContainer<Element>* c_elements() const;
  VContainer<Node>* c_nodes() const;
  VContainer<FuncNode>* c_funcnodes() const;
  VContainer<InterfaceElement>* c_interface_elements() const;
  VContainerP<Node> nodes() const;
  VContainerP<FuncNode> funcnodes() const;
  VContainerP<Element> elements() const;
  VContainerP<InterfaceElement> interface_elements() const;

  const std::vector<FuncNode*>& funcnodes_fast() const;

  Node *newMapNode(const Coord&); // the only way to make a Node
  FuncNode *newFuncNode(const Coord&); // the only way to make a FuncNode

#ifdef HAVE_MPI
  // These carry the extra sharing information derived from the
  // parallel skeleton construction of Haan
  FuncNode *newFuncNode_shares(const Coord&,std::vector<int> * procs,
			       std::vector<int> * remoteindices, int index);
  // Map of inherited index to shared FuncNodes
  std::map<int,FuncNode*> m_indexnodemap;
  // It felt natural to associate CNodeShareInfo directly with a FuncNode
  //* TODO: Give NodeShareMap an explicit comparison operator, so that
  //* its storage order is reproducible.
  typedef std::map<FuncNode*,CNodeShareInfo*> NodeShareMap;
  NodeShareMap m_nodesharemap;
  // These maps are keyed by DoFs and NodalEqns.
  // These link to the sharing information stored in the FuncNode
  // and in the two maps above. The intention is to add to the map only
  // those DoFs and NodalEqns that are associated
  // with a node that is shared between two or more processes.
  // In principle, one can search the doflist or eqnlist of the FuncNode's
  // to get the right FuncNode, but this is slower. (This may be temporary)
  typedef std::map<DegreeOfFreedom*, FuncNode*, DoFCompare> DoFNodeMap;
  DoFNodeMap m_dofnodemap;
  typedef std::map<NodalEquation*, FuncNode*, NodalEqnCompare> EqnNodeMap;
  EqnNodeMap m_eqnnodemap;
#endif	// HAVE_MPI

  void reserveFuncNodes(int n);	// reserve space for n func nodes
  void reserveMapNodes(int n);	// reserve space for n map nodes
  void addElement(Element*);
  void reserveElements(int n);

  void addInterfaceElement(InterfaceElement*);
  std::vector<InterfaceElement*> edgement;
  int nedgements() const;
  
  void renameInterfaceElements(const std::string &oldname,
			       const std::string &newname);

  // Caution: NodeIterator::index is not necessarily the same as
  // node.index().  The argument to FEMesh::getNode() is the
  // NodeIterator::index.
  Node *getNode(unsigned int) const;
  FuncNode *getFuncNode(unsigned int) const;

  // Temporary function for finding the closest node.
#if DIM==3
  Node *closestNode(const double x, const double y, const double z);
#else
  Node *closestNode(const double x, const double y);
#endif // DIM==3

  DegreeOfFreedom *createDoF(double x=0); // only way to make a DoF
  void removeDoF(DegreeOfFreedom*);
  int ndof() const { return dof.size(); }

  // NodalEquations represent one component of one Equation at a Node.
  // They are to the rows of the stiffness matrix what the
  // DegreeOfFreedoms are to the columns.
  NodalEquation *createNodalEqn();
  void removeNodalEqn(NodalEquation*);
  int neqn() const { return nodaleqn.size(); }

  Element *getElement(int i) const;

  void refreshMaterials(PyObject *skelctxt); 
  // Keep track of how many Elements use each Material.
  void addMaterial(const Material*);
  void removeMaterial(const Material*);
  //  void makeMaterialLists();
  MaterialSet *getAllMaterials() const; // creates new set

  int nnodes() const;
  int nfuncnodes() const;
  int nelements() const;

  // Is a field in-plane on this mesh?
  bool in_plane(const Field &field) const;
  void set_in_plane(const Field &field, bool);
  std::vector<std::string> *getFieldSetByID(int) const;	// returns new obj

  // API for setting/referring to the read-write lock.  Set_rwlock
  // should be called exactly once when the femesh is inserted into a
  // mesh context object.
  void set_rwlock(RWLock *rw) { rwlock = rw; };
  inline RWLock *get_rwlock() { return rwlock;};

private:
  // These lists can be accessed through the MeshIterators.
  std::vector<FuncNode*> funcnode; // nodes at which dofs are defined
  std::vector<Node*> mapnode;	// nodes only used for geometry mapping
  std::vector<Element*> element;
  int ncount;			// node counter, for assigning ids

  // Master lists of degrees of freedom and nodal equations
  std::vector<DegreeOfFreedom*> dof;

  std::vector<NodalEquation*> nodaleqn;
  void housekeeping();		     // do garbage collection on the lists
  bool dof_list_needs_cleaning;
  bool nodaleqn_list_needs_cleaning; // do the lists need to be cleaned up?

  // Dictionary of wrappers for Field and Equation lists stored at
  // Nodes.  See fieldeqnlist.h.
  FEWrapper<Field>::AllWrappers fieldwrappers;
  FEWrapper<Equation>::AllWrappers equationwrappers;

  std::vector<bool> in_plane_field;

  void clean_nodaleqn();
  void clean_doflist();

  // All materials used by the Mesh
  typedef std::map<const Material*, int, MaterialCompare> MaterialCountMap;
  MaterialCountMap materialCounts;

  struct PropCmp {
    bool operator()(const Property *a, const Property *b) const {
      return a < b;
    }
  };
  typedef std::map<const Property*, void*, PropCmp> PropertyDataMap;
  PropertyDataMap propertyDataMap;

public:
  // Routines for copying DoF values 
  void get_dofvalues(DoubleVec &x, const DoFMap&) const; // mesh -> x
  bool set_dofvalues(const DoubleVec &x, const DoFMap&,
		     const std::set<int>&); // x -> mesh

  // Retrieve the value of a single DoF. Used by FloatBC, sparingly.
  double get_dofvalue(int) const;
  void dumpDoFs(const std::string&) const; // for debugging

  // Routines for storing and retrieving Mesh specific data used by
  // Properties. 
  void set_property_data(const Property*, void*);
  void *get_property_data(const Property*) const;

  void setCurrentTime(double t);
  double getCurrentTime() const;
  CSubProblem *getCurrentSubProblem() const { return currentSubProblem_; }
  void setCurrentSubProblem(CSubProblem *subp) { currentSubProblem_ = subp; }
  void clearCurrentSubProblem() { currentSubProblem_ = 0; }

private:
  friend class Equation::FindAllEquationWrappers;
  friend class Field::FindAllFieldWrappers;
  friend class Node;
  friend class CSubProblem;
  friend class LinearizedSystem;
  friend long get_globalFEMeshCount();
  friend class DegreeOfFreedom;
  friend class MeshDataCache;
  friend class MemoryDataCache;
  friend class DiskDataCache;
};				// FEMesh

long get_globalFEMeshCount();

#endif // FEMESH_H
