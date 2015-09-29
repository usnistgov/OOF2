// -*- C++ -*-
// $RCSfile: element.h,v $
// $Revision: 1.87 $
// $Author: langer $
// $Date: 2013/12/17 20:11:33 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef ELEMENT_H
#define ELEMENT_H

class Element;
class MasterElement;
#include <Python.h>

#include "common/coord.h"
#include "common/pythonexportable.h"
#include "engine/gausspoint.h"
#include "engine/indextypes.h"
#include "engine/indextypes.h"
#include "engine/shapefunction.h"
#include <string>
#include <vector>

class BoundaryEdge;
class CNonlinearSolver;
class CSkeletonElement;
class CSubProblem;
class DoubleVec;
class Edge;
class EdgeSet;
class InterfaceElementFuncNodeIterator;
class ElementCornerNodeIterator;
class ElementFuncNodeIterator;
class ElementMapNodeIterator;
class ElementNodeIterator;
class ElementReg;
class FEMesh;
class Field;
class Flux;
class FuncNode;
class LinearizedSystem;
class MasterElement;
class MasterPosition;
class Material;
class Node;
class OutputValue;

//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//

// Base class for storage into the element.  Subclasses should
// add fields for the actual data they want to store.
class ElementData : public PythonExportable<ElementData> {
private:
  const std::string name_;
public:
  ElementData(const std::string &nm);
  virtual ~ElementData() {}
  virtual const std::string &classname() const = 0;
  virtual const std::string &modulename() const = 0;
  const std::string &name() const { return name_; }
};


class Element {
private:
  // Set of pointers to data objects.
  mutable std::vector<ElementData*> el_data;

  Element(const Element&);	// prohibited
  Element &operator=(const Element&); // prohibited

  const MasterElement &master;

protected: // Nodelist needs to be visible to interface elements.
  const std::vector<Node*> nodelist;

private:
  const Material *matl;
  int index_;
  std::vector<ElementCornerNodeIterator> *exterior_edges;

  // Elements have to know the SkeletonElements that created them, so
  // that when the SkeletonElement's material changes, the Element can
  // find out about it.  Since a SkeletonElement can create many
  // Elements, it's more efficient to store the SkeletonElement in the
  // Element than vice versa.
  PyObject *skeleton_element;
  CSkeletonElement * cskeleton_element;
  // The edgeset allows elements to own the edges, which are created
  // and manipulated in connection with boundary conditions.  A
  // typical element will have an empty edgeset.  Elements with
  // nontrivial boundaries will allocate enough space for all possible
  // edges at the time that the first edge is requested through a call
  // to getEdge.  Space is allocated in "add_b_edge".
  std::vector<BoundaryEdge*> edgeset;

  //   ShapeFunction *shapefunction() const;
  //   ShapeFunction *mapfunction() const;

  friend class ElementNodeIterator;
  friend class ElementMapNodeIterator;
  friend class ElementFuncNodeIterator;

public:
  const std::vector<Node*> & get_nodelist() const {return nodelist;}
  Element(PyObject *skelel, const MasterElement&, const std::vector<Node*>*,
	  const Material*);
  virtual ~Element();
  CSkeletonElement * get_skeleton_element() const {return cskeleton_element;}
  const std::string *repr() const;	// id string for Python

  const MasterElement &masterelement() const { return master; }
  const Material *material() const { return matl; }

  // Tell the Element that the Material may have changed.
  void refreshMaterial(PyObject *skeletoncontext);

  int ndof() const;  std::vector<int> localDoFmap() const;
  void localDoFs(const FEMesh*, DoubleVec&) const;

  // Compute this element's contribution to the global stiffness
  // matrix at given time.  Redefined in InterfaceElement, to do each
  // "side" separately.
  virtual void make_linear_system(const CSubProblem* const, double time, 
				  const CNonlinearSolver*,
				  LinearizedSystem &) const;
  
  // Post-equilibrium processing.
  void post_process(CSubProblem *) const;

  void set_index(int);
  const int &get_index() const;

  int nnodes() const;
  int nmapnodes() const;
  int nfuncnodes() const;
  int ncorners() const;
  int nexteriorfuncnodes() const;

  // Access to Nodes and ShapeFunctions is done through the
  // ElementNodeIterator classes.  Accessing ShapeFunctions via the
  // iterators ensures that the proper shape function will be selected
  // for non-isoparametric elements, where one node may be associated
  // with more than one shapefunction, the correct choice being
  // determined by whether the node is being used in its role as a
  // mapping node or an interpolation (func) node.
  ElementNodeIterator node_iterator() const;
  ElementMapNodeIterator mapnode_iterator() const;
  virtual ElementFuncNodeIterator* funcnode_iterator() const;
  ElementCornerNodeIterator cornernode_iterator() const;

