 /* -*- C++ -*-
 $RCSfile: skeletonize.C,v $
 $Revision: 1.10 $
 $Author: langer $
 $Date: 2014/09/27 21:41:36 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */ 
 
 
#include "skeletonize.h"
#include "fixborders.h"
 
/*
Deleted non-connecting lines that are one pixel wide. ('twigs' going off of connecting pieces of a microstructure)
Might need to be expanded to two pixel wide non-connecting lines.
This is mainly noise, but sometimes deleted two pieces of a microstructure that are not quite connected. 
*/
DoubleArray Skeletonize::deleteLeafs(DoubleArray gray){
	ICoord size = gray.size();
	int numDeleted = 0;
	DoubleArray temp = DoubleArray(gray);
	do { /* delete pieces that match criteria until there are no more to be deleted. delete only at end of step so that no looking at a pixel again */
		numDeleted = 0;
		for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
			ICoord curr = i.coord();
			if (gray[curr] == 1 && (curr(0) > 0) && curr(1) > 0 && (curr(0) < size(0)-2) && (curr(1) < size(1) -2)) {
				int num = numSideEmpty(curr, gray, 1,1);
				if (num <= 1){
					++numDeleted;
					temp[curr] = 0;
				}
			}
		}
		gray = temp;
	}while (numDeleted > 0);
	
	return gray;
} 

/*
Returns number of sides of that pixel that are of the specified intensity.
Might want to make this into a mask.
*/
int Skeletonize::numSideEmpty(ICoord center, DoubleArray list, int type, int allSides){
	ICoord size = list.size();
	int num = 0;
	ICoord curr;
	curr = center+ICoord(1,0);
	if (pixelInBounds(curr, size) == true){
		if (list[curr] == type)
			++num;
	}
	curr = center+ICoord(0,1);
	if (pixelInBounds(curr, size) == true){
		if (list[curr] == type)
			++num;
	}
	curr = center+ICoord(-1,0);
	if (pixelInBounds(curr, size) == true){
		if (list[curr] == type)
			++num;
	}
	curr = center+ICoord(0,-1);
	if (pixelInBounds(curr, size) == true){
		if (list[curr] == type)
			++num;
	}
	if (allSides == 1){
		curr = center+ICoord(1,1);
		if (pixelInBounds(curr, size) == true){
			if (list[curr] == type)
				++num;
		}
		
		curr = center+ICoord(-1,-1);
		if (pixelInBounds(curr, size) == true){
			if (list[curr] == type)
				++num;
		}
		curr = center+ICoord(1,-1);
		if (pixelInBounds(curr, size) == true){
			if (list[curr] == type)
				++num;
		}
		curr = center+ICoord(-1,1);
		if (pixelInBounds(curr, size) == true){
			if (list[curr] == type)
				++num;
		}
	}
	
	return num;
}


