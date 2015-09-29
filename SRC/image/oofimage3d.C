// -*- C++ -*-
// $RCSfile: oofimage3d.C,v $
// $Revision: 1.6 $
// $Author: langer $
// $Date: 2014/09/27 21:41:27 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include <Python.h>
#include "image/oofimage3d.h"
#ifdef HAVE_MPI
#include "common/mpitools.h"
#endif ////HAVE_MPI
#include "common/IO/bitoverlay.h"
#include "common/ooferror.h"
#include <math.h>
#include <set>
#include "vtk-5.0/vtkImageReader2.h"
#include "vtk-5.0/vtkPNMReader.h"
#include "vtk-5.0/vtkJPEGReader.h"
#include "vtk-5.0/vtkTIFFReader.h"
#include "vtk-5.0/vtkPNGReader.h"
#include "vtk-5.0/vtkImageConstantPad.h"
#include "vtk-5.0/vtkImageChangeInformation.h"
#include "vtk-5.0/vtkImageExtractComponents.h"
#include "vtk-5.0/vtkImageAppendComponents.h"
#include "vtk-5.0/vtkImageGaussianSmooth.h"
#include "vtk-5.0/vtkImageLuminance.h"
#include "vtk-5.0/vtkImageFlip.h"
#include "vtk-5.0/vtkPNMWriter.h"
#include "vtk-5.0/vtkMetaImageWriter.h"
#include "vtk-5.0/vtkImageMathematics.h"
#include "vtk-5.0/vtkImageMedian3D.h"
#include "vtk-5.0/vtkImageThreshold.h"
#include "vtk-5.0/vtkImageShiftScale.h"
#include "vtk-5.0/vtkPicker.h"
#include "vtk-5.0/vtkVolume.h"
#include "vtk-5.0/vtkFixedPointVolumeRayCastMapper.h"
#include "vtk-5.0/vtkVolumeProperty.h"
#include "vtk-5.0/vtkPiecewiseFunction.h"
#include "vtk-5.0/vtkVolumeProperty.h"
#include "vtk-5.0/vtkColorTransferFunction.h"
#include "vtk-5.0/vtkDataSet.h"
#include "vtk-5.0/vtkPointData.h"


// get rid of this after debugging
#include <iostream>

OOFImage3D::OOFImage3D(const std::string &name, const std::string &format, const std::string &filepattern, int numfiles)
  : name_(name)
{

  vtkImageReader2 *imageReader;
  vtkIndent indent;
  int depth = numfiles;
  // the width and height seem to be set automatically
  int extent[6] = {0,0,0,0,0,depth-1};

  if(format.compare("pnm")==0 || format.compare("pbm")==0 || format.compare("ppm")==0) {
    imageReader = vtkPNMReader::New();
  }
  else if(format.compare("jpeg")==0) {
    imageReader = vtkJPEGReader::New();
  }
  else if(format.compare("tiff")==0) {
    imageReader = vtkTIFFReader::New();
  }  
  else if(format.compare("png")==0) {
    imageReader = vtkPNGReader::New();
  }
  else
    throw ErrSetupError("Incompatible image format: " + format);

  //cout << "imageReader refcount " << imageReader->GetReferenceCount() << endl;
  //imageReader->SetReferenceCount(1);
  //imageReader->UnRegister((vtkObjectBase*)imageReader->GetExecutive());
  //cout << "imageReader refcount " << imageReader->GetReferenceCount() << endl;
	
  imageReader->SetDataExtent(extent);
  imageReader->SetDataSpacing(1,1,1);
  imageReader->SetFilePattern( filepattern.c_str() );
  imageReader->SetDataScalarTypeToUnsignedChar();
  //cout << imageReader->GetReleaseDataFlag() << endl;
  //imageReader->ReleaseDataFlagOn();
  //imageReader->DebugOn();
  //cout << imageReader->GetReleaseDataFlag() << endl;
  //cout << "imageReader refcount " << imageReader->GetReferenceCount() << endl;


  image = imageReader->GetOutput();
  image->Update();
  pipeline.push_back(imageReader);
 
  // for certain image formats such as PNG, the bit depth may be
  // greater than 8 and the reader will return a vtkImageData object
  // with a scalar type other than unsigned char.  We need to scale
  // the data and make it an unsigned char type
  if(image->GetScalarType() != VTK_UNSIGNED_CHAR) {
    vtkImageShiftScale *shiftscale = vtkImageShiftScale::New();
    shiftscale->SetInput(image);
    shiftscale->SetShift(0);
    shiftscale->SetScale(255.0/image->GetScalarTypeMax());
    shiftscale->SetOutputScalarTypeToUnsignedChar();
    image = shiftscale->GetOutput();
    image->Update();
    pipeline.push_back(shiftscale);
  }


  //image->DebugOn();
  //cout << "image refcount " << image->GetReferenceCount() << endl;
  //image->Register(NULL);
  //cout << "image refcount " << image->GetReferenceCount() << endl;
  //image->SetSource(NULL);
  //cout << "image refcount " << image->GetReferenceCount() << endl;
  //imageReader->Delete();
  //cout << "image refcount " << image->GetReferenceCount() << endl;

  image = getRGBA();
  padImage(1);
  //image->PrintSelf(cout, indent);

  setup();

}

