// -*- C++ -*-
// $RCSfile: hysteresis.h,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2014/09/27 21:41:30 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modifed
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef HYSTERESIS_H
#define HYSTERESIS_H

class DoubleArray;
class BoolArray;

BoolArray hysteresisThresh(const DoubleArray&,double,double);

#endif // HYSTERESIS_H