/*
My version of skeletonizing. Have not tested a lot, but appears to work better than the previously written skeletonizing. 
If a white pixel has between 2-5 neighbors AND either has only one transition from 0-1 in a 3x3 mask around in OR matches one of 8 masks given below, then this pixel is tagged for deletion. All pixels are looked through once before deleting from actual image. Pixels deleted until there are no more pixels to delete. 
*/
DoubleArray Skeletonize::thinEdges(DoubleArray gray){
  ICoord size = gray.size();;
  DoubleArray a = DoubleArray(gray);
  DoubleArray b = DoubleArray(gray);
  int numDeleted = 0;
  // the commented out section can be added, in which case the above a= and b = lines should be commented out. this would create a border of '0' pixels around the image, which will in theory make edges work better. THough I havent seen it in practice so its commented out
  /*DoubleArray final = DoubleArray(size);
  DoubleArray a = DoubleArray(size + ICoord(2,2));
  DoubleArray b = DoubleArray(size + ICoord(2,2));
  for (DoubleArray::iterator i = gray.begin(); i != gray.end(); ++i){
  	ICoord c = i.coord();
	a[c + ICoord(1,1)] = gray[c];
	b[c + ICoord(1,1)] = gray[c];
  }
  size = a.size();*/
  do{
	numDeleted = 0;
	for (DoubleArray::iterator i = a.begin();i !=a.end(); ++i){
		ICoord center = i.coord();
		if (a[center] == 1){
			int numFull = numNonZeroTransitions(center, a); // num transitions from 0 -1 around the pixel
			int num = numSideEmpty(center, a, 1, 1); // number of sides (all 8 sides) that is an edge
			if (1 < num && num < 6){ // so as not to delete any pixels from the middle
				ICoord above = ICoord(0,1);
				ICoord below = ICoord(0, -1);
				ICoord right = ICoord(1,0);
				ICoord left = ICoord(-1,0);
				if (numFull == 1){ // only one transition around the image from black to white -> loose end
					++numDeleted;
					b[center] = 0;
				}
				else 
				if (pixelInBounds(center + above, size) &&
				pixelInBounds(center + below, size) &&
				pixelInBounds(center + right, size) &&
				pixelInBounds(center + left, size) &&
				pixelInBounds(center + left + below, size) &&
				pixelInBounds(center + left + above, size) &&
				pixelInBounds(center + right + below, size) &&
				pixelInBounds(center + right + above, size)
				){
					if ((a[center + above + right] == 0 &&
					a[center + above] == 0 &&
					a[center + above + left] == 0 &&
					a[center + below] == 1 &&
					a[center + below + right] == 1 &&
					a[center + below + left] == 1) ||
				
					(a[center + above + right] == 0 &&
					a[center + right] == 0 &&
					a[center + below + right] == 0 &&
					a[center + left] == 1 &&
					a[center + left + above] == 1 &&
					a[center + below + left] == 1) ||
				
					(a[center + below + right] == 0 &&
					a[center + below] == 0 &&
					a[center + below + left] == 0 &&
					a[center + above] == 1 &&
					a[center + above + right] == 1 &&
					a[center + above + left] == 1) ||
				
					(a[center + above + left] == 0 &&
					a[center + left] == 0 &&
					a[center + below + left] == 0 &&
					a[center + right] == 1 &&
					a[center + above + right] == 1 &&
					a[center + below + right] == 1) ||
				
					(a[center + above] == 0 &&
					a[center + above + right] == 0 &&
					a[center + right] == 0 &&
					a[center + below] == 1 &&
					a[center + left] ==  1) ||
				
					(a[center + above] == 1 &&
					a[center + left] == 1 &&
					a[center + right] == 0 &&
					a[center + below] == 0 &&
					a[center + below + right] == 0) ||
				
					(a[center + above] == 1 &&
					a[center + right] == 1 &&
					a[center + left] == 0 &&
					a[center + below] == 0 &&
					a[center + below + left] == 0) ||
				
					(a[center + above] == 0 &&
					a[center + above + left] == 0 &&
					a[center + left] == 0 &&
					a[center + below] == 1 &&
					a[center + right] == 1)){
						++numDeleted;
						b[center] = 0;
				
					}	
				}
			}			
		}
	}
    	a = b;
  }while(numDeleted != 0);
/*  for (DoubleArray::iterator i = gray.begin(); i != gray.end(); ++i){
  	ICoord c = i.coord();
	gray[c] = a[c + ICoord(1,1)];
  }
  return gray;*/
  return a;	
}

