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

#include "common/latticesystem.h"
#include "common/ooferror.h"
#include <map>

typedef std::map<std::string, LatticeSymmetry> LatticeSymmetryMap;

static LatticeSymmetryMap symMap;

void addLatticeSymmetryMatrix(const std::string &symbol,
			      const SmallMatrix *matrix)
{
  LatticeSymmetryMap::iterator iter = symMap.find(symbol);
  if(iter == symMap.end()) {
    std::cerr << "addLatticeSymmetryMatrix: adding symbol " << symbol
     	      << std::endl;
    auto insert = symMap.emplace(symbol, LatticeSymmetry{});
    iter = insert.first;
  }
  LatticeSymmetry &ls = iter->second;
  ls.addMatrix(matrix);
}

const LatticeSymmetry *getLatticeSymmetry(const std::string &symbol) {
  LatticeSymmetryMap::const_iterator iter = symMap.find(symbol);
  assert(iter != symMap.end());
  return &iter->second;
}


#ifdef OLD
static std::map<std::string, const LatticeSystem*> lattices_;

#ifdef DEBUG

void testNegDet() {
  // These matrices are the ones with negative determinants that are
  // commented out of the LatticeSystem constructor arguments below.
  // They're here so that we can be sure that we haven't commented out
  // any that shouldn't have been removed.
  static bool tested = false;
  static const std::vector<SmallMatrix3x3> negDet(
   {
    SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
    SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
    SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
    SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
    SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
    SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
    SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
    SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
    SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, -1),
    SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, -1),
    SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
    SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
    SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
    SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
    SmallMatrix3x3(-1, 1, 0, 0, 1, 0, 0, 0, 1),
    SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
    SmallMatrix3x3(0, 1, 0, -1, 1, 0, 0, 0, -1),
    SmallMatrix3x3(1, -1, 0, 1, 0, 0, 0, 0, -1),
    SmallMatrix3x3(1, 0, 0, 1, -1, 0, 0, 0, 1),
    SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
    SmallMatrix3x3(0, -1, 0, 0, 0, -1, -1, 0, 0),
    SmallMatrix3x3(0, 0, -1, -1, 0, 0, 0, -1, 0),
    SmallMatrix3x3(0, 0, 1, 0, 1, 0, 1, 0, 0),
    SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
    SmallMatrix3x3(1, 0, 0, 0, 0, 1, 0, 1, 0),
    SmallMatrix3x3(-1, 0, 0, -1, 1, 0, 0, 0, 1),
    SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
    SmallMatrix3x3(-1, 1, 0, -1, 0, 0, 0, 0, -1),
    SmallMatrix3x3(-1, 1, 0, 0, 1, 0, 0, 0, 1),
    SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
    SmallMatrix3x3(0, -1, 0, 1, -1, 0, 0, 0, -1),
    SmallMatrix3x3(0, 1, 0, -1, 1, 0, 0, 0, -1),
    SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
    SmallMatrix3x3(1, -1, 0, 0, -1, 0, 0, 0, 1),
    SmallMatrix3x3(1, -1, 0, 1, 0, 0, 0, 0, -1),
    SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
    SmallMatrix3x3(1, 0, 0, 1, -1, 0, 0, 0, 1),
    SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
    SmallMatrix3x3(-1, 0, 0, 0, 0, -1, 0, 1, 0),
    SmallMatrix3x3(-1, 0, 0, 0, 0, 1, 0, -1, 0),
    SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
    SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
    SmallMatrix3x3(0, -1, 0, 0, 0, -1, -1, 0, 0),
    SmallMatrix3x3(0, -1, 0, 0, 0, 1, 1, 0, 0),
    SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, -1),
    SmallMatrix3x3(0, 0, -1, -1, 0, 0, 0, -1, 0),
    SmallMatrix3x3(0, 0, -1, 0, -1, 0, 1, 0, 0),
    SmallMatrix3x3(0, 0, -1, 0, 1, 0, -1, 0, 0),
    SmallMatrix3x3(0, 0, -1, 1, 0, 0, 0, 1, 0),
    SmallMatrix3x3(0, 0, 1, -1, 0, 0, 0, 1, 0),
    SmallMatrix3x3(0, 0, 1, 0, -1, 0, -1, 0, 0),
    SmallMatrix3x3(0, 0, 1, 0, 1, 0, 1, 0, 0),
    SmallMatrix3x3(0, 0, 1, 1, 0, 0, 0, -1, 0),
    SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, -1),
    SmallMatrix3x3(0, 1, 0, 0, 0, -1, 1, 0, 0),
    SmallMatrix3x3(0, 1, 0, 0, 0, 1, -1, 0, 0),
    SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
    SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
    SmallMatrix3x3(1, 0, 0, 0, 0, -1, 0, -1, 0),
    SmallMatrix3x3(1, 0, 0, 0, 0, 1, 0, 1, 0),
    SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1)
   });
  if(!tested) {
    for(const SmallMatrix3x3 &mat : negDet) {
      if(mat.determinant() > 0) {
	std::cerr << "Unexpected positive determinant! " << mat
		  << std::endl;
	exit(1);
      }
    }
  }
  tested = true;
}

