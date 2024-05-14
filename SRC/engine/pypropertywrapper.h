// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Base classes for Properties that are defined in Python.  The
// methods in the C++ base class calls the equivalently-named methods
// in the derived Python class via the Python API.

#ifndef PYPROPERTYWRAPPER_H
#define PYPROPERTYWRAPPER_H

#include <oofconfig.h>

#include "engine/element.h"
#include "property.h"
#include "common/pythonexportable.h"

class Field;
class Flux;
class SmallSystem;
class Material;
class FEMesh;
class ElementFuncNodeIterator;
class MasterPosition;


class PyPropertyMethods {
public:
  PyPropertyMethods(PyObject*);
  virtual ~PyPropertyMethods();
  // A "py_" prefix was added to these method names to keep the clang
  // compiler from complaining about hidden overloaded virtual
  // functions.  They will call the corresponding method, without the
  // prefix, in the derived Python class.
  virtual void py_precompute(FEMesh*);
  virtual void py_cross_reference(Material*);
  virtual void py_begin_element(const CSubProblem*, const Element*);
  virtual void py_end_element(const CSubProblem*, const Element*);
  virtual void py_post_process(CSubProblem *, const Element*)
    const;
  virtual bool py_constant_in_space() const;
  virtual void py_output(FEMesh*, const Element*, const PropertyOutput*,
			 const MasterPosition&, OutputVal*);
  bool is_symmetric_K(const CSubProblem*) const;
  bool is_symmetric_C(const CSubProblem*) const;
  bool is_symmetric_M(const CSubProblem*) const;
protected:
  PyObject *referent_;		// pointer to the actual Python Property object
};

class PyPhysicalPropertyMethods {
public:
  virtual int py_integration_order(
		   PyObject*, const CSubProblem*, const Element*) const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class PyFluxProperty : public FluxProperty,
		       public PyPropertyMethods, 
		       public PyPhysicalPropertyMethods,
		       virtual public PythonNative<Property>
{
public:
  PyFluxProperty(PyObject *referent, PyObject *regstn,
		 const std::string &name);
  virtual ~PyFluxProperty();
  virtual void flux_matrix(const FEMesh*, const Element*,
			   const ElementFuncNodeIterator&,
			   const Flux*, const MasterPosition&,
			   double time, SmallSystem*) const;
  virtual void flux_value(const FEMesh*, const Element*,
			  const Flux*, const MasterPosition&,
			  double time, SmallSystem*) const;
  virtual void static_flux_value(const FEMesh*, const Element*,
				 const Flux*, const MasterPosition&,
				 double time, SmallSystem*) const;
  virtual void flux_offset(const FEMesh*, const Element*,
			   const Flux*, const MasterPosition&,
			   double time, SmallSystem*) const;

  virtual void precompute(FEMesh *m) {
    PyPropertyMethods::py_precompute(m);
  }
  virtual void cross_reference(Material *m) { 
    PyPropertyMethods::py_cross_reference(m);
  }
  virtual void begin_element(const CSubProblem *sb, const Element *e) {
    PyPropertyMethods::py_begin_element(sb, e);
  }
  virtual void end_element(const CSubProblem *sb, const Element *e) {
    PyPropertyMethods::py_end_element(sb, e);
  }
  virtual void begin_point(const FEMesh *m, const Element *e,
			   const Flux *f, const MasterPosition &p);
  virtual void end_point(const FEMesh *m, const Element *e,
			 const Flux *f, const MasterPosition &p);
  virtual void post_process(CSubProblem *sb, const Element *e) const {
    PyPropertyMethods::py_post_process(sb, e);
  }
  virtual bool constant_in_space() const {
    return PyPropertyMethods::py_constant_in_space();
  }
  virtual void output(FEMesh *m, const Element *e, 
		      const PropertyOutput *po,
		      const MasterPosition &p, OutputVal *ov)
  {
    PyPropertyMethods::py_output(m, e, po, p, ov);
  }
  virtual int integration_order(const CSubProblem *sb, const Element *e) const {
    return PyPhysicalPropertyMethods::py_integration_order(referent_, sb, e);
  }
  bool is_symmetric_K(const CSubProblem *sb) const {
    return PyPropertyMethods::is_symmetric_K(sb);
  }
  bool is_symmetric_C(const CSubProblem *sb) const  {
    return PyPropertyMethods::is_symmetric_C(sb);
  }
  bool is_symmetric_M(const CSubProblem *sb) const {
    return PyPropertyMethods::is_symmetric_M(sb);
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class PyEqnProperty : public EqnProperty,
		      public PyPropertyMethods,
		      public PyPhysicalPropertyMethods,
		      virtual public PythonNative<Property>
{
public:
  PyEqnProperty(PyObject *referent, PyObject *regstn,
		       const std::string &name);
  virtual ~PyEqnProperty();
  virtual void force_deriv_matrix(const FEMesh*, const Element*,
				  const Equation*,
				  const ElementFuncNodeIterator&,
				  const MasterPosition&,
				  double time, SmallSystem*) const;
  virtual void force_value(const FEMesh*, const Element*,
			   const Equation*, const MasterPosition&,
			   double time, SmallSystem*) const;
  virtual void first_time_deriv_matrix(const FEMesh*, const Element*,
				       const Equation*,
				       const ElementFuncNodeIterator&,
				       const MasterPosition&,
				       double time, SmallSystem*) const;
  virtual void second_time_deriv_matrix(const FEMesh*, const Element*,
				       const Equation*,
				       const ElementFuncNodeIterator&,
				       const MasterPosition&,
					double time, SmallSystem*) const;
  virtual void precompute(FEMesh *m) {
    PyPropertyMethods::py_precompute(m);
  }
  virtual void cross_reference(Material *m) { 
    PyPropertyMethods::py_cross_reference(m);
  }
  virtual void begin_element(const CSubProblem *sb, const Element *e) {
    PyPropertyMethods::py_begin_element(sb, e);
  }
  virtual void end_element(const CSubProblem *sb, const Element *e) {
    PyPropertyMethods::py_end_element(sb, e);
  }
  virtual void post_process(CSubProblem *sb, const Element *e) const {
    PyPropertyMethods::py_post_process(sb, e);
  }
  virtual bool constant_in_space() const {
    return PyPropertyMethods::py_constant_in_space();
  }
  virtual void output(FEMesh *m, const Element *e, 
		      const PropertyOutput *po,
		      const MasterPosition &p, OutputVal *ov)
  {
    PyPropertyMethods::py_output(m, e, po, p, ov);
  }
  virtual int integration_order(const CSubProblem *sb, const Element *e) const {
    return PyPhysicalPropertyMethods::py_integration_order(referent_, sb, e);
  }
  bool is_symmetric_K(const CSubProblem *sb) const {
    return PyPropertyMethods::is_symmetric_K(sb);
  }
  bool is_symmetric_C(const CSubProblem *sb) const  {
    return PyPropertyMethods::is_symmetric_C(sb);
  }
  bool is_symmetric_M(const CSubProblem *sb) const {
    return PyPropertyMethods::is_symmetric_M(sb);
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// TODO: Add PyAuxProperty?

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Data storage class for objects descended from PyFluxProperty or
// PyEqnProperty.

class PyPropertyElementData : public ElementData {
private:
  PyObject *_data;
  static std::string classname_;
public:
  PyPropertyElementData(const std::string &name, PyObject *dat);
  virtual ~PyPropertyElementData();
  virtual const std::string &classname() const { return classname_; }
  PyObject *data();
};


#endif // PYPROPERTYWRAPPER_H
