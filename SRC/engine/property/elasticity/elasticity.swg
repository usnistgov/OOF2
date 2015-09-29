// -*- C++ -*-
// $RCSfile: elasticity.swg,v $
// $Revision: 1.14 $
// $Author: langer $
// $Date: 2009/12/30 21:36:06 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module elasticity

%{
#include "engine/property/elasticity/elasticity.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"
%extern "engine/property/elasticity/cijkl.swg"
%pragma(python) code="from ooflib.SWIG.engine.property.elasticity.cijkl import CijklPtr"
%pragma(python) include="elasticity.spy"

class Elasticity : public Property {
public:
  Cijkl cijkl(const FEMesh*, const Element*, const MasterPosition&);
};
