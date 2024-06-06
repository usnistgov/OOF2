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

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"
%import "engine/rank3tensor.swg"

%{
#include "engine/properties/piezoelectricity/piezoelectricity.h"
%}

class IsotropicPiezoElectricity : public FluxProperty {
public:
  IsotropicPiezoElectricity(std::string &name, PyObject *reg, double d);
};


class AnisotropicPiezoElectricity : public FluxProperty {
public:
  AnisotropicPiezoElectricity(std::string &name, PyObject *reg,
			      Rank3Tensor *dijkTensor);
  Rank3Tensor dijk();
};

%pythoncode "engine/properties/piezoelectricity/piezoelectricity.spy"

#endif // PIEZOELECTRICITY
