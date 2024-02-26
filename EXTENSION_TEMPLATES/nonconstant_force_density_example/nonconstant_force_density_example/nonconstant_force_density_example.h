// -*- C++ -*-
// $RCSfile: nonconstant_force_density_example.h,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2011-02-17 22:44:13 $


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

#include "engine/property/forcedensity/nonconstant/nonconstant_force_density.h"
#include <string>

class DoubleVec;

class %CLASS% : public NonconstantForceDensity {

private:
  double parameter1, parameter2;

public:
  %CLASS%(PyObject *registry, const std::string &name,
				 double param1, double param2)
    : NonconstantForceDensity( registry, name ),
      parameter1( param1 ), parameter2( param2 ) {};
  virtual ~%CLASS%() {};

protected:

  virtual void nonconst_force_density(double x, double y, double z,
				      double time, DoubleVec &result) const;
};

#endif	// %HEADER%
