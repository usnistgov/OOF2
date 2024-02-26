// -*- C++ -*-
// $RCSfile: nonconstant_heat_source_example.h,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2011-02-17 22:44:21 $


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@ctcms.nist.gov.
 */

#ifndef %HEADER%
#define %HEADER%

#include "engine/property/heatsource/nonconstant/nonconstant_heat_source.h"
#include <string>

class %CLASS% : public NonconstantHeatSource {

private:
  double parameter1, parameter2;

public:
  %CLASS%(PyObject *registry, const std::string &name,
			       double param1, double param2)
    : NonconstantHeatSource( registry, name ),
      parameter1( param1 ), parameter2( param2 ) {};
  virtual ~%CLASS%() {};

protected:

  virtual double nonconst_heat_source(double x, double y, double z, double time) const;
};

#endif	// %HEADER%
