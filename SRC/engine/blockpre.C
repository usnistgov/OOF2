// -*- C++ -*-
// $RCSfile: blockpre.C,v $
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

#include "common/printvec.h"
#include "engine/blockpre.h"
#include <iostream>

const std::string BlockPreconditionerCore::modulename_(
					       "ooflib.SWIG.engine.blockpre");
const std::string BlockPreconditioner::classname_("BlockPreconditioner");
const std::string BlockPreconditionerCore::classname_(
					      "BlockPreconditionerCore");


// A "Block" is the out-of-plane degrees of freedom and equations
// corresponding to a particular node.  In this preconditioner, there
// is one block per node of the FE mesh, and they're stored (indexed
// by node ID) in an std::map.

Block::Block(int id) : id_(id), rows(0), cols(0), mtx(0), rhs(0) {}

Block::~Block() {
  if (mtx!=0)
    delete mtx;
  if (rhs!=0)
    delete rhs;
}

void Block::new_row(int rowno) { 
  rows.push_back(rowno);
}

void Block::new_col(int colno) {
  cols.push_back(colno);
}

void Block::assign(const SparseMat &M) {
  if (mtx==0) 
    mtx = new SmallMatrix(rows.size(), cols.size());
  
  // colmap maps global column numbers to local column numbers in the
  // block.
  std::map<int, int> colmap;
  for(std::vector<int>::size_type i=0; i<cols.size(); ++i)
    colmap[cols[i]] = i;

  for(std::vector<int>::size_type lrow=0; lrow<rows.size(); lrow++) {
    int grow = rows[lrow];	// global row
    // Look for entries in the global row whose column numbers are in cols.
    for(SparseMat::const_row_iterator j=M.begin(grow); j<M.end(grow); ++j) {
      std::map<int, int>::iterator icol = colmap.find(j.col());
      if(icol != colmap.end()) {
	(*mtx)(lrow, (*icol).second) = *j;
      }
    }
  }
}

void Block::assign_rhs(const std::vector<double> &b) {

  if (rhs==0) {
    rhs = new SmallMatrix(rows.size(), 1);
  }

  for(std::vector<int>::size_type lrow=0; lrow<rows.size(); lrow++) 
    (*rhs)(lrow,0) = b[rows[lrow]];

}

// Solve the linear system mtx.x = rhs, writing the result into the 
// appropriate slots of the passed-in solution x.
void Block::solve(std::vector<double> &x) {

  // Make a local copy, because solving corrupts the matrix.
  SmallMatrix temp(*mtx);
  // TODO: Check error code, fail if it's singular?  The only reason
  // why not is that iterative solvers *can* handle singular matrices,
  // and bailing out here might break a process that would otherwise
  // work.
  temp.solve(*rhs);
  for(std::vector<int>::size_type lcol=0; lcol<cols.size(); lcol++) {
    x[cols[lcol]] = (*rhs)(lcol,0);
  }
}


void Block::trans_solve(std::vector<double> &x) {
  SmallMatrix trans(*mtx);
  trans.transpose();
  trans.solve(*rhs);
  for(std::vector<int>::size_type lcol=0; lcol<cols.size(); lcol++)
    x[cols[lcol]] = (*rhs)(lcol,0);
}




