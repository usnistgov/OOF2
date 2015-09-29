// -*- C++ -*-
// $RCSfile: masterelement.h,v $
// $Revision: 1.38 $
// $Author: reida $
// $Date: 2011/08/18 20:10:23 $


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef MASTERELEMENT_H
#define MASTERELEMENT_H

class MasterElement;
class MasterEdge;

#include <Python.h>
#include <oofconfig.h>

#include "gausspoint.h"
#include "common/coord.h"
#include "engine/mastercoord.h"

// #if DIM == 2
// #include "engine/IO/contour.h"
// #endif
#include <list>
#include <iostream>
#include <string>
#include <vector>

class ContourCellSkeleton;
class ElementNodeIterator;
class ElementCornerNodeIterator;
class Material;
class Node;
class InterfaceElement; 

// Each Element type has a corresponding MasterElement type.  Only one
// instance of each MasterElement type is created.  The MasterElement
// will need to be constructed *before* the ShapeFunction, because the
// ShapeFunction needs to know the Gauss points so that it can
// precompute its values there.

class ProtoNode {
private:
  const MasterCoord pos;
  MasterElement &element;
  int index_;			// local to a masterelement
  std::vector<int> edgeindex;	// Zero length indicates an interior node.
  bool mapping_;
  bool func_;
  bool corner_;
  // only called by MasterElement::addProtoNode
  ProtoNode(MasterElement &el, const MasterCoord &ps)
    : pos(ps),
      element(el),
      mapping_(false),
      func_(false),
      corner_(false)
  {}
public:
  void set_mapping();
  void set_func();
  void set_corner();
  void on_edge(int);

  const MasterCoord &mastercoord() const { return pos; }
  int index() const { return index_; }
  bool mapping() const { return mapping_; }
  bool func() const { return func_; }
  bool corner() const { return corner_; }
  int nedges() const { return edgeindex.size(); } // # of edges this node is on
  int getedge(int i) const { return edgeindex[i]; }
  friend class MasterElement;
  friend std::ostream &operator<<(std::ostream &os, const ProtoNode &pn);
};

class MasterElement {
private:
  std::string name_;		// short name
  std::string desc_;		// long description
  int id_;
protected:
  // Contour support.  TODO: Should be in RealEstateElement, not here.
  // Fixing that will require RealEstateElement to be swigged, and the
  // contour plotting routines will possibly have to be modified to
  // use them instead.
#if DIM == 2
  virtual int sideno(const MasterCoord&) const = 0;
  virtual const MasterCoord *endpoint(int) const = 0;
#endif	// DIM == 2
public:
  MasterElement(const std::string &nm, const std::string &desc,
		int nnodes, int nsides, int nsc);
  virtual ~MasterElement();
  const std::string &name() const { return name_; }
  const std::string &description() const { return desc_; }
  int id() const { return id_; }

  // get a ProtoNode by number
  const ProtoNode *protonode(int) const;
  const MasterEdge *masteredge(const ElementNodeIterator&,
			       const ElementNodeIterator&) const;

  int nnodes() const;
  int nfuncnodes() const;
  int nmapnodes() const;
  int nedges() const;
  int nsides() const { return nedges(); }
  int ncorners() const { return cornernodes.size(); }
  int nexteriorfuncnodes() const;
  int ninteriorfuncnodes() const { return nfuncnodes() - nexteriorfuncnodes(); }
  int nexteriormapnodes_only() const;
  int ninteriormapnodes_only() const;

  virtual MasterCoord center() const = 0;

  // element order info

  virtual int map_order() const = 0;
  virtual int fun_order() const = 0;

#if DIM == 2
  virtual const std::vector<const MasterCoord*> &perimeter() const = 0;
#endif	// DIM == 2

  // Return a table of gauss points suitable for integration of
  // polynomials of a given degree.  The order of integration (number
  // of gauss points) depends on the subclass.
  virtual const GaussPtTable &gausspointtable(int deg) const = 0;

