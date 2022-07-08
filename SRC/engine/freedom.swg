// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef FREEDOM_SWG
#define FREEDOM_SWG

%include "common/typemaps.swg"
%import "engine/femesh.swg"

%{
#include "engine/freedom.h"
%}

%nodefaultctor DegreeOfFreedom;

class DegreeOfFreedom {
public:
  double value(FEMesh*);
  int dofindex();
};

%extend DegreeOfFreedom {
  void increment(FEMesh *mesh, double x) {
    self->value(mesh) += x;
  }
};

#endif // FREEDOM_SWG