#endif // DEBUG


LatticeSystem::LatticeSystem(const std::string &name,
			     std::initializer_list<SmallMatrix3x3> matlist)
  : matrices_(matlist),
    name_(name)
{
  lattices_[name] = this;
  
#ifdef DEBUG
  for(const SmallMatrix3x3 &mat : matrices_) {
    assert(mat.determinant() == 1.0);
  }
  testNegDet();
#endif // DEBUG
}

const LatticeSystem *getLatticeSystem(const std::string &name) {
  auto it = lattices_.find(name);
  assert(it != lattices_.end());
  return it->second;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// In the initializers for the lists of symmetry matrices for each
// lattice system below, the commented-out matrices are symmetry
// operators but are not rotation matrices.


TriclinicLatticeSystem::TriclinicLatticeSystem()
  : LatticeSystem("Triclinic",
  {SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)})
{}

MonoclinicLatticeSystem::MonoclinicLatticeSystem()
  : LatticeSystem("Monoclinic",
  {
   //#SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
   SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, -1),
   //SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
   SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)
  })
{}

OrthorhombicLatticeSystem::OrthorhombicLatticeSystem()
  : LatticeSystem("Orthorhombic",
  {
   //SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
   SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, 1),
   SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, -1),
   //SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
   SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, -1),
   //SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
   //SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
   SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)
  })
{}

TetragonalLatticeSystem::TetragonalLatticeSystem()
  : LatticeSystem("Tetragonal",
  {
   //SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
   SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, 1),
   SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, -1),
   //SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
   SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, -1),
   //SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
   //SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, -1),
   SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, 1),
   //SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, -1),
   SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, 1),
   SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, -1),
   //SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
   SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, -1),
   //SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
   //SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
   SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)
  })
{}

TrigonalLatticeSystem::TrigonalLatticeSystem()
  : LatticeSystem("Trigonal",
  {
   SmallMatrix3x3(-1, 0, 0, -1, 1, 0, 0, 0, -1),
   //SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
   SmallMatrix3x3(-1, 1, 0, -1, 0, 0, 0, 0, 1),
   //SmallMatrix3x3(-1, 1, 0, 0, 1, 0, 0, 0, 1),
   //SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
   SmallMatrix3x3(0, -1, 0, 1, -1, 0, 0, 0, 1),
   //SmallMatrix3x3(0, 1, 0, -1, 1, 0, 0, 0, -1),
   SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, -1),
   SmallMatrix3x3(1, -1, 0, 0, -1, 0, 0, 0, -1),
   //SmallMatrix3x3(1, -1, 0, 1, 0, 0, 0, 0, -1),
   SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1),
   //SmallMatrix3x3(1, 0, 0, 1, -1, 0, 0, 0, 1)
  })
{}

RhombohedralLatticeSystem::RhombohedralLatticeSystem()
  : LatticeSystem("Rhombohedral",
  {
   //SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
   SmallMatrix3x3(-1, 0, 0, 0, 0, -1, 0, -1, 0),
   SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, -1),
   //SmallMatrix3x3(0, -1, 0, 0, 0, -1, -1, 0, 0),
   //SmallMatrix3x3(0, 0, -1, -1, 0, 0, 0, -1, 0),
   SmallMatrix3x3(0, 0, -1, 0, -1, 0, -1, 0, 0),
   //SmallMatrix3x3(0, 0, 1, 0, 1, 0, 1, 0, 0),
   SmallMatrix3x3(0, 0, 1, 1, 0, 0, 0, 1, 0),
   SmallMatrix3x3(0, 1, 0, 0, 0, 1, 1, 0, 0),
   //SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
   //SmallMatrix3x3(1, 0, 0, 0, 0, 1, 0, 1, 0),
   SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)
  })
{}

HexagonalLatticeSystem::HexagonalLatticeSystem()
  : LatticeSystem("Hexagonal",
  {
   SmallMatrix3x3(-1, 0, 0, -1, 1, 0, 0, 0, -1),
   //SmallMatrix3x3(-1, 0, 0, -1, 1, 0, 0, 0, 1),
   //SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
   SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, 1),
   //SmallMatrix3x3(-1, 1, 0, -1, 0, 0, 0, 0, -1),
   SmallMatrix3x3(-1, 1, 0, -1, 0, 0, 0, 0, 1),
   SmallMatrix3x3(-1, 1, 0, 0, 1, 0, 0, 0, -1),
   //SmallMatrix3x3(-1, 1, 0, 0, 1, 0, 0, 0, 1),
   SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, -1),
   //SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
   //SmallMatrix3x3(0, -1, 0, 1, -1, 0, 0, 0, -1),
   SmallMatrix3x3(0, -1, 0, 1, -1, 0, 0, 0, 1),
   //SmallMatrix3x3(0, 1, 0, -1, 1, 0, 0, 0, -1),
   SmallMatrix3x3(0, 1, 0, -1, 1, 0, 0, 0, 1),
   SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, -1),
   //SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
   SmallMatrix3x3(1, -1, 0, 0, -1, 0, 0, 0, -1),
   //SmallMatrix3x3(1, -1, 0, 0, -1, 0, 0, 0, 1),
   //SmallMatrix3x3(1, -1, 0, 1, 0, 0, 0, 0, -1),
   SmallMatrix3x3(1, -1, 0, 1, 0, 0, 0, 0, 1),
   //SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
   SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1),
   SmallMatrix3x3(1, 0, 0, 1, -1, 0, 0, 0, -1),
   //SmallMatrix3x3(1, 0, 0, 1, -1, 0, 0, 0, 1)
  })
{}

