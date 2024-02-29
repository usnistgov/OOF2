/*
Kevin Chang
August 26, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

gaborNugget.C

The class contained in this file is a self-contained unit that can apply the
Gabor Wavelet Filter to various types of images given the requisite inputs.
*/

#include "gaborNugget.h"

/*----------*/

gaborClass::gaborClass(double ain, double bin, int nin) {
  a = ain;
  b = bin;
  n = nin;
}

/*----------*/

grayImage gaborClass::run(const grayImage & imagein) {  // Apply the Gabor Wavelet Filter
  grayImage gaborImage;

  gaborImage = gabor(a, b, imagein, n);  // Creates the Gabor image (first step)

  /*
  // Save the image
  ofstream gaborOut("gabor");
  gaborImage.save(gaborOut);
  gaborOut.close();
  cout << "End: Gabor image saved to file 'gabor'" << endl;
  */

  return gaborImage;
}

/*----------*/

grayImage gaborClass::rawToImage(const grayImage &rawMaskedImage, double low, double high) {
  //      getMax(image[], int numImages)  // Scales the image; a new image is produced with 255 corresponding to "high" and
  //                                      // 0 corresponding to "low."  Values not contained by high and low become 255 or 0.

  int w = rawMaskedImage.width();
  int h = rawMaskedImage.height();
  grayImage maskedImage(w, h);
  double maxMaskValue = -999999.;
  double minMaskValue = 999999.;
  
  for (int a = 0; a < w; a++) {  // For all width
    for (int b = 0; b < h; b++) {  // For all height
      double mVal = rawMaskedImage[ICoord(a,b)];

      if (mVal > maxMaskValue)
	maxMaskValue = mVal;
      if (mVal < minMaskValue)
	minMaskValue = mVal;
    }
  }

  cout << "Max value in rawToImage is: " << maxMaskValue << endl;
  cout << "Min value in rawToImage is: " << minMaskValue << endl;
  double scale = 256./(maxMaskValue-minMaskValue);
  
  for (int i = 0; i < w; i++) {
    for (int j = 0; j < h; j++) {
      double tempValue = (rawMaskedImage[ICoord(i,j)] - minMaskValue) * scale;

      double color;
      if (tempValue > high)
        color = high;  // Sets out-of-bounds points to extrema
      else if (tempValue < low)
	color = low;  // Sets out-of-bounds points to extrema
      else
        color = (tempValue - low) * (255.0 / (high - low));  // Scaling formula
      maskedImage[ICoord(i,j)] = color;
    }
  }



  //TEST CODE

  int imageW = maskedImage.width();
  int imageH = maskedImage.height();

  for (int kevin = 0; kevin < imageW; kevin++) {
    for (int chang = 0; chang< imageH; chang++) {
      maskedImage[ICoord(kevin,chang)] = maskedImage[ICoord(kevin,chang)] / 256.0;
      //      cout << maskedImage[ICoord(kevin,chang)] << " ";
    }
    //    cout << endl;
  }

  //TEST CODE


  cout << "Raw image converted and scaled to 256 color grayscale." << endl;

  return maskedImage;
}

/*----------*/

grayImage gaborClass::getMax(grayImage image[], int numImages) {  // Finds the image with the highest value of each pixel and returns a composite of all the max pixels

  cout << "getMax beginning" << endl;

  int w = image[0].width(), h = image[0].height();
  grayImage temp(w,h);
  for (int a = 0; a < w; a++) {
    for (int b = 0; b < h; b++) {
      double max = -999999;
      for (int c = 0; c < numImages; c++) {
	if (image[c][ICoord(a,b)] > max) {
	  max = image[c][ICoord(a,b)];
	}
      }
      temp[ICoord(a,b)] = max;
    }
  }

  cout << "getMax done" << endl;

  return temp;
}

/*----------*/

grayImage gaborClass::applyRealGabor(int a, int b, const grayImage & image, int n) {  // Applies the Real Gabor Filter
  // gabor(a, b, image, n);  // What's this line here for?  What's the return value?

  ImageMask masks[40];
  grayImage images[40];
  // double p=1./(double)a/(double)b; p=1;  // Sets p, a double, to 1/a/b, then sets it to 1.  Why the first line?
  double p = 1.;

  for (int deg = 0, k = 0; deg < 180; deg += 180/n, k++) {
    masks[k].makeRealGabor(a,b,1./2./a,deg);
  }

  for (int c = 0; c < n; c++) {
    images[c]=masks[c].applyMask(image,p);
  }

  return (getMax(images, n));
}

/*----------*/

grayImage gaborClass::gabor(int a, int b, grayImage image, int n) {  // Image rawToImage(const grayImage &rawMaskedImage, int low,int high) 

  cout << "h,w" << image.height() << ", "<< image.width() << endl;

  return rawToImage(applyRealGabor(a, b, image, n), 0.0, 255.0);  // Image applyRealGabor(int a,int b,const grayImage & image, int n)
}

/*----------*/
