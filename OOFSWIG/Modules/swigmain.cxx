/*******************************************************************************
 * Simplified Wrapper and Interface Generator  (SWIG)
 * 
 * Author : David Beazley
 *
 * Department of Computer Science        
 * University of Chicago
 * 1100 E 58th Street
 * Chicago, IL  60637
 * beazley@cs.uchicago.edu
 *
 * Please read the file LICENSE for the copyright and terms by which SWIG
 * can be used and distributed.
 *******************************************************************************/

/***********************************************************************
 * $Header: /users/langer/FE/CVSoof/OOF2/OOFSWIG/Modules/swigmain.cxx,v 1.3 2014/06/27 14:57:08 lck Exp $
 *
 * swigmain.cxx
 *
 * The main program.
 *
 ***********************************************************************/

#include "wrap.h"
#include "python.h"
// #include "pythoncom.h"
#include "debug.h"
#include <ctype.h>

static const char  *usage = "\
swig <options> filename\n\n\
Target Language Options:\n\
     -python         - Generate Python wrappers.\n\
     -debug          - Parser debugging module.\n";



//-----------------------------------------------------------------
// main()
//
// Main program.    Initializes the files and starts the parser.
//-----------------------------------------------------------------

int main(int argc, char **argv) {

  int i;

  Language *dl;
  extern int SWIG_main(int, char **, Language *);
  init_args(argc,argv);
  
  // Get options
  for (i = 1; i < argc; i++) {
      if (argv[i]) {	  
	  if (strcmp(argv[i],"-python") == 0) {
	      dl = new PYTHON;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-debug") == 0) {
	      dl = new DEBUGLANG;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-help") == 0) {
	      fputs(usage,stderr);
	      mark_arg(i);
	  }
      }
  }
  SWIG_main(argc,argv,dl);

  return 0;
}

