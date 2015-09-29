// -*- C++ -*-
// $RCSfile: histogram.h,v $
// $Revision: 1.2 $
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

#ifndef HISTOGRAM_H
#define HISTOGRAM_H

class DoubleArray;
class OOFImage;

void printHistogram(const DoubleArray&, int);
//void createHistogram2(const OOFImage&);


#endif //HISTOGRAM_H
