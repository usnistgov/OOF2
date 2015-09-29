 
/* -*- C++ -*-
 $RCSfile: fixborders.C,v $
 $Revision: 1.8 $
 $Author: langer $
 $Date: 2014/09/27 21:41:35 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */ 
 
  
#include "image/SEGMENTATION/fixborders.h"

NoFix::NoFix(){

}

/*
n -> Minimum number of pixels in a 'clump'
c -> Attempt to connect neighbors if this is true.
Set the classified array to nothing for now. 
*/
FixBorders::FixBorders(int n, bool c) 
  :classified(ICoord(1,1),0.0)
{
	numClump = n;
	connectNeighbors = c;
}

/*
Used by some functions that do not call fix method, and just need touch borders or something directly.
*/
FixBorders::FixBorders()
  :classified(ICoord(1,1),0.0)
{
	numClump = 0;
	connectNeighbors = 0;
}

/*
What is called by segmenter.spy in order to 'tidy up' the image.
*/
DoubleArray FixBorders::fix(DoubleArray original){
	DoubleArray newgray = DoubleArray(original.size());
	newgray = deleteSmallClumps(original, numClump);
	if (connectNeighbors){
		newgray = connectBorders(newgray);
		touchBorders(newgray, numClump);
	}
	return newgray;
}



/*
There have been some issues with shading pixels one or two away from the border. This shades them if the pixel one or two away is checked. Also used in Canny class.
*/
void FixBorders::touchBorders(DoubleArray &final, double lowerThreshold){
	ICoord size = final.size();
	ICoord r;
	ICoord l;
	ICoord ra;
	ICoord la;
	/*
	Checks all of the pixels along the edges. If this is a dark pixel (background) but there is a qhite pixel within a 2pixel radius of it, then this pixel is shaded white. 
	*/
	for (int i = 0; i < size(0); ++i){
		r = ICoord(i, 0);
		l = ICoord(i, size(1)-1);
		ra = ICoord(i,1);
		la = ICoord(i, size(1) -2);
		if (final[ra] == 0 && final[ICoord(i, 2)] == 1)
			final[ra] = 1;
		if (final[la] == 0 && final[ICoord(i, size(1)-3)] == 1)
			final[la] = 1;
		if (final[r] == 0 && final[ICoord(i, 1)] == 1)
			final[r] = 1;
		if (final[l] == 0 && final[ICoord(i, size(1)-2)] == 1)
			final[l] = 1;
	}
	
	for (int i = 0; i < size(1); ++i){
		r = ICoord(0, i);
		l = ICoord(size(0)-1, i);
		ra = ICoord(1, i);
		la = ICoord(size(0)-2, i);
		if (final[ra] == 0 && final[ICoord(2, i)] == 1)
			final[ra] = 1;
		if (final[la] == 0 && final[ICoord(size(0)-3, i)] == 1)
			final[la] = 1;
		if (final[r] == 0 && final[ICoord(1, i)] == 1)
			final[r] = 1;
		if (final[l] == 0 && final[ICoord(size(0)-2, i)] == 1)
			final[l] = 1;
	}
}


/*
Check if given pixel is within the bounds of the image
*/
bool FixBorders::pixelInBounds(ICoord pxl, ICoord size) {
  int xx = (pxl)(0);
  int yy = (pxl)(1);
  if ( (xx<0) || (xx>=size(0)) || (yy<0) || (yy>=size(1)) )
    return false;
  return true;
}


/*
Clear all regions of the same color that contains less than threshold pixels in size. Counts for pixels to be connected if they are at a diagonal from each other.  
*/
DoubleArray FixBorders::deleteSmallClumps(DoubleArray gray, int threshold){
	ICoord center;
	ICoord size = gray.size();
	int num;
	BoolArray looked_at = BoolArray(size); /* Pixels that have been examined already and classified into an area */
	
	for (DoubleArray::iterator i = gray.begin(); i != gray.end(); ++i){
		center = i.coord();
		if (gray[center] == 1 && !looked_at[center]){ /* only classify the 'border pixels' (1s) */
			std::vector<ICoord> members = burn(gray, looked_at, center); /* burn function finds num pixels in an area as well as returns those pixels in a vector for easy access. Also tags these pixels as seen in the looked_at array*/
			num = members.size();
			if (num < threshold){
				unsigned int i = 0;
				while (i < members.size()){
					gray[members[i]] = 0;
					++i;
				}
			}
		} 
	
	}
	return gray;

}