  // Return a table of gauss points for a given integration order.
  const GaussPtTable &gptable(int) const;

  // Number of orders of integration available.
  // This is defined in the TriangularMaster and QuadrilateralMaster classes.
  int ngauss_sets() const;

  // Number of Gauss points used at given integration order.
  int ngauss(int order) const;

  // Create a real Element
  Element *build(PyObject *skelel, Material *m, const std::vector<Node*> *v)
    const;

#if DIM == 2

  //Interface branch
  // Create a real InterfaceElement
  InterfaceElement *buildInterfaceElement(PyObject *skelel, PyObject *skelel2,
					  int segmentordernumber,
					  Material *m,
					  const std::vector<Node*> *v,
					  const std::vector<Node*> *v2,
					  bool leftnodesinorder, 
					  bool rightnodesinorder,
			  const std::vector<std::string> *interfacenames)
    const;

  // ***********************

  // These next four functions are purely virtual here.  Should have
  // benign implementations in EdgeMaster, and real implementations in
  // subclasses of RealEstateElement.

  // Return the subcells to be used for contouring
  virtual std::vector<ContourCellSkeleton*>* contourcells(int n) const = 0;
  // Return an object used to sort points along the boundary of the
  // element, used in closing contours.
  virtual MasterEndPointComparator bdysorter() const = 0;
  CCurve *perimeterSection(const MasterCoord*, const MasterCoord*) const;
  
  // Is a point on the boundary of the element?
  virtual bool onBoundary(const MasterCoord&) const = 0;
  virtual bool onBoundary2(const MasterCoord&, const MasterCoord&) const = 0;

  // Are two points on the same exterior boundary of the element?
  // Exterior boundaries are those corresponding to node iterators
  // passed in through the third argument of this function.
  virtual bool exterior(const MasterCoord&, const MasterCoord&,
			const std::vector<ElementCornerNodeIterator> &ext)
    const = 0;
#endif	// DIM == 2

  // How far outside the element is the given point?  Returns 0 or
  // negative if the point is inside the element.  If the point is
  // outside, the (positive) value returned doesn't have to be
  // precise, but it should be good enough to find the closest
  // element.
  virtual double outOfBounds(const MasterCoord&) const = 0;


  // Superconvergent patch recovery
  int nSCpoints() const { return sc_points.size(); }
  const MasterCoord &getSCpoint(int i) const { return sc_points[i]; }

  // ***********************

protected:
  ShapeFunction *shapefunction;	// set in derived class constructor
  ShapeFunction *mapfunction;	// ditto

  // The MasterElement derived classes must create their ProtoNodes by
  // calling MasterElement::addProtoNode().  They must start at a
  // corner and proceed counterclockwise around the boundary of the
  // element.  The interior nodes, if any, must come last.  Not
  // following this rule will confuse the skeleton when it's
  // constructing real elements, and the correspondence between
  // ProtoNodes in the MasterElement and Nodes in the Element will be
  // lost.
  ProtoNode *addProtoNode(const MasterCoord&);
  std::vector<const ProtoNode*> protonodes;
  std::vector<int> funcnodes;	// indices into protonode list
  std::vector<int> mapnodes;	// ditto
  std::vector<int> cornernodes;	// ditto ditto
  std::vector<int> exteriorfuncnodes; // ditto ditto ditto
  std::vector<MasterEdge*> edges;

  // Superconvergent patch recovery
  void addSCpoint(const MasterCoord&);
  std::vector<MasterCoord> sc_points;

  const std::vector<const MasterCoord*> *findPerimeter() const;
  
  
  // Return a vector of tables of gauss points for all integration orders.
  virtual const std::vector<GaussPtTable> &gptable_vec() const = 0;

  friend class Element;
  friend class InterfaceElement; 
  friend class ElementNodeIterator;
  friend class ElementMapNodeIterator;
  friend class ElementFuncNodeIterator;
  friend class ElementCornerNodeIterator;
  friend class ElementExteriorNodeIterator;
  friend class ShapeFunction;
  friend class ProtoNode;
  friend std::ostream& operator<<(std::ostream&, const MasterElement&);

};