OOFImage3D::OOFImage3D(const std::string &name)
  : name_(name)
{
}

OOFImage3D::OOFImage3D(const std::string &name, const ICoord &isize,
		       const std::vector<unsigned short> *data) 
  : name_(name)
{
  image = vtkImageData::New();
  image->SetDimensions(isize(0),isize(1),isize(2));
  image->SetScalarTypeToUnsignedChar();
  image->SetNumberOfScalarComponents(3);
  image->AllocateScalars();

  int i,j,k;
  for (i=0; i<isize(0); i++) {
    for (j=0; j<isize(1); j++) {
      for (k=0; k<isize(2); k++) {			
	image->SetScalarComponentFromFloat(i,j,k,0,
					   (float)((*data)[3*(i*(isize(1))*(isize(2))+j*isize(2)+k)]));
	image->SetScalarComponentFromFloat(i,j,k,1,
					   (float)((*data)[3*(i*(isize(1))*(isize(2))+j*isize(2)+k)+1]));
	image->SetScalarComponentFromFloat(i,j,k,2,
					   (float)((*data)[3*(i*(isize(1))*(isize(2))+j*isize(2)+k)+2]));
      }
    }
  }	

  image->Update();
  image = getRGBA();
  padImage(1);

  setup();
}

void OOFImage3D::setSize(const Coord *sighs) {
  size_ = *sighs;
  if(sizeInPixels_ != size_){
    // We need to change the data spacing of the image object
    vtkImageChangeInformation *changer;
    double x_spacing, y_spacing, z_spacing;

    x_spacing = size_(0)/(double)sizeInPixels_(0);
    y_spacing = size_(1)/(double)sizeInPixels_(1);
    z_spacing = size_(2)/(double)sizeInPixels_(2);
    changer = vtkImageChangeInformation::New();
    changer->SetInputConnection(image->GetProducerPort());
    // TODO: check that all spacings are non-zero and throw error.
    if (!(x_spacing && y_spacing && z_spacing)) { cout << "zero spacing" << endl;}
    changer->SetOutputSpacing(x_spacing, y_spacing, z_spacing);
    image = changer->GetOutput();
    image->Update();
  }	


}

void OOFImage3D::setup() {
  // TODO: catch errors?
  int *sighs = image->GetDimensions();
  // subtract 1 because of padding
  sizeInPixels_ = ICoord(sighs[0]-1, sighs[1]-1, sighs[2]-1);
}

OOFImage3D::~OOFImage3D() 
{

  // TODO 3D: Figure out how to free the memory!  Waiting for response
  // on vtk mail list.
  //cout << "IN OOFIMAGE3D DESTRUCTOR" << endl;
  //cout << "pipeline size " << pipeline.size() << endl;
  vtkIndent indent;
  //cout << "image refcounts " << image->GetReferenceCount() << endl;
  pipeline_vector::iterator here = pipeline.begin(); 
  //image->UnRegister((*here));
  //(*here)->UnRegister(NULL);
  //(*here)->SetReferenceCount(1);
  //cout << "unregistered" << endl;
  //cout << (*here)->GetClassName() << " " << (*here)->GetReferenceCount() << endl;
  for( ;
      here != pipeline.end(); ++here)  {
    //cout << (*here)->GetClassName() << " " << (*here)->GetReferenceCount() << endl;
    //(*here)->RemoveAllInputs();
    //(*here)->ReleaseDataFlagOn();
    //cout << (*here)->GetClassName() << " " << (*here)->GetReferenceCount() << endl;
    (*here)->Delete();
    //cout << "after delete" << endl;
  }
  //cout << "image refcounts " << image->GetReferenceCount() << endl;
  //image->Delete();
  
}

