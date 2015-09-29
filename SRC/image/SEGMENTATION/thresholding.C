// -*- C++ -*-
// $RCSfile: thresholding.C,v $
// $Revision: 1.10 $
// $Author: langer $
// $Date: 2014/09/27 21:41:36 $

/* This software was produced by NIST, an agency of the U.S. government,
* and by statute is not subject to copyright in the United States.
* Recipients of this software assume all responsibilities associated
* with its operation, modification and maintenance. However, to
* facilitate maintenance we ask that before distributing modified
* versions of this software, you first contact the authors at
* oof_manager@nist.gov. 
*/ 

#include "image/SEGMENTATION/thresholding.h"
#include "image/SEGMENTATION/imageops.h"
#include "image/SEGMENTATION/newgabor.h"
#include "common/boolarray.h"

NewGabor::NewGabor(int a, int b, int numAngles, int line_color, double t1, double t2){
	(*this).a = a;
	(*this).b = b;
	(*this).numAngles = numAngles;
	(*this).line_color = line_color;
	(*this).t1 = t1;
	(*this).t2 = t2;
}

DoubleArray NewGabor::threshold(DoubleArray original){
	DoubleArray old = DoubleArray(original.size());
	for (int i = 0; i < numAngles; ++i){
		double phi = double(i*180)/numAngles;
		
		DoubleArray current = newGabors(original, a, b, phi);
		if (i != 0){
			old = findLargerValss(current, old);
		}
		else
			old = current;
	}

	DoubleArray scaled = scaleArrays(old, 0.0, 1.0, line_color);
	BoolArray bools = hysteresisThreshs(scaled, t1, t2);
	DoubleArray grays = DoubleArray(original.size());
	for (DoubleArray::iterator i = grays.begin(); i != grays.end(); ++i){
		ICoord curr = i.coord();
		if (bools[curr] == true)
			grays[curr] = 1;
		else
			grays[curr] = 0;
	}
	return grays;
}

DoubleArray NewGabor::scaleArrays(const DoubleArray& arr, double min, double max,int lineColor) {
//Scales the double values from applying a filter into values between the min
//and the max.
  double minArr=999999, maxArr=-999999;

  for(DoubleArray::const_iterator i=arr.begin();i!=arr.end();++i) {
    double val=0.;
    if(lineColor==2)//Detect both white and dark colored lines.
      val=fabs(arr[i]);
    else if(lineColor==1)//Detect only white lines.
      val=arr[i];
    else if(lineColor==0)//Detect only dark lines.
      val=-arr[i];
      
    if(val<minArr)
      minArr=val;
    if(val>maxArr)
      maxArr=val;
  }
  if(lineColor!=2)
    minArr=0;
  double scaleFactor=(max-min)/(maxArr-minArr);
  double shift=max-maxArr*scaleFactor;
  DoubleArray newArr(arr.width(),arr.height());
  for(DoubleArray::const_iterator j=arr.begin();j!=arr.end();++j) {
    if(lineColor==2)
      newArr[j.coord()]=fabs(arr[j])*scaleFactor+shift;
    else if(lineColor==1) {
      if(arr[j]>0)
	newArr[j.coord()]=arr[j]*scaleFactor+shift;
      else
	newArr[j.coord()]=0;
    }
    else {
      if(arr[j]<0)
	newArr[j.coord()]=-arr[j]*scaleFactor+shift;
      else
	newArr[j.coord()]=0;
    }
  }
  return newArr;    
}

DoubleArray NewGabor::findLargerValss(const DoubleArray &arr1, const DoubleArray &arr2) {
  //Both arrays must be the same size, or it will go out of bounds.
  DoubleArray newArr(arr1.width(),arr1.height());
  for(DoubleArray::const_iterator i=arr1.begin(); i!=arr1.end(); ++i) {
    if(fabs(arr1[i])>=fabs(arr2[i]))
      newArr[i.coord()]=arr1[i];
    else
      newArr[i.coord()]=arr2[i];
  }
  return newArr;
}

DoubleArray NewGabor::newGabors(const DoubleArray& image,int a,int b,double phi) {
//Applies the Imaginary Gabor Filter to an image and returns raw data.
  NewGB newGaborMask(a,b,phi);
  return newGaborMask.apply(image);
}

