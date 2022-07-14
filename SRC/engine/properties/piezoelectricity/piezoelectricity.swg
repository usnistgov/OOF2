// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef PIEZOELECTRICITY_SWG
#define PIEZOELECTRICITY_SWG

%module(package="ooflib.SWIG.engine.properties.piezoelectricity") piezoelectricity

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"
%import "engine/rank3tensor.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/properties/piezoelectricity/piezoelectricity.h"
%}

//%pragma(python) code="from ooflib.SWIG.engine.symmmatrix import SymmMatrix3Ptr"
//%pragma(python) code="from ooflib.SWIG.engine.rank3tensor import Rank3TensorPtr"


class IsotropicPiezoElectricity : public Property {
public:
  IsotropicPiezoElectricity(PyObject *reg, char *name, double d);
};


class AnisotropicPiezoElectricity : public Property {
public:
  AnisotropicPiezoElectricity(PyObject *registry, char *name,
			      Rank3Tensor *dijkTensor);
  Rank3Tensor dijk();
};

%pythoncode "engine/properties/piezoelectricity/piezoelectricity.spy"

#endif // PIEZOELECTRICITY
