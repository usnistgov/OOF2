// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#include <oofconfig.h>

#include "engine/edge.h"
#include "engine/edgeset.h"
#include "engine/element.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/gausspoint.h"
#include "engine/outputval.h"

//#include "engine/SparseLib++/mvblasd.h"

#include <vector>

// Helper function for integrating the flux through a boundary.
ArithmeticOutputValue integrateFlux(const FEMesh *mesh, const Flux *flux,
				    const EdgeSet *es)
{
  ArithmeticOutputVal *resultptr = 0;
  for(EdgeSetIterator esi=es->edge_iterator(); !esi.end(); ++esi) {
    BoundaryEdge *bdy_edge = esi.edge();
    const Element *el = bdy_edge->el;
    int order = el->shapefun_degree();
    for(EdgeGaussPoint egpt=bdy_edge->integrator(order); !egpt.end(); ++egpt) {
      if(!resultptr) {
	resultptr = flux->contract( mesh, el, egpt );
	*resultptr *= egpt.weight();
      }
      else {
	ArithmeticOutputVal *r = flux->contract( mesh, el, egpt );
	*r *= egpt.weight();
	*resultptr += *r;
	delete r;
      }
    }
  }
  return ArithmeticOutputValue(resultptr);
}

ArithmeticOutputValue averageField(const FEMesh *m, const Field *field,
				   const EdgeSet *es)
{
  ArithmeticOutputValue result(field->newOutputValue());
  double weight = 0.0;
  for(EdgeSetIterator esi=es->edge_iterator(); !esi.end(); ++esi) {
    BoundaryEdge *bdy_edge = esi.edge();
    const Element *el = bdy_edge->el;
    int order = el->shapefun_degree();

    for(EdgeGaussPoint egpt=bdy_edge->integrator(order); !egpt.end(); ++egpt) {
      double w = egpt.weight();
      result += el->outputField(m, *field, egpt.mastercoord())*w;
      weight += w;
    }
  }
  return result/weight;
}