BoolArray NewGabor::hysteresisThreshs(const DoubleArray& image, double T1, double T2)
{//T1 is the lower threshold and T2 is the higher threshold

  BoolArray newimage(image.width(),image.height());

  for (DoubleArray::const_iterator i = image.begin(); i != image.end(); ++i) {
    newimage[i.coord()] = image[i]>=T2;
  }
  
  int xChange[8]= {-1,0,1,1,1,0,-1,-1}, yChange[8]={1,1,1,0,-1,-1,-1,0};

  bool changed=1;
  while(changed) {
    changed=0;
    for (DoubleArray::const_iterator i = image.begin(); i != image.end(); ++i) {
      if(!newimage[i.coord()] && image[i]>=T1) {
	int x=i.coord()(0), y=i.coord()(1);
      	for(int dir=0;dir<8;dir++) {
	  int newX=x+xChange[dir], newY=y+yChange[dir];
	  if(newX>=0 && newX<image.width() && newY>=0 && newY<image.height() 
	     && newimage[ICoord(newX,newY)]) {
	    newimage[i.coord()]=1;
	    changed=1;
	    break;
	  }
	}
      }
    }
  }
  return newimage;
}

RegularThresholding::RegularThresholding(DiffusionRHS d, int n, double th){
	num = n;
	diff = d;
	t = th;
}


/*
There seems to be a problem when going from swingging to c with carrying what type of class the DiffusionRHS is. It always defaults to DiffusionRHS. THe only way I found to look at what the actual class is, is to set a variable to equal what type of class it really is, and then reinitialize it here. 
*/
DoubleArray RegularThresholding::threshold(DoubleArray original){
	DoubleArray changed = DoubleArray(original);
	DoubleArray final = DoubleArray(original.size());
	DoubleArray changes = DoubleArray(original.size());
	ICoord size = original.size();
	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord curr = i.coord();
		final[curr] = .5;
	}
	DoubleArray previous = DoubleArray(original);
	DoubleArray double_previous = DoubleArray(original);
	for (int i = 0; i < num; ++i){
		if (diff.type == DiffusionRHS::ANTIGEOMETRIC){
			AntiGeometric newdiff = AntiGeometric(diff.time);
			changed = newdiff.timestep(changed);
		}
		else if (diff.type == DiffusionRHS::GEOMETRIC){
			Geometric newdiff = Geometric(diff.time);
			changed = newdiff.timestep(changed);
		}
		else if (diff.type == DiffusionRHS::LARGELAPLACE){
			LargeLaplace newdiff = LargeLaplace(diff.time);
			changed = newdiff.timestep(changed);
		}
		else if (diff.type == DiffusionRHS::LAPLACE){
			Laplace newdiff = Laplace(diff.time);
			changed = newdiff.timestep(changed);
		}
		else if (diff.type == DiffusionRHS::LARGEGAUSSIAN){
			LargeGaussian newdiff = LargeGaussian();
			changed = newdiff.timestep(changed);
		}
		else if (diff.type == DiffusionRHS::GAUSSIAN){
			Gaussian newdiff = Gaussian();
			changed = newdiff.timestep(changed);
		}
		else if (diff.type == DiffusionRHS::NOTYPE){
			changed = original;
		}
		else std::cout << "have added new type and not added statement in thresholding.C " << std::endl;
		
		for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
			ICoord curr = i.coord();
			double change = changed[curr] - original[curr];
			if (change < 0)
				change = 0;
			changes[curr] = change;
		}
		changes = normalizeImage(changes);
		/* there are different values pixels are set to. 1 means going up above threshold, -1 means decreasing. .9 means it is steadily decreasing with time. .5 means it hasnt been set yet */
		for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
			ICoord curr = i.coord();
			double change = changes[curr];
			if (change <= 0 && final[curr] == .5)
				final[curr] = -1;
			if ((change > t) && final[curr] == .5)
				final[curr] = 1;
			if (changed[curr] > previous[curr] && previous[curr] > double_previous[curr] && change > (3*t/4) && final[curr] == .5){ // if image intensity keeps going up each time
				final[curr] = .9;
			}
			
		}
		original = changed;
		double_previous = previous;
		previous = changed;
	}

	/*
	Combine all values that are edges to be 1. 
	*/
	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord c = i.coord();
		if (final[c] < .6)
			final[c] = 0;
		if (final[c] >= .6)
			final[c] = 1;
		

	}
	return final;
}


OddThresholding::OddThresholding(DiffusionRHS d, double tr){
	diff = d;
	t = tr;
}


