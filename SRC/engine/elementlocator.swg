// -*- C++ -*-
// $RCSfile: elementlocator.swg,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:40:44 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ELEMENTLOCATOR_SWG
#define ELEMENTLOCATOR_SWG

%module elementlocator

%include "engine/typemaps.swg"
%{
#include "engine/elementlocator.h"
#include "vtk-5.0/vtkPythonUtil.h"
#include "vtk-5.0/vtkDataSet.h"
#include "vtk-5.0/vtkGenericCell.h"
%}

class ElementLocator {
public:		     
  ElementLocator();
  
  
  %addmethods {
    void SetDataSet(PyObject* dataset) {
      self->SetDataSet(vtkDataSet::SafeDownCast(vtkPythonGetPointerFromObject(dataset, "vtkDataSet")));
    }

    void BuildLocator() {
      self->BuildLocator();
    }
    
    int getElementIdFromPoint(double x, double y, double z) {
      double p[3], q[3], dist2;
      int cellId = 0, subId = 0;
      p[0] = x;
      p[1] = y;
      p[2] = z;
      vtkIndent indent;
      vtkGenericCell *cell = vtkGenericCell::New();
      self->FindClosestPoint(p,q,cell,cellId,subId,dist2);
      return cellId;
    }	


    
  }
  
};

#endif //ELEMENTLOCATOR_SWG
		    