// This is used by the image modifiers so that we may have a ring
// buffer.  One way to do this is to just doing a shallow copy on the
// image pointer.  The idea is that if we undo, we go back to an
// earlier point in the pipeline.  The bad thing is that the filters
// created past that point won't be deleted explicitly and if the copy
// image is deleted, the shared pipeline will be deleted.  OOF2 uses
// the image magick copy constructor, which presumably does a deep
// copy, so that's what we'll do here.  Then we can destroy that copy
// without worrying about the pipeline we have here...  TODO: rethink
// how to do this.  Do we want a ring buffer?  Or should we just move
// a pointer to the pipeline.
OOFImage3D *OOFImage3D::clone(const std::string &nm) const {
  OOFImage3D *copy = new OOFImage3D(nm);
  copy->image = vtkImageData::New();
  copy->image->DeepCopy(image);
  copy->setup();	 
  copy->size_ = size_;
  copy->setMicrostructure(microstructure);
  return copy;
}

// For now, save just writes the slices as pnms.  We
// might want to implement different formats later, but for now, this
// is a sensible default since it's something we can read in easily.
void OOFImage3D::save(const std::string &filepattern) {
  vtkPNMWriter *writer;
  writer = vtkPNMWriter::New();

  padImage(-1);
  vtkImageData *rgb = getRGB();

  writer->SetFilePattern(filepattern.c_str());
  writer->SetInputConnection(rgb->GetProducerPort());
  writer->Update();
  writer->Write();

}

std::vector<unsigned short> *OOFImage3D::getPixels() {
  int n = 3*sizeInPixels_(0)*sizeInPixels_(1)*sizeInPixels_(2);
  std::vector<unsigned short> *pxls = new std::vector<unsigned short>(n);
  // TODO: Clean up and use iterators
  int i,j,k;
  ICoord coord;
  for (i=0; i<sizeInPixels_(0); i++) {
    for (j=0; j<sizeInPixels_(1); j++) {
      for (k=0; k<sizeInPixels_(2); k++) {
	(*pxls)[3*(i*(sizeInPixels_(1))*(sizeInPixels_(2))+j*sizeInPixels_(2)+k)] = 
	  (unsigned short)(image->GetScalarComponentAsFloat(i,j,k,0));
	(*pxls)[3*(i*(sizeInPixels_(1))*(sizeInPixels_(2))+j*sizeInPixels_(2)+k)+1] = 
	  (unsigned short)(image->GetScalarComponentAsFloat(i,j,k,1));
	(*pxls)[3*(i*(sizeInPixels_(1))*(sizeInPixels_(2))+j*sizeInPixels_(2)+k)+2] = 
	  (unsigned short)(image->GetScalarComponentAsFloat(i,j,k,2));
      }
    }
  }
  return pxls;
}

OOFImage3D *newImageFromData(const std::string &name, const ICoord *isize,
			     const std::vector<unsigned short> *data)
{
  return new OOFImage3D(name, *isize, data);
}

const CColor OOFImage3D::operator[](const ICoord &c) const {
  return CColor(image->GetScalarComponentAsFloat(c(0),c(1),c(2),0)/255,
		image->GetScalarComponentAsFloat(c(0),c(1),c(2),1)/255,
		image->GetScalarComponentAsFloat(c(0),c(1),c(2),2)/255);

}

bool OOFImage3D::compare(const OOFImage3D &other, double tol) const {
  if (sizeInPixels_ != other.sizeInPixels_) return false;

  for(int i=0;i<sizeInPixels_(0);i++) {
    for(int j=0;j<sizeInPixels_(1);j++) {
      for(int k=0;j<sizeInPixels_(2);j++) {
	CColor c0 = (*this)[ICoord(i,j,k)];
	CColor c1 = other[ICoord(i,j,k)];
	if (!c0.compare(c1, tol))
	  return false;
      }
    }
  }
  return true;

}

