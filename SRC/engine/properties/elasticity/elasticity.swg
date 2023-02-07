// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module(package="ooflib.SWIG.engine.properties.elasticity") elasticity

%{
#include "engine/properties/elasticity/elasticity.h"
%}

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/cijkl.swg"

%nodefaultctor Elasticity;

class Elasticity : public Property {
public:
  Cijkl cijkl(const FEMesh*, const Element*, const MasterPosition&);
};