// list of all master elements
std::vector<MasterElement*>* masterElementList();

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

#if DIM == 2

class EdgeMaster : public MasterElement {
  //this class corresponds to the one dimensional
  //element
protected:
  virtual int sideno(const MasterCoord&) const { return 0; }
  virtual const MasterCoord *endpoint(int) const { return 0; }
public:
  EdgeMaster(const std::string &name, const std::string &desc, 
	     int nnodes, int nsc)
    : MasterElement(name, desc, nnodes, 2, nsc) {}
  virtual ~EdgeMaster() {}
  virtual const GaussPtTable &gausspointtable(int deg) const;
  virtual MasterCoord center() const;
  // element order info
  virtual int map_order() const = 0;
  virtual int fun_order() const = 0;

  virtual std::vector<ContourCellSkeleton*>* contourcells(int n) const {
    return new std::vector<ContourCellSkeleton*>();
  }

  virtual bool onBoundary(const MasterCoord&) const { return 0; }
  virtual bool onBoundary2(const MasterCoord&, const MasterCoord&) const 
  { return 0;}

  // Are two points on the same exterior boundary of the element?
  // Exterior boundaries are those corresponding to node iterators
  // passed in through the third argument of this function.
  virtual bool exterior(const MasterCoord&, const MasterCoord&,
			const std::vector<ElementCornerNodeIterator> &ext) 
    const {
    return 0;
  }
  virtual const std::vector<const MasterCoord*> &perimeter() const;
  virtual MasterEndPointComparator bdysorter() const;

  //Interface branch
  virtual double outOfBounds(const MasterCoord&) const;

private:
  virtual const std::vector<GaussPtTable> &gptable_vec() const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Since EdgeMaster element has nothing to do with contour,
// having functions related to contour in MasterElement is not reasonable.
// A new element class, "RealEstateElement" which is derived from
// MasterElement will take care of these functions.
// Thus, TriangularMaster and QuadrilateralMaster will be derived from
// RealEstateElement but not directly from MasterElement.

class RealEstateElement : public MasterElement {
public:
  RealEstateElement(const std::string &name, const std::string &desc, 
		    int nnodes, int nsides, int nsc)
    : MasterElement(name, desc, nnodes, nsides, nsc) {}
  virtual ~RealEstateElement() {}
  // Return the subcells to be used for contouring
  virtual std::vector<ContourCellSkeleton*>* contourcells(int n) const = 0;

  // Is a point on the boundary of the element?
  virtual bool onBoundary(const MasterCoord&) const = 0;
  virtual bool onBoundary2(const MasterCoord&, const MasterCoord&) const = 0;

