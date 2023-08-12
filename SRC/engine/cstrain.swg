// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CSTRAIN_SWG
#define CSTRAIN_SWG

%module(package="ooflib.SWIG.engine") cstrain

%include "common/typemaps.swg"
%import "engine/IO/propertyoutput.swg"

%{
#include "engine/cstrain.h"
#include "engine/IO/propertyoutput.h"
#include "engine/symmmatrix.h"
%}


class POInitGeometricStrain : public PropertyOutputValInit {
public:
  POInitGeometricStrain();
};

%newobject getGeometricStrain;

%inline %{
  SymmMatrix3 *getGeometricStrain(const FEMesh *mesh, const Element *el,
				  const MasterPosition &pos, bool nonlinear)
  {
    SymmMatrix3 *strain = new SymmMatrix3();
    findGeometricStrain(mesh, el, pos, strain, nonlinear);
    return strain;
  }
%}

%pythoncode "engine/cstrain.spy"

#endif // CSTRAIN_SWG