/*
Counts the number of transitions from 0-1 around a pixel in a 3x3 mask (with the pixel in question being the center 
*/
int  Skeletonize::numNonZeroTransitions(ICoord center, DoubleArray gray){
  int num = 0;
  ICoord size = gray.size();
  if (pixelInBounds(center + ICoord(0,1),size) && pixelInBounds(center + ICoord(-1,1),size) && ((gray[center + ICoord(0,1)] == 0 && gray[center + ICoord(-1,1)] == 1))){ 
    ++num;
  }
  if (pixelInBounds(center + ICoord(-1,1),size) && pixelInBounds(center + ICoord(-1,0),size) && ((gray[center + ICoord(-1,1)] == 0 && gray[center + ICoord(-1,0)] == 1))){ 
    ++num;
  }
  if (pixelInBounds(center + ICoord(-1,0),size) && pixelInBounds(center + ICoord(-1,-1),size) && ((gray[center + ICoord(-1,0)] == 0 && gray[center + ICoord(-1,-1)] == 1))){ 
    ++num;
  }
  if (pixelInBounds(center + ICoord(-1,-1),size) && pixelInBounds(center + ICoord(0,-1),size) && ((gray[center + ICoord(-1,-1)] == 0 && gray[center + ICoord(0,-1)] == 1))){ 
    ++num;
  }
  if (pixelInBounds(center + ICoord(0,-1),size) && pixelInBounds(center + ICoord(1,-1),size) && ((gray[center + ICoord(0,-1)] == 0 && gray[center + ICoord(1,-1)] == 1))){ 
    ++num;
  }
  if (pixelInBounds(center + ICoord(1,-1),size) && pixelInBounds(center + ICoord(1,0),size) && ((gray[center + ICoord(1,-1)] == 0 && gray[center + ICoord(1,0)] == 1))){ 
    ++num;
  }
  if (pixelInBounds(center + ICoord(1,0),size) && pixelInBounds(center + ICoord(1,1),size) && ((gray[center + ICoord(1,0)] == 0 && gray[center + ICoord(1,1)] == 1))){ 
    ++num;
  }
  if (pixelInBounds(center + ICoord(1,1),size) && pixelInBounds(center + ICoord(0,1),size) && ((gray[center + ICoord(1,1)] == 0 && gray[center + ICoord(0,1)] == 1))){ 
    ++num;
  }
  return num;
}
 
 
/*
  Returns the number of sides of the center pixel that are of color type (in all directions)
*/
int Skeletonize::numBorderSides(ICoord center, DoubleArray list, int type){
  int num = 0;
  ICoord curr;
  ICoord size = list.size();
  curr = center+ICoord(1,0);
  if (pixelInBounds(curr,size) == true){
    if (list[curr] == type)
      ++num;
  }
  else
    ++num;
  curr = center+ICoord(0,1);
  if (pixelInBounds(curr,size) == true){
    if (list[curr] == type)
      ++num;
  }
  else
    ++num;
  curr = center+ICoord(-1,0);
  if (pixelInBounds(curr,size) == true){
    if (list[curr] == type)
      ++num;
  }
  else
    ++num;
  curr = center+ICoord(0,-1);
  if (pixelInBounds(curr,size) == true){
    if (list[curr] == type)
      ++num;
  }
  else
    ++num;
  return num;

}
 
/*
Checks if the pixel is in the bounds of the image 
*/
bool Skeletonize::pixelInBounds(ICoord pxl, ICoord size) {
  int xx = (pxl)(0);
  int yy = (pxl)(1);
  if ( (xx<0) || (xx>=size(0)) || (yy<0) || (yy>=size(1)) )
    return false;
  return true;
}

 
/********
Past this point, I didnt write this functions and havent probed into how the work. They skeletonize an image. They have some issues when the line of a skeleton approaches the edge of an image. This is why the above skeletonization method was written, but both are available in the skeletonization step. If the boolean value is checked the above is executed, if it is unchecked then the below methods are executed. If you want more info on the functions written below please see image/GRAINBDY/SummerWorkSummary.txt
*******/


bool Skeletonize::isContour(const BoolArray &image,const ICoord pt) {
  if(image[pt]==1 && (pt(0)==0 || pt(0)==image.width()-1 || pt(1)==0 || pt(1)==image.height()-1))
    return true;
  if (image[pt]==1) {  // If the point is white
    for (int a = -1; a <= 1; a++) {  // Twice
      for (int b = -1; b <= 1; b++) {  // Twice
	if (image[pt+ICoord(a,b)] == 0)
	  return true;  // Returns true if any of the points surrounding the white one is black
      }
    }
  }
  return false;
}

bool Skeletonize::isDeletable(const BoolArray& image,ICoord pt) {
  int numTrans=0;
  int xChange[9]={-1,0,1,1,1,0,-1,-1,-1};
  int yChange[9]={1,1,1,0,-1,-1,-1,0,1};

  for(int a=0;a<8;a++) {
    bool pixVal1,pixVal2;
    if(image.contains(pt+ICoord(xChange[a],yChange[a])))
      pixVal1=image[pt+ICoord(xChange[a],yChange[a])];
    else
      pixVal1=0;
    
    if(image.contains(pt+ICoord(xChange[a+1],yChange[a+1])))
      pixVal2=image[pt+ICoord(xChange[a+1],yChange[a+1])];
    else
      pixVal2=0;
    if(pixVal1==0 && pixVal2==1)
      numTrans++;
  }
 
  if (numTrans!=1)
    return false;

  //check nonzero neighbors
  int numNonzero=0;
  for (int a=-1;a<=1;a++) {
    for (int b=-1;b<=1;b++) {
      if(image.contains(pt+ICoord(a,b)) && (a!=0 || b!=0) && image[pt+ICoord(a,b)])
	numNonzero++;
    }
  }
  if ((numNonzero<2) || (numNonzero>6))
    return false;

  return true;
}