  // Are two points on the same exterior boundary of the element?
  // Exterior boundaries are those corresponding to node iterators
  // passed in through the third argument of this function.
  virtual bool exterior(const MasterCoord&, const MasterCoord&,
			const std::vector<ElementCornerNodeIterator> &ext)
    const = 0;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class TriangularMaster : public RealEstateElement {
public:
  TriangularMaster(const std::string &name, const std::string &desc, int nnodes, int nsc)
    : RealEstateElement(name, desc, nnodes, 3, nsc) {}
  virtual ~TriangularMaster() {}
  virtual const GaussPtTable &gausspointtable(int deg) const;
  virtual MasterCoord center() const;
  // element order info
  virtual int map_order() const = 0;
  virtual int fun_order() const = 0;
  virtual std::vector<ContourCellSkeleton*>* contourcells(int) const;
  virtual bool onBoundary(const MasterCoord&) const;
  virtual bool onBoundary2(const MasterCoord&, const MasterCoord&) const;
  virtual bool exterior(const MasterCoord&, const MasterCoord&,
			const std::vector<ElementCornerNodeIterator> &ext)
    const;
  virtual double outOfBounds(const MasterCoord&) const;
  virtual const std::vector<const MasterCoord*> &perimeter() const;
  virtual MasterEndPointComparator bdysorter() const;
  static bool endPointComparator(const MasterEndPoint&, const MasterEndPoint&);
  static int sidenumber(const MasterCoord&);
protected:
  virtual int sideno(const MasterCoord &x) const { return sidenumber(x); }
  virtual const MasterCoord *endpoint(int) const;
private:
  virtual const std::vector<GaussPtTable> &gptable_vec() const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class QuadrilateralMaster : public RealEstateElement {
public:
  QuadrilateralMaster(const std::string &name, const std::string &desc,
		      int nnodes, int nsc)
    : RealEstateElement(name, desc, nnodes, 4, nsc) {}
  virtual ~QuadrilateralMaster() {}
  virtual const GaussPtTable &gausspointtable(int deg) const;
  virtual MasterCoord center() const;
  // element order info
  virtual int map_order() const = 0;
  virtual int fun_order() const = 0;
  virtual std::vector<ContourCellSkeleton*>* contourcells(int) const;
  virtual bool onBoundary(const MasterCoord&) const;
  virtual bool onBoundary2(const MasterCoord&, const MasterCoord&) const;
  virtual bool exterior(const MasterCoord&, const MasterCoord&,
			const std::vector<ElementCornerNodeIterator> &ext)
    const;
  virtual double outOfBounds(const MasterCoord&) const;
  virtual const std::vector<const MasterCoord*> &perimeter() const;
  virtual MasterEndPointComparator bdysorter() const;
  static bool endPointComparator(const MasterEndPoint&, const MasterEndPoint&);
  static int sidenumber(const MasterCoord&);
protected:
  virtual int sideno(const MasterCoord &x) const { return sidenumber(x); }
  virtual const MasterCoord *endpoint(int) const;
private:
  virtual const std::vector<GaussPtTable> &gptable_vec() const;
};

#endif

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class MasterEdge {
private:
  // linked list of nodes on this edge, in order of increasing index,
  // therefore going counterclockwise around the element
  std::list<const ProtoNode*> nlist;
  int funcsize_;
public:
  MasterEdge() : funcsize_(0) {}
  void addNode(const ProtoNode*);
  int size() const { return nlist.size(); }
  int func_size() const { return funcsize_; }
  friend class MasterElement;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

#if DIM == 3

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class TetrahedralMaster : public MasterElement {
public:
  TetrahedralMaster(const std::string &name, const std::string &desc,
		      int nnodes, int nsc)
    : MasterElement(name, desc, nnodes, 6, nsc) {}
  virtual ~TetrahedralMaster() {}
  virtual const GaussPtTable &gausspointtable(int deg) const;
  virtual MasterCoord center() const;
  int ncorners() {return 4;}
//   // element order info
  virtual int map_order() const = 0;
  virtual int fun_order() const = 0;
//   virtual std::vector<ContourCellSkeleton*>* contourcells(int) const;
//   virtual bool onBoundary(const MasterCoord&) const;
//   virtual bool onBoundary2(const MasterCoord&, const MasterCoord&) const;
//   virtual bool exterior(const MasterCoord&, const MasterCoord&,
// 			const std::vector<ElementCornerNodeIterator> &ext)
//     const;
  virtual double outOfBounds(const MasterCoord&) const;
//   virtual const std::vector<const MasterCoord*> &perimeter() const;
//   virtual MasterEndPointComparator bdysorter() const;
//   static bool endPointComparator(const MasterEndPoint&, const MasterEndPoint&);
//   static int sidenumber(const MasterCoord&);
// protected:
//   virtual int sideno(const MasterCoord &x) const { return sidenumber(x); }
//   virtual const MasterCoord *endpoint(int) const;
private:
  virtual const std::vector<GaussPtTable> &gptable_vec() const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

#endif


extern int integration_reduction;

#endif
