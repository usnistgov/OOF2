// -*- C++ -*-
// $RCSfile: resampleimage.swg,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:41:28 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef RESAMPLEIMAGE_SWG
#define RESAMPLEIMAGE_SWG

%module resampleimage
%include "common/typemaps.swg"
%{
#include "image/resampleimage.h"
#include "vtk-5.0/vtkPythonUtil.h"
#include "vtk-5.0/vtkAlgorithmOutput.h"
#include "vtk-5.0/vtkImageData.h"
  %}

class ResampleImage {
public:
  ResampleImage();
  // 	ResampleImage *New();
  void SetBitmap(BitmapOverlay *Bitmap);
  BitmapOverlay* GetBitmap();

  %addmethods {
    void SetInputConnection(PyObject* input) {
      self->SetInputConnection( 0, vtkAlgorithmOutput::SafeDownCast(vtkPythonGetPointerFromObject(input, "vtkAlgorithmOutput")) );
    }

    PyObject* GetOutput() {
      return vtkPythonGetObjectFromPointer( self->GetOutput() );
    }

    void RemoveAllInputs() {
      self->RemoveAllInputs();
    }

    int GetTotalNumberOfInputConnections() {
      return self->GetTotalNumberOfInputConnections();
    }

    int GetNumberOfInputConnections(int port) {
      return self->GetNumberOfInputConnections(port);
    }


    void Update() {
      self->Update();
    }

  }
};


#endif //RESAMPLEIMAGE_SWG
