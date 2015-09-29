// -*- C++ -*-
// $RCSfile: skeletonize.h,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:41:40 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

/*
Kevin Chang
August 27, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

skeletonize.h

This file contains a function used by SWIG to start the skeletonization function.
*/

#include <oofconfig.h>

#ifndef SKELETONIZE_H
#define SKELETONIZE_H

class OOFImage;
class grayImage;
class BWImage;

void makeSkel(OOFImage&, double, double, int, int);

#endif // SKELETONIZE_H
