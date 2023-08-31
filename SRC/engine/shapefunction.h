// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Shape function base class. Derived classes must:
// (1)
//      provide two functions that compute the function and its
//      derivatives at a given point in the master element coordinates
// and (2)
//      invoke the precompute() function in their
//      constructor. precompute() takes a MasterElement as an
//      argument.  The MasterElement corresponding to this shape
//      function will call the shapefunction's constructor from its
//      own constructor. precompute() can't be called in the
//      constructor for the ShapeFunction base class, because it uses
//      virtual functions that are only defined in the derived
//      classes.


#ifndef SHAPEFUNCTION_H
#define SHAPEFUNCTION_H

#include "common/coord.h"
#include "gausspoint.h"
#include "engine/indextypes.h"
#include <vector>

class Element;
class ElementNodeIterator;
class MasterElement;

class ShapeFunctionTable;	// only used in shapefunction.C
class ShapeFunctionCache;	// ditto


class ShapeFunction {
public:
  ShapeFunction(int nsf, const MasterElement&);
  virtual ~ShapeFunction();

  // The derived classes need to provide the following functions:
  // value at a master coordinate
  virtual double value(ShapeFunctionIndex, const MasterCoord&) const  = 0;
  // derivative wrt master coordinate at a master coordinate
  virtual double masterderiv(ShapeFunctionIndex, SpaceIndex, const MasterCoord&)
    const = 0;
  // highest degree of any polynomial term in the shape functions
  virtual int degree() const = 0;
  // The highest degree of a derivative is not necessarily one less
  // than the highest degree of the shapefunction itself.  A bilinear
  // shape function has degree 1, but so does its derivative. 
  virtual int deriv_degree() const = 0;

  // ----
  // nothing below here needs to be defined in the derived classes
  // ----

  // When handed a generic MasterPosition, these functions use
  // double-dispatch to evaluate the shapefunction at a MasterCoord or
  // a GaussPoint, as appropriate.
  double value(ShapeFunctionIndex, const MasterPosition&) const;
  double masterderiv(ShapeFunctionIndex, SpaceIndex,
		     const MasterPosition&) const;

  // These NONvirtual functions are computed via lookup tables. The
  // lookup tables are computed by precompute(), which must be called
  // in the derived class's constructor. These functions don't depend
  // on the Element.
  double value(ShapeFunctionIndex, const GaussPoint&) const;
  double masterderiv(ShapeFunctionIndex, SpaceIndex, const GaussPoint&) const;

  // These functions depend on the Element, so they can't be
  // precomputed, but they may be needed repeatedly during one
  // Element's stiffness matrix computation, so they are cached (at
  // the GaussPoints).

  // derivative wrt real coordinates
  double realderiv(const Element*, ShapeFunctionIndex, SpaceIndex,
		   const GaussPoint&) const;
  double realderiv(const Element*, ShapeFunctionIndex, SpaceIndex,
		   const MasterCoord&) const;
  double realderiv(const Element*, ShapeFunctionIndex, SpaceIndex,
		   const MasterPosition&) const;
  double det_jacobian(const Element*, const GaussPoint&) const;
  double det_jacobian(const Element*, const MasterCoord&) const;

protected:
  void precompute(const MasterElement&);
private:
  // precomputed values for different integration orders
  std::vector<ShapeFunctionTable*> sftable;
  // cached Element-dependent values
  std::vector<ShapeFunctionCache*> sfcache;
  int nfunctions;

#ifdef OOF_USE_OPENMP
  // Mesh elements with the same shape, such as triangle, are 
  // sharing one master element which includes cache of shape
  // function values. During make_linear_system, values of 
  // shape functions of each element are calculated and cached
  // in sfcache for reuse.
  // In order to protect sfcache from pollution by different
  // threads when make_linear_system is running in parallel,
  // each thread works on its own sfcache.

  int ngauss_sets; // size of sfcache for each thread
  int nthreads; // Maximun number of threads
#endif
};

#endif

