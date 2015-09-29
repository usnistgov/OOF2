/* -*- C++ -*-
 $RCSfile: segmenter.h,v $
 $Revision: 1.2 $
 $Author: langer $
 $Date: 2014/09/27 21:41:37 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */

 
 /*   
 This class is the controller for image segmentation. 
 
 */
#include <oofconfig.h>
#include <stdio.h>
#include <math.h>
#include "common/doublearray.h"
#include "image/oofimage.h"
#include "engine/sparselink.h"
#include "engine/matvec.h"
#include "engine/csrmatrix.h"
#include "engine/solver.h"
#include <string>


#ifndef SEGMENTER_H
#define SEGMENTER_H

class ICoord;
class OOFImage;
class CColor;
class ColorDifference;
class OOFImage;


  
void doClassifying(DoubleArray&);


 
#endif

 