void OOFImage3D::padImage(int amount) {
  // pad the image with extra voxels because of vtk off by 1
  // annoyance in calculating image bounds
  image->Update();
  int *currentextent = image->GetExtent();
  int newextent[6] = {0,0,0,0,0,0};
  vtkImageConstantPad *padder = vtkImageConstantPad::New();
  //cout << "padder refcount right after New " << padder->GetReferenceCount() << endl;
  
  // Be careful to not overwrite the extent in the current image.	
  for(int i = 1; i<7; i+=2) newextent[i]=currentextent[i]+amount;
  
  padder->SetInputConnection(image->GetProducerPort());
  //cout << "padder refcount right after adding input " << padder->GetReferenceCount() << endl;
  padder->SetOutputWholeExtent(newextent);
  padder->SetOutputNumberOfScalarComponents(4);
  // we want the constant to represent transparency in the fourth channel
  padder->SetConstant(255);
  pipeline.push_back(padder);
  
  image = padder->GetOutput();
  image->Update();	
  
}	


// Not sure we'll need these functions...
// vtkImageData* OOFImage3D::makeAlphaChannel() {
// 	vtkImageExtractComponents *extractor;
// 	vtkImageData *alpha;
// 	int *sighs;

// 	extractor = vtkImageExtractComponents::New();
// 	extractor->SetInputConnection(image->GetProducerPort());
// 	extractor->SetComponents(0);
// 	alpha = extractor->GetOutput();
// 	alpha->Update();
// 	sighs = alpha->GetDimensions();
// 	// TODO: more efficient way to do this?
// 	for(int i = 0; i<sighs[0]; i++) {
// 		for(int j = 0; j<sighs[1]; j++) {
// 			for(int k = 0; k<sighs[2]; k++) {
// 				alpha->SetScalarComponentFromFloat(i,j,k,0,0.0);
// 			}
// 		}
// 	}
// 	return alpha;
// }

void OOFImage3D::combineChannels(vtkImageData *color, vtkImageData *alpha){
  vtkImageAppendComponents *appender;
  appender = vtkImageAppendComponents::New();
  int numcomponents = color->GetNumberOfScalarComponents();
  if(numcomponents==1)
    for(int i = 0; i<3; i++) appender->AddInputConnection(color->GetProducerPort());
  if(numcomponents==3)
    appender->AddInputConnection(color->GetProducerPort());
  appender->AddInputConnection(alpha->GetProducerPort());
  image = appender->GetOutput();
  image->Update();

}

vtkImageData* OOFImage3D::getRGB() {
  // get a 3 channel RGB image from image of 1,2,3,or 4 channels
  vtkImageAppendComponents *appender;
  appender = vtkImageAppendComponents::New();
  vtkImageExtractComponents *extractor;
  extractor = vtkImageExtractComponents::New();
  vtkImageData *rgb;
  int numcomponents = image->GetNumberOfScalarComponents();

  switch(numcomponents) {
  case 1:
    for(int i = 0; i<3; i++) appender->AddInput(image);
    rgb = appender->GetOutput();
    break;
  case 2:
    extractor->SetInputConnection(image->GetProducerPort());
    extractor->SetComponents(0);
    for(int i = 0; i<3; i++) appender->AddInput(extractor->GetOutput());
    rgb = appender->GetOutput();
    break;
  case 3:
    rgb = image;
    break;
  case 4:
    extractor->SetInputConnection(image->GetProducerPort());
    extractor->SetComponents(0,1,2);
    rgb = extractor->GetOutput();
    //default --- throw error
  }
  rgb->Update();
  return rgb;

}

