// -*- C++ -*-
// $RCSfile: clipimage3d.swg,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:40:41 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CLIPIMAGE3D_SWG
#define CLIPIMAGE3D_SWG

%module clipimage3d
%include "common/typemaps.swg"
%{
#include "engine/clipimage3d.h"
#include "vtk-5.0/vtkUnstructuredGridAlgorithm.h"
#include "vtk-5.0/vtkPolyDataAlgorithm.h"
#include "vtk-5.0/vtkPythonUtil.h"
#include "vtk-5.0/vtkAlgorithmOutput.h"
#include "vtk-5.0/vtkImplicitFunction.h"
#include "vtk-5.0/vtkUnstructuredGrid.h"
#include "vtk-5.0/vtkPointLocator.h"
#include "vtk-5.0/vtkImageData.h"
#include "vtk-5.0/vtkCell3D.h"
#include "vtk-5.0/vtkIdList.h"
#include "vtk-5.0/vtkDataObject.h"
%}

class ClipImage3D {

public:
	ClipImage3D();

  double getVolume();



	%addmethods {
		void SetInputConnection(PyObject *input) {
			self->SetInputConnection( 0, vtkAlgorithmOutput::SafeDownCast(vtkPythonGetPointerFromObject(input, "vtkAlgorithmOutput")) );	
		}

		void SetOutput(PyObject *output) {
			self->SetOutput( vtkDataObject::SafeDownCast(vtkPythonGetPointerFromObject(output, "vtkDataObject")) );
		}

		void Update() {
			self->Update();
		}

		PyObject* GetOutput() {
			return vtkPythonGetObjectFromPointer( self->GetOutput() );
		}

// 		void InsideOutOn() {
// 			self->InsideOutOn();
// 		}

// 		void SetClipFunction(PyObject* function) {
// 			self->SetClipFunction( vtkImplicitFunction::SafeDownCast(vtkPythonGetPointerFromObject(function, "vtkImplicitFunction")) );
// 		}

// 		void Mixed3DCellGenerationOff() {
// 			self->Mixed3DCellGenerationOff();
// 		}

// 	  PyObject* GetLocator() {
// 			return vtkPythonGetObjectFromPointer( self->GetLocator() );
// 		}

		// the points seem to be reset when converted to python
		//void setClipCell(PyObject *clipCell, PyObject *points) {
			//self->setClipCell(vtkCell3D::SafeDownCast(vtkPythonGetPointerFromObject(clipCell, "vtkCell3D")));
		//}
 
// 		void setClipCell(int npts, IntVec pts, PyObject *points) {
// 			vtkCell3D *clipCell_C = vtkCell3D::SafeDownCast(vtkCell3D::New()); 
// 			//vtkCell3D::SafeDownCast(vtkPythonGetPointerFromObject(clipCell, "vtkCell3D"));
// // 			vtkIdList *ptIds = vtkIdList::SafeDownCast(vtkPythonGetPointerFromObject(pts, "vtkIdList"));
// // 			vtkIndent indent;
// // 			ptIds->PrintSelf(cout, indent);
// // 			ptIds->WritePointer(0,8);
// // 			cout << "got pointer" << endl;
// 			vtkPoints *points_C = vtkPoints::SafeDownCast(vtkPythonGetPointerFromObject(points, "vtkPoints"));
// 			clipCell_C->Initialize(npts, pts, points_C);
// 			//Initialize (int npts, vtkIdType *pts, vtkPoints *p)
// 		  self->setClipCell(clipCell_C);
// 		}

// 		void setClipCell(PyObject *grid, int cellID) {
// 			self->setClipCell(vtkUnstructuredGrid::SafeDownCast(vtkPythonGetPointerFromObject(grid, "vtkUnstructuredGrid")), cellID);
// 		}


		// we have to pass the cell data from python this way so that the
		// point locations are preserved.  This is clunky, but will
		// probably only be used by the prototype code.
		void SetClipCell(PyObject *grid, int cellID) {
			vtkUnstructuredGrid *grid_C = vtkUnstructuredGrid::SafeDownCast(vtkPythonGetPointerFromObject(grid, "vtkUnstructuredGrid"));
			self->SetClipCell( vtkCell3D::SafeDownCast(grid_C->GetCell(cellID)) );
		}

		void SetIndexedImage(PyObject *image) {
// 			vtkImageData *cimage =  vtkImageData::SafeDownCast( vtkPythonGetPointerFromObject(image, "vtkImageData") );
// 			cout << "got pointer" << endl;
// 			vtkIndent indent;
// 			cimage->PrintSelf(cout, indent);
			self->SetIndexedImage( vtkImageData::SafeDownCast( vtkPythonGetPointerFromObject(image, "vtkImageData") ) );
		}

		void SetValue(int value) {
			self->SetValue(value);
		}


	}
};

#endif //CLIPIMAGE3D_SWG



