// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// A wrapper for strerror_r, which is defined differently on different
// systems.

#ifndef OOFSTRERROR_H
#define OOFSTRERROR_H

#include <string>

std::string oof_strerror();

#endif // OOFSTRERROR_H
