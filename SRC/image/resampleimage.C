// -*- C++ -*-
// $RCSfile: resampleimage.C,v $
// $Revision: 1.4 $
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

// See vtkSimpleImageFilterExample.cxx

#include "common/coord.h"
#include "common/ccolor.h"
#include "image/resampleimage.h"

#include "vtk-5.0/vtkImageData.h"
#include "vtk-5.0/vtkObjectFactory.h"
#include "vtk-5.0/vtkImageProgressIterator.h"
#include "vtk-5.0/vtkInformation.h"
#include "vtk-5.0/vtkInformationVector.h"
#include "vtk-5.0/vtkObjectFactory.h"
#include "vtk-5.0/vtkStreamingDemandDrivenPipeline.h"

#include <math.h>


//----------------------------------------------------------------------------
ResampleImage::ResampleImage()
	:Bitmap(&Coord(0,0,0),&ICoord(0,0,0))
{
  this->SetNumberOfInputPorts(1);
  this->SetNumberOfOutputPorts(1);
}


//----------------------------------------------------------------------------
template <class T>
void ResampleImageExecute(ResampleImage *self, vtkImageData *inData, 
			  vtkImageData *outData, int extent[6], T* inPtr, T* outPtr)
{
  int idxX, idxY, idxZ, C=4;
  
  CColor tint = self->GetBitmap()->getFG();
  double alpha1 = self->GetBitmap()->getTintAlpha();
  double alpha2 = self->GetBitmap()->getVoxelAlpha();
  ICoord temp;
  
  for (idxZ = extent[4]; idxZ <= extent[5]; idxZ++){
    for (idxY = extent[2]; idxY <= extent[3]; idxY++){
      for (idxX = extent[0]; idxX <= extent[1]; idxX++){
	temp = ICoord(idxX,idxY,idxZ);
	if(self->GetBitmap()->get(&temp)) {
	  outPtr[0] = (unsigned char)(alpha1*255*tint.getRed()+(1-alpha1)*inPtr[0]);
	  outPtr[1] = (unsigned char)(alpha1*255*tint.getGreen()+(1-alpha1)*inPtr[1]);
	  outPtr[2] = (unsigned char)(alpha1*255*tint.getBlue()+(1-alpha1)*inPtr[2]);
	  outPtr[3] = (unsigned char)(255*log(101-100*alpha2)/log(101));
	}
	else {
	  outPtr[0] = inPtr[0];
	  outPtr[1] = inPtr[1];
	  outPtr[2] = inPtr[2];
	  outPtr[3] = inPtr[3];
	}
	outPtr+=C;
	inPtr+=C;
      }
    }		
  }
  
  // 	for(std::vector<ICoord>::iterator iter=self->GetBitmap()->pixels(1)->begin();
  // 			iter!=self->GetBitmap()->pixels(1)->end(); iter++) {
  
  
  
}

//----------------------------------------------------------------------------
void ResampleImage::SimpleExecute(vtkImageData* input,
				  vtkImageData* output)
{
  
  void* inPtr = input->GetScalarPointer();
  void* outPtr = output->GetScalarPointer();
  int extent[6];
  input->GetExtent(extent);
  
  switch(output->GetScalarType())
    {
      // This is simple a #define for a big case list. It handles
      // all data types vtk can handle.
      vtkTemplateMacro(
		       ResampleImageExecute( this,
					     input, output, extent,
					     (VTK_TT *)(inPtr), 
					     (VTK_TT *)(outPtr)));
    default:
      vtkGenericWarningMacro("Execute: Unknown input ScalarType");
      return;
    }
}