vtkImageData* OOFImage3D::getRGBA() {
  // get a 4 channel RGB image from image of 1,2,3,or 4 channels
  // and set the fourth channel to 0 (representing total opacity)
  int numcomponents = image->GetNumberOfScalarComponents();
  vtkImageAppendComponents *appender = vtkImageAppendComponents::New();
  vtkImageExtractComponents *extractor = vtkImageExtractComponents::New();
  vtkImageData *rgba;
  
  switch(numcomponents) {
  case 1:
    for(int i = 0; i<4; i++) appender->AddInput(image);
    rgba = appender->GetOutput();
    //pipeline.push_back(appender);
    break;
  case 2:
    extractor->SetInputConnection(image->GetProducerPort());
    extractor->SetComponents(0);
    for(int i = 0; i<4; i++) appender->AddInput(extractor->GetOutput());
    rgba = appender->GetOutput();
    //pipeline.push_back(extractor);
    //pipeline.push_back(appender);
    break;
  case 3:
    //cout << "extractor refcount " << extractor->GetReferenceCount() << endl;
    //cout << "appender refcount " << appender->GetReferenceCount() << endl;
    extractor->SetInputConnection(image->GetProducerPort());
    extractor->SetComponents(0);
    appender->AddInput(image);
    appender->AddInput(extractor->GetOutput());
    rgba = appender->GetOutput();
    pipeline.push_back(extractor);
    pipeline.push_back(appender);
    //cout << "extractor refcount " << extractor->GetReferenceCount() << endl;
    //cout << "appender refcount " << appender->GetReferenceCount() << endl;
    //cout << "rgba refcount " << rgba->GetReferenceCount() << endl;
    //rgba->Register(NULL);
    //cout << "rgba refcount " << rgba->GetReferenceCount() << endl;
    //rgba->SetSource(NULL);
    //cout << "extractor refcount " << extractor->GetReferenceCount() << endl;
    //cout << "appender refcount " << appender->GetReferenceCount() << endl;
    //cout << "rgba refcount " << rgba->GetReferenceCount() << endl;
    //appender->Delete();
    //extractor->Delete();
    break;
  case 4:
    rgba = image;
    break;
    //default --- throw error
  }
  rgba->Update();
  rgba->GetPointData()->GetScalars()->FillComponent(3,0);
  return rgba;

}

vtkImageData* OOFImage3D::getAlpha() {
  vtkImageExtractComponents *extractor;
  extractor = vtkImageExtractComponents::New();
  vtkImageData *alpha;
	
  extractor->SetInputConnection(image->GetProducerPort());
  extractor->SetComponents(3);
  alpha = extractor->GetOutput();

  alpha->Update();
  return alpha;
}


PyObject* OOFImage3D::getVolumeActor() {
  vtkFixedPointVolumeRayCastMapper *mapper;
  mapper = vtkFixedPointVolumeRayCastMapper::New();
  mapper->IntermixIntersectingGeometryOn();
  vtkIndent indent;
  image->Update();
  mapper->SetInputConnection(image->GetProducerPort());

  vtkVolumeProperty *volproperty;
  volproperty = vtkVolumeProperty::New();

  vtkColorTransferFunction *red;
  red = vtkColorTransferFunction::New();
  red->AddRGBSegment(0,0,0,0,255,1,0,0);
  volproperty->SetColor(0,red);
  vtkColorTransferFunction *green;
  green = vtkColorTransferFunction::New();
  green->AddRGBSegment(0,0,0,0,255,0,1,0);
  volproperty->SetColor(1,green);
  vtkColorTransferFunction *blue;
  blue = vtkColorTransferFunction::New();
  blue->AddRGBSegment(0,0,0,0,255,0,0,1);
  volproperty->SetColor(2,blue);
  vtkPiecewiseFunction *opacity;
  opacity = vtkPiecewiseFunction::New();
  opacity->AddSegment(0,1,255,0);
  volproperty->SetScalarOpacity(3,opacity);

  vtkVolume *volume;
  volume = vtkVolume::New();
  volume->SetMapper(mapper);
  volume->SetProperty(volproperty);

  return vtkPythonGetObjectFromPointer(volume);
}

// void OOFImage3D::addImageToPicker(PyObject* pypicker){
// 	vtkPicker *picker;
// 	picker = vtkPythonGetPointerFromObject(pypicker);
// }

void OOFImage3D::imageChanged() {
  ++timestamp;			// marks image as changed
}

void OOFImage3D::gray() {
  vtkImageData *rgb = getRGB();
  vtkImageData *alpha = getAlpha();
  vtkImageData *gray;
  vtkImageLuminance *luminance;

  luminance = vtkImageLuminance::New();

  luminance->SetInputConnection(rgb->GetProducerPort());
  gray = luminance->GetOutput();
  gray->Update();

  combineChannels(gray,alpha);
  imageChanged();

}

