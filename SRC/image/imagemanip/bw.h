// -*- C++ -*-
// $RCSfile: bw.h,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2014/09/27 21:41:37 $

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
August 26, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

bw.h

This file contains a function used by SWIG to start the function
that converts an image to black and white.
*/

#include <oofconfig.h>

#ifndef BW_H
#define BW_H

class OOFImage;

void makeBW(OOFImage&, double a, double b, int n, int t);

#endif // BW_H
