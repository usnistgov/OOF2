// -*- C++ -*-
// $RCSfile: edge3.C,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:41:05 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "engine/masterelement.h"
#include "edge3shapefunction.h"
#include "common/trace.h"

// Master element for the 3-noded edge element:
//
//     0----------1------------2
//  (-1,0)       (0,0)       (1,0)
// Here, the y-component of master-coord is totally trivial.


class Edge3MasterElement : public EdgeMaster{
public:
  Edge3MasterElement():
    //Interface branch
    EdgeMaster("D3_3","Isoparametric 3-noded edge element", 3, 0)
		    //    EdgeMaster("Isoparametric 3-noded edge element", 3)
  {
    shapefunction = new Edge3ShapeFunction(*this);
    mapfunction = shapefunction;

    ProtoNode *pn0 = addProtoNode(MasterCoord(-1., 0.));
    pn0->set_mapping();
    pn0->set_func();
    // not sure about these two ...
    pn0->set_corner();
    pn0->on_edge(0);

    ProtoNode *pn1 = addProtoNode(MasterCoord(0., 0.));
    pn1->set_mapping();
    pn1->set_func();
    // not sure about the edge thing ...
    pn1->on_edge(0);

    ProtoNode *pn2 = addProtoNode(MasterCoord(1., 0.));
    pn2->set_mapping();
    pn2->set_func();
    // not sure about these two ...
    pn2->set_corner();
    pn2->on_edge(0);
  }

  virtual ~Edge3MasterElement(){
    delete shapefunction;
  }

  int map_order() const {
    return 2;
  }
  int fun_order() const {
    return 2;
  }

};

static Edge3MasterElement m;