bool Skeletonize::satisfiesStep1(const BoolArray &image,ICoord pt) {
  int p2=0,p4=0,p6=0,p8=0;
  if(pt(1)+1<image.height())
    p2=int(image[ICoord(pt(0),pt(1)+1)]);
  if(pt(0)+1<image.width())
    p4=int(image[ICoord(pt(0)+1,pt(1))]);
  if(pt(1)-1>=0)
    p6=int(image[ICoord(pt(0),pt(1)-1)]);
  if(pt(0)-1>=0)
    p8=int(image[ICoord(pt(0)-1,pt(1))]);
  if ((p2*p4*p6==0)&&(p4*p6*p8==0)) {
    return true;
  }    
  else {
    return false;
  }
}

bool Skeletonize::satisfiesStep2(const BoolArray &image,ICoord pt) {
  int p2=0,p4=0,p6=0,p8=0;
  if(pt(1)+1<image.height())
    p2=image[ICoord(pt(0),pt(1)+1)];
  if(pt(0)+1<image.width())
    p4=image[ICoord(pt(0)+1,pt(1))];
  if(pt(1)-1>=0)
    p6=image[ICoord(pt(0),pt(1)-1)];
  if(pt(0)-1>=0)
    p8=image[ICoord(pt(0)-1,pt(1))];
  if ((p2*p4*p8==0)&&(p2*p6*p8==0))
    return true;
  else
    return false;
}


/*
The function called by segmenter.spy to start the skeletonization process.
*/
DoubleArray Skeletonize::skeletonize(DoubleArray &im) {

	if (useMyVersion) // the version i wrote is ran instead of this one. 
		return thinEdges(im);
	BoolArray image = BoolArray(im.size());
	for (DoubleArray::iterator i = im.begin();i !=im.end(); ++i){
	ICoord c = i.coord();
		if (im[c] == 0)
			image[c] = 0;
		else
			image[c] = 1;
	}
		
	int w=image.width();
	int h=image.height();
	BoolArray flag(ICoord(w,h),false);
	for(BoolArray::iterator i=flag.begin();i!=flag.end(); ++i)
	flag[i]=0;
	BoolArray deleted = image.clone();

	int step=1;
	bool stop=false;

	while (!stop) {
		int numChanged=0;
		for (int a = 0; a < w; a++) {
			for (int b = 0; b < h; b++) {
				if (isContour(deleted,ICoord(a,b)) && isDeletable(deleted,ICoord(a,b))) {
					if (step == 1) {
						if (satisfiesStep1(deleted,ICoord(a,b))) {
							flag[ICoord(a,b)]=1;
							numChanged++;
						}
					}
				else {
					if (satisfiesStep2(deleted,ICoord(a,b))) {  
						flag[ICoord(a,b)]=1;  // Marks point for deletion
						numChanged++;
					}
				}
			}
		}
	}

	//remove flagged points
	for (int c = 0; c < w; c++) {
		for (int d = 0; d < h; d++) {
			if (flag[ICoord(c,d)]==1) {
				flag[ICoord(c,d)]=0;
				deleted[ICoord(c,d)]=0;
			}
		}
	}
	step *= -1;
	if (numChanged==0)
		stop=true;
	}
	DoubleArray toReturn = DoubleArray(deleted.size());
	for (BoolArray::iterator i = deleted.begin(); i != deleted.end(); ++i){
		ICoord c = i.coord();
		if (deleted[c] == 0)
			toReturn[c] = 0;
		else
			toReturn[c] = 1;
	}
	if (deleteLooseEnds == true)
		toReturn = deleteLeafs(toReturn);
	return toReturn;
}