/*
Attempt to do region merging. 
Concept: Undersegment an image. Classify pixels as definately edges, and definately background. For all other pixels, merge them into the other regions if they preserve connectivity. More info can be found in paper ANti-Geometric Diffusion for Adaptive Thresholding and Fast Segmentation. 
Doesnt work yet. Problems with finding what regions are next to each other, and then with regions not being set that are too large and should be spit up before attempting to merge.
*/
DoubleArray OddThresholding::threshold(DoubleArray original){
	DoubleArray changed = DoubleArray(original);
	DoubleArray final = DoubleArray(original.size());
	DoubleArray changes = DoubleArray(original.size());
	ICoord size = original.size();
	DoubleArray correct = DoubleArray(original);
	DoubleArray changing = DoubleArray(original);
	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord curr = i.coord();
		final[curr] = .5;
	}
	if (diff.type == DiffusionRHS::ANTIGEOMETRIC){
		AntiGeometric newdiff = AntiGeometric(diff.time);
		changed = newdiff.timestep(changed);
	}
	else if (diff.type == DiffusionRHS::GEOMETRIC){
		Geometric newdiff = Geometric(diff.time);
		changed = newdiff.timestep(changed);
	}
	else if (diff.type == DiffusionRHS::LARGELAPLACE){
		LargeLaplace newdiff = LargeLaplace(diff.time);
		changed = newdiff.timestep(changed);
	}
	else if (diff.type == DiffusionRHS::LAPLACE){
		Laplace newdiff = Laplace(diff.time);
		changed = newdiff.timestep(changed);
	}
	else if (diff.type == DiffusionRHS::LARGEGAUSSIAN){
		LargeGaussian newdiff = LargeGaussian();
		changed = newdiff.timestep(changed);
	}
	else if (diff.type == DiffusionRHS::GAUSSIAN){
		Gaussian newdiff = Gaussian();
		changed = newdiff.timestep(changed);
	}
	else if (diff.type == DiffusionRHS::NOTYPE){
		changed = original;
	}
	else std::cout << "have added new type and not added statement in thresholding.C " << std::endl;
	
	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord curr = i.coord();
		double change = changed[curr] - original[curr];
		if (change < 0)
			change = 0;
		changes[curr] = change;
	}
	changes = normalizeImage(changes);
	
	for (DoubleArray::iterator i = changes.begin();i !=changes.end(); ++i){
		ICoord curr = i.coord();
		if (changes[curr] > t){
			final[curr] = 1;
		}
		if (changes[curr] <= 0){
			final[curr] = 0;
		}
	}
	
	
	std::vector<area> all_areas; // the areas that are .5 (not classified at this point
	std::vector<area> good_areas; // areas that are 1s or 0s -> classified at this point
	BoolArray burned = BoolArray(size);
	for (DoubleArray::iterator i = final.begin();i != final.end(); ++i){
		ICoord c = i.coord();
		if (!burned[c]){
			std::vector<ICoord> neighbors;
			std::vector<ICoord> current = burn(final, burned, c);
			int current_size = current.size();
			double total = 0;
			double total_average = 0;
			double squared_total = 0;
			int cur = 0;
			ICoord now;
			while (cur < current_size){ /* find all the neighbors of this area, so can find out later if another area is next to this area */
				now = current[cur];
				total = total + changed[now];
				squared_total = squared_total + changed[now]*changed[now];
				++cur;
				setNeighbors(size,neighbors, now);
			}
			total_average = total/current_size;
			double squared_error = squared_total - 2*total_average*total + total_average*total_average*current_size;
			area a = area();
			a.neighbors = neighbors;
			a.color = final[now];
			a.members = current;
			a.size = current_size;
			a.sum_intensities = total;
			a.squared_sum_intensities = squared_total;
			a.mean_intensity = total_average;
			a.squared_error = squared_error;
			if (a.color == .5)
				all_areas.push_back(a);
			else
				good_areas.push_back(a);
		}
	}
	// at this point the all_areas and good_areas vectors are storing all of the areas of pixels. Now will want to scan throughthe all_areas vector to group those pixels with areas that have already been classified.
	unsigned int num_regions = all_areas.size();
	unsigned int num = 1;
	//std::cout << "about to start" << std::endl;
	while (num < (num_regions*3/4) && num < all_areas.size()){
		area here = all_areas[num];
		std::cout << "about to find neighbors" << std::endl;
		int n = findNeighbor(good_areas, here, here.neighbors); //need to add to a neighboring area, so find it here
		std::cout << "found neighbors " << std::endl;
		area next;
		std::cout << "before " << num << " " << all_areas.size()<< std::endl;
		if (n == -1){ // did not find a neighbor
			++num;
			continue;
		}
		else
			next = good_areas[n];
		std::cout << "after " << std::endl;
		int aij = here.size + next.size;
		double sij = here.sum_intensities + next.sum_intensities;
		double qij = here.squared_sum_intensities + next.squared_sum_intensities;
		double uij = sij/aij;
		double Eij = qij - 2*uij*sij + uij*uij*aij;
		double changeEij = here.sum_intensities*here.mean_intensity + next.sum_intensities*here.mean_intensity - sij*uij;
		if (changeEij > .05){ // dont know what number to set here yet. this is threshold for combining the two areas. Basically if this is over a certain number, then the error in the image does not increase significantly, and the merging of the two areas can happen.
			double main_color = next.color;
			int current_size = here.members.size();
			int cur = 0;
			while (cur < current_size){
				ICoord now = here.members[cur];
				final[now] = main_color;
				next.members.push_back(now);
				++cur;
			}
			next.size = aij;
			next.sum_intensities = sij;
			next.squared_sum_intensities = qij;
			next.mean_intensity = uij;
			next.squared_error = Eij;
			all_areas.erase(all_areas.begin() + num);
			--num;
			if (num > 0)
				--num;
		}
		++num;
	}
	num_regions = all_areas.size();
	return final;
}

