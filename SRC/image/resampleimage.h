// -*- C++ -*-
// $RCSfile: resampleimage.h,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2010/12/13 21:52:12 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */



#ifndef RESAMPLEIMAGE_H
#define RESAMPLEIMAGE_H

#include "vtk-5.0/vtkSimpleImageToImageFilter.h"
#include "vtk-5.0/vtkImageData.h"
#include "vtk-5.0/vtkPythonUtil.h"
#include "vtk-5.0/vtkObject.h"
#include "vtk-5.0/vtkObjectBase.h"
#include "vtk-5.0/vtkImageAlgorithm.h"
#include "vtk-5.0/vtkAlgorithm.h"
#include <vector>
#include "common/IO/bitoverlay.h"


// TODO 3D, MAYBE, SOMEDAY: Inherit from vtkThreadedImageAlgorithm instead

class VTK_IMAGING_EXPORT ResampleImage : public vtkSimpleImageToImageFilter

{
public:
// 	static ResampleImage *New();
	
	//protected:
	ResampleImage();
	~ResampleImage() {};

	void SetBitmap(BitmapOverlay *Bitmap) {this->Bitmap.copy(Bitmap);}
	BitmapOverlay* GetBitmap() {return &Bitmap;};

protected:

	void SimpleExecute(vtkImageData* input, vtkImageData* output);

	BitmapOverlay Bitmap;
	

private:
  ResampleImage(const ResampleImage&);  // Not implemented.
  void operator=(const ResampleImage&);  // Not implemented.

};

#endif //RESAMPLEIMAGE_H