  int shapefun_degree() const;
  int dshapefun_degree() const;
  int mapfun_degree() const;

  MasterCoord to_master(const Coord&) const; // slow!
  Coord from_master(const MasterPosition&) const;
  // swig requires versions that take pointers instead of references
  MasterCoord to_master(const Coord *c) const { return to_master(*c); }
  Coord from_master(const MasterPosition *m) const { return from_master(*m); }
  MasterCoord center() const;

  // Superconvergent patch recovery
  int nSCpoints() const;
  const MasterCoord &getMasterSCpoint(int i) const;

  // det_jacobian times d(master coord)/d(real coord)
  // includes the factor of |J| for efficiency... don't compute it too often
  double Jdmasterdx(SpaceIndex, SpaceIndex, const GaussPoint&) const;
  double Jdmasterdx(SpaceIndex, SpaceIndex, const MasterCoord&) const;
  double Jdmasterdx(SpaceIndex, SpaceIndex, const Coord&) const; // slow

  // Jacobian of the transformation from master to real coordinates
  virtual double jacobian(SpaceIndex, SpaceIndex, const GaussPoint&) const;
  virtual double jacobian(SpaceIndex, SpaceIndex, const MasterCoord&) const;

  virtual double det_jacobian(const GaussPoint &g) const;
  virtual double det_jacobian(const MasterCoord &mc) const;

  double area() const;

  // Functions for manipulating the element's data sets. TODO: As a
  // practical matter, in the actual property classes, you don't know
  // who else has put data into the element, so you end up retrieving
  // and deleting the data by name, rather than position.  This is
  // inefficient for a vector, but it's what we want to do, therefore
  // the ElementData* vector should be changed to a name-indexed map,
  // to preserve this API but increase the efficiency of the
  // name-based searches.
  int appendData(ElementData *x) const;
  void setDataByName(ElementData *x) const;
  void setData(int i, ElementData *x) const;
  ElementData *getData(int i) const;
  int getIndexByName(const std::string &name)const ;
  ElementData *getDataByName(const std::string &name) const;
  // Deletion functions remove the pointer from the array, but do NOT
  // delete the pointed-to object -- that's the caller's
  // responsibility.
  void delDataByName(const std::string &name) const;
  void delData(int i) const;
  void clearData() const; // Clears the whole structure.  Do not use.


  // Function to return a bunch of gausspoints, for doing integration
  // in Python.  This is probably temporary.
  std::vector<GaussPoint*>* integration_points(int order) const;

  GaussPointIterator integrator(int order) const;
  // int ngauss(int order);	// number of gauss points used at this order

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  OutputValue outputField(const FEMesh*, const Field&, const MasterPosition&)
    const;

  std::vector<OutputValue> *outputFields(const FEMesh*, const Field&,
					 const std::vector<MasterCoord*>*)
    const;

  std::vector<OutputValue> *outputFields(const FEMesh*, const Field&,
					 const std::vector<MasterCoord>&)
    const;

  std::vector<OutputValue> *outputFieldDerivs(const FEMesh*, const Field&,
					      SpaceIndex*,
					      const std::vector<MasterCoord*>*)
    const;

  OutputValue outputFieldDeriv(const FEMesh*, const Field &, SpaceIndex *,
			       const MasterPosition &) const;

  // OutputValue outputFlux(const FEMesh*, const Flux&, const MasterPosition&)
  //   const;

  std::vector<OutputValue> *outputFluxes(const FEMesh*, const Flux &flux,
					 const std::vector<MasterCoord*>*)
    const;

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

//   // Wrappers for Material::begin_element and Material::end_element,
//   // to be called when doing material dependent computations outside
//   // of the make_stiffness machinery.
//   void begin_material_computation(FEMesh*) const;
//   void end_material_computation(FEMesh*) const;

#if DIM==2
  // Identify the edge between the two given nodes as an exterior edge.
  void set_exterior(const Node&, const Node&);

  // Are two master coordinates on the same exterior edge?  An
  // exterior edge is a geometrical boundary of the system (as opposed
  // to a boundary where boundary conditions apply).
  bool exterior(const MasterCoord &, const MasterCoord&) const;
  void dump_exterior() const; // debugging
#endif
  // Edge machinery below this line.

