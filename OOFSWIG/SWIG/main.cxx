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
 * $Header: /users/langer/FE/CVSoof/OOF2/OOFSWIG/SWIG/main.cxx,v 1.2 2014/06/27 14:57:03 lck Exp $
 *
 * main.cxx
 *
 * The main program.
 *
 ***********************************************************************/

// TODO: Stupid calls to std::string::c_str() are because all of the
// std::strings in here used to be char[256], and not everything has
// been modified to use the std::strings.  If the c_str() is being
// passed to a function that might modify the string, it may have to
// be fixed.  (Leaving the strings as char[256] causes problems with
// very long file paths, such as are generated when building OOF2 with
// MacPorts).  This probably shouldn't be fixed since we hope to be
// abandoning this version of swig.

#define WRAP

#include "internal.h"
#include "ascii.h"
#include "latex.h"
#include "html.h"
#include "nodoc.h"
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

#include <string>

class SwigException {};

static const char *usage = "\
\nDocumentation Options\n\
     -dascii         - ASCII documentation.\n\
     -dhtml          - HTML documentation.\n\
     -dlatex         - LaTeX documentation.\n\
     -dnone          - No documentation.\n\n\
General Options\n\
     -c              - Produce raw wrapper code (omit support code)\n\
     -c++            - Enable C++ processing\n\
     -ci             - Check a file into the SWIG library\n\
     -co             - Check a file out of the SWIG library\n\
     -d docfile      - Set name of the documentation file.\n\
     -Dsymbol        - Define a symbol (for conditional compilation)\n\
     -I<dir>         - Look for SWIG files in <dir>\n\
     -l<ifile>       - Include SWIG library file.\n\
     -make_default   - Create default constructors/destructors\n\
     -nocomment      - Ignore all comments (for documentation).\n\
     -o outfile      - Set name of the output file.\n\
     -objc           - Enable Objective C processing\n\
     -stat           - Print statistics\n\
     -strict n       - Set pointer type-checking strictness\n\
     -swiglib        - Report location of SWIG library and exit\n\
     -t typemap_file - Use a typemap file.\n\
     -v              - Run in verbose mode\n\
     -version        - Print SWIG version number\n\
     -help           - This output.\n\n";

//-----------------------------------------------------------------
// main()
//
// Main program.    Initializes the files and starts the parser.
//-----------------------------------------------------------------

std::string  infilename;
std::string  fn_header;
std::string  fn_wrapper;
std::string  fn_init;
std::string  output_dir;

char *SwigLib;

