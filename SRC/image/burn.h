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

#include "common/activearea.h"
#include "common/ccolor.h"
#include "common/boolarray.h"
#include <vector>
class ICoord;
class OOFImage;


class BurnerBase {
protected:
  // Nbr holds a list of directions to neighbors. There is one static
  // instance of this class.
  class Nbr {
  private:
    ICoord nbr[8];
    Nbr();			// loads the directions into the array.
    const ICoord &operator[](int x) const { return nbr[x]; }
    friend class BurnerBase;
    template <typename BURNABLE, typename IMAGE> friend class Burner;
  };
  static Nbr neighbor;
};

template <class BURNABLE, class IMAGE>
class Burner : public BurnerBase {
public:
  Burner(bool nn) : next_nearest(nn), activeArea(nullptr) {};
  virtual ~Burner() {};
  void burn(const IMAGE&, const ICoord*, BoolArray&);
  virtual bool spread(const BURNABLE &from, const BURNABLE &to) const = 0;
protected:
  bool next_nearest;		// parameter
  BURNABLE startvalue;
  const ActiveArea *activeArea;
private:
  void burn_nbrs(const IMAGE&, std::vector<ICoord>&,
		 BoolArray&, int&, const ICoord&);

};

template <class BURNABLE, class IMAGE>
void Burner<BURNABLE, IMAGE>::burn(const IMAGE &image, const ICoord *spark,
				   BoolArray &burned)
{
  // Initialize the data structures.
  int nburnt = 0;
  startvalue = image[spark];
  activeArea = image.getCMicrostructure()->getActiveArea();
  std::vector<ICoord> activesites; // sites whose neighbors have to be checked
  activesites.reserve(image.sizeInPixels()(0)*image.sizeInPixels()(1));

  // burn the first pixel
  burned[*spark] = true;
  nburnt++;
  activesites.push_back(*spark);

  while(activesites.size() > 0) {
    // Remove the last site in the active list, burn its neighbors,
    // and add them to the list.
    const ICoord here = activesites.back();
    activesites.pop_back();
    burn_nbrs(image, activesites, burned, nburnt, here);
  }
}

template <class BURNABLE, class IMAGE>
void Burner<BURNABLE, IMAGE>::burn_nbrs(const IMAGE &image,
				 std::vector<ICoord> &activesites,
				 BoolArray &burned, int &nburnt,
				 const ICoord &here) {
  // Burn neighboring pixels and put them in the active list.
  // const ActiveArea *aa = microstructure->getActiveArea();
  int nbrmax = (next_nearest? 8 : 4);
  BURNABLE thiscolor(image[here]);
  for(int i=0; i<nbrmax; i++) {
    ICoord target = here + neighbor[i];
    if(activeArea->isActive(&target)
       && burned.contains(target)
       && !burned[target]
       && spread(thiscolor, image[target]))
      {
	burned[target] = true;
	nburnt++;
	activesites.push_back(target);
      }
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

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
