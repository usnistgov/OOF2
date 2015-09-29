// -*- C++ -*-
// $RCSfile: nodegroup.h,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2014/09/27 21:40:48 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef NODEGROUP_H
#define NODEGROUP_H

#include "group.h"

class FEMesh;

class NodeGroup : public Group<Node*> {

};

class FiniteNodeGroup : public NodeGroup {

};

class GlobalNodeGroup : public NodeGroup {
  // This should override most virtual functions inherited from Group
 private:
  FEMesh *mesh;
 public:
  GlobalNodeGroup(FEMesh *);
};

#endif
