/* -*- C++ -*-
 $RCSfile: classify.C,v $
 $Revision: 1.12 $
 $Author: langer $
 $Date: 2014/09/27 21:41:34 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */  

 #include "image/SEGMENTATION/classify.h"
 #include "common/boolarray.h"
 #include "image/burn.h"
 #include "image/pixelselectioncourieri.h"
 
 ClassifyClass::ClassifyClass(){
	return;
 }

/*
Checks if the given pixel is in bounds of the image.
*/
bool ClassifyClass::pixelInBounds(ICoord pxl, ICoord size) {
  int xx = (pxl)(0);
  int yy = (pxl)(1);
  if ( (xx<0) || (xx>=size(0)) || (yy<0) || (yy>=size(1)) )
    return false;
  return true;
}


/*
Uses burn algorithm from pixel selection. While all of the pixels have nto been classified 'sparks' the next non-assigned pixel. Adds each neighboring pixel of the same color to a vector and assigns them all to a same color. 
*/
void ClassifyClass::burn(DoubleArray & image){
	std::vector<ICoord> activesites;
	int nburnt = 0;
	int maxBurned = image.size()(0)*image.size()(1);
	BoolArray burned = BoolArray(image.size());
	ICoord spark;
	double changecolor = 0;
	while (nburnt < maxBurned){ // while still have pixels that have not been classified
		for (BoolArray::iterator i = burned.begin();i !=burned.end(); ++i){ // look for next one ont classified
			if (*i == false){
				spark = i.coord();
				break;
			}
		}
		burned[spark] = true;
		double startcolor = image[spark];
		changecolor = changecolor + .1; // way of changing color, may be some better way, because sometimes regions of same color are next to each other causing confusion. 
		nburnt++;
		image[spark] = changecolor;
		activesites.push_back(spark);
		while (activesites.size() > 0){
			int n = activesites.size() - 1;
			const ICoord here = activesites[n];
			activesites.pop_back();
			burn_nbrs(image, activesites, burned, nburnt, here, startcolor, changecolor);
	
		}
	}
}

/*
Might want to make this into a mask rather than series of if statements. 
All pixels in 3x3 mask around the center pixel are examined. If they are of the same color, then they are added to the vector, and checked off as burned. 
*/
void ClassifyClass::burn_nbrs(DoubleArray & image, std::vector<ICoord> &activesites, BoolArray &burned, int &nburnt, const ICoord & here, double startcolor, double changecolor){
	ICoord size = image.size();
	ICoord add = ICoord(0,1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
		image[here + add] = changecolor;
	}
	add = ICoord(0,-1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
		image[here + add] = changecolor;
	}
	add = ICoord(1,0);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
		image[here + add] = changecolor;
	}
	add = ICoord(-1,0);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
		image[here + add] = changecolor;
	}
	add = ICoord(1,-1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
		image[here + add] = changecolor;
	}
	add = ICoord(-1,-1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
		image[here + add] = changecolor;
	}
	add = ICoord(1,1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
		image[here + add] = changecolor;
	}
	add = ICoord(-1,1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
		image[here + add] = changecolor;
	}
}