/*
Connects edges that are within 2 pixels of each other in any direction
Might want to turn this into a mask in mask.C
*/
DoubleArray FixBorders::connectBorders(DoubleArray gray){
	ICoord center;
	ICoord size = gray.size();
	for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
		center = i.coord();
		if (gray[center] == 1){
			if ((pixelInBounds(center + ICoord(1,-1), size) == true) && (gray[center + ICoord(1,-1)] == 0)){
				if ((pixelInBounds(center + ICoord(2,-2), size) == true) && (gray[center + ICoord(2,-2)] == 1)){
					gray[center + ICoord(1,-1)] = 1;
				}
			}
			if ((pixelInBounds(center + ICoord(-1,-1), size) == true) && (gray[center + ICoord(-1,-1)] == 0)){
				if ((pixelInBounds(center + ICoord(-2,-2), size) == true) && (gray[center + ICoord(-2,-2)] == 1)){
					gray[center + ICoord(-1,-1)] = 1;
				}
			}
			if ((pixelInBounds(center + ICoord(1,1), size) == true) && (gray[center + ICoord(1,1)] == 0)){
				if ((pixelInBounds(center + ICoord(2,2), size) == true) && (gray[center + ICoord(2,2)] == 1)){
					gray[center + ICoord(1,1)] = 1;
				}
			}
			if ((pixelInBounds(center + ICoord(-1,1), size) == true) && (gray[center + ICoord(-1,1)] == 0)){
				if ((pixelInBounds(center + ICoord(-2,2), size) == true) && (gray[center + ICoord(-2,2)] == 1)){
					gray[center + ICoord(-1,1)] = 1;
				}
			}
			if ((pixelInBounds(center + ICoord(1,0), size) == true) && (gray[center + ICoord(1,0)] == 0)){
				if ((pixelInBounds(center + ICoord(2,0), size) == true) && (gray[center + ICoord(2,0)] == 1)){
					gray[center + ICoord(1,0)] = 1;
				}
			}
			if ((pixelInBounds(center + ICoord(-1,0), size) == true) && (gray[center + ICoord(-1,0)] == 0)){
				if ((pixelInBounds(center + ICoord(-2,0), size) == true) && (gray[center + ICoord(-2,0)] == 1)){
					gray[center + ICoord(-1,0)] = 1;
				}
			}
			if ((pixelInBounds(center + ICoord(0,1), size) == true) && (gray[center + ICoord(0,1)] == 0)){
				if ((pixelInBounds(center + ICoord(0,2), size) == true) && (gray[center + ICoord(0,2)] == 1)){
					gray[center + ICoord(0,1)] = 1;
				}
			}
			if ((pixelInBounds(center + ICoord(0,-1), size) == true) && (gray[center + ICoord(0,-1)] == 0)){
				if ((pixelInBounds(center + ICoord(0,-2), size) == true) && (gray[center + ICoord(0,-2)] == 1)){
					gray[center + ICoord(0,-1)] = 1;
				}
			}
		}
	}
	return gray;
}

/*
Uses burn function from pixel selection to find the pixels in an area. This doesnt overflow and works very fast. Returns the pixels in that area (includes pixels touching at a diagonal). 
*/
std::vector<ICoord> FixBorders::burn(DoubleArray & image, BoolArray & burned, ICoord spark){
	std::vector<ICoord> activesites;
	int nburnt = 0;
	burned[spark] = true;
	std::vector<ICoord> all;
	double startcolor = image[spark];
	nburnt++;
	activesites.push_back(spark);
	all.push_back(spark);
	while (activesites.size() > 0){
		int n = activesites.size() - 1;
		const ICoord here = activesites[n];
		activesites.pop_back();
		burn_nbrs(image, activesites, burned, nburnt, here, startcolor, all);
	}
	return all;
}

/*
Used by burn to find pixels neighboring each pixel (so in a 3x3 mask around each pixel). 
Adds every pixel around it that is of the same color to the 'all' array and tags it as looked at in the 'burned' BoolArray
*/
void FixBorders::burn_nbrs(DoubleArray & image, std::vector<ICoord> &activesites, BoolArray &burned, int &nburnt, const ICoord & here, double startcolor, std::vector<ICoord> & all){
	ICoord size = image.size();
	ICoord add = ICoord(0,1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		all.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
	}
	add = ICoord(0,-1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		all.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
	}
	add = ICoord(1,0);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		all.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
	}
	add = ICoord(-1,0);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		all.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
	}
	add = ICoord(1,-1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		all.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
	}
	add = ICoord(-1,-1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		all.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
	}
	add = ICoord(1,1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		all.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
	}
	add = ICoord(-1,1);
	if ((add != ICoord(0,0)) && pixelInBounds(here + add, size) && (burned[here + add] == false) && (image[here +add] == startcolor)){
		activesites.push_back(here + add);
		all.push_back(here + add);
		burned[here + add] = true;
		++nburnt;
	}
}
