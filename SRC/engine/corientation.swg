// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CORIENTATION_SWG
#define CORIENTATION_SWG

%module(package="ooflib.SWIG.engine") corientation

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/fieldindex.swg"
%import "engine/outputval.swg"
%import "engine/IO/propertyoutput.swg"
#endif // NOSECONDIMPORTS

PYTHONEXPORTABLE(FieldIndex);

%{
#include "engine/corientation.h"
#include "common/tostring.h"
%}

%nodefaultctor COrientation;

class COrientation : public NonArithmeticOutputVal {
public:
  ~COrientation();
  COrientABG abg();
  COrientBunge bunge();
  COrientQuaternion quaternion();
  COrientX X();
  COrientXYZ XYZ();
  COrientAxis axis();
  COrientRodrigues rodrigues();
  double misorientation(COrientation&, char*);
  ComponentsP components();
};

%extend COrientation {
  bool __eq__(COrientation *other) {
    return self->abg() == other->abg();
  }
  bool __ne__(COrientation *other) {
    return self->abg() != other->abg();
  }
};

// OIndex is a template defined in corientation.h.  I think that we
// should be able to swig the instantiated templates like this:
//   template <class ORIENT> class OIndex : public FieldIndex {};
//   %nodefaultctor OIndex<COrientABG>;
//   %template(OIndex_COrientABG) OIndex<COrientABG>;
// which would create a python class called OIndex_whatever for each
// COrientation class whatever.  However, that doesn't work (at least
// with swig 4.1.0).  When I tried it,
// PythonExportable::pythonObject() returned a swig object of unknown
// type.  So instead, this macro does it the ugly way, hiding the
// template from swig.

%define ORIENTATION_INDEX(CLASS)
 // Create a swigged class named OIndex_CLASS that stands in for OIndex<CLASS>
  %{
  typedef OIndex<CLASS> OIndex_##CLASS;
  %}
  %nodefaultctor OIndex_##CLASS;
  class OIndex_##CLASS : public FieldIndex {};
%enddef

ADD_REPR_GENERIC(COrientation);

class COrientABG : public COrientation {
public:
  COrientABG(double, double, double);
  ~COrientABG();
  double alpha();
  double beta();
  double gamma();
};

%extend COrientABG {
  COrientABG __neg__() {
    return -(*self);
  }
};

ADD_REPR_GENERIC(COrientABG);
ORIENTATION_INDEX(COrientABG);

class COrientBunge : public COrientation {
public:
  COrientBunge(double, double, double);
  ~COrientBunge();
  double phi1();
  double theta();
  double phi2();
};

ADD_REPR_GENERIC(COrientBunge);
ORIENTATION_INDEX(COrientBunge);

class COrientQuaternion : public COrientation {
public:
  COrientQuaternion(double, double, double, double);
  ~COrientQuaternion();
  double e0() const;
  double e1() const;
  double e2() const;
  double e3() const;
};

ADD_REPR_GENERIC(COrientQuaternion);
ORIENTATION_INDEX(COrientQuaternion);

class COrientX : public COrientation {
public:
  COrientX(double, double, double);
  ~COrientX();
  double phi();
  double theta();
  double psi();
};

ADD_REPR_GENERIC(COrientX);
ORIENTATION_INDEX(COrientX);

class COrientXYZ : public COrientation {
public:
  COrientXYZ(double, double, double);
  ~COrientXYZ();
  double phi();
  double theta();
  double psi();
};

ADD_REPR_GENERIC(COrientXYZ);
ORIENTATION_INDEX(COrientXYZ);

class COrientAxis : public COrientation {
public:
  COrientAxis(double, double, double, double);
  ~COrientAxis();
  double angle();
  double x();
  double y();
  double z();
};

ADD_REPR_GENERIC(COrientAxis);
ORIENTATION_INDEX(COrientAxis);

class COrientRodrigues : public COrientation {
public:
  COrientRodrigues(double, double, double);
  ~COrientRodrigues();
  double r1();
  double r2();
  double r3();
};

ADD_REPR_GENERIC(COrientRodrigues);
ORIENTATION_INDEX(COrientRodrigues);

class OrientationPropertyOutputInit : public NonArithmeticPropertyOutputInit {
public:
  OrientationPropertyOutputInit();
};

%pythoncode "engine/corientation.spy"

#endif	// CORIENTATION_SWG
