// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Small utilities for handling python objects in C++

#ifndef PYUTILS_H
#define PYUTILS_H

#include <oofconfig.h>
#include <string>

std::string pyStringAsString(PyObject*);

std::string repr(PyObject*);
std::string repr_nolock(PyObject*);

#endif // PYUTILS_H
