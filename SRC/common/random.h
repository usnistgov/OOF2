// -*- C++ -*-
// $RCSfile: random.h,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2011/10/12 21:15:51 $


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */


#ifndef RANDOM_H
#define RANDOM_H

void rndmseed(int seed);
double rndm();
int irndm();
double gasdev();

#endif
