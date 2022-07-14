// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CFIDDLENODESBASEPARALLEL_SWG
#define CFIDDLENODESBASEPARALLEL_SWG

%module(package="ooflib.SWIG.engine") cfiddlenodesbaseParallel

%include "common/typemaps.swg"

%{
#include "engine/cfiddlenodesbaseParallel.h"
%}

MAKE_LISTVEC_TYPEMAPS(CFiddleNodesMoveData);

class CFiddleNodesMoveData {
public:
  CFiddleNodesMoveData(int, int, double, double);
  int master;
  int index;
  double x;
  double y;
};

void tuneFiddle();
CFiddleNodesMoveData create_movedata(int, int, double, double);
void _Send_MoveData(CFiddleNodesMoveDataVec*, IntVec*, int);
void _Isend_MoveData(CFiddleNodesMoveDataVec*, IntVec*, int);
CFiddleNodesMoveData _Recv_MoveData(int, int);

%pythoncode "engine/cfiddlenodesbaseParallel.spy"
#endif // CFIDDLENODEBASEPARALLEL_SWG