CubicLatticeSystem::CubicLatticeSystem()
  : LatticeSystem("Cubic",
  {
   //SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
   SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, 1),
   SmallMatrix3x3(-1, 0, 0, 0, 0, -1, 0, -1, 0),
   //SmallMatrix3x3(-1, 0, 0, 0, 0, -1, 0, 1, 0),
   //SmallMatrix3x3(-1, 0, 0, 0, 0, 1, 0, -1, 0),
   SmallMatrix3x3(-1, 0, 0, 0, 0, 1, 0, 1, 0),
   SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, -1),
   //SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
   SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, -1),
   //SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
   //SmallMatrix3x3(0, -1, 0, 0, 0, -1, -1, 0, 0),
   SmallMatrix3x3(0, -1, 0, 0, 0, -1, 1, 0, 0),
   SmallMatrix3x3(0, -1, 0, 0, 0, 1, -1, 0, 0),
   //SmallMatrix3x3(0, -1, 0, 0, 0, 1, 1, 0, 0),
   //SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, -1),
   SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, 1),
   //SmallMatrix3x3(0, 0, -1, -1, 0, 0, 0, -1, 0),
   SmallMatrix3x3(0, 0, -1, -1, 0, 0, 0, 1, 0),
   SmallMatrix3x3(0, 0, -1, 0, -1, 0, -1, 0, 0),
   //SmallMatrix3x3(0, 0, -1, 0, -1, 0, 1, 0, 0),
   //SmallMatrix3x3(0, 0, -1, 0, 1, 0, -1, 0, 0),
   SmallMatrix3x3(0, 0, -1, 0, 1, 0, 1, 0, 0),
   SmallMatrix3x3(0, 0, -1, 1, 0, 0, 0, -1, 0),
   //SmallMatrix3x3(0, 0, -1, 1, 0, 0, 0, 1, 0),
   SmallMatrix3x3(0, 0, 1, -1, 0, 0, 0, -1, 0),
   //SmallMatrix3x3(0, 0, 1, -1, 0, 0, 0, 1, 0),
   //SmallMatrix3x3(0, 0, 1, 0, -1, 0, -1, 0, 0),
   SmallMatrix3x3(0, 0, 1, 0, -1, 0, 1, 0, 0),
   SmallMatrix3x3(0, 0, 1, 0, 1, 0, -1, 0, 0),
   //SmallMatrix3x3(0, 0, 1, 0, 1, 0, 1, 0, 0),
   //SmallMatrix3x3(0, 0, 1, 1, 0, 0, 0, -1, 0),
   SmallMatrix3x3(0, 0, 1, 1, 0, 0, 0, 1, 0),
   //SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, -1),
   SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, 1),
   SmallMatrix3x3(0, 1, 0, 0, 0, -1, -1, 0, 0),
   //SmallMatrix3x3(0, 1, 0, 0, 0, -1, 1, 0, 0),
   //SmallMatrix3x3(0, 1, 0, 0, 0, 1, -1, 0, 0),
   SmallMatrix3x3(0, 1, 0, 0, 0, 1, 1, 0, 0),
   SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, -1),
   //SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
   SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, -1),
   //SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
   //SmallMatrix3x3(1, 0, 0, 0, 0, -1, 0, -1, 0),
   SmallMatrix3x3(1, 0, 0, 0, 0, -1, 0, 1, 0),
   SmallMatrix3x3(1, 0, 0, 0, 0, 1, 0, -1, 0),
   //SmallMatrix3x3(1, 0, 0, 0, 0, 1, 0, 1, 0),
   //SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
   SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)
  })
{}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Create singleton instances of each lattice system.

static const TriclinicLatticeSystem triclinic;
static const MonoclinicLatticeSystem monoclinic;
static const OrthorhombicLatticeSystem orthorhombic;
static const TetragonalLatticeSystem tetragonal;
static const TrigonalLatticeSystem trigonal;
static const RhombohedralLatticeSystem rhombohedral;
static const HexagonalLatticeSystem hexagonal;
static const CubicLatticeSystem cubic;
#endif // OLD
