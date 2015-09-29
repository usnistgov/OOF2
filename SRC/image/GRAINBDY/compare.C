// -*- C++ -*-
// $RCSfile: compare.C,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:41:28 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modifed
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include <math.h>
#include "image/oofimage.h"
#include "common/boolarray.h"
#include "common/doublearray.h"
#include "image/GRAINBDY/imageops.h"

/*bool isMatch(const BoolArray & solution, const BoolArray& guess, ICoord center, int radius) {
  //checks if a white point, center, on the guess image is coincident with a white point in the solution image where coincident is defined as within the radius
  int w=solution.width(), h=solution.height();
  for (int a=-radius;a<=radius;a++) {
    for (int b=-radius;b<radius;b++) {
      int newX=a+center(0), newY=b+center(1);
      if (newX>=0 && newY>=0 && newX<w && newY<h && solution[ICoord(newX,newY)]==1)
	return true;
    }
  }
  return false;
}

int calculateMatches(const BoolArray& solution, const BoolArray& guess, int radius) {
  int numMatches=0;
  //calculates the number of coincident points in images guess and solution with coincident radius as parameter radius
  for (int a=0;a<guess.width();a++) {
    for (int b=0;b<guess.height();b++) {
      ICoord here(a,b);
      if ((guess[here]==1) && isMatch(solution,guess,here,radius))
	numMatches++;
    }
  }
  return numMatches;
}

double min(double n1,double n2) {
  if (n1<n2)
    return n1;
  else
    return n2;
}*/

double compare(const BoolArray& guess, int radius) {
  //radius specifies the radius of error in which two points will be considered coincident.  A greater radius will result in higher compare scores. radius=3 is a good value
  
  OOFImage image("image2","FTO_4B3_smallJUSTtrace.jpg");
  DoubleArray dbls=grayify(image);

  BoolArray solution=threshold(dbls,.5);
  
  int w=solution.width();
  int h=solution.height();
  
  int numSig=0, numNoise=0, numCorr=0, numSolution=0;
  for(BoolArray::const_iterator i=guess.begin();i!=guess.end();++i) {
    if(guess[i]) {
      bool sig=0;
      for (int a=-radius;a<=radius;a++) {
	for (int b=-radius;b<=radius;b++) {
	  int newX=a+i.coord()(0), newY=b+i.coord()(1);
	  if (newX>=0 && newY>=0 && newX<w && newY<h 
	      && solution[ICoord(newX,newY)]) {
	    sig=1;
	    numSig++;
	    break;
	  }
	}
	if(sig)
	  break;
      }
      if(!sig)
	numNoise++;
    }

    if(solution[i.coord()]) {
      numSolution++;
      bool endYN=0;
      for (int a=-radius;a<=radius;a++) {
	for (int b=-radius;b<=radius;b++) {
	  int newX=a+i.coord()(0), newY=b+i.coord()(1);
	  if (newX>=0 && newY>=0 && newX<w && newY<h 
	      && guess[ICoord(newX,newY)]) {
	    numCorr++;
	    endYN=1;
	    break;
	  }
	}
	if(endYN)
	  break;
      }
    }
  }
    
  double score1=double(numSig)/double(numNoise);
  double score2=double(numSig)/double(numSig+numNoise);
  double score3=double(numCorr)/double(numSolution);
  std::cout<<score1<<" "<<score2<<" "<<score3<< std::endl;
    
/*  int w=solution.width();
    int h=solution.height();

    in	t numPixelsInGuess=0;
    int	 numPixelsInSolution=0;
    
    for(int a=0;a<w;a++) {
    for(int b=0;b<h;b++) {
    ICoord here(a,b);
    if (solution[here]==1)
    numPixelsInSolution++;
    if (guess[here]==1)
    numPixelsInGuess++;
    }		
    }	
    
    int numMatches1=calculateMatches(solution,guess,radius);
    double score1=(double)numMatches1/numPixelsInSolution;
    
    int numMatches2=calculateMatches(guess,solution,radius);
    double score2=(double)numMatches2/numPixelsInGuess;
    cout<<score1<<" "<<score2<<endl;

  return min(score1,score2);*/
  return 1;
}