void OOFImage3D::threshold(double T) {
  vtkImageData *rgb = getRGB();
  vtkImageData *alpha = getAlpha();
  vtkImageData *gray;
  vtkImageLuminance *luminance;
  vtkImageThreshold *thold1, *thold2; 

  luminance = vtkImageLuminance::New();

  luminance->SetInputConnection(rgb->GetProducerPort());
  gray = luminance->GetOutput();
	
  thold1 = vtkImageThreshold::New();
  thold1->ThresholdByUpper(T*255);
  thold1->SetOutValue(0);
  thold1->SetInputConnection(gray->GetProducerPort());
	
  thold2 = vtkImageThreshold::New();
  thold2->ThresholdByLower(T*255);
  thold2->SetOutValue(255);
  thold2->SetInputConnection(thold1->GetOutputPort());

  gray = thold2->GetOutput();
  gray->Update();

  combineChannels(gray,alpha);
  imageChanged();

}

void OOFImage3D::blur(double radius, double sigma) {

  vtkImageGaussianSmooth *gauss;

  padImage(-1);

  gauss = vtkImageGaussianSmooth::New();
  gauss->SetRadiusFactors(radius, radius, radius);
  gauss->SetStandardDeviation(sigma, sigma, sigma);
  gauss->SetInputConnection(image->GetProducerPort());

  image = gauss->GetOutput();
	
  padImage(1);
	
  imageChanged();

}


void OOFImage3D::dim(double factor) {
  vtkImageData *rgb = getRGB();
  vtkImageData *alpha = getAlpha();
  vtkImageMathematics *dimmer;

  dimmer = vtkImageMathematics::New();
  dimmer->SetOperationToMultiplyByK();
  dimmer->SetConstantK(factor);
  dimmer->SetInputConnection(rgb->GetProducerPort());
  rgb = dimmer->GetOutput();
  rgb->SetScalarTypeToUnsignedChar();
  rgb->Update();
	
  combineChannels(rgb,alpha);
  imageChanged();

}

void OOFImage3D::fade(double factor) {
  vtkImageData *rgb = getRGB();
  vtkImageData *alpha = getAlpha();
  vtkImageMathematics *fade1, *fade2;

  fade1 = vtkImageMathematics::New();
  fade1->SetOperationToMultiplyByK();
  fade1->SetConstantK(1.0-factor);
  fade1->SetInputConnection(rgb->GetProducerPort());
	
  fade2 = vtkImageMathematics::New();
  fade2->SetOperationToAddConstant();
  fade2->SetConstantC(255*factor);
  fade2->SetInputConnection(fade1->GetOutputPort());
	
  rgb = fade2->GetOutput();
  rgb->SetScalarTypeToUnsignedChar();
  rgb->Update();
	
  combineChannels(rgb,alpha);
  imageChanged();

}

void OOFImage3D::negate(double dummy) {
  vtkImageData *rgb = getRGB();
  vtkImageData *alpha = getAlpha();
  vtkImageMathematics *negator, *corrector;

  negator = vtkImageMathematics::New();
  negator->SetOperationToMultiplyByK();
  negator->SetConstantK(-1.0);
  negator->SetInputConnection(rgb->GetProducerPort());

  corrector = vtkImageMathematics::New();
  corrector->SetOperationToAddConstant();
  corrector->SetConstantC(255);
  corrector->SetInputConnection(negator->GetOutputPort());

  rgb = corrector->GetOutput();
  rgb->SetScalarTypeToUnsignedChar();
  rgb->Update();
	
  combineChannels(rgb,alpha);
  imageChanged();

}

void OOFImage3D::medianFilter(int radius) {
  padImage(-1);
  vtkImageData *rgb = getRGB();
  vtkImageData *alpha = getAlpha();
  vtkImageMedian3D *median;
	
  median = vtkImageMedian3D::New();
  median->SetKernelSize(radius*2, radius*2, radius*2);
  median->SetInputConnection(rgb->GetProducerPort());
	
  rgb = median->GetOutput();
  rgb->Update();
	
  combineChannels(rgb,alpha);
  padImage(1);
  imageChanged();
}

