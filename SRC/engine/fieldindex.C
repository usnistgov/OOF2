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

const std::string &EmptyFieldIterator::classname() const {
  static const std::string nm("EmptyFieldIterator");
  return nm;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::vector<int> *ScalarFieldIndex::getComponents() const {
  return new std::vector<int>;	// empty vector
}

const std::string &ScalarFieldIndex::shortstring() const {
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

const std::string& ScalarFieldCompIterator::classname() const {
  static const std::string nm("ScalarFieldCompIterator");
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

IndexP ScalarFieldCompIterator::operator*() const {
  assert(!done);
  return IndexP(new ScalarFieldIndex());
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

const std::string &VectorFieldIndex::classname() const {
  static const std::string nm("VectorFieldIndex");
  return nm;
}

std::vector<int> *VectorFieldIndex::getComponents() const {
  std::vector<int> *c = new std::vector<int>(1);
  (*c)[0] = index_;
  return c;
}

const std::string &VectorFieldIndex::shortstring() const {
  static const std::string names[] = {std::string("x"),
				      std::string("y"), 
				      std::string("z")};
  return names[index_];
}

void VectorFieldIndex::print(std::ostream &os) const {
  os << "VectorFieldIndex(" << index_ << ")";
}

const std::string& VectorFieldCompIterator::classname() const {
  static const std::string nm("VectorFieldCompIterator");
  return nm;
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

const std::string &OutOfPlaneVectorFieldCompIterator::classname() const {
  static const std::string nm("OutOfPlaneVectorFieldCompIterator");
  return nm;
}

bool OutOfPlaneVectorFieldCompIterator::operator!=(
					   const ComponentIterator &othr) const
{
  const OutOfPlaneVectorFieldCompIterator &other =
    dynamic_cast<const OutOfPlaneVectorFieldCompIterator&>(othr);
  return other.index != index;
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

const std::string &SymTensorIterator::classname() const {
  static const std::string nm("SymTensorIterator");
  return nm;
}

const std::string &SymTensorInPlaneIterator::classname() const {
  static const std::string nm("SymTensorInPlaneIterator");
  return nm;
}

const std::string &SymTensorOutOfPlaneIterator::classname() const {
  static const std::string nm("SymTensorOutOfPlaneIterator");
  return nm;
}

const std::string &OutOfPlaneSymTensorIterator::classname() const {
  static const std::string nm("OutOfPlaneSymTensorIterator");
  return nm;
}

IndexP SymTensorIterator::operator*() const {
  return IndexP(new SymTensorIndex(v));
}

IndexP OutOfPlaneSymTensorIterator::operator*() const {
  return IndexP(new OutOfPlaneSymTensorIndex(v));
}

// TODO PYTHON3: Get rid of this method.
std::vector<int> *SymTensorIndex::getComponents() const {
  std::vector<int> *c = new std::vector<int>(2);
  (*c)[0] = rowset[v];
  (*c)[1] = colset[v];
  return c;
}

const std::string &SymTensorIndex::shortstring() const {
  static const std::string voigt[] = {"xx", "yy", "zz", "yz", "xz", "xy"};
  return voigt[v];
}

void SymTensorIndex::print(std::ostream &os) const {
  os << "SymTensorIndex(" << row() << "," << col() << ")";
}

// SymTensor components are often needed independent of a flux or
// field, so they can be retrieved from this.
SymTensorIJComponents symTensorIJComponents;
