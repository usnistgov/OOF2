/*
Kevin Chang
August 26, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

imagemask.C

The class contained in this file provides helper functions for application of
the Gabor Wavelet Filter, for which the main functions are in gaborNugget.

Defines a class of image masks, rectangular arrays of values that can be
convoluted onto an image
*/

#include "imagemask.h"

/*----------*/

ImageMask::ImageMask()  //default constructor
  //  :Array<double>(1,1), mean = 0., weightSum = 0.  {}
{
  weight = grayImage(1,1);
  mean = 0.;
  weightSum = 0.;
  srand(204);
}

/*----------*/

ImageMask::ImageMask(int w, int h)  //constructor
  //  :Array<double>(w,h), mean = 0., weightSum = 0.  {}
{
  weight = grayImage(w,h);
  mean = 0.;
  weightSum = 0.;
  srand(204);
}

/*----------*/

double ImageMask::getMaskValue(const grayImage &image, ICoord ic) {
  //returns the mask value on the image at a point specified by ic.

  int maskW = (*this).width();
  int maskH = (*this).height();
  int imageW = image.width();
  int imageH = image.height();
  int lowerLeftX = ic(0) - maskW / 2;
  int lowerLeftY = ic(1) - maskH / 2;
  double sum = 0.;
  double imageSum = 0.;
  double pixelSum = 0.;

  //calculate the mean of the image by summing up all pixel values.
  //Can be made more efficient by saving the sums from the previous
  //point and then simply adding the difference between the new 
  //column and the old column

  double pixelValue = 0.;
  double convertMe = 0.;

  double imageMean = imageSum / weightSum;

  for (int u = 0; u < maskW; u++) {
    for (int v = 0; v < maskH; v++) {
      int llxu = lowerLeftX + u;
      int llyv = lowerLeftY + v;
      if (llxu < 0)
        llxu *= -1;
      if (llyv < 0)
        llyv *= -1;
      if(llxu >= imageW)
        llxu -= imageW;
      if(llyv >= imageH)
        llyv -= imageH;
      pixelValue = image[ICoord(llxu, llyv)];

      sum += ((*this)[ICoord(u,v)] - weight[ICoord(u,v)] * mean) * (pixelValue - imageMean);
    }
  }

  return fabs(sum);
}

/*----------*/

void ImageMask::output() {
  int maskW, maskH;
  maskW = (*this).width();
  maskH = (*this).height();
  cout << "Mask is " << maskW << "x" << maskH << endl;
//   for (int a = maskH - 1; a >= 0; a--) {
//     for (int b = 0; b < maskW; b++)
//       cout << (int) (1000*(*this)[ICoord(b,a)])/1000. << " ";
//     cout << endl;
//   }
  return;
}

/*----------*/

void ImageMask::define() {
  int maskW, maskH;
  cout << "Mask Width: ";
  cin >> maskW;
  cout << endl;
  cout << "Mask Height: ";
  cin >> maskH;
  cout << endl;
  (*this).resize(ICoord(maskW,maskH));
  cout<<"Enter mask values (across rows): "<<endl;
  for (int a = 0; a < maskH; a++) {
    for (int b = 0; b < maskW; b++) {
      cin>>(*this)[ICoord(b,a)];
      cout<<" ";
    }
    cout<<endl;
  }
  (*this).output();
  return;
}

/*----------*/

grayImage ImageMask::applyMask(const grayImage &image, double n) {
  int w = image.width();
  int h = image.height();

  grayImage rawMaskedImage(w,h);

  //  /*
  for (int silver = 0; silver < w; silver++)
    for (int chips = 0; chips < h; chips++)
      rawMaskedImage[ICoord(silver,chips)] = image[ICoord(silver,chips)];
  //  */

  for (int g = 0; g < w; g++) {
    for (int i = 0; i < h; i++) {
      double mVal = getMaskValue(image, ICoord(g,i));  // * n;
      rawMaskedImage[ICoord(g,i)] = mVal;
    }
  }

  cout << "Raw image mask pixel values calculated." << endl;

  return rawMaskedImage;
}

/*----------*/

grayImage ImageMask::applyMaskArray(const grayImage &image, double n) {
  int w = image.width();
  int h = image.height();

  grayImage rawMaskedArray(w,h);

  for (int g = 0; g < w; g++) {
    for (int i = 0; i < h; i++) {
      double mVal = (*this).getMaskValue(image, ICoord(g, i)) * n;
      rawMaskedArray[ICoord(g,i)] = mVal;
    }
  }

  cout << "Raw array mask pixel values calculated." << endl;
  return rawMaskedArray;
}

/*----------*/