void OOFImage3D::normalize() {
  padImage(-1);
  vtkImageData *alpha = getAlpha();
	
  vtkImageAppendComponents *appender;
  vtkImageExtractComponents *extractor[3];
  vtkImageMathematics *adder[3], *mult[3];
  double *minmax, K;

  appender = vtkImageAppendComponents::New();

  for(int i=0; i<3; i++) {

    extractor[i] = vtkImageExtractComponents::New();
    extractor[i]->SetInputConnection(image->GetProducerPort());
    extractor[i]->SetComponents(i);
    extractor[i]->Update();
		
    minmax = extractor[i]->GetOutput()->GetScalarRange();
		
    adder[i] = vtkImageMathematics::New();
    adder[i]->SetInputConnection(extractor[i]->GetOutputPort());
    adder[i]->SetOperationToAddConstant();
    if(minmax[0] > 0 && minmax[0] != minmax[1]) {
      adder[i]->SetConstantC(256-minmax[0]);
    }
    else{
      adder[i]->SetConstantC(0);
    }

    mult[i] = vtkImageMathematics::New();
    mult[i]->SetInputConnection(adder[i]->GetOutputPort());
    mult[i]->SetOperationToMultiplyByK();
    if(minmax[0]!=minmax[1]) {
      K = 255.0/(minmax[1]-minmax[0]);
      mult[i]->SetConstantK(K);
    }
    else {
      mult[i]->SetConstantK(1.0);
    }
    mult[i]->GetOutput()->SetScalarTypeToUnsignedChar();


    appender->AddInputConnection(mult[i]->GetOutputPort());

  }

  appender->AddInputConnection(alpha->GetProducerPort());
  image = appender->GetOutput();
  padImage(1);
  imageChanged();

}
	
void OOFImage3D::flip(const std::string &axis) {

  padImage(-1);
  vtkImageFlip *flipper[3];
	
  for(int i=0; i<axis.size(); i++) {
    flipper[i] = vtkImageFlip::New();
    flipper[i]->SetFilteredAxis((int)axis[i]-(int)'x');
    flipper[i]->SetInputConnection(image->GetProducerPort());
    image = flipper[i]->GetOutput();
  }

  image->Update();
  padImage(1);
  imageChanged();

}


// This is kind of slow for very large images.  It might make sense to
// have a progress bar.
void OOFImage3D::getColorPoints(const CColor &ref, 
				const ColorDifference &diff,
				BoolArray &selected)
  const
{
  //   for(ConstOOFImage3DIterator i=this->begin(); i!=this->end(); ++i)
  //     if (diff.contains(ref, *i)) selected[i.coord()] = true;

  int i,j,k;
  ICoord coord;
  for (i=0; i<sizeInPixels_(0); i++) {
    for (j=0; j<sizeInPixels_(1); j++) {
      for (k=0; k<sizeInPixels_(2); k++) {
	coord = ICoord(i,j,k);
	if (diff.contains(ref, operator[](coord))) selected[coord] = true;
      }
    }
  }

}





//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// OOFImage3D::iterator OOFImage3D::begin() {
//   return OOFImage3DIterator(*this, 0);
// }

// OOFImage3D::const_iterator OOFImage3D::begin() const {
//   return ConstOOFImage3DIterator(*this, 0);
// }

// OOFImage3D::iterator OOFImage3D::end() {
//   return OOFImage3DIterator(*this, sizeInPixels_(0)*sizeInPixels_(1)*sizeInPixels_(2));
// }

// OOFImage3D::const_iterator OOFImage3D::end() const {
//   return ConstOOFImage3DIterator(*this, sizeInPixels_(0)*sizeInPixels_(1)*sizeInPixels_(2));
// }


// ICoord OOFImage3DIterator::coord() const {
//   int width = image.sizeInPixels()(0);
//   int y = pos/width;
//   int x = pos - width*y;
//   return ICoord(x, y, 0);
// }

// ICoord ConstOOFImage3DIterator::coord() const {
//   int width = image.sizeInPixels()(0);
//   int y = pos/width;
//   int x = pos - width*y;
//   return ICoord(x, y, 0);
// }

// bool operator==(const OOFImage3DIterator &a, const OOFImage3DIterator &b) {
//   return a.pos == b.pos;
// }

// bool operator!=(const OOFImage3DIterator &a, const OOFImage3DIterator &b) {
//   return a.pos != b.pos;
// }


// bool operator==(const ConstOOFImage3DIterator &a, const ConstOOFImage3DIterator &b){
//   return a.pos == b.pos;
// }

// bool operator!=(const ConstOOFImage3DIterator &a, const ConstOOFImage3DIterator &b){
//   return a.pos != b.pos;
// }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
