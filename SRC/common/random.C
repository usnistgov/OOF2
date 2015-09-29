// -*- C++ -*-
// $RCSfile: random.C,v $
// $Revision: 1.4 $
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


// random number generator.

// This uses the stateful version of the stdlib random() function.
// Using the stateful version means that we get the same random
// sequence even if a third party library (we're talking to you,
// fontconfig!) makes uncontrolled calls to random().

#include "random.h"
#include <math.h>
#include <stdlib.h>

static const long BIGGEST = 2147483647; // 2^31-1

// TODO: Make this thread safe

#define STATE_SIZE 128
static char randomstate[STATE_SIZE];
static char *state;

void rndmseed(int seed) {
  char *oldstate = initstate(seed, randomstate, STATE_SIZE);
  state = setstate(oldstate);
}

double rndm() {
  return irndm()/(BIGGEST + 1.0);
}

int irndm() {
  char *oldstate = setstate(state);
  int x = random();
  state = setstate(oldstate);
  return x;
}

// gaussian deviates, copied from numerical recipes

double gasdev() {
  static int saved = 0;
  static double save_me;
  double v1, v2, rsq;
  if(!saved) {
    do {
      v1 = 2.0*rndm() - 1.0;
      v2 = 2.0*rndm() - 1.0;
      rsq = v1*v1 + v2*v2;
    } while(rsq >= 1.0 || rsq == 0);
    
    double fac = sqrt(-2.0*log(rsq)/rsq);
    save_me = v1*fac;
    saved = 1;
    return v2*fac;
  }
  else {
    saved = 0;
    return save_me;
  }
}
