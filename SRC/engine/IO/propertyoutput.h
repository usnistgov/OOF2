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

#ifndef PROPERTYOUTPUT_H
#define PROPERTYOUTPUT_H

#include <Python.h>

class PropertyOutput;
class ArithmeticPropertyOutput;
class ArithmeticPropertyOutputInit;
class NonArithmeticPropertyOutput;
class NonArithmeticPropertyOutputInit;

#include "common/pythonexportable.h"
#include "engine/outputval.h"
#include <string>
#include <vector>

class ArithmeticOutputVal;
class ArithmeticOutputValue;
class NonArithmeticOutputVal;
class Element;
class FEMesh;
class MasterCoord;
class Property;

class PropertyOutputInit : public PythonExportable<PropertyOutputInit> {
private:
  static const std::string modulename_;
public:
  virtual ~PropertyOutputInit() {}
  virtual const std::string &modulename() const { return modulename_; }
  virtual PropertyOutput *instantiate(const std::string&, PyObject*) const = 0;
};

class ArithmeticPropertyOutputInit : public PropertyOutputInit {
private:
  static const std::string classname_; 
public:
  virtual const std::string &classname() const { return classname_; }
  virtual PropertyOutput *instantiate(const std::string&, PyObject*) const;
  virtual ArithmeticOutputVal *operator()(const ArithmeticPropertyOutput*,
					  const FEMesh*, const Element*,
					  const MasterCoord&) const = 0;
};

class NonArithmeticPropertyOutputInit : public PropertyOutputInit {
private:
  static const std::string classname_; 
public:
  virtual const std::string &classname() const { return classname_; }
  virtual PropertyOutput *instantiate(const std::string&, PyObject*) const;
  virtual NonArithmeticOutputVal *operator()(const NonArithmeticPropertyOutput*,
					     const FEMesh*, const Element*,
					     const MasterCoord&) const = 0;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class ScalarPropertyOutputInit : public ArithmeticPropertyOutputInit {
public:
  ScalarOutputVal *operator()(const ArithmeticPropertyOutput*,
				  const FEMesh*,
				  const Element*, const MasterCoord&) const;
};

class TwoVectorPropertyOutputInit : public ArithmeticPropertyOutputInit {
public:
  VectorOutputVal *operator()(const ArithmeticPropertyOutput*,
				  const FEMesh*,
				  const Element*, const MasterCoord&) const;
};

class ThreeVectorPropertyOutputInit : public ArithmeticPropertyOutputInit {
public:
  VectorOutputVal *operator()(const ArithmeticPropertyOutput*,
				  const FEMesh*,
				  const Element*, const MasterCoord&) const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class PropertyOutput : public PythonExportable<PropertyOutput> {
private:
  const std::string name_;
  PyObject* params_;
  const int index_;
  static const std::string modulename_;
public:
  PropertyOutput(const std::string &name, PyObject *params);
  virtual ~PropertyOutput();
  const std::string &name() const { return name_; }
  virtual const std::string &modulename() const { return modulename_; }
  int index() const { return index_; }
  // These functions retrieve the values of the Python parameters
  // defined in the PropertyOutputRegistration.  The 'name' argument
  // is the name of the parameter.  It's a char* because that's what
  // Python expects to get.
  double getFloatParam(const char *name) const;
  int getIntParam(const char *name) const;
  const std::string *getStringParam(const char *name) const;
  const std::string *getEnumParam(const char *name) const;
  const std::string *getRegisteredParamName(const char *name) const;
};

class ArithmeticPropertyOutput : public PropertyOutput {
private:
  static const std::string classname_;
public:
  ArithmeticPropertyOutput(const std::string &name, PyObject *params)
    : PropertyOutput(name, params)
  {}
  virtual const std::string &classname() const { return classname_; }
  std::vector<ArithmeticOutputValue> *evaluate(
			       FEMesh*, Element*,
			       const ArithmeticPropertyOutputInit*,
			       const std::vector<MasterCoord*>*);
};

class NonArithmeticPropertyOutput : public PropertyOutput {
private:
  static const std::string classname_;
public:
  NonArithmeticPropertyOutput(const std::string &name, PyObject *params)
    : PropertyOutput(name, params)
  {}
  virtual const std::string &classname() const { return classname_; }
  std::vector<NonArithmeticOutputValue> *evaluate(
			     FEMesh*, Element*,
			     const NonArithmeticPropertyOutputInit*,
			     const std::vector<MasterCoord*>*);
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The bare PropertyOutputRegistration defined here should not be used
// directly.  propertyoutputreg.py defines some Python classes derived
// from PropertyOutputRegistration that should be used instead.  Those
// do useful things like create actual Output objects of the correct
// type, and handle the registration's parameters.

class PropertyOutputRegistration {
private:
  const std::string name_;
  const int index_;
  const PropertyOutputInit *initializer_;
  static std::vector<PropertyOutputRegistration*> &allPropertyOutputRegs();
public:
  PropertyOutputRegistration(const std::string &name,
			     const PropertyOutputInit *init);
  const std::string &name() const { return name_; }
  int index() const { return index_; }
  PropertyOutput *instantiate(PyObject *params) const {
    return initializer_->instantiate(name_, params);
  }
  const PropertyOutputInit *initializer() const { return initializer_; }

  friend PropertyOutputRegistration *getPropertyOutputReg(const std::string&);
  friend int nPropertyOutputRegistrations();
};

PropertyOutputRegistration *getPropertyOutputReg(const std::string&);
int nPropertyOutputRegistrations();

#endif // PROPERTYOUTPUT_H