/*
Set the neighbors of the current pixels into the array vector.
*/
void OddThresholding::setNeighbors(ICoord size, std::vector<ICoord> & array, ICoord curr){
	DoubleArray arr = DoubleArray(size);
	arr[curr] = 1;
	for (int i = -1; i <= 1; ++i){
		for (int j = -1; j <= 1; ++j){
			ICoord a = ICoord(i,j);
			if (pixelInBounds(curr + a,size) && arr[curr + a] == 0)
				arr[curr + a] = 1;
		}
	}
	for (DoubleArray::iterator i = arr.begin();i !=arr.end(); ++i){
		if (*i == 1)
			array.push_back(i.coord());
	}
	
}

/*
Find the next area that neighbors the current area. Might need to be modified in some way so it doesnt always return the next area in the list. 
*/
int OddThresholding::findNeighbor(std::vector<area> all_areas, area here, std::vector<ICoord> neighbors){
	unsigned int curr = 0;
	bool set = false;
	int final = -1;
	while (curr < all_areas.size() && set == false){
			std::vector<ICoord> curr_neighbors = all_areas[curr].neighbors;
			unsigned int a = 0;
			while (a < neighbors.size() && set == false) {
				unsigned int b = 0;
				ICoord cur_a = neighbors[a];
				while (b < curr_neighbors.size() && set == false){
					if (cur_a == neighbors[b]){
						set = true;
						final = curr;
					}
					++b;
				}
				++a;
			}
		++curr;
	}
	return final;
}

/* needs to be written later, for now no result */
DoubleArray OddThresholding::parse(DoubleArray original){
	return original;
}

/* see classify.C for explanation of how burn function works 
Makes a vector of all of the pixels neighboring and of the same color as the 'spark' pixel*/
std::vector<ICoord> Thresholding::burn(DoubleArray & image, BoolArray & burned, ICoord spark){
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

/* called by the 'burn' function above */
void Thresholding::burn_nbrs(DoubleArray & image, std::vector<ICoord> &activesites, BoolArray &burned, int &nburnt, const ICoord & here, double startcolor, std::vector<ICoord> & all){
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

/*
Is passed in the changes in the image. Returns image threshoded basically by change. 
Used in 'ThresholdBasedOnChange' option.
*/
DoubleArray RegularThresholding::parse(DoubleArray original){
	DoubleArray final = DoubleArray(original.size());
	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord curr = i.coord();
		if (original[curr] < 0)
			original[curr] = 0;
	}
	normalizeImage(original);
	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord curr = i.coord();
		if (original[curr] >= t)
			final[curr] = 1;
		else
			final[curr] = 0;
	}
	return final;
}


Canny::Canny(double lower, double upper){
	lowerThreshold = lower;
	upperThreshold = upper;
}

/*
For more infor on Canny algorithm see image/SEGMENTATION/canny.h
*/
DoubleArray Canny::threshold(DoubleArray original){
	CannyClass can = CannyClass(original.size());
	DoubleArray final = can.updateCannyArray(original, lowerThreshold, upperThreshold);
	return final;
}
