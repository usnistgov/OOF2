// -*- C++ -*-
// $RCSfile: hough.C,v $
// $Revision: 1.6 $
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

#include <math.h>

#include "hough.h"
#include "common/array.h"
#include "common/boolarray.h"
#include "common/intarray.h"
#include "common/doublearray.h"
#include "image/oofimage.h"
#include "imageops.h"
#include "image/SEGMENTATION/imageops.h"


/**********************************************************************
   Currently, this file has the functions needed to apply a hough transform to
an image, however choosing peaks of the resulting transformed image doesn't
work. There is also no function to turn a point in hough space back into the
desired segment on the original image. Two simple equations can be used to
calculate the point (x,y) where the perpendicular line intersects the desired
segment as well as the angle of the desired line form the horizontal, but
deciding where to begin the segment and when to end it is more complicated. 
   The current idea for applying the hough transform is to only use it around 
endpoints of real edges in the image.
***********************************************************************/


bool isEnd(const BoolArray &image, const ICoord pt)
{
//This function checks if a point is an endpoint. This is the same function as
//isDiscontinuous in connectEdge.C

  if(pt(0)==84 && pt(1)==0)
    std::cout<<"in End "<<image[pt]<<std::endl;
  if(image[pt]==0 || pt(0)==0 || pt(0)==image.width()-1 || pt(1)==0 || pt(1)==image.height()-1)
    return false;
  int p1=image[ICoord(pt(0)-1,pt(1)+1)];
  int p2=image[ICoord(pt(0),pt(1)+1)];
  int p3=image[ICoord(pt(0)+1,pt(1)+1)];
  int p4=image[ICoord(pt(0)-1,pt(1))];
  int p6=image[ICoord(pt(0)+1,pt(1))];
  int p7=image[ICoord(pt(0)-1,pt(1)-1)];
  int p8=image[ICoord(pt(0),pt(1)-1)];
  int p9=image[ICoord(pt(0)+1,pt(1)-1)];
  
  

  int numNonZero=0;
  
  for(int a=-1;a<=1;a++)
    for(int b=-1;b<=1;b++)
      numNonZero+=image[pt+ICoord(a,b)];
  if(numNonZero==1 || numNonZero==2)
    return true;
  
  int compVal=p1 + 2*p2 + 4*p3 + 8*p4 + 16*p6 + 32*p7 + 64*p8 + 128*p9;
  if(compVal==3 || compVal==6 || compVal==96 || compVal==192 || compVal==20
     || compVal==9 || compVal==40 || compVal==144)
    return true;
  return false;
}

DoubleArray hough(const BoolArray &image, const ICoord& start, const ICoord& end) {
/* This function performs a hough transform on the given portion of a given
   image. The ICoords start and end define the box to be transformed
*/

  //start is lower left corner, end is upper right corner of small box

  //IntArray imagePart(ICoord(width,width),0);
  DoubleArray accumulator(end(1)-start(1)+end(0)-start(0),361);
  ICoord cur;
  int x,y;
  double radius;
  double cosAngles[361];
  double sinAngles[361];
  int cellsize=1; //size of box surrounding a cell to increment.

  for(int angle1 = 0; angle1<=360; angle1++) {
    double tempAngle = angle1*M_PI/180.;
    cosAngles[angle1] = cos(tempAngle);
    sinAngles[angle1] = sin(tempAngle);
    //std::cout<<angle1<<":"<<cosAngles[angle1]<<" "<<sinAngles[angle1]<<std::endl;
  }

//  for(BoolArray::const_iterator i=image.begin(); i!=image.end();++i) {
//  std::cout<<"START LOOP"<<std::endl;

  for(ICoord i=start; i!=end;){
  //    std::cout<<i(0)<<" "<<i(1)<<")))))))))"<<image.width()<<" "<<image.height()<<std::endl;
    //cur=i.coord();
    x=i(0)-start(0); y=i(1)-start(1);
   /* if(isEnd(image,cur)) { //if this point is an endpoint
      //find lines created with it
    }*/
    //   if(i.coord()(1)<110 && i.coord()(0)<170 && i.coord()(1)>50 && i.coord()(0)>50) {
    if(image[i]) {
      //Start turning the point into Hough spacesmall
      //r=x cos t + y sin t
      for(int angle = 0; angle<=360; angle++) {
	radius=x*cosAngles[angle] + y*sinAngles[angle];
      //	if(i.coord()(0)==167 && i.coord()(1)==101)
      //	  std::cout<<radius<<" ";
	if(radius>0 
) {
          for(int a=-cellsize/2;a<=cellsize/2; a++) {
	    if(radius+a>=0 && /*radius+a<= */angle+a>=0 && angle+a<=360) {
	      //  std::cout<<"before accum"<<std::endl;
	    //	      std::cout<<"R "<<int(radius)+a<<" "<<angle+a<<std::endl;
	      accumulator[ICoord(int(radius)+a,angle+a)]++;
	    //	      std::cout<<"after accum"<<std::endl;
	      //      if(i.coord()(1)<110 && i.coord()(0)<170 && i.coord()(1)>50 && i.coord()(0)>50)
	      //	std::cout<<angle<<","<<radius<<"   ";
	    }
	  }
	}
      }
    }
    //   }
    if(i(0)<end(0))
      i(0)++;
    else {
      i(0)=start(0);
      i(1)++;
    }
  }

  OOFImage tempIm("hough",Coord(0,0),Magick::Geometry(accumulator.width(),accumulator.height()));
  accumulator = scaleArray(accumulator,0.0,1.0,1);
  setFromArray(tempIm,accumulator);
  tempIm.save("houghResults.jpg");

  return accumulator;
}