  // Retrieve an edge from the edgelist if present, or create
  // it if not.  This is the "universal" exterior interface that
  // other programs should use.  On the very first call,
  // this routine also
  // allocates space for the edgelist.  Edge lists are not
  // allocated beforehand because (1) only a few elements
  // will need edges, and (2) their size is not known a priori.
  BoundaryEdge *getBndyEdge(const FuncNode*, const FuncNode*);


  void add_b_edge(BoundaryEdge*);
  BoundaryEdge *find_b_edge(const FuncNode*, const FuncNode*);

  // Create a BoundaryEdge object joining the given nodes.  This
  // function is implemented by the concrete element class,
  // because it can depend on node-ordering and spatial
  // configuration information which isn't known until that level.
  BoundaryEdge *newBndyEdge(const FuncNode*, const FuncNode*) const;

  // A routine which returns Edge objects corresponding to all of the
  // edges of the element -- used to draw the element.
#if DIM==2
  std::vector<Edge*> *perimeter() const;
#endif

  friend std::ostream &operator<<(std::ostream&, const Element&);

  Node* getCornerNode(int i) const;
  void setMaterial(const Material* pMat){matl=pMat;}
  //These definitions won't be (shouldn't be) used.
  virtual const std::string &name() const {
    static const std::string _ename="Element";
    return _ename;
  }
  virtual std::vector<std::string>* namelist() const { return 0; }
};


// InterfaceElements have split nodes, and add storage in the subclass for a
// second list of nodes -- by arbitrary convention, these extra nodes
// are the "left side" nodes, and the ones stored in the base class
// are the "right side" nodes.  The iterators and some node access
// functions use the left-right nomenclature.  The constructor
// guarantees that these are assigned correctly.

enum Sidedness { LEFT, RIGHT }; // Used for the internal element state.

class InterfaceElement: public Element
{
private:
  const std::vector<Node*> nodelist2;  // Right-side nodes.
  bool left_nodes_in_interface_order;
  bool right_nodes_in_interface_order;
  PyObject *skeleton_element2;
  CSkeletonElement * cskeleton_element2;
  int _segmentordernumber;
  std::vector<std::string> _interfacenames;
  mutable Sidedness current_side;  
public:
  virtual const std::string &name() const; //retrieve the last name in the list
  virtual std::vector<std::string>* namelist() const;
  const std::vector<Node*> & get_leftnodelist() const { return nodelist;}
  const std::vector<Node*> & get_rightnodelist() const { return nodelist2;}
  InterfaceElement(PyObject *leftskelel, PyObject *rightskelel,
		   int segmentordernumber,
		   const MasterElement&,
		   const std::vector<Node*>*, const std::vector<Node*>*,
		   bool leftnodes_inorder, bool rightnodes_inorder,
		   const Material*,
		   const std::vector<std::string>* interfacenames);
  virtual ~InterfaceElement();
  bool isSubProblemInterfaceElement(const CSubProblem*) const;

  virtual void make_linear_system(const CSubProblem* const,
				  double time,
				  const CNonlinearSolver *nlsolver,
				  LinearizedSystem &system) const;
  // Tell the Element that the Material may have changed.
  void refreshInterfaceMaterial(PyObject *skeletoncontext);
  void rename(const std::string& oldname, const std::string& newname);

  // "Span" is a pair of nodes, the start and end, in interface order.
  // It's used by some properties to compute the element normal.
  std::vector<const Node*> get_left_span() const;
  std::vector<const Node*> get_right_span() const;

  Sidedness side() const { return current_side; }

  virtual ElementFuncNodeIterator* funcnode_iterator() const;

  virtual double jacobian(SpaceIndex i, 
			  SpaceIndex j, const GaussPoint &g) const;
  virtual double jacobian(SpaceIndex i,
			  SpaceIndex j, const MasterCoord &mc) const;

  virtual double det_jacobian(const GaussPoint &) const;
  virtual double det_jacobian(const MasterCoord &) const;

  friend std::ostream &operator<<(std::ostream&, const InterfaceElement&);
};


class CoordElementData : public ElementData {
private:
  const Coord coord_;
  static std::string class_;
  static std::string module_;
public:
  CoordElementData(const std::string &nm, 
		   const Coord c) : ElementData(nm),coord_(c) 
  {}
  virtual ~CoordElementData() {}
  virtual const std::string &classname() const { return class_; }
  virtual const std::string &modulename() const { return module_; }
  const Coord &coord() const { return coord_; }
};

#endif
