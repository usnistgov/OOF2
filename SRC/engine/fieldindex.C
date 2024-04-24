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
#include "fieldindex.h"
#include "outputval.h"
#include "common/tostring.h"

bool operator==(const FieldIndex &a, const FieldIndex &b) {
  return a.integer() == b.integer();
}

std::ostream &operator<<(std::ostream &os, const FieldIndex &fi) {
  fi.print(os);
  return os;
}

std::ostream &operator<<(std::ostream &os, const IndexP &ip) {
  const FieldIndex &fi(ip);
  os << "IndexP(" << fi << ")";
  return os;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

const std::string &ScalarFieldIndex::shortrepr() const {
  static std::string ss("");
  return ss;
}

void ScalarFieldIndex::print(std::ostream &os) const {
  os << "ScalarFieldIndex()";
}

const std::string& ScalarFieldIndex::classname() const {
  static const std::string nm("ScalarFieldIndex");
  return nm;
}

ScalarFieldCompIterator &ScalarFieldCompIterator::operator++() {
  done = true;
  return *this;
}

bool ScalarFieldCompIterator::operator!=(const ComponentIterator &othr) const {
  const ScalarFieldCompIterator& other =
    dynamic_cast<const ScalarFieldCompIterator&>(othr);
  return other.done != done;
}

FieldIndex *ScalarFieldCompIterator::fieldindex() const {
  assert(!done);
  return new ScalarFieldIndex();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

const std::string &VectorFieldIndex::classname() const {
  static const std::string nm("VectorFieldIndex");
  return nm;
}

const std::string &VectorFieldIndex::shortrepr() const {
  static const std::string names[] = {std::string("x"),
				      std::string("y"), 
				      std::string("z")};
  return names[index_];
}

void VectorFieldIndex::print(std::ostream &os) const {
  os << "VectorFieldIndex(" << index_ << ")";
}

bool VectorFieldCompIterator::operator!=(const ComponentIterator &othr) const {
  const VectorFieldCompIterator &other =
    dynamic_cast<const VectorFieldCompIterator&>(othr);
  return other.index != index;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

const std::string &OutOfPlaneVectorFieldIndex::classname() const {
  static const std::string nm("OutOfPlaneVectorFieldIndex");
  return nm;
}

bool OutOfPlaneVectorFieldCompIterator::operator!=(
					   const ComponentIterator &othr) const
{
  const OutOfPlaneVectorFieldCompIterator &other =
    dynamic_cast<const OutOfPlaneVectorFieldCompIterator&>(othr);
  return other.index != index;
}

void OutOfPlaneVectorFieldIndex::print(std::ostream &os) const {
  os << "OutOfPlaneVectorFieldIndex(" << index_ << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

static const int rowset[] = { 0, 1, 2, 1, 0, 0 };
static const int colset[] = { 0, 1, 2, 2, 2, 1 };

const std::string &SymTensorIndex::classname() const {
  static const std::string nm("SymTensorIndex");
  return nm;
}

const std::string &OutOfPlaneSymTensorIndex::classname() const {
  static const std::string nm("OutOfPlaneSymTensorIndex");
  return nm;
}

int SymTensorIndex::row() const {
  return rowset[v];
}

int SymTensorIndex::col() const {
  return colset[v];
}

int SymTensorIterator::row() const {
  return rowset[v];
}

int SymTensorIterator::col() const {
  return colset[v];
}

SymTensorIterator::SymTensorIterator(SpaceIndex i, SpaceIndex j)
  : v(SymTensorIndex::ij2voigt(i, j))
{}


bool SymTensorIterator::operator!=(const ComponentIterator &othr) const {
  const SymTensorIterator &other =
    dynamic_cast<const SymTensorIterator&>(othr);
  return other.v != v;
}

const std::string &SymTensorIndex::shortrepr() const {
  static const std::string voigt[] = {"xx", "yy", "zz", "yz", "xz", "xy"};
  return voigt[v];
}

void SymTensorIndex::print(std::ostream &os) const {
  os << "SymTensorIndex(" << row() << "," << col() << ")";
}

void OutOfPlaneSymTensorIndex::print(std::ostream &os) const {
  os << "OutOfPlaneSymTensorIndex(" << row() << ", " << col() << ")";
}

// SymTensor components are often needed independent of a flux or
// field, so they can be retrieved from this...
// TODO: This should be const.
SymTensorIJComponents symTensorIJComponents;

// ... or via this which is more like the other field index machinery
const Components* getSymTensorComponents(Planarity plan) {
  if(plan == IN_PLANE) {
    static const SymTensorInPlaneComponents inplane;
    return &inplane;
  }
  else if(plan == OUT_OF_PLANE) {
    static const SymTensorOutOfPlaneComponents outplane;
    return &outplane;
  }
  static const SymTensorComponents comps;
  return &comps;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const ComponentIterator &ci) {
  ci.print(os);
  return os;
}

std::ostream &operator<<(std::ostream &os, const ComponentIteratorP &cip) {
  os << "ComponentIteratorP(";
  cip.iterator()->print(os);
  os << ")";
  return os;
}

void EmptyFieldIterator::print(std::ostream& os) const {
  os << "EmptyFieldIterator";
}

void ScalarFieldCompIterator::print(std::ostream &os) const {
  os << "ScalarFieldCompIterator(" << (done?"done":"not done") << ")";
}

void VectorFieldCompIterator::print(std::ostream &os) const {
  os << "VectorFieldCompIterator(" << index << ")";
}

void OutOfPlaneVectorFieldCompIterator::print(std::ostream &os) const {
  os << "OutOfPlaneVectorFieldCompIterator(" << index << ")";
}

void SymTensorIterator::print(std::ostream &os) const {
  os << "SymTensorIterator(" << v << ")";
}

void SymTensorInPlaneIterator::print(std::ostream &os) const {
  os << "SymTensorInPlaneIterator(" << v << ")";
}

void SymTensorOutOfPlaneIterator::print(std::ostream &os) const {
  os << "SymTensorOutOfPlaneIterator(" << v << ")";
}

void OutOfPlaneSymTensorIterator::print(std::ostream &os) const {
  os << "OutOfPlaneSymTensorIterator(" << v << ")";
}

std::ostream &operator<<(std::ostream &os, const SymTensorIJIterator &it) {
  os << "SymTensorIJIterator(" << it.v << ")";
  return os;
}
