// -*- C++ -*-
// $RCSfile: blockpre.h,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2010/12/05 05:06:20 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

OBSOLETE

#include <oofconfig.h>

#ifndef BLOCKPRE_H
#define BLOCKPRE_H

#include "engine/preconditioner.h"
#include "engine/smallmatrix.h"
#include "engine/sparsemat.h"

#include <map>
#include <vector>

class UnitPreconditioner;

// The "Block" class represents the actual blocks inside the
// preconditioners.  They know the local block matrix, in dense form.
// The relationship between local block rows and cols and main-matrix
// rows and cols is encoded in the "rows" and "cols" vector, each
// element of which is the row/col in the main matrix to which that
// position corresponds, i.e. element (i,j) of the block corresponds
// to element (rows[i], cols[j]) of the main matrix.

class Block {
private:
  int id_;
  std::vector<int> rows, cols;
  SmallMatrix *mtx, *rhs;
public:
  Block(int);
  ~Block();

  int id() const { return id_; }
  int nrows() const { return rows.size(); }
  int ncols() const { return cols.size(); }

  void new_row(int);
  void new_col(int);
  
  void assign(const SparseMat &);
  void assign_rhs(const std::vector<double> &);

  void solve(std::vector<double> &);
  void trans_solve(std::vector<double> &);
};


typedef std::map<int, Block> Blockmap;

// The block preconditioner takes a list of row and column group
// identities.  Zero and positive integers define "regular blocks",
// and negative integers define a single "special block".  The special
// block is presumed to be large, and is preconditioned separately.
// The regular blocks are presumed to be small enough to be
// efficiently directly solved.  The preconditioner M consists of the
// preconditioned special block, and the sum of the regular blocks.
// Matrix elements which are outside of any block are excluded from M.

class BlockPreconditionerCore : public PreconditionerBase {
private:
  std::vector<double> diags;
  PreconditionerBase *subconditioner;
  const std::vector<int> &rowgroups, &colgroups;
  mutable Blockmap blocks; // Blocks get modified during "solve".
  // These are maps used to extract the in-plane submatrix.
  std::vector<int> in_plane_rows, in_plane_cols;
  SparseMat A_inplane;
  
 public:
  BlockPreconditionerCore(const SparseMat &A,
				     const std::vector<int> &rowgroups,
				     const std::vector<int> &colgroups,
				     UnitPreconditioner *inplane);
  ~BlockPreconditionerCore(void);

  std::vector<double> solve(const std::vector<double> &x) const;
  std::vector<double> trans_solve(const std::vector<double> &x) const;

  static const std::string classname_;
  virtual const std::string &classname() const { return classname_; }
  static const std::string modulename_;
  virtual const std::string &modulename() const { return modulename_; }

};



#endif // BLOCKPRE_H