int SWIG_main(int argc, char *argv[], Language *l, Documentation *d) {

  int    i;
  char   *c;
  extern  FILE   *LEX_in;
  extern  void   add_directory(const char *);
  extern  char   *get_time();
  std::string    infile;

  std::string outfile_name;
  extern  int add_iname(const char *);
  int     help = 0;
  int     ignorecomments = 0;
  int     checkout = 0;
  // int     checkin = 0;
  char   *typemap_file = 0;
  char   *includefiles[256];
  int     includecount = 0;
  extern  void check_suffix(const char *);
  extern  void scanner_file(FILE *);

  f_wrappers = 0;
  f_init = 0;
  f_header = 0;

  lang = l;
  doc = d;
  Status = 0;
  TypeStrict = 2;                   // Very strict type checking
  Verbose = 0;
  // char    *doc_file = 0;
  
  DataType::init_typedef();         // Initialize the type handler

  // Set up some default symbols (available in both SWIG interface files
  // and C files)

  add_symbol("SWIG",0,0);            // Define the SWIG symbol
#ifdef SWIGWIN32
  add_symbol("SWIGWIN32",0,0);
#endif
  
  // Check for SWIG_LIB environment variable

  if ((c = getenv("SWIG_LIB")) == (char *) 0) {
      sprintf(LibDir,"%s",SWIG_LIB);    // Build up search paths
  } else {
      strcpy(LibDir,c);
  }
  
  SwigLib = copy_string(LibDir);        // Make a copy of the real library location
  std::string temp = std::string(LibDir) + "/config";
  add_directory(temp.c_str());
  add_directory((char*)"./swig_lib/config");
  add_directory(LibDir);
  add_directory((char*)"./swig_lib");
  sprintf(InitName,"init_wrap");

  sprintf(InitName,"init_wrap");  

  // Get options
  for (i = 1; i < argc; i++) {
      if (argv[i]) {
	  if (strncmp(argv[i],"-I",2) == 0) {
	    // Add a new directory search path 
	    includefiles[includecount++] = copy_string(argv[i]+2);
	    mark_arg(i);
	  } else if (strncmp(argv[i],"-D",2) == 0) {
	    // Create a symbol
	    add_symbol(argv[i]+2, (DataType *) 0, (char *) 0);
	    mark_arg(i);
	  } else if (strcmp(argv[i],"-strict") == 0) {
	    if (argv[i+1]) {
	      TypeStrict = atoi(argv[i+1]);
	      mark_arg(i);
	      mark_arg(i+1);
	      i++;
	    } else {
	      arg_error();
	    }
	  } else if ((strcmp(argv[i],"-verbose") == 0) || (strcmp(argv[i],"-v") == 0)) {
	      Verbose = 1;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-dascii") == 0) {
	      doc = new ASCII;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-dnone") == 0) {
	      doc = new NODOC;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-dhtml") == 0) {
	      doc = new HTML;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-dlatex") == 0) {
	      doc = new LATEX;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-nocomment") == 0) {
	      ignorecomments = 1;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-stat") == 0) {
	      Stats=1;
	      mark_arg(i);
	  } else if (strcmp(argv[i],"-c++") == 0) {
	      CPlusPlus=1;
	      mark_arg(i);  
          } else if (strcmp(argv[i],"-objc") == 0) {
	      ObjC = 1;
              mark_arg(i);
	  } else if (strcmp(argv[i],"-c") == 0) {
	      NoInclude=1;
	      mark_arg(i);
          } else if (strcmp(argv[i],"-make_default") == 0) {
	    GenerateDefault = 1;
	    mark_arg(i);
          } else if (strcmp(argv[i],"-swiglib") == 0) {
	    printf("%s\n", LibDir);
	    SWIG_exit(0);
	  } else if (strcmp(argv[i],"-o") == 0) {
	      mark_arg(i);
	      if (argv[i+1]) {
		outfile_name = std::string(argv[i+1]);
		mark_arg(i+1);
		i++;
	      } else {
		arg_error();
	      }
	  } 
	  else if (strcmp(argv[i],"-t") == 0) {
	      mark_arg(i);
	      if (argv[i+1]) {
		typemap_file = copy_string(argv[i+1]);
		mark_arg(i+1);
		i++;
	      } else {
		arg_error();
	      }
	  } else if (strcmp(argv[i],"-version") == 0) {
 	      fprintf(stderr,"\nOOFSWIG Version %d.%d %s\n", SWIG_MAJOR_VERSION,
		      SWIG_MINOR_VERSION, SWIG_SPIN);
	      fprintf(stderr,"SWIG version 1.1 (Build 883) is Copyright (c) 1995-98\n");
	      fprintf(stderr,"University of Utah and the Regents of the University of California\n");
	      fprintf(stderr,"\nCompiled with %s\n", SWIG_CC);
	      fprintf(stderr, "Heavily modified and visciously abridged by OOF at NIST\n");
	      SWIG_exit(0);
	  } else if (strncmp(argv[i],"-l",2) == 0) {
	    // Add a new directory search path 
	    library_add(argv[i]+2);
	    mark_arg(i);
          }
      else if (strcmp(argv[i],"-help") == 0) {
	    fputs(usage,stderr);
	    mark_arg(i);
	    help = 1;
	  }
      }
  }

  while (includecount > 0) {
    add_directory(includefiles[--includecount]);
  }
    
  // Create a new documentation handler

  if (doc == 0) doc = new ASCII;  

  // Open up a comment handler

  comment_handler = new CommentHandler();
  comment_handler->parse_args(argc,argv);
  if (ignorecomments) comment_handler->style("ignore",0);

  // Parse language dependent options

  lang->parse_args(argc,argv);

  if (help) SWIG_exit(0);              // Exit if we're in help mode

  // Check all of the options to make sure we're cool.
  
  check_options();

  // If we made it this far, looks good. go for it....

  // Create names of temporary files that are created

  // input_file could be a std::string too.
  infilename = std::string(argv[argc-1]);
  input_file = new char[infilename.size()+1];
  strcpy(input_file, infilename.c_str());

  {	    // useless vestigial bracket
    // Check the suffix for a .c file.  If so, we're going to 
    // declare everything we see as "extern"
    
    check_suffix(infilename.c_str());
    
    // Strip off suffix

    auto sfx = infilename.rfind(".");
    if(sfx != std::string::npos) {
      infilename.erase(sfx);
    }

    if (outfile_name.size() == 0) {
      fn_header = infilename + "_wrap.c";
      infile = infilename;
      output_dir = "";
    } else {
      fn_header = outfile_name;
      
      // Try to identify the output directory
      output_dir = std::string(outfile_name.begin(),
			       outfile_name.begin() + outfile_name.rfind("/"));

      // Patch up the input filename
      // That is, set infile to everything after the last slash in infilename.
      infile = std::string(infilename.begin() + infilename.rfind("/")+1,
			   infilename.end());
    }

    fn_wrapper = output_dir + infile + "_wrap.wrap";
    fn_init = output_dir + infile + "_wrap.init";
    
    // Open up files
    
    if ((f_input = fopen(input_file,"r")) == 0) {
      // Okay. File wasn't found right away.  Let's see if we can
      // extract it from the SWIG library instead.
      if ((checkout_file(input_file,input_file)) == -1) {
	fprintf(stderr,"Unable to open %s\n", input_file);
	SWIG_exit(0);
      } else {
	// Successfully checked out a file from the library, print a warning and
        // continue
	checkout = 1;
	fprintf(stderr,"%s checked out from the SWIG library.\n",input_file);
	if ((f_input = fopen(input_file,"r")) == 0) {
	  fprintf(stderr,"Unable to open %s\n", input_file);
	  SWIG_exit(0);
	}
      }
    }
    
    // Add to the include list
    
    add_iname(infilename.c_str());

    // Initialize the scanner
    
    LEX_in = f_input;
    scanner_file(LEX_in);
    
    // fprintf(stderr, "SWIG: fn_header = %s\n", fn_header.c_str());
    // fprintf(stderr, "SWIG: fn_wrapper = %s\n", fn_wrapper.c_str());
    // fprintf(stderr, "SWIG: fn_init = %s\n", fn_init.c_str());

    if((f_header = fopen(fn_header.c_str(),"w")) == 0) {
      fprintf(stderr,"Unable to open %s\n", fn_header.c_str());
      exit(0);
    }
    if((f_wrappers = fopen(fn_wrapper.c_str(),"w")) == 0) {
      fprintf(stderr,"Unable to open %s\n",fn_wrapper.c_str());
      exit(0);
    }
    if ((f_init = fopen(fn_init.c_str(),"w")) == 0) {
      fprintf(stderr,"Unable to open %s\n",fn_init.c_str());
      exit(0);
    }
    
    // Set up the typemap for handling new return strings
    {
      DataType *temp_t = new DataType(T_CHAR);
      temp_t->is_pointer++;
      if (CPlusPlus) 
	typemap_register("newfree",typemap_lang,temp_t,"","delete [] $source;\n",0);
      else 
	typemap_register("newfree",typemap_lang,temp_t,"","free($source);\n",0);

      delete temp_t;
    }

    // Define the __cplusplus symbol
    if (CPlusPlus)
      add_symbol("__cplusplus",0,0);           


    // Load up the typemap file if given

    if (typemap_file) {
      if (include_file(typemap_file) == -1) {
	fprintf(stderr,"Unable to locate typemap file %s.  Aborting.\n", typemap_file);
	SWIG_exit(1);
      }
    }

    // Pass control over to the specific language interpreter    

    lang->parse();
    
    fclose(f_wrappers);
    fclose(f_init);
    
    swig_append(fn_wrapper.c_str(), f_header);
    swig_append(fn_init.c_str(), f_header);
    
    fclose(f_header);
    
    // Remove temporary files
    
    remove(fn_wrapper.c_str());
    remove(fn_init.c_str());

    // Check for undefined types that were used.

    if (Verbose)
      type_undefined_check();

    if (Stats) {
      fprintf(stderr,"Wrapped %d functions\n", Stat_func);
      fprintf(stderr,"Wrapped %d variables\n", Stat_var);
      fprintf(stderr,"Wrapped %d constants\n", Stat_const);
      type_undefined_check();
    }

    if (checkout) {
      // File was checked out from the SWIG library.   Remove it now
      remove(input_file);
    }
  }
  exit(error_count);
  return(error_count);
}

// --------------------------------------------------------------------------
// SWIG_exit()
//
// Fatal parser error. Exit and cleanup
// --------------------------------------------------------------------------

void SWIG_exit(int) {

  if (f_wrappers) {
    fclose(f_wrappers);
    remove(fn_wrapper.c_str());
  }
  if (f_header) {
    fclose(f_header);
    remove(fn_header.c_str());
  }
  if (f_init) {
    fclose(f_init);
    remove(fn_init.c_str());
  }
  exit(1);
}


// --------------------------------------------------------------------------
// swig_pragma(char *name, char *value)
//
// Handle pragma directives.  Not many supported right now
// --------------------------------------------------------------------------

void swig_pragma(char *name, char *value) {
  
  if (strcmp(name,"make_default") == 0) {
    GenerateDefault = 1;
  }
  if (strcmp(name,"no_default") == 0) {
    GenerateDefault = 0;
  }
  if (strcmp(name,"objc_new") == 0) {
    objc_construct = copy_string(value);
  }
  if (strcmp(name,"objc_delete") == 0) {
    objc_destruct = copy_string(value);
  }
}
