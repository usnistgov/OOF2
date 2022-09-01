// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// This is the SWIG file for the "random.[Ch]" files. It has a name
// different from random because there's already a Python module
// called "random".
#ifndef CRANDOM_SWG
#define CRANDOM_SWG

%module(package="ooflib.SWIG.common") crandom

%include "common/typemaps.swg"
%{
#include "common/random.h"
%}

void rndmseed(int);
double rndm();
int irndm();
double gasdev();

class OOFRandomNumberGenerator {
public:
  OOFRandomNumberGenerator();
  int operator()(int);
};

%pythoncode %{
def gauss(mean, dev):
    return mean + dev*gasdev()

# Python translation of the shuffle algorithm in random.h.  Doing the
# shuffle in Python is maybe faster than copying a long list to C++
# and back.

def shuffle(liszt):
    if len(liszt) > 0:
        rand = OOFRandomNumberGenerator()
        for i in range(1, len(liszt)):
            other = rand(i+1)
            temp = liszt[i]
            liszt[i] = liszt[other]
            liszt[other] = temp
%}


#endif // CRANDOM_SWG
