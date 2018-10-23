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

#ifndef BURN_H
#define BURN_H

#include "common/ccolor.h"
#include "common/boolarray.h"
#include <vector>
class ICoord;
class OOFImage;

template <class BURNABLE, class IMAGE>
class Burner {
public:
  bool next_nearest;		// parameter
  Burner(bool nn) : next_nearest(nn) {};
  virtual ~Burner() {};
  void burn(const IMAGE&, const ICoord*, BoolArray&);
  virtual bool spread(const BURNABLE &from, const BURNABLE &to) const = 0;
protected:
  CColor startcolor;
private:
  void burn_nbrs(const IMAGE&, std::vector<ICoord>&,
		 BoolArray&, int&, const ICoord&);

  // List of directions to neighbors. There is one static instance of
  // this class.
  class Nbr {
  private:
    ICoord nbr[8];
    Nbr();			// loads the directions into the array.
    const ICoord &operator[](int x) const { return nbr[x]; }
    friend class Burner;
  };
  static Nbr neighbor;
};

class BasicBurner : public Burner<CColor, OOFImage> {
public:
  double local_flammability;
  double global_flammability;
  bool useL2norm;
  BasicBurner(double lcl, double glbl, bool L2norm, bool nn)
    : Burner(nn),
      local_flammability(lcl),
      global_flammability(glbl),
      useL2norm(L2norm)
  {}
  virtual bool spread(const CColor &from, const CColor &to) const;
};

#endif // BURN_H
