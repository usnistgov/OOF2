// -*- C++ -*-
// $RCSfile: histogram.C,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2014/09/27 21:41:29 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/array.h"
#include "image/oofimage.h"
#include "common/doublearray.h"
#include <iostream>
#include <fstream>
#include <iomanip>

void printHistogram(const DoubleArray& image, int val) {
  
  int histogram[256];
  for(int a=0; a<256; a++)
    histogram[a]=0; //Initializes array.
  
  for(DoubleArray::const_iterator i=image.begin(); i!=image.end();++i) {
    //  std::cout<<i.coord()(0)<<" "<<i.coord()(1)<<std::endl;
    histogram[int(image[i]*val)]++;
  }

  std::ofstream outfile("histogram.txt");
  
  for(int j=0;j<=val;j++)
    outfile<<std::setprecision(2)<<std::setw(4)<<double(j)/double(val)<<" "<<histogram[j]<<std::endl;
  
}

/*
void createHistogram2(const OOFImage& image) {
  int histogram[256];
  for(int a=0;a<256; histogram[a]=0 && a++); //Initializes array.

  for(Array<double>::iterator i=image.begin(); i<image.end();i++) 
    histogram[int(image[i].gray()*255]]++;

  ofstream outfile;
  outfile.open("histogram.txt");

  for(int j=0;j<256;j++)
    outfile<<j<<" "<<histogram[j]<<endl;
}*/