void findPeaks(const DoubleArray &array, const int numPeaks)
{
/* Using the accumulator from the hough transform of the image, this function
   looks for peaks in the array. The function is not yet finished, since the
   current method used for finding the peaks is not very good. Later, the
   top X (to be determined) peaks will be used and fit back onto the real image.
   This can either be done by returning the ICoords of the peaks in an array,
   or the function for converting hough to normal space can be called in this
   function as soon as the peaks are found.
*/

  BoolArray peakYN(array.width(),array.height());
  for(BoolArray::iterator i=peakYN.begin(); i!=peakYN.end();++i)
    peakYN[i]=1;
  
//   const int size=array.width()+array.height();
//  double size
  int curFound=0;
  int numSquares=0;
  //  double values[numPeaks];
  //  ICoord list[numPeaks];
  double *values;
  ICoord *list;
  
  values = new double[numPeaks];
  values[0]=0;
  list = new ICoord[numPeaks];

  int xChange[8]= {-1,0,1,1,1,0,-1,-1}, yChange[8]={1,1,1,0,-1,-1,-1,0};

  for(DoubleArray::const_iterator i=array.begin(); i!=array.end(); ++i) {
    numSquares++;
    if(peakYN[i.coord()]) {
      int curX=i.coord()(0), curY=i.coord()(1);
//       int count=0;
      for(int cur = 0; cur<8;cur++) { //loop through adjacent pixels
	int newX = curX+xChange[cur], newY=curY+yChange[cur];
	ICoord newPt(newX,newY);
	if(newX>=0 && newX<array.width() && newY>=0 && newY<array.height()){
	  if(array[i]>array[newPt])
	    peakYN[newPt]=0;
	  else if(array[i]<=array[newPt])
	    peakYN[i.coord()]=0;
	}
      }
      
      
      if(peakYN[i.coord()]) {
	std::cout<<i.coord()(0)<<","<<i.coord()(1)<<"----"<<array[i]<<std::endl;
	curFound++;
      }
    }
  }
  std::cout<<std::endl;
  
  std::cout<<"Squares: "<<numSquares<<" "<<curFound<<std::endl;

/*  if(array[i.coord()]>values[0]) {
      if(curFound==0) {
	values[0]=array[i.coord()];
	list[0]=i.coord();
	curFound++;
      }
      else if(curFound<numPeaks) {
	values[curFound]=array[i.coord()];
	list[

      }
    }
  }*/

  delete[] values;
  delete[] list;
}

void convertFromHough(ICoord houghCoord)
{//Converts the hough coordinate into a line in normal space
  //r=x cos t +y sin t
// Incomplete function?  Commented out to avoid compiler warnings.
//   double angle=houghCoord(1)*M_PI/180.;
//   double x=double(houghCoord(0))/cos(angle);
//   double y=double(houghCoord(0))/sin(angle);
}

BoolArray houghTrans(const BoolArray &image)
{
  std::cout<<image[ICoord(84,0)]<<std::endl;
  int size = 41; //Size isn't determined yet, maybe image width/3
  ICoord first, last;
  for(BoolArray::const_iterator i=image.begin(); i!=image.end(); ++i) {
    if(isEnd(image,i.coord()) && i.coord()==ICoord(174,246)) {
    //      std::cout<<i.coord()(0)<<" "<<i.coord()(1)<<std::endl;
      first(0)=i.coord()(0)-size/2; first(1)=i.coord()(1)-size/2;
      if(first(0)<0)
	first(0)=0;
      if(first(1)<0)
	first(1)=0;
      last(0)=i.coord()(0)+size/2; last(1)=i.coord()(1)+size/2;
      if(last(0)>=image.width())
	last(0)=image.width()-1;
      if(last(1)>=image.height())
	last(1)=image.height()-1;

      std::cout<<i.coord()(0)<<" "<<i.coord()(1)<<std::endl;
      std::cout <<first(0)<<" "<<first(1)<<"--"<<last(0)<<" "<<last(1)<<std::endl;
      DoubleArray temp=hough(image,first,last);

      findPeaks(temp,5);

    }
  }
  return image;
}

/*
DoubleArray FindLines(const BoolArray &image)
{
  DoubleArray final=houghTrans(image,start,end);
  





}*/
