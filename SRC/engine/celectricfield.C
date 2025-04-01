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

#include "common/doublevec.h"
#include "engine/celectricfield.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/field.h"
#include "engine/mastercoord.h"
#include "engine/outputval.h"

void findElectricField(const FEMesh *mesh, const Element *element,
		       const MasterPosition &pos, DoubleVec &efield)
{
  static const ScalarField *voltage =
    dynamic_cast<ScalarField*>(Field::getField("Voltage"));
  static const Field *voltage_z = voltage->out_of_plane();

  for(int j=0; j<DIM; ++j) {
    ArithmeticOutputValue vderiv =
      element->outputFieldDeriv(mesh, *voltage, j, pos);
    efield[j] = -vderiv[ScalarFieldIndex()];
  }
  bool inplane = voltage->in_plane(mesh);
  if(!inplane) {
    ArithmeticOutputValue vz = element->outputField(mesh, *voltage_z, pos);
    efield[2] = -vz[ScalarFieldIndex()];
  }
}

void findElectricFieldRate(const FEMesh *mesh, const Element *element,
			   const MasterPosition &pos, DoubleVec &erate)
{
  static const ScalarField *voltage =
    dynamic_cast<ScalarField*>(Field::getField("Voltage"));
  static const Field *vrate = voltage->time_derivative();
  static const Field *vzrate = voltage->out_of_plane_time_derivative();

  for(int j=0; j<DIM; ++j) {
    ArithmeticOutputValue vderiv =
      element->outputFieldDeriv(mesh, *vrate, j, pos);
    erate[j] = -vderiv[ScalarFieldIndex()];
  }
  bool inplane = voltage->in_plane(mesh);
  if(!inplane) {
    ArithmeticOutputValue vz = element->outputField(mesh, *vzrate, pos);
    erate[2] = -vz[ScalarFieldIndex()];
  }
}