BlockPreconditionerCore::BlockPreconditionerCore(const SparseMat &A,
						 const std::vector<int> &rowids,
						 const std::vector<int> &colids,
						 UnitPreconditioner *inplane) 
  : subconditioner(0),
    rowgroups(rowids), colgroups(colids),
    in_plane_rows(0), in_plane_cols(0)
{
  in_plane_rows.reserve(rowids.size());
  in_plane_cols.reserve(colids.size());

//     std::cerr << "Rowgroups: " << std::endl;
//     for(int i=0; i<rowgroups.size(); i++)
//       std::cerr << i << ": " << rowids[i] << std::endl;

//     std::cerr << "Colgroups: " << std::endl;
//     for(int i=0; i<colgroups.size(); i++)
//       std::cerr << i << ": " << colids[i] << std::endl;

  std::vector<int> in_plane_rowmap(rowgroups.size());
  std::vector<int> in_plane_colmap(colgroups.size());


  // Build the blocks, and set up their row and column mapping arrays.
  // The ID of the block is the index of the node to which it
  // corresponds; these indices need not be contiguous, but they are 
  // all greater than or equal to zero.
  int in_plane_count = 0;
  for(std::vector<int>::size_type i=0;i<rowgroups.size();i++) {
    int r = rowgroups[i];
    if ( r >= 0) {
      in_plane_rows.push_back(-1);
      Blockmap::iterator bf = blocks.find(r);
      if (bf==blocks.end()) 
	// Can't use blocks[r]=Block(r) because operator[] in the map
	// class calls the default Block constructor, and the Block
	// class doesn't have one.
	blocks.insert(Blockmap::value_type(r,Block(r)));
      (*blocks.find(r)).second.new_row(i);
    }
    else
      in_plane_rows.push_back(in_plane_count++);
  }
  in_plane_count = 0;
  for(std::vector<int>::size_type i=0;i<colgroups.size();i++) {
    int c = colgroups[i];
    if ( c >= 0) {
      in_plane_cols.push_back(-1);
      Blockmap::iterator bf = blocks.find(c);
      if (bf==blocks.end())
	throw ErrSetupError("Column node not present in row set.");
      (*(blocks.find(c))).second.new_col(i);
    }
    else
      in_plane_cols.push_back(in_plane_count++);
  }

  for(Blockmap::iterator i = blocks.begin(); i!=blocks.end(); ++i)
    (*i).second.assign(A);
  // Extract the in-plane submatrix from A, and build the sub-conditioner.
  // std::cerr << "A: " << A.nrows() << " " << A.ncols() << std::endl;
  A_inplane = SparseMat(A, in_plane_rows, in_plane_cols);
  subconditioner = inplane->build_preconditioner(A_inplane);
}


BlockPreconditionerCore::~BlockPreconditionerCore() {
  delete subconditioner;
}

std::vector<double> 
BlockPreconditionerCore::solve(const std::vector<double> &b) const {
  std::vector<double> x=b;

  // std::cerr << "Calling Preconditioner_double::solve." << std::endl;
  // std::cerr << "There are " << blocks.size() << " blocks." << std::endl;
  for(Blockmap::iterator i = blocks.begin(); i!=blocks.end(); ++i) {
    (*i).second.assign_rhs(b);
  }

  for(Blockmap::iterator i = blocks.begin(); i!=blocks.end(); ++i) {
    (*i).second.solve(x);
  }

  // In-plane part.
  std::vector<double> y(A_inplane.nrows());
  for(std::vector<int>::size_type i=0;i<in_plane_rows.size();i++) 
    if (in_plane_rows[i]>=0)
      y[in_plane_rows[i]]=b[i];

  std::vector<double> z = subconditioner->solve(y);

  for(std::vector<int>::size_type i=0;i<in_plane_cols.size();i++)
    if (in_plane_cols[i]>=0) 
      x[i]=z[in_plane_cols[i]];
  return x;
}

std::vector<double> 
BlockPreconditionerCore::trans_solve(const std::vector<double> &b) const {
  std::vector<double> x=b;

  for(Blockmap::iterator i = blocks.begin(); i!=blocks.end(); ++i)
    (*i).second.assign_rhs(b);
  
  for(Blockmap::iterator i = blocks.begin(); i!=blocks.end(); ++i)
    (*i).second.trans_solve(x);
  
  // In-plane part.
  std::vector<double> y(A_inplane.nrows());
  for(std::vector<int>::size_type i=0;i<in_plane_rows.size();i++) 
    if (in_plane_rows[i]>=0)
      y[in_plane_rows[i]]=b[i];

  std::vector<double> z = subconditioner->trans_solve(y);

  for(std::vector<int>::size_type i=0;i<in_plane_cols.size();i++)
    if (in_plane_cols[i]>=0) 
      x[i]=z[in_plane_cols[i]];

  return x;
}
