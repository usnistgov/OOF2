// -*- C++ -*-
// $RCSfile: cdebug.h,v $
// $Revision: 1.13 $
// $Author: langer $
// $Date: 2013/02/19 19:50:02 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef CDEBUG_H
#define CDEBUG_H

// Routines used to catch C++ signals and dump the current Python
// stack before bailing out.  These are not used except when OOF2 is
// built with --debug.

#include <Python.h>
#include <vector>

void initDebug(PyObject*);
void installSignals_();
void restoreSignals_();

#ifdef DEBUG
#define installSignals installSignals_()
#define restoreSignals restoreSignals_()
#else
#define installSignals /**/
#define restoreSignals /**/
#endif

// Test routines.
void segfault(int delay);
void throwException();
void throwPythonException();
void throwPythonCException();

void spinCycle(int);

#endif // CDEBUG_H