void ImageMask::loadMask(ifstream &file) {
  int maskW, maskH;
  file >> maskW >> maskH;
  (*this).resize(ICoord(maskW,maskH));
  weight.resize(ICoord(maskW,maskH));
  for (int a = maskH - 1; a >= 0; a--) {
    for (int b = 0; b < maskW; b++) {
      file >> (*this)[ICoord(b,a)];
      weight[ICoord(b,a)]=1;
    }
  }
  weightSum = maskW*maskH;
  //calculate mean of mask
  double sum = 0.;

  int width = (*this).width();
  int height = (*this).height();

  for (int c = 0; c < width; c++) {
    for (int d = 0; d < height; d++) {
      sum+=(*this)[ICoord(c,d)];
    }
  }
  mean=sum/((double)maskH*maskW);
  cout<<"Mean is "<<mean<<endl;
  cout<<"File loaded."<<endl;
}

/*----------*/

void ImageMask::saveMask(ofstream &file) {
  int maskW,maskH;

  maskW = (*this).width();
  maskH = (*this).height();

  file << maskW << " " << maskH << endl;

  for (int a = maskH - 1; a >= 0; a--) {
    for (int b = 0; b < maskW; b++) {
      file << (*this)[ICoord(b,a)] << " ";
      file << " ";
    }
  file << endl;
  }
  cout << "File saved." << endl;
}

/*----------*/

void ImageMask::makeRealGabor(double a, double b, double w, double phi) {
  phi *= M_PI/180.0;
  int size;
  if (a > b)
    size = (int)a;
  else
    size = (int)b;
  cout << a << " " << b << endl;
  size *= 2;
  size++;

  resize(ICoord(size,size));
  weight.resize(ICoord(size,size));
  for (int x=-size/2;x<=size/2;x++) {
    for (int y=-size/2;y<=size/2;y++) {
      double r=sqrt(x*x+y*y);
      double theta;
      theta=atan2(y,x);

      double xp=x*cos(phi)+y*sin(phi);
      double yp=y*cos(phi)-x*sin(phi);
      weight[ICoord(x+size/2,y+size/2)]=exp((-1*M_PI*(xp*xp/a/a+yp*yp/b/b)));  // The famous Gabor filter equations
      (*this)[ICoord(x+size/2,y+size/2)]=exp((-1*M_PI*(xp*xp/a/a+yp*yp/b/b)))*cos(2*M_PI*w*r*cos(theta-phi));
    }
  }

  //calculate mean of mask
  double sum=0.;
  double reidSum = 0.;
  weightSum=0.;
  for (int c = 0; c < (*this).width(); c++) {
    for (int d = 0; d < (*this).height();d++) {
      cout << (*this)[ICoord(c,d)] << " ";
      sum+=(*this)[ICoord(c,d)];
      reidSum += (*this)[ICoord(c,d)] * weight[ICoord(c,d)];
      weightSum+=weight[ICoord(c,d)];
    }

    cout << endl;

  }

  mean=sum/weightSum;
  weightedMean = reidSum/weightSum;

  cout << "Real mean is: " << mean << endl;
  cout << "Weighted mean is " << weightedMean << endl;
  cout << "Real weight sum is: " << weightSum << endl;

  cout << "End makeRealGabor" << endl;

  return;
}

/*----------*/

void ImageMask::makeImagGabor(double a, double b, double w, double phi) {
  phi *= M_PI/180.;
  int size;
  if (a > b)
    size = (int)a;
  else
    size = (int)b;
  cout << a << " " << b << endl;
  size *= 2;
  size++;

  resize(ICoord(size,size));
  weight.resize(ICoord(size,size));

  for (int x = -size/2; x <= size / 2; x++) {
    for (int y = -size/2; y <= size / 2; y++) {
      double r = sqrt(x * x + y * y);
      double theta;
      theta = atan2(y,x);

      double xp = x*cos(phi)+y*sin(phi);
      double yp = y*cos(phi)-x*sin(phi);
      weight[ICoord(x+size/2,y+size/2)] = exp((-1*M_PI*(xp*xp/a/a+yp*yp/b/b)));
      (*this)[ICoord(x+size/2,y+size/2)] = exp((-1*M_PI*(xp*xp/a/a+yp*yp/b/b)))*sin(2*M_PI*w*r*cos(theta-phi));
    }
  }
  //calculate mean of mask
  double sum=0.;
  weightSum=0.;
  for (int c = 0; c < (*this).width(); c++) {
    for (int d = 0; d < (*this).height(); d++) {
      sum += (*this)[ICoord(c,d)]; 
      weightSum += weight[ICoord(c,d)];
    }
  }
  mean = sum / weightSum;
  cout << "Imag mean is: " << mean << endl;
  cout << "Imag weight sum is: "<< weightSum << endl;
  return;
}
