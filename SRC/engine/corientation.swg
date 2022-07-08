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

%module corientation
%include "common/typemaps.swg"
%import "engine/outputval.swg"
%import "engine/IO/propertyoutput.swg"

%{
#include "engine/corientation.h"
#include "common/tostring.h"
%}

// %pragma(python) code="from ooflib.SWIG.engine.outputval import NonArithmeticOutputValPtr"
// %pragma(python) code="from ooflib.SWIG.engine.IO.propertyoutput import NonArithmeticPropertyOutputInitPtr"

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

};

%extend COrientation {
  bool __eq__(COrientation *other) {
    return self->abg() == other->abg();
  }
  bool __ne__(COrientation *other) {
    return self->abg() != other->abg();
  }
};

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

class COrientBunge : public COrientation {
public:
  COrientBunge(double, double, double);
  ~COrientBunge();
  double phi1();
  double theta();
  double phi2();
};

ADD_REPR_GENERIC(COrientBunge);

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

class COrientX : public COrientation {
public:
  COrientX(double, double, double);
  ~COrientX();
  double phi();
  double theta();
  double psi();
};

ADD_REPR_GENERIC(COrientX);

class COrientXYZ : public COrientation {
public:
  COrientXYZ(double, double, double);
  ~COrientXYZ();
  double phi();
  double theta();
  double psi();
};

ADD_REPR_GENERIC(COrientXYZ);

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

class COrientRodrigues : public COrientation {
public:
  COrientRodrigues(double, double, double);
  ~COrientRodrigues();
  double r1();
  double r2();
  double r3();
};

ADD_REPR_GENERIC(COrientRodrigues);

class OrientationPropertyOutputInit : public NonArithmeticPropertyOutputInit {
public:
  OrientationPropertyOutputInit();
};

%pythoncode "engine/corientation.spy"

#endif	// CORIENTATION_SWG
