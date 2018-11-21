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
#include <map>

typedef std::map<std::string, const LatticeSystem*> LatMap;
static LatMap lattices_;

LatticeSystem::LatticeSystem(const std::string &name,
			     std::initializer_list<SmallMatrix3x3> matlist)
  : matrices_(matlist),
    name_(name)
{
  lattices_[name] = this;
}

const LatticeSystem *getLatticeSystem(const std::string &name) {
  LatMap::const_iterator it = lattices_.find(name);
  assert(it != lattices_.end());
  return it->second;
}

TriclinicLatticeSystem::TriclinicLatticeSystem()
  : LatticeSystem("Triclinic",
  {SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)})
{}

MonoclinicLatticeSystem::MonoclinicLatticeSystem()
  : LatticeSystem("Monoclinic",
        {SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)})
{}

OrthorhombicLatticeSystem::OrthorhombicLatticeSystem()
  : LatticeSystem("Orthorhombic",
        {SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)})

{}

TetragonalLatticeSystem::TetragonalLatticeSystem()
  : LatticeSystem("Tetragonal",
        {SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)})
{}

TrigonalLatticeSystem::TrigonalLatticeSystem()
  : LatticeSystem("Trigonal",
        {SmallMatrix3x3(-1, 0, 0, -1, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 1, 0, -1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(-1, 1, 0, 0, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(0, -1, 0, 1, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(0, 1, 0, -1, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(1, -1, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, -1, 0, 1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 1, -1, 0, 0, 0, 1)})
{}

RhombohedralLatticeSystem::RhombohedralLatticeSystem()
  : LatticeSystem("Rhombohedral",
        {SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, 0, -1, 0, -1, 0),
	 SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, -1, 0, 0, 0, -1, -1, 0, 0),
	 SmallMatrix3x3(0, 0, -1, -1, 0, 0, 0, -1, 0),
	 SmallMatrix3x3(0, 0, -1, 0, -1, 0, -1, 0, 0),
	 SmallMatrix3x3(0, 0, 1, 0, 1, 0, 1, 0, 0),
	 SmallMatrix3x3(0, 0, 1, 1, 0, 0, 0, 1, 0),
	 SmallMatrix3x3(0, 1, 0, 0, 0, 1, 1, 0, 0),
	 SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, 0, 1, 0, 1, 0),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)})
{}

HexagonalLatticeSystem::HexagonalLatticeSystem()
  : LatticeSystem("Hexagonal",
        {SmallMatrix3x3(-1, 0, 0, -1, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, -1, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(-1, 1, 0, -1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 1, 0, -1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(-1, 1, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 1, 0, 0, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(0, -1, 0, 1, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(0, -1, 0, 1, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(0, 1, 0, -1, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(0, 1, 0, -1, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(1, -1, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, -1, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(1, -1, 0, 1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(1, -1, 0, 1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 1, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 1, -1, 0, 0, 0, 1)})
{}

CubicLatticeSystem::CubicLatticeSystem()
  : LatticeSystem("Cubic",
        {SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(-1, 0, 0, 0, 0, -1, 0, -1, 0),
	 SmallMatrix3x3(-1, 0, 0, 0, 0, -1, 0, 1, 0),
	 SmallMatrix3x3(-1, 0, 0, 0, 0, 1, 0, -1, 0),
	 SmallMatrix3x3(-1, 0, 0, 0, 0, 1, 0, 1, 0),
	 SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(-1, 0, 0, 0, 1, 0, 0, 0, 1),
	 SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, -1, 0, -1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(0, -1, 0, 0, 0, -1, -1, 0, 0),
	 SmallMatrix3x3(0, -1, 0, 0, 0, -1, 1, 0, 0),
	 SmallMatrix3x3(0, -1, 0, 0, 0, 1, -1, 0, 0),
	 SmallMatrix3x3(0, -1, 0, 0, 0, 1, 1, 0, 0),
	 SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, -1, 0, 1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(0, 0, -1, -1, 0, 0, 0, -1, 0),
	 SmallMatrix3x3(0, 0, -1, -1, 0, 0, 0, 1, 0),
	 SmallMatrix3x3(0, 0, -1, 0, -1, 0, -1, 0, 0),
	 SmallMatrix3x3(0, 0, -1, 0, -1, 0, 1, 0, 0),
	 SmallMatrix3x3(0, 0, -1, 0, 1, 0, -1, 0, 0),
	 SmallMatrix3x3(0, 0, -1, 0, 1, 0, 1, 0, 0),
	 SmallMatrix3x3(0, 0, -1, 1, 0, 0, 0, -1, 0),
	 SmallMatrix3x3(0, 0, -1, 1, 0, 0, 0, 1, 0),
	 SmallMatrix3x3(0, 0, 1, -1, 0, 0, 0, -1, 0),
	 SmallMatrix3x3(0, 0, 1, -1, 0, 0, 0, 1, 0),
	 SmallMatrix3x3(0, 0, 1, 0, -1, 0, -1, 0, 0),
	 SmallMatrix3x3(0, 0, 1, 0, -1, 0, 1, 0, 0),
	 SmallMatrix3x3(0, 0, 1, 0, 1, 0, -1, 0, 0),
	 SmallMatrix3x3(0, 0, 1, 0, 1, 0, 1, 0, 0),
	 SmallMatrix3x3(0, 0, 1, 1, 0, 0, 0, -1, 0),
	 SmallMatrix3x3(0, 0, 1, 1, 0, 0, 0, 1, 0),
	 SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, 1, 0, -1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(0, 1, 0, 0, 0, -1, -1, 0, 0),
	 SmallMatrix3x3(0, 1, 0, 0, 0, -1, 1, 0, 0),
	 SmallMatrix3x3(0, 1, 0, 0, 0, 1, -1, 0, 0),
	 SmallMatrix3x3(0, 1, 0, 0, 0, 1, 1, 0, 0),
	 SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, -1),
	 SmallMatrix3x3(0, 1, 0, 1, 0, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, -1, 0, 0, 0, 1),
	 SmallMatrix3x3(1, 0, 0, 0, 0, -1, 0, -1, 0),
	 SmallMatrix3x3(1, 0, 0, 0, 0, -1, 0, 1, 0),
	 SmallMatrix3x3(1, 0, 0, 0, 0, 1, 0, -1, 0),
	 SmallMatrix3x3(1, 0, 0, 0, 0, 1, 0, 1, 0),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, -1),
	 SmallMatrix3x3(1, 0, 0, 0, 1, 0, 0, 0, 1)})
{}

// Create singleton instances of each lattice system.

static const TriclinicLatticeSystem triclinic;
static const MonoclinicLatticeSystem monoclinic;
static const OrthorhombicLatticeSystem orthorhombic;
static const TetragonalLatticeSystem tetragonal;
static const TrigonalLatticeSystem trigonal;
static const RhombohedralLatticeSystem rhombohedral;
static const HexagonalLatticeSystem hexagonal;
static const CubicLatticeSystem cubic;
