/* A Bison parser, made by GNU Bison 2.5.  */

/* Bison implementation for Yacc-like parsers in C
   
      Copyright (C) 1984, 1989-1990, 2000-2011 Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.5"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1

/* Using locations.  */
#define YYLSP_NEEDED 0



/* Copy the first part of user declarations.  */

/* Line 268 of yacc.c  */
#line 1 "parser.y"

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
 * $Header: /users/langer/FE/CVSoof/OOF2/OOFSWIG/SWIG/parser.cxx,v 1.2 2014/06/26 17:27:35 lck Exp $
 *
 * parser.y
 *
 * YACC parser for parsing function declarations.
 *
 * *** DISCLAIMER ***
 *
 * This is the most ugly, incredibly henious, and completely unintelligible
 * file in SWIG.  While it started out simple, it has grown into a
 * monster that is almost unmaintainable.   A complete parser rewrite is
 * currently in progress that should make this file about 1/4 the size
 * that it is now.   Needless to say, don't modify this file or even look
 * at it for that matter!
 ***********************************************************************/

#define yylex yylex

extern "C" int yylex();
void   yyerror (const char *s);       
    
extern int  line_number;
extern int  start_line;
extern void skip_brace(void);
extern void skip_define(void);
extern void skip_decl(void);
extern int  skip_cond(int);
extern void skip_to_end(void);
extern void skip_template(void);
extern void scanner_check_typedef(void);
extern void scanner_ignore_typedef(void);
extern void scanner_clear_start(void);
extern void start_inline(char *, int);
extern void format_string(char *);
extern void swig_pragma(char *, char *);

#include "internal.h"

#ifdef NEED_ALLOC
void *alloca(unsigned n) {
  return((void *) malloc(n));
}
#else
// This redefinition is apparently needed on a number of machines,
// particularly HPUX
#undef  alloca
#define alloca  malloc
#endif

// Initialization flags.   These indicate whether or not certain
// features have been initialized.  These were added to allow
// interface files without the block (required in previous
// versions).

static int     module_init = 0;    /* Indicates whether the %module name was given */
static int     title_init = 0;     /* Indicates whether %title directive has been given */
static int     doc_init = 0;    

static int     lang_init = 0;      /* Indicates if the language has been initialized */

static int            i;
       int            Error = 0;
static char           temp_name[128];
static DataType      *temp_typeptr, temp_type;
static char           yy_rename[256];
static int            Rename_true = 0;
static DataType      *Active_type = 0;         // Used to support variable lists
static int            Active_extern = 0;       // Whether or not list is external
static int            Active_static = 0;
static DataType       *Active_typedef = 0;     // Used for typedef lists
static int            InArray = 0;             // Used when an array declaration is found 
static int            in_then = 0;
static int            in_else = 0;       
static int            allow = 1;               // Used during conditional compilation
static int            doc_scope = 0;           // Documentation scoping
static String         ArrayString;             // Array type attached to parameter names
static String         ArrayBackup;             // Array backup string
static char           *DefArg = 0;             // Default argument hack
static char           *ConstChar = 0;          // Used to store raw character constants
static ParmList       *tm_parm = 0;            // Parameter list used to hold typemap parameters
static Hash            name_hash;              // Hash table containing renamings
       char           *objc_construct = (char*)"new"; // Objective-C constructor
       char           *objc_destruct = (char*)"free"; // Objective-C destructor

/* Some macros for building constants */

#define E_BINARY(TARGET, SRC1, SRC2, OP)  \
        TARGET = new char[strlen(SRC1) + strlen(SRC2) +strlen(OP)+1];\
	sprintf(TARGET,"%s%s%s",SRC1,OP,SRC2);

/* C++ modes */

#define  CPLUS_PUBLIC    1
#define  CPLUS_PRIVATE   2
#define  CPLUS_PROTECTED 3

int     cplus_mode;

// Declarations of some functions for handling C++ 

extern void cplus_open_class(const char *name, char *rname,const char *ctype);
extern void cplus_member_func(char *, char *, DataType *, ParmList *, int);
extern void cplus_constructor(char *, char *, ParmList *);
extern void cplus_destructor(char *, char *);
extern void cplus_variable(char *, char *, DataType *);
extern void cplus_static_func(char *, char *, DataType *, ParmList *);
extern void cplus_declare_const(const char *,const char *, DataType *,const char *);
extern void cplus_class_close(char *);
extern void cplus_inherit(int, char **);
extern void cplus_cleanup(void);
extern void cplus_static_var(char *, char *, DataType *);
extern void cplus_register_type(char *);
extern void cplus_register_scope(Hash *);
extern void cplus_inherit_scope(int, char **);
extern void cplus_add_pragma(char *, char *, char *);
extern DocEntry *cplus_set_class(char *);
extern void cplus_unset_class();
extern void cplus_abort();
  
// ----------------------------------------------------------------------
// static init_language()
//
// Initialize the target language.
// Does nothing if this function has already been called.
// ----------------------------------------------------------------------

static void init_language() {
  if (!lang_init) {
    lang->initialize();
    
    // Initialize the documentation system

    if (!doctitle) {
      doctitle = new DocTitle(title,0);
    }
    if (!doc_init)
      doctitle->usage = title;

    doc_stack[0] = doctitle;
    doc_stack_top = 0;
    
    int oldignore = IgnoreDoc;
    IgnoreDoc = 1;
    if (ConfigFile) {
      include_file(ConfigFile);
    }
    IgnoreDoc = oldignore;
  }
  lang_init = 1;
  title_init = 1;
}

// ----------------------------------------------------------------------
// int promote(int t1, int t2)
//
// Promote types (for constant expressions)
// ----------------------------------------------------------------------

int promote(int t1, int t2) {

  if ((t1 == T_ERROR) || (t2 == T_ERROR)) return T_ERROR;
  if ((t1 == T_DOUBLE) || (t2 == T_DOUBLE)) return T_DOUBLE;
  if ((t1 == T_FLOAT) || (t2 == T_FLOAT)) return T_FLOAT;
  if ((t1 == T_ULONG) || (t2 == T_ULONG)) return T_ULONG;
  if ((t1 == T_LONG) || (t2 == T_LONG)) return T_LONG;
  if ((t1 == T_UINT) || (t2 == T_UINT)) return T_UINT;
  if ((t1 == T_INT) || (t2 == T_INT)) return T_INT;
  if ((t1 == T_USHORT) || (t2 == T_USHORT)) return T_SHORT;
  if ((t1 == T_SHORT) || (t2 == T_SHORT)) return T_SHORT;
  if ((t1 == T_UCHAR) || (t2 == T_UCHAR)) return T_UCHAR;
  if (t1 != t2) {
    fprintf(stderr,"%s : Line %d. Type mismatch in constant expression\n",
	    input_file, line_number);
    FatalError();
  }
  return t1;
}

/* Generate the scripting name of an object.  Takes %name directive into 
   account among other things */

static char *make_name(char *name) {
  // Check to see if the name is in the hash
  char *nn = (char *) name_hash.lookup(name);
  if (nn) return nn;        // Yep, return it.

  if (Rename_true) {
    Rename_true = 0;
    return yy_rename;
  } else {
    // Now check to see if the name contains a $
    if (strchr(name,'$')) {
      static String temp;
      temp = "";
      temp << name;
      temp.replace("$","_S_");
      return temp;
    } else {
      return name;
    }
  }
}

/* Return the parent of a documentation entry.   If wrapping externally, this is 0 */

static DocEntry *doc_parent() {
  if (!WrapExtern) 
    return doc_stack[doc_stack_top];
  else
    return 0;
}

// ----------------------------------------------------------------------
// create_function(int ext, char *name, DataType *t, ParmList *l)
//
// Creates a function and manages documentation creation.  Really
// only used internally to the parser.
// ----------------------------------------------------------------------

void create_function(int ext, char *name, DataType *t, ParmList *l) {
  if (Active_static) return;     // Static declaration. Ignore

  init_language();
  if (WrapExtern) return;        // External wrapper file. Ignore

  char *iname = make_name(name);

  // Check if symbol already exists

  if (add_symbol(iname, t, (char *) 0)) {
    fprintf(stderr,"%s : Line %d. Function %s multiply defined (2nd definition ignored).\n",
	    input_file, line_number, iname);
  } else {
    Stat_func++;
    if (Verbose) {
      fprintf(stderr,"Wrapping function : ");
      emit_extern_func(name, t, l, 0, stderr);
    }

    // If extern, make an extern declaration in the SWIG wrapper file

    if (ext) 
      emit_extern_func(name, t, l, ext, f_header);
    else if (ForceExtern) {
      emit_extern_func(name, t, l, 1, f_header);
    }

    // If this function has been declared inline, produce a function

    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
    lang->create_function(name, iname, t, l);
    l->check_defined();
    t->check_defined();
  }
  scanner_clear_start();
}

// -------------------------------------------------------------------
// create_variable(int ext, char *name, DataType *t)
//
// Create a link to a global variable.
// -------------------------------------------------------------------

void create_variable(int ext, char *name, DataType *t) {

  if (WrapExtern) return;        // External wrapper file. Ignore
  int oldstatus = Status;

  if (Active_static) return;  // If static ignore
				   
  init_language();

  char *iname = make_name(name);
  if (add_symbol(iname, t, (char *) 0)) {
    fprintf(stderr,"%s : Line %d. Variable %s multiply defined (2nd definition ignored).\n",
	    input_file, line_number, iname);
  } else {
    Stat_var++;
    if (Verbose) {
      fprintf(stderr,"Wrapping variable : ");
      emit_extern_var(name, t, 0, stderr);
    }

    // If externed, output an external declaration

    if (ext) 
      emit_extern_var(name, t, ext, f_header);
    else if (ForceExtern) {
      emit_extern_var(name, t, 1, f_header);
    }

    // If variable datatype is read-only, we'll force it to be readonly
    if (t->status & STAT_READONLY) Status = Status | STAT_READONLY;

    // Now dump it out
    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
    lang->link_variable(name, iname, t);
    t->check_defined();
    Status = oldstatus;
  }
  scanner_clear_start();
}

// ------------------------------------------------------------------
// create_constant(char *name, DataType *type, char *value)
//
// Creates a new constant.
// -------------------------------------------------------------------

void create_constant(char *name, DataType *type, char *value) {

  if (Active_static) return;
  if (WrapExtern) return;        // External wrapper file. Ignore
  init_language();

  if (Rename_true) {
    fprintf(stderr,"%s : Line %d. %%name directive ignored with #define\n",
	    input_file, line_number);
    Rename_true = 0;
  }

  if ((type->type == T_CHAR) && (!type->is_pointer))
    type->is_pointer++;
  
  if (!value) value = copy_string(name);
  sprintf(temp_name,"const:%s", name);
  if (add_symbol(temp_name, type, value)) {
    fprintf(stderr,"%s : Line %d. Constant %s multiply defined. (2nd definition ignored)\n",
	    input_file, line_number, name);
  } else {
    // Update symbols value if already defined.
    update_symbol(name, type, value);

    if (!WrapExtern) {    // Only wrap the constant if not in %extern mode
      Stat_const++;
      if (Verbose) 
	fprintf(stderr,"Creating constant %s = %s\n", name, value);

      doc_entry = new DocDecl(name,doc_stack[doc_stack_top]);	   
      lang->declare_const(name, name, type, value);
      type->check_defined();
    }
  }
  scanner_clear_start();
}


/* Print out array brackets */
void print_array() {
  int i;
  for (i = 0; i < InArray; i++)
    fprintf(stderr,"[]");
}

/* manipulate small stack for managing if-then-else */

static int then_data[100];
static int else_data[100];
static int allow_data[100];
static int te_index = 0;
static int prev_allow = 1;

void if_push() {
  then_data[te_index] = in_then;
  else_data[te_index] = in_else;
  allow_data[te_index] = allow;
  prev_allow = allow;
  te_index++;
  if (te_index >= 100) {
    fprintf(stderr,"SWIG.  Internal parser error. if-then-else stack overflow.\n");
    SWIG_exit(1);
  }
}

void if_pop() {
  if (te_index > 0) {
    te_index--;
    in_then = then_data[te_index];
    in_else = else_data[te_index];
    allow = allow_data[te_index];
    if (te_index > 0) {
      prev_allow = allow_data[te_index-1];
    } else {
      prev_allow = 1;
    }
  }
}

// Structures for handling code fragments built for nested classes

struct Nested {
  String   code;         // Associated code fragment
  int      line;         // line number where it starts
  char     *name;        // Name associated with this nested class
  DataType *type;        // Datatype associated with the name
  Nested   *next;        // Next code fragment in list
};

// Some internal variables for saving nested class information

static Nested      *nested_list = 0;

// Add a function to the nested list

static void add_nested(Nested *n) {
  Nested *n1;
  if (!nested_list) nested_list = n;
  else {
    n1 = nested_list;
    while (n1->next) n1 = n1->next;
    n1->next = n;
  }
}

// Dump all of the nested class declarations to the inline processor
// However.  We need to do a few name replacements and other munging
// first.  This function must be called before closing a class!

static void dump_nested(char *parent) {
  Nested *n,*n1;
  n = nested_list;
  int oldstatus = Status;

  Status = STAT_READONLY;
  while (n) {
    // Token replace the name of the parent class
    n->code.replace("$classname",parent);

    // Fix up the name of the datatype (for building typedefs and other stuff)
    sprintf(n->type->name,"%s_%s",parent,n->name);
    
    // Add the appropriate declaration to the C++ processor
    doc_entry = new DocDecl(n->name,doc_stack[doc_stack_top]);
    cplus_variable(n->name,(char *) 0, n->type);

    // Dump the code to the scanner
    if (Verbose)
      fprintf(stderr,"Splitting from %s : (line %d) \n%s\n", parent,n->line, n->code.get());

    fprintf(f_header,"\n%s\n", n->code.get());
    start_inline(n->code.get(),n->line);

    n1 = n->next;
    delete n;
    n = n1;
  }
  nested_list = 0;
  Status = oldstatus;
}    



/* Line 268 of yacc.c  */
#line 540 "y.tab.c"

/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Enabling the token table.  */
#ifndef YYTOKEN_TABLE
# define YYTOKEN_TABLE 0
#endif


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     ID = 258,
     HBLOCK = 259,
     WRAPPER = 260,
     POUND = 261,
     STRING = 262,
     NUM_INT = 263,
     NUM_FLOAT = 264,
     CHARCONST = 265,
     NUM_UNSIGNED = 266,
     NUM_LONG = 267,
     NUM_ULONG = 268,
     TYPEDEF = 269,
     TYPE_INT = 270,
     TYPE_UNSIGNED = 271,
     TYPE_SHORT = 272,
     TYPE_LONG = 273,
     TYPE_FLOAT = 274,
     TYPE_DOUBLE = 275,
     TYPE_CHAR = 276,
     TYPE_VOID = 277,
     TYPE_SIGNED = 278,
     TYPE_BOOL = 279,
     TYPE_TYPEDEF = 280,
     LPAREN = 281,
     RPAREN = 282,
     COMMA = 283,
     SEMI = 284,
     EXTERN = 285,
     INIT = 286,
     LBRACE = 287,
     RBRACE = 288,
     DEFINE = 289,
     PERIOD = 290,
     CONST = 291,
     STRUCT = 292,
     UNION = 293,
     EQUAL = 294,
     SIZEOF = 295,
     MODULE = 296,
     LBRACKET = 297,
     RBRACKET = 298,
     WEXTERN = 299,
     ILLEGAL = 300,
     READONLY = 301,
     READWRITE = 302,
     NAME = 303,
     RENAME = 304,
     INCLUDE = 305,
     CHECKOUT = 306,
     ADDMETHODS = 307,
     PRAGMA = 308,
     CVALUE = 309,
     COUT = 310,
     ENUM = 311,
     ENDDEF = 312,
     MACRO = 313,
     CLASS = 314,
     PRIVATE = 315,
     PUBLIC = 316,
     PROTECTED = 317,
     COLON = 318,
     STATIC = 319,
     VIRTUAL = 320,
     FRIEND = 321,
     OPERATOR = 322,
     THROW = 323,
     TEMPLATE = 324,
     NATIVE = 325,
     INLINE = 326,
     IFDEF = 327,
     IFNDEF = 328,
     ENDIF = 329,
     ELSE = 330,
     UNDEF = 331,
     IF = 332,
     DEFINED = 333,
     ELIF = 334,
     RAW_MODE = 335,
     ALPHA_MODE = 336,
     TEXT = 337,
     DOC_DISABLE = 338,
     DOC_ENABLE = 339,
     STYLE = 340,
     LOCALSTYLE = 341,
     TYPEMAP = 342,
     EXCEPT = 343,
     IMPORT = 344,
     ECHO = 345,
     NEW = 346,
     APPLY = 347,
     CLEAR = 348,
     DOCONLY = 349,
     TITLE = 350,
     SECTION = 351,
     SUBSECTION = 352,
     SUBSUBSECTION = 353,
     LESSTHAN = 354,
     GREATERTHAN = 355,
     USERDIRECTIVE = 356,
     OC_INTERFACE = 357,
     OC_END = 358,
     OC_PUBLIC = 359,
     OC_PRIVATE = 360,
     OC_PROTECTED = 361,
     OC_CLASS = 362,
     OC_IMPLEMENT = 363,
     OC_PROTOCOL = 364,
     OR = 365,
     XOR = 366,
     AND = 367,
     RSHIFT = 368,
     LSHIFT = 369,
     MINUS = 370,
     PLUS = 371,
     SLASH = 372,
     STAR = 373,
     LNOT = 374,
     NOT = 375,
     UMINUS = 376,
     DCOLON = 377
   };
#endif
/* Tokens.  */
#define ID 258
#define HBLOCK 259
#define WRAPPER 260
#define POUND 261
#define STRING 262
#define NUM_INT 263
#define NUM_FLOAT 264
#define CHARCONST 265
#define NUM_UNSIGNED 266
#define NUM_LONG 267
#define NUM_ULONG 268
#define TYPEDEF 269
#define TYPE_INT 270
#define TYPE_UNSIGNED 271
#define TYPE_SHORT 272
#define TYPE_LONG 273
#define TYPE_FLOAT 274
#define TYPE_DOUBLE 275
#define TYPE_CHAR 276
#define TYPE_VOID 277
#define TYPE_SIGNED 278
#define TYPE_BOOL 279
#define TYPE_TYPEDEF 280
#define LPAREN 281
#define RPAREN 282
#define COMMA 283
#define SEMI 284
#define EXTERN 285
#define INIT 286
#define LBRACE 287
#define RBRACE 288
#define DEFINE 289
#define PERIOD 290
#define CONST 291
#define STRUCT 292
#define UNION 293
#define EQUAL 294
#define SIZEOF 295
#define MODULE 296
#define LBRACKET 297
#define RBRACKET 298
#define WEXTERN 299
#define ILLEGAL 300
#define READONLY 301
#define READWRITE 302
#define NAME 303
#define RENAME 304
#define INCLUDE 305
#define CHECKOUT 306
#define ADDMETHODS 307
#define PRAGMA 308
#define CVALUE 309
#define COUT 310
#define ENUM 311
#define ENDDEF 312
#define MACRO 313
#define CLASS 314
#define PRIVATE 315
#define PUBLIC 316
#define PROTECTED 317
#define COLON 318
#define STATIC 319
#define VIRTUAL 320
#define FRIEND 321
#define OPERATOR 322
#define THROW 323
#define TEMPLATE 324
#define NATIVE 325
#define INLINE 326
#define IFDEF 327
#define IFNDEF 328
#define ENDIF 329
#define ELSE 330
#define UNDEF 331
#define IF 332
#define DEFINED 333
#define ELIF 334
#define RAW_MODE 335
#define ALPHA_MODE 336
#define TEXT 337
#define DOC_DISABLE 338
#define DOC_ENABLE 339
#define STYLE 340
#define LOCALSTYLE 341
#define TYPEMAP 342
#define EXCEPT 343
#define IMPORT 344
#define ECHO 345
#define NEW 346
#define APPLY 347
#define CLEAR 348
#define DOCONLY 349
#define TITLE 350
#define SECTION 351
#define SUBSECTION 352
#define SUBSUBSECTION 353
#define LESSTHAN 354
#define GREATERTHAN 355
#define USERDIRECTIVE 356
#define OC_INTERFACE 357
#define OC_END 358
#define OC_PUBLIC 359
#define OC_PRIVATE 360
#define OC_PROTECTED 361
#define OC_CLASS 362
#define OC_IMPLEMENT 363
#define OC_PROTOCOL 364
#define OR 365
#define XOR 366
#define AND 367
#define RSHIFT 368
#define LSHIFT 369
#define MINUS 370
#define PLUS 371
#define SLASH 372
#define STAR 373
#define LNOT 374
#define NOT 375
#define UMINUS 376
#define DCOLON 377




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 293 of yacc.c  */
#line 475 "parser.y"
         
  char        *id;
  struct Declaration {
    char *id;
    int   is_pointer;
    int   is_reference;
  } decl;
  struct InitList {
    char **names;
    int    count;
  } ilist;
  struct DocList {
    char **names;
    char **values;
    int  count;
  } dlist;
  struct Define {
    char *id;
    int   type;
  } dtype;
  DataType     *type;
  Parm         *p;
  TMParm       *tmparm;
  ParmList     *pl;
  int           ivalue;



/* Line 293 of yacc.c  */
#line 849 "y.tab.c"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif


/* Copy the second part of user declarations.  */


/* Line 343 of yacc.c  */
#line 861 "y.tab.c"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yytype_int8;
#else
typedef short int yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(msgid) dgettext ("bison-runtime", msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(msgid) msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(e) ((void) (e))
#else
# define YYUSE(e) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(n) (n)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int yyi)
#else
static int
YYID (yyi)
    int yyi;
#endif
{
  return yyi;
}
#endif

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
	 || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)				\
    do									\
      {									\
	YYSIZE_T yynewbytes;						\
	YYCOPY (&yyptr->Stack_alloc, Stack, yysize);			\
	Stack = &yyptr->Stack_alloc;					\
	yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yyptr += yynewbytes / sizeof (*yyptr);				\
      }									\
    while (YYID (0))

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from FROM to TO.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(To, From, Count) \
      __builtin_memcpy (To, From, (Count) * sizeof (*(From)))
#  else
#   define YYCOPY(To, From, Count)		\
      do					\
	{					\
	  YYSIZE_T yyi;				\
	  for (yyi = 0; yyi < (Count); yyi++)	\
	    (To)[yyi] = (From)[yyi];		\
	}					\
      while (YYID (0))
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  3
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   2144

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  123
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  136
/* YYNRULES -- Number of rules.  */
#define YYNRULES  428
/* YYNRULES -- Number of states.  */
#define YYNSTATES  907

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   377

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    98,    99,   100,   101,   102,   103,   104,
     105,   106,   107,   108,   109,   110,   111,   112,   113,   114,
     115,   116,   117,   118,   119,   120,   121,   122
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     4,     7,    10,    12,    15,    18,    21,
      24,    26,    27,    35,    40,    41,    49,    54,    55,    65,
      73,    74,    83,    91,    99,   100,   110,   112,   114,   119,
     124,   125,   129,   130,   136,   144,   156,   160,   164,   168,
     172,   174,   176,   178,   181,   183,   185,   188,   191,   194,
     197,   200,   202,   206,   210,   214,   217,   220,   221,   230,
     231,   232,   243,   252,   259,   268,   275,   286,   295,   301,
     305,   311,   314,   320,   323,   325,   327,   329,   331,   337,
     339,   341,   344,   347,   349,   351,   353,   354,   360,   371,
     383,   384,   391,   395,   399,   401,   404,   407,   409,   411,
     414,   417,   422,   425,   428,   436,   440,   447,   449,   450,
     457,   458,   467,   470,   472,   475,   477,   479,   482,   485,
     488,   490,   494,   496,   498,   501,   504,   508,   512,   521,
     525,   528,   531,   533,   535,   538,   542,   545,   548,   550,
     552,   554,   557,   559,   561,   564,   567,   570,   573,   577,
     582,   584,   586,   588,   591,   594,   596,   598,   600,   602,
     604,   607,   610,   613,   616,   619,   622,   626,   629,   632,
     634,   637,   640,   642,   644,   646,   648,   650,   653,   656,
     659,   662,   665,   667,   669,   672,   675,   677,   679,   681,
     684,   687,   689,   691,   693,   694,   697,   699,   701,   705,
     707,   709,   711,   715,   717,   719,   720,   725,   728,   730,
     732,   734,   736,   738,   740,   742,   744,   749,   754,   756,
     760,   764,   768,   772,   776,   780,   784,   788,   792,   796,
     799,   802,   806,   808,   810,   811,   820,   821,   822,   834,
     835,   836,   846,   851,   861,   868,   874,   876,   877,   884,
     887,   890,   892,   895,   896,   897,   905,   906,   910,   912,
     919,   927,   933,   940,   947,   948,   954,   959,   960,   966,
     974,   977,   980,   983,   988,   989,   993,   994,  1002,  1004,
    1006,  1008,  1012,  1014,  1016,  1018,  1022,  1029,  1030,  1037,
    1038,  1044,  1048,  1052,  1056,  1060,  1062,  1064,  1066,  1068,
    1070,  1072,  1074,  1076,  1077,  1083,  1084,  1091,  1094,  1097,
    1100,  1105,  1108,  1112,  1114,  1116,  1120,  1126,  1134,  1137,
    1139,  1142,  1144,  1146,  1150,  1152,  1155,  1159,  1162,  1166,
    1168,  1170,  1172,  1174,  1176,  1178,  1180,  1185,  1187,  1191,
    1195,  1198,  1200,  1202,  1206,  1211,  1215,  1217,  1221,  1222,
    1232,  1233,  1243,  1245,  1247,  1252,  1256,  1259,  1261,  1263,
    1266,  1267,  1271,  1272,  1276,  1277,  1281,  1282,  1286,  1288,
    1292,  1295,  1299,  1300,  1307,  1311,  1316,  1318,  1321,  1322,
    1328,  1329,  1336,  1337,  1341,  1343,  1349,  1355,  1357,  1359,
    1363,  1368,  1370,  1374,  1376,  1381,  1383,  1385,  1388,  1392,
    1397,  1399,  1402,  1405,  1407,  1409,  1411,  1414,  1418,  1420,
    1423,  1427,  1431,  1440,  1443,  1444,  1449,  1450,  1454,  1456,
    1460,  1462,  1464,  1466,  1472,  1475,  1478,  1481,  1484
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     124,     0,    -1,    -1,   125,   126,    -1,   126,   127,    -1,
     258,    -1,    50,   255,    -1,    44,   255,    -1,    89,   255,
      -1,    51,   255,    -1,     6,    -1,    -1,   150,   164,   160,
     163,   157,   128,   146,    -1,   150,   165,    26,   118,    -1,
      -1,    64,   164,   160,   163,   157,   129,   146,    -1,    64,
     165,    26,   118,    -1,    -1,   150,   164,   160,    26,   152,
      27,   214,   130,   146,    -1,   150,   164,   160,    26,   152,
      27,   151,    -1,    -1,   150,   160,    26,   152,    27,   214,
     131,   146,    -1,    64,   164,   160,    26,   152,    27,   151,
      -1,    71,   164,   160,    26,   152,    27,   151,    -1,    -1,
      64,   164,   160,    26,   152,    27,   214,   132,   146,    -1,
      46,    -1,    47,    -1,    48,    26,     3,    27,    -1,    49,
       3,     3,    29,    -1,    -1,    91,   133,   127,    -1,    -1,
      48,    26,    27,   134,   178,    -1,    70,    26,     3,    27,
     150,     3,    29,    -1,    70,    26,     3,    27,   150,   164,
     160,    26,   152,    27,    29,    -1,    95,     7,   245,    -1,
      96,     7,   245,    -1,    97,     7,   245,    -1,    98,     7,
     245,    -1,    81,    -1,    80,    -1,   138,    -1,    82,     4,
      -1,   139,    -1,     4,    -1,     5,     4,    -1,    31,     4,
      -1,    71,     4,    -1,    90,     4,    -1,    90,     7,    -1,
      94,    -1,    31,     3,   171,    -1,    41,     3,   171,    -1,
      34,     3,   149,    -1,    34,    58,    -1,    76,     3,    -1,
      -1,   150,    56,   172,    32,   135,   173,    33,    29,    -1,
      -1,    -1,    14,    56,   172,    32,   136,   173,    33,     3,
     137,   142,    -1,    87,    26,     3,    28,   247,    27,   248,
      32,    -1,    87,    26,   247,    27,   248,    32,    -1,    87,
      26,     3,    28,   247,    27,   248,    29,    -1,    87,    26,
     247,    27,   248,    29,    -1,    87,    26,     3,    28,   247,
      27,   248,    39,   250,    29,    -1,    87,    26,   247,    27,
     248,    39,   250,    29,    -1,    92,   250,    32,   248,    33,
      -1,    93,   248,    29,    -1,    88,    26,     3,    27,    32,
      -1,    88,    32,    -1,    88,    26,     3,    27,    29,    -1,
      88,    29,    -1,    29,    -1,   178,    -1,   220,    -1,     1,
      -1,    30,     7,    32,   126,    33,    -1,   143,    -1,   145,
      -1,    85,   244,    -1,    86,   244,    -1,   256,    -1,    83,
      -1,    84,    -1,    -1,    14,   164,   160,   140,   142,    -1,
      14,   164,    26,   118,   156,    27,    26,   152,    27,    29,
      -1,    14,   164,   161,    26,   118,   156,    27,    26,   152,
      27,    29,    -1,    -1,    14,   164,   160,   162,   141,   142,
      -1,    28,   160,   142,    -1,    28,   160,   162,    -1,   258,
      -1,    72,     3,    -1,    73,     3,    -1,    75,    -1,    74,
      -1,    77,   144,    -1,    79,   144,    -1,    78,    26,     3,
      27,    -1,    78,     3,    -1,   119,   144,    -1,    53,    26,
       3,    28,     3,   246,    27,    -1,    53,     3,   246,    -1,
      53,    26,     3,    27,     3,   246,    -1,    29,    -1,    -1,
      28,   160,   163,   157,   147,   146,    -1,    -1,    28,   160,
      26,   152,    27,   214,   148,   146,    -1,   169,    57,    -1,
      57,    -1,     1,    57,    -1,    30,    -1,   258,    -1,    30,
       7,    -1,   214,    32,    -1,   154,   153,    -1,   258,    -1,
      28,   154,   153,    -1,   258,    -1,   155,    -1,   159,   155,
      -1,   164,   156,    -1,   164,   161,   156,    -1,   164,   112,
     156,    -1,   164,    26,   161,   156,    27,    26,   152,    27,
      -1,    35,    35,    35,    -1,     3,   157,    -1,     3,   162,
      -1,   162,    -1,   258,    -1,    39,   169,    -1,    39,   112,
       3,    -1,    39,    32,    -1,    63,     8,    -1,   258,    -1,
      54,    -1,    55,    -1,   159,   158,    -1,   158,    -1,     3,
      -1,   161,     3,    -1,   112,     3,    -1,   118,   258,    -1,
     118,   161,    -1,    42,    43,   163,    -1,    42,   177,    43,
     163,    -1,   162,    -1,   258,    -1,    15,    -1,    17,   168,
      -1,    18,   168,    -1,    21,    -1,    24,    -1,    19,    -1,
      20,    -1,    22,    -1,    23,   166,    -1,    16,   167,    -1,
      25,   224,    -1,     3,   224,    -1,    36,   164,    -1,   213,
       3,    -1,     3,   122,     3,    -1,   122,     3,    -1,    56,
       3,    -1,    15,    -1,    17,   168,    -1,    18,   168,    -1,
      21,    -1,    24,    -1,    19,    -1,    20,    -1,    22,    -1,
      23,   166,    -1,    16,   167,    -1,    25,   224,    -1,    36,
     164,    -1,   213,     3,    -1,   258,    -1,    15,    -1,    17,
     168,    -1,    18,   168,    -1,    21,    -1,   258,    -1,    15,
      -1,    17,   168,    -1,    18,   168,    -1,    21,    -1,    15,
      -1,   258,    -1,    -1,   170,   177,    -1,     7,    -1,    10,
      -1,   171,    28,     3,    -1,   258,    -1,     3,    -1,   258,
      -1,   173,    28,   174,    -1,   174,    -1,     3,    -1,    -1,
       3,    39,   175,   176,    -1,   143,   174,    -1,   258,    -1,
     177,    -1,    10,    -1,     8,    -1,     9,    -1,    11,    -1,
      12,    -1,    13,    -1,    40,    26,   164,    27,    -1,    26,
     165,    27,   177,    -1,     3,    -1,     3,   122,     3,    -1,
     177,   116,   177,    -1,   177,   115,   177,    -1,   177,   118,
     177,    -1,   177,   117,   177,    -1,   177,   112,   177,    -1,
     177,   110,   177,    -1,   177,   111,   177,    -1,   177,   114,
     177,    -1,   177,   113,   177,    -1,   115,   177,    -1,   120,
     177,    -1,    26,   177,    27,    -1,   179,    -1,   185,    -1,
      -1,   150,   213,     3,   209,    32,   180,   188,    33,    -1,
      -1,    -1,    14,   213,     3,   209,    32,   181,   188,    33,
     160,   182,   142,    -1,    -1,    -1,    14,   213,    32,   183,
     188,    33,   160,   184,   142,    -1,   150,   213,     3,    29,
      -1,   150,   164,   160,   122,     3,    26,   152,    27,    29,
      -1,   150,   164,   160,   122,     3,    29,    -1,   150,   164,
     160,   122,    67,    -1,    69,    -1,    -1,    52,     3,    32,
     186,   187,    33,    -1,   192,   188,    -1,   238,   234,    -1,
     258,    -1,   192,   188,    -1,    -1,    -1,    52,    32,   189,
     188,    33,   190,   188,    -1,    -1,     1,   191,   188,    -1,
     258,    -1,   164,   160,    26,   152,    27,   205,    -1,    65,
     164,   160,    26,   152,    27,   206,    -1,     3,    26,   152,
      27,   215,    -1,   120,     3,    26,   152,    27,   205,    -1,
      65,   120,     3,    26,    27,   205,    -1,    -1,   164,   160,
     157,   193,   202,    -1,   164,   160,   162,   157,    -1,    -1,
      64,   164,   160,   194,   202,    -1,    64,   164,   160,    26,
     152,    27,   205,    -1,    61,    63,    -1,    60,    63,    -1,
      62,    63,    -1,    48,    26,     3,    27,    -1,    -1,    91,
     195,   192,    -1,    -1,    56,   172,    32,   196,   207,    33,
      29,    -1,    46,    -1,    47,    -1,    66,    -1,   164,   201,
      67,    -1,   143,    -1,   139,    -1,   197,    -1,    53,     3,
     246,    -1,    53,    26,     3,    27,     3,   246,    -1,    -1,
     213,     3,    32,   198,   200,    29,    -1,    -1,   213,    32,
     199,   160,    29,    -1,   213,     3,    29,    -1,   164,   161,
      26,    -1,   165,    26,   118,    -1,     3,    26,   118,    -1,
     138,    -1,    29,    -1,   160,    -1,   258,    -1,   161,    -1,
     112,    -1,   258,    -1,    29,    -1,    -1,    28,   160,   157,
     203,   202,    -1,    -1,    28,   160,   162,   157,   204,   202,
      -1,   214,    29,    -1,   214,    32,    -1,   214,    29,    -1,
     214,    39,   169,    29,    -1,   214,    32,    -1,   207,    28,
     208,    -1,   208,    -1,     3,    -1,     3,    39,   176,    -1,
      48,    26,     3,    27,     3,    -1,    48,    26,     3,    27,
       3,    39,   176,    -1,   143,   208,    -1,   258,    -1,    63,
     210,    -1,   258,    -1,   211,    -1,   210,    28,   211,    -1,
       3,    -1,    65,     3,    -1,    65,   212,     3,    -1,   212,
       3,    -1,   212,    65,     3,    -1,    61,    -1,    60,    -1,
      62,    -1,    59,    -1,    37,    -1,    38,    -1,    36,    -1,
      68,    26,   152,    27,    -1,   258,    -1,   214,   216,    29,
      -1,   214,   216,    32,    -1,    63,   217,    -1,   258,    -1,
     218,    -1,   217,    28,   218,    -1,     3,    26,   219,    27,
      -1,     3,    26,    27,    -1,   177,    -1,   219,    28,   177,
      -1,    -1,   102,     3,   223,   221,    32,   225,    33,   234,
     103,    -1,    -1,   102,     3,    26,     3,    27,   224,   222,
     234,   103,    -1,   108,    -1,   109,    -1,   107,     3,   171,
      29,    -1,    63,     3,   224,    -1,   224,   258,    -1,    99,
      -1,   258,    -1,   230,   225,    -1,    -1,   104,   226,   225,
      -1,    -1,   105,   227,   225,    -1,    -1,   106,   228,   225,
      -1,    -1,     1,   229,   225,    -1,   258,    -1,   231,   233,
      29,    -1,   164,   160,    -1,   164,   160,   162,    -1,    -1,
      48,    26,     3,    27,   232,   231,    -1,    28,   160,   233,
      -1,    28,   160,   162,   233,    -1,   258,    -1,   238,   234,
      -1,    -1,    52,    32,   235,   234,    33,    -1,    -1,    48,
      26,     3,    27,   236,   234,    -1,    -1,     1,   237,   234,
      -1,   258,    -1,   115,   240,     3,   242,   239,    -1,   116,
     240,     3,   242,   239,    -1,    29,    -1,    32,    -1,    26,
     164,    27,    -1,    26,   164,   161,    27,    -1,   258,    -1,
      26,   154,    27,    -1,   258,    -1,   242,   243,   241,     3,
      -1,   258,    -1,    63,    -1,     3,    63,    -1,     3,   246,
     245,    -1,   245,    28,     3,   246,    -1,   258,    -1,    39,
       8,    -1,    39,     7,    -1,   258,    -1,     3,    -1,    36,
      -1,   250,   249,    -1,    28,   250,   249,    -1,   258,    -1,
     164,   251,    -1,   164,   161,   251,    -1,   164,   112,   251,
      -1,   164,    26,   161,   251,    27,    26,   152,    27,    -1,
       3,   254,    -1,    -1,     3,   162,   252,   254,    -1,    -1,
     162,   253,   254,    -1,   254,    -1,    26,   152,    27,    -1,
     258,    -1,     3,    -1,     7,    -1,   101,    26,   152,    27,
     257,    -1,   101,   257,    -1,     3,    29,    -1,     7,    29,
      -1,    32,    33,    -1,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   559,   559,   559,   582,   586,   590,   601,   618,   636,
     646,   657,   657,   688,   696,   696,   708,   717,   717,   733,
     746,   746,   759,   774,   797,   797,   812,   819,   825,   833,
     842,   842,   850,   850,   862,   874,   895,   943,   973,  1009,
    1046,  1054,  1062,  1066,  1075,  1079,  1090,  1100,  1109,  1119,
    1125,  1132,  1138,  1160,  1176,  1195,  1202,  1208,  1208,  1223,
    1223,  1223,  1243,  1256,  1275,  1287,  1305,  1320,  1341,  1352,
    1369,  1376,  1383,  1388,  1394,  1395,  1396,  1397,  1415,  1416,
    1420,  1424,  1440,  1453,  1459,  1473,  1492,  1492,  1508,  1530,
    1554,  1554,  1583,  1595,  1606,  1626,  1652,  1675,  1694,  1704,
    1730,  1759,  1768,  1775,  1781,  1789,  1793,  1801,  1802,  1802,
    1829,  1829,  1842,  1845,  1848,  1856,  1857,  1858,  1870,  1879,
    1885,  1888,  1893,  1896,  1901,  1916,  1942,  1961,  1973,  1984,
    1994,  2003,  2008,  2014,  2021,  2022,  2028,  2032,  2034,  2037,
    2038,  2041,  2044,  2051,  2055,  2060,  2070,  2071,  2075,  2079,
    2086,  2089,  2097,  2100,  2103,  2106,  2109,  2112,  2115,  2118,
    2121,  2125,  2129,  2140,  2155,  2160,  2165,  2174,  2180,  2190,
    2193,  2196,  2199,  2202,  2205,  2208,  2211,  2214,  2218,  2222,
    2226,  2231,  2240,  2243,  2249,  2255,  2261,  2271,  2274,  2280,
    2286,  2292,  2300,  2301,  2304,  2304,  2310,  2317,  2329,  2335,
    2345,  2346,  2352,  2353,  2357,  2362,  2362,  2369,  2370,  2373,
    2385,  2396,  2400,  2404,  2408,  2412,  2416,  2421,  2426,  2438,
    2445,  2451,  2457,  2464,  2471,  2482,  2494,  2506,  2518,  2530,
    2537,  2547,  2558,  2559,  2565,  2565,  2633,  2667,  2633,  2734,
    2757,  2734,  2798,  2809,  2830,  2850,  2858,  2866,  2866,  2884,
    2885,  2886,  2889,  2890,  2892,  2890,  2895,  2895,  2906,  2909,
    2933,  2956,  2977,  2997,  3017,  3017,  3070,  3101,  3101,  3124,
    3144,  3155,  3166,  3177,  3185,  3185,  3192,  3192,  3210,  3215,
    3221,  3229,  3235,  3240,  3244,  3249,  3252,  3275,  3275,  3301,
    3301,  3326,  3333,  3338,  3343,  3348,  3349,  3352,  3353,  3356,
    3357,  3358,  3361,  3362,  3362,  3387,  3387,  3415,  3418,  3421,
    3422,  3423,  3426,  3427,  3430,  3445,  3461,  3476,  3492,  3493,
    3496,  3499,  3505,  3518,  3527,  3532,  3537,  3546,  3555,  3566,
    3567,  3568,  3572,  3573,  3574,  3577,  3578,  3579,  3584,  3587,
    3590,  3591,  3594,  3595,  3598,  3599,  3602,  3603,  3611,  3611,
    3644,  3644,  3660,  3661,  3662,  3677,  3678,  3682,  3688,  3693,
    3694,  3694,  3697,  3697,  3700,  3700,  3703,  3703,  3717,  3720,
    3727,  3749,  3771,  3771,  3776,  3796,  3818,  3821,  3822,  3822,
    3827,  3827,  3831,  3831,  3845,  3848,  3868,  3889,  3890,  3893,
    3896,  3900,  3908,  3912,  3920,  3926,  3931,  3932,  3943,  3953,
    3960,  3967,  3970,  3973,  3983,  3986,  3991,  3997,  4001,  4004,
    4017,  4031,  4044,  4059,  4063,  4063,  4072,  4072,  4082,  4088,
    4091,  4096,  4097,  4103,  4104,  4107,  4108,  4109,  4141
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "ID", "HBLOCK", "WRAPPER", "POUND",
  "STRING", "NUM_INT", "NUM_FLOAT", "CHARCONST", "NUM_UNSIGNED",
  "NUM_LONG", "NUM_ULONG", "TYPEDEF", "TYPE_INT", "TYPE_UNSIGNED",
  "TYPE_SHORT", "TYPE_LONG", "TYPE_FLOAT", "TYPE_DOUBLE", "TYPE_CHAR",
  "TYPE_VOID", "TYPE_SIGNED", "TYPE_BOOL", "TYPE_TYPEDEF", "LPAREN",
  "RPAREN", "COMMA", "SEMI", "EXTERN", "INIT", "LBRACE", "RBRACE",
  "DEFINE", "PERIOD", "CONST", "STRUCT", "UNION", "EQUAL", "SIZEOF",
  "MODULE", "LBRACKET", "RBRACKET", "WEXTERN", "ILLEGAL", "READONLY",
  "READWRITE", "NAME", "RENAME", "INCLUDE", "CHECKOUT", "ADDMETHODS",
  "PRAGMA", "CVALUE", "COUT", "ENUM", "ENDDEF", "MACRO", "CLASS",
  "PRIVATE", "PUBLIC", "PROTECTED", "COLON", "STATIC", "VIRTUAL", "FRIEND",
  "OPERATOR", "THROW", "TEMPLATE", "NATIVE", "INLINE", "IFDEF", "IFNDEF",
  "ENDIF", "ELSE", "UNDEF", "IF", "DEFINED", "ELIF", "RAW_MODE",
  "ALPHA_MODE", "TEXT", "DOC_DISABLE", "DOC_ENABLE", "STYLE", "LOCALSTYLE",
  "TYPEMAP", "EXCEPT", "IMPORT", "ECHO", "NEW", "APPLY", "CLEAR",
  "DOCONLY", "TITLE", "SECTION", "SUBSECTION", "SUBSUBSECTION", "LESSTHAN",
  "GREATERTHAN", "USERDIRECTIVE", "OC_INTERFACE", "OC_END", "OC_PUBLIC",
  "OC_PRIVATE", "OC_PROTECTED", "OC_CLASS", "OC_IMPLEMENT", "OC_PROTOCOL",
  "OR", "XOR", "AND", "RSHIFT", "LSHIFT", "MINUS", "PLUS", "SLASH", "STAR",
  "LNOT", "NOT", "UMINUS", "DCOLON", "$accept", "program", "$@1",
  "command", "statement", "$@2", "$@3", "$@4", "$@5", "$@6", "$@7", "$@8",
  "$@9", "$@10", "$@11", "doc_enable", "typedef_decl", "$@12", "$@13",
  "typedeflist", "cond_compile", "cpp_const_expr", "pragma", "stail",
  "$@14", "$@15", "definetail", "extern", "func_end", "parms", "ptail",
  "parm", "parm_type", "pname", "def_args", "parm_specifier",
  "parm_specifier_list", "declaration", "stars", "array", "array2", "type",
  "strict_type", "opt_signed", "opt_unsigned", "opt_int", "definetype",
  "$@16", "initlist", "ename", "enumlist", "edecl", "$@17", "etype",
  "expr", "cpp", "cpp_class", "$@18", "$@19", "$@20", "$@21", "$@22",
  "cpp_other", "$@23", "added_members", "cpp_members", "$@24", "$@25",
  "$@26", "cpp_member", "$@27", "$@28", "$@29", "$@30", "cpp_pragma",
  "$@31", "$@32", "nested_decl", "type_extra", "cpp_tail", "$@33", "$@34",
  "cpp_end", "cpp_vend", "cpp_enumlist", "cpp_edecl", "inherit",
  "base_list", "base_specifier", "access_specifier", "cpptype",
  "cpp_const", "ctor_end", "ctor_initializer", "mem_initializer_list",
  "mem_initializer", "expr_list", "objective_c", "$@35", "$@36",
  "objc_inherit", "objc_protolist", "objc_data", "$@37", "$@38", "$@39",
  "$@40", "objc_vars", "objc_var", "$@41", "objc_vartail", "objc_methods",
  "$@42", "$@43", "$@44", "objc_method", "objc_end", "objc_ret_type",
  "objc_arg_type", "objc_args", "objc_separator", "stylelist", "styletail",
  "stylearg", "tm_method", "tm_list", "tm_tail", "typemap_parm",
  "typemap_name", "$@45", "$@46", "typemap_args", "idstring",
  "user_directive", "uservalue", "empty", 0
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320,   321,   322,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   334,
     335,   336,   337,   338,   339,   340,   341,   342,   343,   344,
     345,   346,   347,   348,   349,   350,   351,   352,   353,   354,
     355,   356,   357,   358,   359,   360,   361,   362,   363,   364,
     365,   366,   367,   368,   369,   370,   371,   372,   373,   374,
     375,   376,   377
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint16 yyr1[] =
{
       0,   123,   125,   124,   126,   126,   127,   127,   127,   127,
     127,   128,   127,   127,   129,   127,   127,   130,   127,   127,
     131,   127,   127,   127,   132,   127,   127,   127,   127,   127,
     133,   127,   134,   127,   127,   127,   127,   127,   127,   127,
     127,   127,   127,   127,   127,   127,   127,   127,   127,   127,
     127,   127,   127,   127,   127,   127,   127,   135,   127,   136,
     137,   127,   127,   127,   127,   127,   127,   127,   127,   127,
     127,   127,   127,   127,   127,   127,   127,   127,   127,   127,
     127,   127,   127,   127,   138,   138,   140,   139,   139,   139,
     141,   139,   142,   142,   142,   143,   143,   143,   143,   143,
     143,   144,   144,   144,   145,   145,   145,   146,   147,   146,
     148,   146,   149,   149,   149,   150,   150,   150,   151,   152,
     152,   153,   153,   154,   154,   155,   155,   155,   155,   155,
     156,   156,   156,   156,   157,   157,   157,   157,   157,   158,
     158,   159,   159,   160,   160,   160,   161,   161,   162,   162,
     163,   163,   164,   164,   164,   164,   164,   164,   164,   164,
     164,   164,   164,   164,   164,   164,   164,   164,   164,   165,
     165,   165,   165,   165,   165,   165,   165,   165,   165,   165,
     165,   165,   166,   166,   166,   166,   166,   167,   167,   167,
     167,   167,   168,   168,   170,   169,   169,   169,   171,   171,
     172,   172,   173,   173,   174,   175,   174,   174,   174,   176,
     176,   177,   177,   177,   177,   177,   177,   177,   177,   177,
     177,   177,   177,   177,   177,   177,   177,   177,   177,   177,
     177,   177,   178,   178,   180,   179,   181,   182,   179,   183,
     184,   179,   185,   185,   185,   185,   185,   186,   185,   187,
     187,   187,   188,   189,   190,   188,   191,   188,   188,   192,
     192,   192,   192,   192,   193,   192,   192,   194,   192,   192,
     192,   192,   192,   192,   195,   192,   196,   192,   192,   192,
     192,   192,   192,   192,   192,   197,   197,   198,   197,   199,
     197,   197,   197,   197,   197,   197,   197,   200,   200,   201,
     201,   201,   202,   203,   202,   204,   202,   205,   205,   206,
     206,   206,   207,   207,   208,   208,   208,   208,   208,   208,
     209,   209,   210,   210,   211,   211,   211,   211,   211,   212,
     212,   212,   213,   213,   213,   214,   214,   214,   215,   215,
     216,   216,   217,   217,   218,   218,   219,   219,   221,   220,
     222,   220,   220,   220,   220,   223,   223,   224,   224,   225,
     226,   225,   227,   225,   228,   225,   229,   225,   225,   230,
     231,   231,   232,   231,   233,   233,   233,   234,   235,   234,
     236,   234,   237,   234,   234,   238,   238,   239,   239,   240,
     240,   240,   241,   241,   242,   242,   243,   243,   244,   245,
     245,   246,   246,   246,   247,   247,   248,   249,   249,   250,
     250,   250,   250,   251,   252,   251,   253,   251,   251,   254,
     254,   255,   255,   256,   256,   257,   257,   257,   258
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     0,     2,     2,     1,     2,     2,     2,     2,
       1,     0,     7,     4,     0,     7,     4,     0,     9,     7,
       0,     8,     7,     7,     0,     9,     1,     1,     4,     4,
       0,     3,     0,     5,     7,    11,     3,     3,     3,     3,
       1,     1,     1,     2,     1,     1,     2,     2,     2,     2,
       2,     1,     3,     3,     3,     2,     2,     0,     8,     0,
       0,    10,     8,     6,     8,     6,    10,     8,     5,     3,
       5,     2,     5,     2,     1,     1,     1,     1,     5,     1,
       1,     2,     2,     1,     1,     1,     0,     5,    10,    11,
       0,     6,     3,     3,     1,     2,     2,     1,     1,     2,
       2,     4,     2,     2,     7,     3,     6,     1,     0,     6,
       0,     8,     2,     1,     2,     1,     1,     2,     2,     2,
       1,     3,     1,     1,     2,     2,     3,     3,     8,     3,
       2,     2,     1,     1,     2,     3,     2,     2,     1,     1,
       1,     2,     1,     1,     2,     2,     2,     2,     3,     4,
       1,     1,     1,     2,     2,     1,     1,     1,     1,     1,
       2,     2,     2,     2,     2,     2,     3,     2,     2,     1,
       2,     2,     1,     1,     1,     1,     1,     2,     2,     2,
       2,     2,     1,     1,     2,     2,     1,     1,     1,     2,
       2,     1,     1,     1,     0,     2,     1,     1,     3,     1,
       1,     1,     3,     1,     1,     0,     4,     2,     1,     1,
       1,     1,     1,     1,     1,     1,     4,     4,     1,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     2,
       2,     3,     1,     1,     0,     8,     0,     0,    11,     0,
       0,     9,     4,     9,     6,     5,     1,     0,     6,     2,
       2,     1,     2,     0,     0,     7,     0,     3,     1,     6,
       7,     5,     6,     6,     0,     5,     4,     0,     5,     7,
       2,     2,     2,     4,     0,     3,     0,     7,     1,     1,
       1,     3,     1,     1,     1,     3,     6,     0,     6,     0,
       5,     3,     3,     3,     3,     1,     1,     1,     1,     1,
       1,     1,     1,     0,     5,     0,     6,     2,     2,     2,
       4,     2,     3,     1,     1,     3,     5,     7,     2,     1,
       2,     1,     1,     3,     1,     2,     3,     2,     3,     1,
       1,     1,     1,     1,     1,     1,     4,     1,     3,     3,
       2,     1,     1,     3,     4,     3,     1,     3,     0,     9,
       0,     9,     1,     1,     4,     3,     2,     1,     1,     2,
       0,     3,     0,     3,     0,     3,     0,     3,     1,     3,
       2,     3,     0,     6,     3,     4,     1,     2,     0,     5,
       0,     6,     0,     3,     1,     5,     5,     1,     1,     3,
       4,     1,     3,     1,     4,     1,     1,     2,     3,     4,
       1,     2,     2,     1,     1,     1,     2,     3,     1,     2,
       3,     3,     8,     2,     0,     4,     0,     3,     1,     3,
       1,     1,     1,     5,     2,     2,     2,     2,     0
};

/* YYDEFACT[STATE-NAME] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       2,     0,   428,     1,     0,     5,    77,    45,     0,    10,
       0,    74,   115,     0,     0,     0,     0,    26,    27,     0,
       0,     0,     0,     0,     0,     0,   246,     0,     0,     0,
       0,    98,    97,     0,     0,     0,    41,    40,     0,    84,
      85,     0,     0,     0,     0,     0,     0,    30,     0,     0,
      51,     0,     0,     0,     0,     0,     0,     0,   352,   353,
       4,    42,    44,    79,    80,     0,    75,   232,   233,    76,
      83,   116,    46,   428,   152,   428,   428,   428,   157,   158,
     155,   159,   428,   156,   428,     0,   333,   334,   428,   332,
       0,     0,     0,   117,   428,    47,     0,    55,   428,   421,
     422,     7,     0,     0,     6,     9,     0,   428,     0,   152,
     428,   428,   428,   157,   158,   155,   159,   428,   156,   428,
       0,     0,     0,     0,     0,     0,    48,     0,     0,    95,
      96,    56,     0,     0,    99,   100,    43,   428,    81,    82,
       0,     0,    73,    71,     8,    49,    50,     0,   428,     0,
       0,   428,   428,   428,   428,   428,     0,     0,   428,     0,
     424,   428,   428,   428,   428,     0,   428,     0,     0,     0,
       0,     0,   357,     0,   163,   358,   188,   428,   428,   191,
     161,   187,   192,   153,   193,   154,   183,   428,   428,   186,
     160,   182,   162,   164,   168,     0,   201,   167,   143,     0,
      86,     0,   165,   239,   428,    52,   199,     0,   196,   197,
     113,    54,     0,     0,    53,     0,    32,     0,   247,     0,
     105,   403,     0,   161,   153,   154,   160,   162,   164,   168,
     428,     0,   165,     0,     0,   165,   102,     0,   103,   428,
     404,   405,     0,     0,    31,   428,   428,     0,   428,   428,
     416,   409,   418,   420,     0,    69,     0,   406,   408,    36,
     400,    37,    38,    39,   425,   426,     0,   139,   140,     0,
     428,   123,   142,     0,   428,   120,   427,     0,     0,   348,
     428,     0,     0,   145,   147,   146,   428,   144,   428,     0,
     165,   166,   189,   190,   184,   185,    59,   428,   428,    90,
       0,     0,     0,   321,     0,     0,     0,   114,   112,   218,
     211,   212,   213,   214,   215,     0,     0,     0,     0,   195,
      28,   428,    29,   428,   402,   401,     0,     0,   428,   150,
     428,   151,    16,   428,   428,     0,   398,     0,     0,     0,
     428,   414,   413,     0,   428,   428,     0,   411,   410,   428,
       0,   428,     0,     0,     0,     0,   119,   122,   124,   141,
     428,     0,   428,   125,   428,   132,   133,     0,   428,     0,
     356,   354,    57,     0,   428,     0,   428,    13,   242,     0,
     428,     0,     0,    87,    94,   428,   428,   324,   330,   329,
     331,     0,   320,   322,     0,   236,   256,   428,     0,   296,
     278,   279,     0,     0,     0,   428,     0,     0,     0,     0,
       0,   280,   274,     0,   295,   283,   282,   428,     0,     0,
       0,   284,     0,   258,    78,   198,     0,   169,   428,   428,
     428,   174,   175,   172,   176,   428,   173,   428,     0,     0,
       0,     0,     0,   229,   230,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   115,     0,    33,   428,   428,
       0,     0,     0,   251,   428,   428,     0,   194,     0,    14,
     138,     0,     0,   101,   404,     0,     0,    72,    70,   428,
     419,     0,   148,   428,   417,    68,   407,   428,   129,   423,
     428,   130,   131,   428,   127,   126,   428,   355,     0,   428,
     428,     0,     0,   245,    11,   234,   204,   428,     0,   203,
     208,     0,   428,    91,     0,   325,     0,     0,   327,     0,
       0,     0,   428,     0,   253,   428,     0,     0,   271,   270,
     272,     0,     0,     0,     0,     0,   300,   428,   299,     0,
     301,     0,     0,   252,   165,   289,   219,   178,   170,   171,
     177,   179,   180,     0,   231,   181,     0,   225,   226,   224,
     228,   227,   221,   220,   223,   222,     0,   117,     0,     0,
       0,     0,   391,     0,   248,   249,   382,     0,     0,   250,
       0,   384,   106,     0,   428,   136,     0,   134,   137,     0,
     428,     0,   428,     0,    65,    63,     0,   415,     0,   149,
     399,   121,     0,   350,   366,     0,   360,   362,   364,     0,
       0,     0,   428,   368,     0,   335,     0,    20,   337,   428,
     428,   244,     0,     0,   205,   207,   428,     0,   428,    92,
      93,     0,   326,   323,   328,     0,   257,   294,     0,     0,
       0,   285,     0,   276,   267,     0,     0,   275,   428,   428,
     264,   428,   292,   281,   293,   240,   291,   287,     0,   217,
     216,   428,     0,   165,     0,   428,   428,     0,     0,   378,
     377,   104,    22,    24,   135,     0,   107,    15,    34,     0,
      23,     0,     0,     0,   428,     0,     0,     0,     0,     0,
       0,     0,   370,     0,   359,     0,     0,   376,     0,   428,
       0,    19,    17,     0,    12,     0,     0,   202,    60,     0,
     428,     0,   428,   273,     0,     0,   428,   428,     0,     0,
     428,     0,     0,     0,   266,   428,   428,     0,   389,     0,
       0,   395,     0,   383,     0,     0,   118,     0,   428,   428,
      64,    62,     0,    67,     0,   428,     0,   367,     0,   361,
     363,   365,   371,     0,   428,   369,    58,     0,    21,     0,
       0,   235,   210,   206,   209,   428,     0,     0,   237,   428,
     261,   254,   428,   314,     0,   428,     0,   313,   319,     0,
       0,   302,   268,   428,     0,   428,   428,   265,   241,   297,
       0,   298,   290,   390,     0,   387,   388,   396,   385,   428,
     386,   380,     0,    25,   428,   428,     0,     0,   412,     0,
     351,   372,   349,   428,   374,   336,    18,   243,    61,    88,
       0,   428,     0,     0,   341,     0,   286,     0,     0,   318,
     428,     0,   428,   428,   263,     0,   428,   262,   259,   288,
     397,     0,     0,   393,     0,   379,     0,   108,     0,    66,
     128,     0,   375,    89,   238,     0,   340,   342,   338,   339,
     255,   315,     0,   312,   277,   269,   303,   428,   307,   308,
     260,     0,     0,   394,   381,   428,     0,    35,   373,     0,
       0,     0,     0,   305,   309,   311,   194,   392,   110,   109,
     345,   346,     0,   343,   316,   304,     0,     0,     0,   344,
       0,     0,   306,   310,   111,   347,   317
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     1,     2,     4,    60,   622,   589,   759,   700,   737,
     147,   321,   499,   380,   765,   414,   415,   298,   385,   383,
     416,   134,    64,   677,   876,   898,   211,    65,   672,   343,
     356,   270,   271,   363,   469,   272,   273,   167,   168,   365,
     330,   274,   418,   190,   180,   183,   212,   213,   205,   195,
     508,   509,   706,   763,   764,    66,    67,   623,   520,   821,
     304,   725,    68,   323,   460,   419,   640,   825,   521,   420,
     723,   718,   534,   716,   421,   726,   658,   790,   539,   782,
     882,   896,   834,   870,   776,   777,   302,   392,   393,   394,
     128,   835,   770,   823,   856,   857,   892,    69,   369,   686,
     279,   174,   610,   689,   690,   691,   687,   611,   612,   851,
     696,   579,   735,   844,   667,   580,   798,   571,   842,   730,
     799,   138,   259,   220,   242,   150,   257,   151,   251,   479,
     349,   252,   101,    70,   160,   275
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -789
static const yytype_int16 yypact[] =
{
    -789,   170,  -789,  -789,   967,  -789,  -789,  -789,   221,  -789,
    1866,  -789,   191,    65,   165,   235,    63,  -789,  -789,   244,
     282,    63,    63,   306,    57,  1912,  -789,   313,  1733,   351,
     360,  -789,  -789,   440,    70,    70,  -789,  -789,   437,  -789,
    -789,   446,   446,   448,   458,    63,   432,  -789,  1936,  1936,
    -789,   471,   488,   496,   500,   387,   452,   519,  -789,  -789,
    -789,  -789,  -789,  -789,  -789,  1686,  -789,  -789,  -789,  -789,
    -789,  -789,  -789,    68,  -789,   494,   513,   513,  -789,  -789,
    -789,  -789,   512,  -789,   462,  1936,  -789,  -789,   531,  -789,
     536,   103,   198,   537,  -789,  -789,   555,  -789,  -789,  -789,
    -789,  -789,   231,   568,  -789,  -789,   551,   545,   582,   560,
     494,   513,   513,   565,   567,   570,   580,   512,   581,   462,
    1936,   586,    45,   587,   591,   611,  -789,    45,   612,  -789,
    -789,  -789,   294,    70,  -789,  -789,  -789,   545,  -789,  -789,
      48,   613,  -789,  -789,  -789,  -789,  -789,  1210,   169,   588,
     589,   594,  -789,  -789,  -789,  -789,   590,   596,   871,   595,
    -789,     1,  -789,     3,   531,   620,   511,   606,   627,    45,
     609,   633,  -789,   634,  -789,  -789,  -789,   513,   513,  -789,
    -789,  -789,  -789,  -789,  -789,  -789,  -789,   513,   513,  -789,
    -789,  -789,  -789,  -789,   607,   610,  -789,  -789,  -789,   523,
     601,   341,    15,  -789,  -789,   617,  -789,   593,  -789,  -789,
    -789,  -789,   603,  1998,   617,   619,  -789,   618,  -789,   173,
    -789,  -789,   520,   622,   636,   640,   641,   642,   646,  -789,
     182,   556,   647,   649,   652,  -789,  -789,   676,  -789,  -789,
     653,  -789,   656,   663,  -789,   375,  1617,   742,   322,   322,
    -789,  -789,  -789,  -789,  1936,  -789,  1936,  -789,  -789,   666,
    -789,   666,   666,   666,  -789,  -789,   661,  -789,  -789,   672,
     673,  -789,  -789,   871,   194,  -789,  -789,   697,   699,  -789,
    -789,   485,   675,  -789,  -789,  -789,   871,  -789,     0,   614,
     237,  -789,  -789,  -789,  -789,  -789,  -789,   202,   677,  -789,
     621,    29,   679,  -789,  1320,  1100,   701,  -789,  -789,   605,
    -789,  -789,  -789,  -789,  -789,  2024,   683,  1998,  1998,   838,
    -789,   205,  -789,  1451,  -789,  -789,   709,   710,   871,  -789,
     238,  -789,  -789,   695,   871,   704,   666,    62,  1936,   450,
     871,  -789,  -789,   708,   322,   601,   981,  -789,  -789,   702,
     705,   594,   734,   706,   273,   871,  -789,  -789,  -789,  -789,
     349,   511,   202,  -789,   202,  -789,  -789,   713,   462,   711,
    -789,  -789,  -789,   715,   871,    52,   238,  -789,  -789,   714,
     332,   721,    45,  -789,  -789,   677,   202,  -789,  -789,  -789,
    -789,   229,   728,  -789,    76,  -789,  -789,     8,  1936,  -789,
    -789,  -789,   731,   726,   376,   531,   698,   703,   712,  1936,
    1794,  -789,  -789,   757,  -789,  -789,  -789,   100,   736,   732,
    1320,  -789,   276,  -789,  -789,  -789,   761,  -789,   494,   513,
     513,  -789,  -789,  -789,  -789,   512,  -789,   462,  1936,   744,
     829,   766,  1936,  -789,  -789,  1998,  1998,  1998,  1998,  1998,
    1998,  1998,  1998,  1998,   410,   767,  1936,  -789,   750,   750,
     745,  1320,   125,  -789,   545,   545,   752,    30,   769,  -789,
    -789,  1960,   753,  -789,  -789,   760,   429,  -789,  -789,   702,
    -789,   762,  -789,   601,  -789,  -789,  -789,   545,  -789,  -789,
     673,  -789,  -789,   202,  -789,  -789,   462,  -789,  1397,   332,
      20,   763,   495,  -789,  -789,  -789,   749,   332,   289,  -789,
    -789,   765,   323,  -789,   768,  -789,   789,    29,  -789,   791,
    1320,  1320,  1662,   795,  -789,   545,   796,   770,  -789,  -789,
    -789,    45,   797,    45,  1540,   775,   620,   333,   411,   737,
    -789,   687,    45,  -789,   514,  -789,  -789,  -789,  -789,  -789,
    -789,  -789,  -789,  1998,  -789,  -789,   779,   604,   540,   486,
     435,   435,   442,   442,  -789,  -789,   279,  -789,    45,   804,
    1936,   807,  -789,   809,  -789,  -789,  -789,   788,   783,  -789,
     337,  -789,  -789,   790,    20,  -789,   813,  -789,  -789,   546,
       2,    45,    20,  1936,  -789,  -789,  1936,  -789,   792,  -789,
    -789,  -789,   793,  -789,  -789,   798,  -789,  -789,  -789,    45,
     794,  1397,   801,  -789,   364,  -789,   799,  -789,  -789,    20,
     871,  -789,   546,  1320,  -789,  -789,   332,   818,   871,  -789,
    -789,   800,  -789,  -789,  -789,   802,  -789,  -789,   805,   810,
    1320,  -789,   811,  -789,   814,   815,   817,  -789,   871,   871,
    -789,   238,  -789,  -789,  -789,  -789,  -789,  -789,    45,  -789,
    -789,   776,   722,     9,    26,  -789,  -789,   337,   843,  -789,
    -789,  -789,  -789,   827,  -789,    45,  -789,  -789,  -789,   821,
    -789,   827,   441,   831,   871,   835,   266,  1397,   860,  1397,
    1397,  1397,   601,   266,  -789,    45,   837,  -789,   840,   871,
     546,  -789,   827,   844,  -789,   834,   842,  -789,  -789,   845,
     871,    45,    20,  -789,   846,   867,   427,   871,   548,   848,
     871,   849,   850,   548,  -789,   677,    45,   851,  -789,   856,
     210,  -789,   210,  -789,   858,   125,  -789,   546,   408,   871,
    -789,  -789,  1936,  -789,   870,   871,   812,  -789,   873,  -789,
    -789,  -789,  -789,   816,   329,  -789,  -789,   874,  -789,   546,
     869,  -789,  -789,  -789,   838,   677,   875,   876,  -789,   839,
    -789,  -789,   545,   866,   852,   427,   438,  -789,  -789,   883,
      45,  -789,  -789,    20,   885,    20,    20,  -789,  -789,  -789,
     884,  -789,  -789,  -789,   853,  -789,  -789,  -789,  -789,   888,
    -789,  -789,   887,  -789,   871,   238,   890,   892,  -789,   895,
    -789,  -789,  -789,   801,  -789,  -789,  -789,  -789,  -789,  -789,
     894,   677,   921,   509,  -789,  1320,  -789,   842,   926,  -789,
     427,   902,    20,   349,  -789,   525,    20,  -789,  -789,  -789,
    -789,   871,   929,  -789,   337,  -789,   906,  -789,   905,  -789,
    -789,  1820,  -789,  -789,  -789,   909,   908,  -789,  -789,  -789,
    -789,  -789,   910,  -789,  -789,  -789,  -789,   238,  -789,  -789,
    -789,   454,   911,  -789,  -789,    20,   546,  -789,  -789,  1991,
     921,   955,   548,  -789,  -789,  -789,   563,  -789,  -789,  -789,
    -789,   838,   552,  -789,   920,  -789,   548,   931,   546,  -789,
    1998,   842,  -789,  -789,  -789,   838,  -789
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -789,  -789,  -789,   759,   819,  -789,  -789,  -789,  -789,  -789,
    -789,  -789,  -789,  -789,  -789,    19,    24,  -789,  -789,  -379,
      18,   -10,  -789,  -605,  -789,  -789,  -789,   111,  -436,  -112,
     474,  -352,   688,  -248,  -341,   692,  -789,   138,   -67,   -61,
    -284,   288,   -11,  -108,   -98,    16,  -457,  -789,   -31,  -144,
     470,  -489,  -789,  -788,  -197,   655,  -789,  -789,  -789,  -789,
    -789,  -789,  -789,  -789,  -789,  -409,  -789,  -789,  -789,  -308,
    -789,  -789,  -789,  -789,  -789,  -789,  -789,  -789,  -789,  -690,
    -789,  -789,  -445,  -789,  -789,  -597,  -283,  -789,   457,   608,
      11,  -437,  -789,  -789,  -789,   114,  -789,  -789,  -789,  -789,
    -789,   -76,  -266,  -789,  -789,  -789,  -789,  -789,   129,  -789,
    -677,  -476,  -789,  -789,  -789,   684,   263,   541,  -789,   336,
    -789,   964,   -96,  -132,   685,  -241,   658,   -47,  -204,  -789,
    -789,  -215,   355,  -789,   667,    -2
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -429
static const yytype_int16 yytable[] =
{
       5,   149,    71,   490,   376,   239,   513,   379,   192,   226,
     587,   543,   223,   350,   123,   461,   319,   704,   625,   491,
     282,    92,    63,    61,   201,   135,   374,   277,    62,  -143,
     342,   678,   387,   787,   522,   504,   124,   208,   378,   861,
     209,  -428,   247,   227,   347,   348,   269,  -428,   198,   381,
     346,   240,   575,   728,   170,   502,   615,   261,   262,   263,
     107,   482,   585,   617,   278,   474,    99,   214,    94,    95,
     100,   175,   301,   181,   184,   184,   171,   814,   301,   518,
     191,   249,   175,   108,   241,   280,   196,   250,   616,   388,
     389,   390,   206,   185,   391,   758,   206,   476,   241,   284,
     172,   172,   172,   198,   670,   221,   198,   172,   181,   184,
     184,   635,   636,   906,   494,   191,   495,   175,   440,   503,
     443,   444,   375,   238,   173,   173,   576,   224,   225,   199,
     173,   281,   803,   629,   484,   221,   852,   707,   514,   299,
     481,   519,   586,   336,   166,    71,   253,   673,   132,   258,
     260,   260,   260,   260,   816,   681,   680,   165,  -428,   175,
     206,   175,   196,   166,   285,    63,    61,   172,    96,   329,
       3,    62,   245,   577,   373,   184,   184,   578,   829,   344,
     324,   325,   702,   701,   341,   184,   184,   250,   250,   133,
     173,   733,   895,   292,   293,   246,   650,   360,    93,   599,
     303,   202,     5,   294,   295,   360,   902,   364,   328,   351,
     746,   247,   536,   794,   705,   165,   466,   753,   166,   454,
     361,   166,   472,    97,   247,    72,   647,   329,   331,   200,
     203,   714,   515,   863,   215,   455,   247,   260,    98,   795,
     458,   459,   796,   253,   247,   602,   253,   253,   557,   558,
     559,   560,   561,   562,   563,   564,   565,    23,   216,   802,
     230,   527,   501,  -181,   597,   234,   378,   576,   357,  -428,
     102,   889,   366,   797,    26,   769,   156,   467,   370,   544,
     157,   248,   661,   250,   329,   103,   331,   166,   303,   388,
     389,   390,   497,   904,   493,   366,   384,   236,    91,   492,
     301,   468,   423,    71,   439,   159,   362,   288,   545,   106,
     724,   203,   166,   122,   577,   422,   127,   626,   578,    71,
     237,   463,   627,    63,    61,   245,   441,   550,   470,    62,
     547,    71,   582,   583,   422,   506,   148,   148,   576,   125,
     837,   838,   253,   331,   287,   694,   788,   253,   340,   258,
     538,   382,   682,   169,   129,   600,   659,   695,   470,   649,
     366,   551,   366,   130,   247,   247,   175,   300,   874,  -428,
    -428,   247,   467,   193,   470,   247,   104,   105,   510,   525,
     379,   458,   459,   384,   366,   577,   818,   865,   467,   578,
     156,   247,   626,   641,   157,   175,   468,   698,   507,   871,
     144,   340,   526,   196,    29,    30,    31,    32,   228,    34,
     638,    35,   468,   158,   287,   540,   860,   247,   423,   159,
     603,   747,   329,   749,   750,   751,   181,   184,   184,   897,
     773,   422,   456,   191,   804,   175,   145,   652,   888,   146,
    -428,   136,   854,   131,   471,   548,   549,    86,    87,   137,
     247,   630,   458,   459,   805,   161,   572,   572,   594,   423,
     581,   595,   221,   221,   847,   566,   830,   569,   596,    89,
     740,   831,   422,   741,   140,   774,   651,   253,   152,   477,
     742,   331,   478,   884,   141,   221,   885,   142,   357,   872,
     143,   366,   866,   886,   175,   153,   613,   510,   618,    29,
      30,    31,    32,   154,    34,   510,    35,   155,   703,   176,
     384,   177,   178,   306,   371,   179,   709,   507,   423,   423,
     512,   620,   162,   221,   621,   507,   883,   186,   182,   187,
     188,   422,   422,   189,   194,   470,   721,   722,   858,   197,
    -181,   859,   148,   656,   148,   422,   657,   326,   327,   683,
     450,   451,   452,   453,   868,   537,   207,   869,  -194,   452,
     453,   172,   208,  -194,  -194,   209,  -194,  -194,  -194,   204,
     208,   217,   744,   209,   675,   676,   780,   781,   581,   899,
     900,  -194,   618,   218,   219,   222,  -169,   757,   175,   229,
     618,  -174,   417,  -175,   232,  -194,  -172,   729,   767,   448,
     449,   450,   451,   452,   453,   779,  -176,  -173,   784,   613,
     697,   417,   210,   231,   233,   235,   243,   618,   255,   264,
     254,   423,   256,   283,   510,   265,   148,   806,   276,   166,
     287,   752,   286,   809,   422,   289,   290,   291,   423,  -200,
     826,   297,   296,   247,   507,   306,   320,   322,  -178,   470,
     307,   422,   447,   448,   449,   450,   451,   452,   453,   303,
     308,   303,  -170,   731,   731,   581,  -171,  -177,  -179,   644,
    -194,   646,  -180,  -181,   332,  -194,   333,   329,   334,   335,
     655,   337,   891,   338,   581,   613,    91,   613,   613,   613,
     339,   581,   846,   813,   352,   807,   353,   531,   533,   354,
     367,   355,   368,   905,   425,   382,   662,   372,   417,   442,
     618,   395,   464,   465,   778,   446,   447,   448,   449,   450,
     451,   452,   453,   384,   791,   455,   552,   426,   340,   679,
     556,   473,   377,   581,   775,   480,   331,   487,   485,   386,
     496,   488,   500,   498,   568,   309,   505,   692,   511,   417,
     310,   311,   697,   312,   313,   314,   517,   523,   524,   591,
     535,   528,   541,   384,   546,   542,   529,   824,   315,   555,
     221,   553,   867,   778,   567,   530,   570,   588,   574,   584,
     592,   618,   316,   618,   618,   345,   609,   593,   624,   598,
     619,   628,   632,   775,   634,   631,   727,   843,   639,   642,
     645,   648,   643,   470,   653,   654,   660,   663,   417,   417,
     665,   697,   666,   738,   668,   669,   674,   671,   684,   384,
     685,   708,   417,   423,   688,   699,   710,   693,   778,   695,
     618,   470,   712,   754,   618,   711,   422,   713,   715,   301,
     717,   719,   581,   720,   375,   309,   734,   739,   775,   768,
     310,   311,   762,   312,   313,   314,   554,   317,   664,   736,
     743,   745,   318,   748,   789,   470,   755,   761,   315,   756,
     772,   760,   766,   618,    73,   783,   785,   786,   828,   771,
     792,   148,   316,   793,   148,   801,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,   808,   817,   609,
     811,   815,   822,   820,   819,   827,   266,    85,    86,    87,
     832,   417,   836,   839,   841,   810,   840,   848,   833,   812,
     845,   849,   850,   853,   855,   267,   268,   121,   417,   862,
      89,   864,   873,   875,   877,   879,   880,   881,   887,   445,
     446,   447,   448,   449,   450,   451,   452,   453,   445,   446,
     447,   448,   449,   450,   451,   452,   453,   317,   894,   901,
     903,   358,   318,   305,   601,   359,   244,    -3,     6,   614,
    -428,     7,     8,     9,   633,   609,   457,   609,   609,   609,
     878,    10,  -428,  -428,  -428,  -428,  -428,  -428,  -428,  -428,
    -428,  -428,  -428,    90,   893,   800,    11,    12,    13,   516,
     573,    14,   732,  -428,  -428,  -428,   139,   462,    15,   486,
       0,    16,     0,    17,    18,    19,    20,    21,    22,    23,
      24,   489,   475,  -428,   483,     0,  -428,     0,     0,     0,
     148,    25,     0,     0,     0,     0,    26,    27,    28,    29,
      30,    31,    32,    33,    34,     0,    35,    36,    37,    38,
      39,    40,    41,    42,    43,    44,    45,    46,    47,    48,
      49,    50,    51,    52,    53,    54,     0,     0,    55,    56,
       0,     0,     0,     0,    57,    58,    59,     0,     0,  -428,
       0,     0,     0,     0,     0,  -428,     0,     0,     0,  -428,
       0,   445,   446,   447,   448,   449,   450,   451,   452,   453,
       0,     6,     0,  -428,     7,     8,     9,     0,     0,     0,
       0,     0,     0,   417,    10,  -428,  -428,  -428,  -428,  -428,
    -428,  -428,  -428,  -428,  -428,  -428,     0,     0,     0,    11,
      12,    13,     0,   424,    14,     0,  -428,  -428,  -428,   609,
       0,    15,     0,     0,    16,     0,    17,    18,    19,    20,
      21,    22,    23,    24,     0,     0,  -428,     0,     0,  -428,
       0,     0,     0,     0,    25,     0,     0,     0,     0,    26,
      27,    28,    29,    30,    31,    32,    33,    34,     0,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,    48,    49,    50,    51,    52,    53,    54,     0,
       0,    55,    56,     0,     0,     0,     0,    57,    58,    59,
       0,     6,  -428,  -428,     7,     8,     9,     0,  -428,     0,
       0,     0,  -428,     0,    10,  -428,  -428,  -428,  -428,  -428,
    -428,  -428,  -428,  -428,  -428,  -428,     0,     0,     0,    11,
      12,    13,     0,     0,    14,     0,  -428,  -428,  -428,     0,
       0,    15,     0,     0,    16,     0,    17,    18,    19,    20,
      21,    22,    23,    24,     0,     0,  -428,     0,     0,  -428,
       0,     0,     0,     0,    25,     0,     0,     0,     0,    26,
      27,    28,    29,    30,    31,    32,    33,    34,     0,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,    48,    49,    50,    51,    52,    53,    54,     0,
       0,    55,    56,     0,     0,     0,     0,    57,    58,    59,
       0,   396,  -428,   397,     0,     0,     0,     0,  -428,     0,
       0,     0,  -428,     0,   398,   109,   110,   111,   112,   113,
     114,   115,   116,   117,   118,   119,     0,     0,     0,   399,
       0,     0,     0,  -428,     0,     0,   120,    86,    87,     0,
       0,     0,     0,     0,     0,     0,   400,   401,   402,     0,
       0,     0,   403,   404,     0,     0,   405,     0,     0,    89,
     406,   407,   408,     0,   409,   410,   411,     0,     0,     0,
       0,     0,    29,    30,    31,    32,     0,    34,   604,    35,
      73,     0,     0,    39,    40,     0,     0,     0,     0,     0,
       0,   412,    74,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    84,     0,     0,     0,     0,     0,     0,     0,
    -428,     0,     0,    85,    86,    87,     0,     0,     0,     0,
     413,     0,    90,     0,     0,   605,     0,     0,     0,     0,
       0,     0,     0,   121,   397,     0,    89,     0,     0,     0,
       0,     0,     0,     0,     0,   398,   109,   110,   111,   112,
     113,   114,   115,   116,   117,   118,   119,     0,     0,     0,
     399,     0,     0,     0,     0,     0,     0,   120,    86,    87,
       0,     0,     0,     0,     0,     0,     0,   400,   401,   402,
       0,   606,   607,   608,   404,     0,     0,   405,     0,     0,
      89,   406,   407,   408,     0,   409,   410,   411,     0,    90,
       0,     0,     0,    29,    30,    31,    32,     0,    34,     0,
      35,     0,     0,     0,    39,    40,     0,     0,     0,     0,
       0,     0,   412,   397,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   398,   109,   110,   111,   112,   113,
     114,   115,   116,   117,   118,   119,   458,   459,     0,   399,
       0,   413,     0,    90,     0,     0,   120,    86,    87,     0,
       0,     0,     0,     0,     0,     0,   400,   401,   402,     0,
       0,     0,     0,   404,     0,     0,   405,     0,     0,    89,
     406,   407,   408,     0,   409,   410,   411,     0,     0,     0,
       0,     0,    29,    30,    31,    32,     0,    34,     0,    35,
      73,     0,     0,    39,    40,     0,     0,     0,     0,     0,
       0,   412,    74,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    84,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   266,    85,    86,    87,     0,     0,     0,     0,
     413,     0,    90,     0,     0,    73,     0,     0,     0,     0,
       0,   267,   268,   121,     0,     0,    89,    74,    75,    76,
      77,    78,    79,    80,    81,    82,    83,    84,     0,   163,
       0,     0,     0,     0,     0,     0,     0,   266,    85,    86,
      87,   109,   110,   111,   112,   113,   114,   115,   116,   117,
     118,   119,     0,     0,     0,     0,   267,   268,   121,     0,
       0,    89,   120,    86,    87,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   166,    73,   126,     0,    90,
       0,     0,   164,     0,     0,    89,     0,     0,    74,    75,
      76,    77,    78,    79,    80,    81,    82,    83,    84,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    85,
      86,    87,     0,     0,     0,     0,     0,     0,     0,     0,
     637,     0,     0,     0,    90,     0,     0,     0,     0,   121,
       0,     0,    89,     0,     0,     0,     0,    73,   165,     0,
       0,     0,     0,     0,   166,     0,     0,     0,    90,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
       0,     0,     0,    73,     0,     0,     0,     0,     0,     0,
      85,    86,    87,     0,     0,    74,    75,    76,    77,    78,
      79,    80,    81,    82,    83,    84,     0,     0,     0,     0,
     121,     0,     0,    89,     0,    90,    85,    86,    87,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   605,    73,
       0,     0,     0,     0,     0,     0,   121,     0,     0,    89,
       0,    74,    75,    76,    77,    78,    79,    80,    81,    82,
      83,    84,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    85,    86,    87,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   532,    73,    90,     0,     0,     0,
       0,     0,    88,     0,     0,    89,     0,   109,   110,   111,
     112,   113,   114,   115,   116,   117,   118,   119,     0,    73,
       0,     0,    90,     0,     0,     0,     0,     0,   120,    86,
      87,    74,    75,    76,    77,    78,    79,    80,    81,    82,
      83,    84,     0,   590,     0,     0,     0,     0,   121,     0,
       0,    89,    85,    86,    87,    74,    75,    76,    77,    78,
      79,    80,    81,    82,    83,    84,     0,     0,    90,     0,
       0,     0,   121,     0,   309,    89,    85,    86,    87,   310,
     311,   309,   312,   313,   314,     0,   310,   311,     0,   312,
     313,   314,     0,     0,     0,     0,   121,   315,   890,    89,
       0,     0,     0,     0,   315,     0,     0,   309,     0,     0,
       0,   316,   310,   311,    90,   312,   313,   314,   316,   427,
     428,   429,   430,   431,   432,   433,   434,   435,   436,   437,
     315,     0,     0,     0,     0,     0,     0,     0,    90,     0,
     438,    86,    87,     0,   316,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    90,    89,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   317,     0,     0,     0,
       0,   318,     0,   317,     0,     0,     0,     0,   318,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   317,
       0,     0,     0,     0,   318
};

#define yypact_value_is_default(yystate) \
  ((yystate) == (-789))

#define yytable_value_is_error(yytable_value) \
  YYID (0)

static const yytype_int16 yycheck[] =
{
       2,    48,     4,   355,   288,   137,   385,   290,    84,   117,
     467,   420,   110,   254,    25,   323,   213,   622,   507,   360,
     164,    10,     4,     4,    91,    35,    26,    26,     4,    26,
     245,    29,     3,   723,    26,   376,    25,     7,    29,   827,
      10,    32,    42,   119,   248,   249,   158,    32,     3,   297,
     247,     3,   461,    27,    65,     3,    36,   153,   154,   155,
       3,   345,    32,   500,    63,     3,     3,    98,     3,     4,
       7,    73,    63,    75,    76,    77,    65,   754,    63,     3,
      82,   148,    84,    26,    36,   161,    88,   148,    68,    60,
      61,    62,    94,    77,    65,   700,    98,   338,    36,   166,
      99,    99,    99,     3,   580,   107,     3,    99,   110,   111,
     112,   520,   521,   901,   362,   117,   364,   119,   315,    67,
     317,   318,   122,   133,   122,   122,     1,   111,   112,    26,
     122,   162,   737,   512,   349,   137,   813,   626,   386,   200,
     344,    65,   112,   239,   118,   147,   148,   584,    78,   151,
     152,   153,   154,   155,   759,   592,   592,   112,    33,   161,
     162,   163,   164,   118,   166,   147,   147,    99,     3,   230,
       0,   147,     3,    48,   286,   177,   178,    52,   775,   246,
       7,     8,   619,   619,   245,   187,   188,   248,   249,   119,
     122,   667,   882,   177,   178,    26,   537,     3,     7,   483,
     202,     3,   204,   187,   188,     3,   896,   274,    26,   256,
     686,    42,   112,     3,   623,   112,   328,   693,   118,    14,
      26,   118,   334,    58,    42,     4,   534,   288,   230,    91,
      32,   640,     3,   830,     3,    30,    42,   239,     3,    29,
     115,   116,    32,   245,    42,   493,   248,   249,   445,   446,
     447,   448,   449,   450,   451,   452,   453,    52,    27,   735,
     122,   405,   374,    26,   479,   127,    29,     1,   270,    32,
      26,   876,   274,    63,    69,   712,     3,    39,   280,     3,
       7,   112,     3,   344,   345,     3,   288,   118,   290,    60,
      61,    62,   368,   898,   361,   297,   298,     3,    10,   360,
      63,    63,   304,   305,   315,    32,   112,   169,    32,     3,
     651,    32,   118,    25,    48,   304,    28,    28,    52,   321,
      26,   323,    33,   305,   305,     3,   315,   435,   330,   305,
     428,   333,   464,   465,   323,     3,    48,    49,     1,    26,
     785,   786,   344,   345,     3,   611,   725,   349,    26,   351,
     417,    28,   593,    65,     3,   487,   553,    28,   360,    26,
     362,   437,   364,     3,    42,    42,   368,    26,   844,   103,
      33,    42,    39,    85,   376,    42,    21,    22,   380,     3,
     663,   115,   116,   385,   386,    48,   765,   832,    39,    52,
       3,    42,    28,   525,     7,   397,    63,    33,   380,   836,
      45,    26,    26,   405,    72,    73,    74,    75,   120,    77,
     522,    79,    63,    26,     3,   417,   825,    42,   420,    32,
     496,   687,   483,   689,   690,   691,   428,   429,   430,   886,
       3,   420,   321,   435,    26,   437,     4,    26,   875,     7,
     103,     4,   821,     3,   333,   429,   430,    37,    38,     3,
      42,   512,   115,   116,   738,     3,   458,   459,    29,   461,
     462,    32,   464,   465,   805,   454,    28,   456,    39,    59,
      29,    33,   461,    32,    26,    48,   537,   479,     7,    29,
      39,   483,    32,    29,    26,   487,    32,    29,   490,   841,
      32,   493,   833,    39,   496,     7,   498,   499,   500,    72,
      73,    74,    75,     7,    77,   507,    79,     7,   620,    15,
     512,    17,    18,    28,    29,    21,   628,   499,   520,   521,
     382,    26,     3,   525,    29,   507,   867,    15,    15,    17,
      18,   520,   521,    21,     3,   537,   648,   649,    29,     3,
      26,    32,   254,    29,   256,   534,    32,    27,    28,   596,
     115,   116,   117,   118,    29,   417,     1,    32,     3,   117,
     118,    99,     7,     8,     9,    10,    11,    12,    13,    32,
       7,     3,   684,    10,    28,    29,    28,    29,   580,    27,
      28,    26,   584,    32,    39,     3,    26,   699,   590,     3,
     592,    26,   304,    26,     3,    40,    26,   664,   710,   113,
     114,   115,   116,   117,   118,   717,    26,    26,   720,   611,
     612,   323,    57,    26,     3,     3,     3,   619,    29,    29,
      32,   623,    28,     3,   626,    29,   338,   739,    33,   118,
       3,   692,    26,   745,   623,    26,     3,     3,   640,    32,
     772,   118,    32,    42,   626,    28,    27,    29,    26,   651,
      57,   640,   112,   113,   114,   115,   116,   117,   118,   661,
      57,   663,    26,   665,   666,   667,    26,    26,    26,   531,
     115,   533,    26,    26,   118,   120,    27,   738,    26,     3,
     542,    28,   879,    27,   686,   687,   398,   689,   690,   691,
      27,   693,   804,   754,    28,   742,    35,   409,   410,    27,
       3,    28,     3,   900,     3,    28,   568,    32,   420,    26,
     712,    32,     3,     3,   716,   111,   112,   113,   114,   115,
     116,   117,   118,   725,   726,    30,   438,   122,    26,   591,
     442,    27,   118,   735,   716,    27,   738,     3,    33,   118,
      27,    35,    27,    32,   456,     3,    32,   609,    27,   461,
       8,     9,   754,    11,    12,    13,    28,    26,    32,   471,
       3,    63,    26,   765,     3,    33,    63,   769,    26,     3,
     772,    27,   833,   775,     7,    63,    26,     8,    33,    27,
      27,   783,    40,   785,   786,    43,   498,    27,    39,    27,
      27,    26,     3,   775,     3,    27,   658,   799,     3,     3,
       3,    26,    32,   805,    67,   118,    27,     3,   520,   521,
       3,   813,     3,   675,    26,    32,     3,    27,    26,   821,
      27,     3,   534,   825,    26,    26,    26,    33,   830,    28,
     832,   833,    27,   695,   836,    33,   825,    27,    27,    63,
      26,    26,   844,    26,   122,     3,     3,    26,   830,   711,
       8,     9,    10,    11,    12,    13,    27,   115,   570,    32,
      29,    26,   120,     3,   726,   867,    29,    33,    26,    29,
       3,    27,    27,   875,     3,    27,    27,    27,    26,    33,
      29,   593,    40,    27,   596,    27,    15,    16,    17,    18,
      19,    20,    21,    22,    23,    24,    25,    27,    29,   611,
      27,    27,    63,    27,    29,    39,    35,    36,    37,    38,
      27,   623,    27,    29,    26,   103,    63,    27,   780,   103,
      33,    29,    27,    29,     3,    54,    55,    56,   640,     3,
      59,    29,     3,    27,    29,    26,    28,    27,    27,   110,
     111,   112,   113,   114,   115,   116,   117,   118,   110,   111,
     112,   113,   114,   115,   116,   117,   118,   115,     3,    39,
      29,   273,   120,   204,   490,   273,   147,     0,     1,   499,
       3,     4,     5,     6,   517,   687,   321,   689,   690,   691,
     851,    14,    15,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,   122,   880,   732,    29,    30,    31,   391,
     459,    34,   666,    36,    37,    38,    42,   323,    41,   351,
      -1,    44,    -1,    46,    47,    48,    49,    50,    51,    52,
      53,   354,   337,    56,    43,    -1,    59,    -1,    -1,    -1,
     742,    64,    -1,    -1,    -1,    -1,    69,    70,    71,    72,
      73,    74,    75,    76,    77,    -1,    79,    80,    81,    82,
      83,    84,    85,    86,    87,    88,    89,    90,    91,    92,
      93,    94,    95,    96,    97,    98,    -1,    -1,   101,   102,
      -1,    -1,    -1,    -1,   107,   108,   109,    -1,    -1,   112,
      -1,    -1,    -1,    -1,    -1,   118,    -1,    -1,    -1,   122,
      -1,   110,   111,   112,   113,   114,   115,   116,   117,   118,
      -1,     1,    -1,     3,     4,     5,     6,    -1,    -1,    -1,
      -1,    -1,    -1,   825,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    -1,    -1,    -1,    29,
      30,    31,    -1,    33,    34,    -1,    36,    37,    38,   851,
      -1,    41,    -1,    -1,    44,    -1,    46,    47,    48,    49,
      50,    51,    52,    53,    -1,    -1,    56,    -1,    -1,    59,
      -1,    -1,    -1,    -1,    64,    -1,    -1,    -1,    -1,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    -1,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    88,    89,
      90,    91,    92,    93,    94,    95,    96,    97,    98,    -1,
      -1,   101,   102,    -1,    -1,    -1,    -1,   107,   108,   109,
      -1,     1,   112,     3,     4,     5,     6,    -1,   118,    -1,
      -1,    -1,   122,    -1,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    -1,    -1,    -1,    29,
      30,    31,    -1,    -1,    34,    -1,    36,    37,    38,    -1,
      -1,    41,    -1,    -1,    44,    -1,    46,    47,    48,    49,
      50,    51,    52,    53,    -1,    -1,    56,    -1,    -1,    59,
      -1,    -1,    -1,    -1,    64,    -1,    -1,    -1,    -1,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    -1,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    88,    89,
      90,    91,    92,    93,    94,    95,    96,    97,    98,    -1,
      -1,   101,   102,    -1,    -1,    -1,    -1,   107,   108,   109,
      -1,     1,   112,     3,    -1,    -1,    -1,    -1,   118,    -1,
      -1,    -1,   122,    -1,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    -1,    -1,    -1,    29,
      -1,    -1,    -1,    33,    -1,    -1,    36,    37,    38,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    46,    47,    48,    -1,
      -1,    -1,    52,    53,    -1,    -1,    56,    -1,    -1,    59,
      60,    61,    62,    -1,    64,    65,    66,    -1,    -1,    -1,
      -1,    -1,    72,    73,    74,    75,    -1,    77,     1,    79,
       3,    -1,    -1,    83,    84,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    15,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      33,    -1,    -1,    36,    37,    38,    -1,    -1,    -1,    -1,
     120,    -1,   122,    -1,    -1,    48,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    56,     3,    -1,    59,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    14,    15,    16,    17,    18,
      19,    20,    21,    22,    23,    24,    25,    -1,    -1,    -1,
      29,    -1,    -1,    -1,    -1,    -1,    -1,    36,    37,    38,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    46,    47,    48,
      -1,   104,   105,   106,    53,    -1,    -1,    56,    -1,    -1,
      59,    60,    61,    62,    -1,    64,    65,    66,    -1,   122,
      -1,    -1,    -1,    72,    73,    74,    75,    -1,    77,    -1,
      79,    -1,    -1,    -1,    83,    84,    -1,    -1,    -1,    -1,
      -1,    -1,    91,     3,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,   115,   116,    -1,    29,
      -1,   120,    -1,   122,    -1,    -1,    36,    37,    38,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    46,    47,    48,    -1,
      -1,    -1,    -1,    53,    -1,    -1,    56,    -1,    -1,    59,
      60,    61,    62,    -1,    64,    65,    66,    -1,    -1,    -1,
      -1,    -1,    72,    73,    74,    75,    -1,    77,    -1,    79,
       3,    -1,    -1,    83,    84,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    15,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    35,    36,    37,    38,    -1,    -1,    -1,    -1,
     120,    -1,   122,    -1,    -1,     3,    -1,    -1,    -1,    -1,
      -1,    54,    55,    56,    -1,    -1,    59,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    -1,     3,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,    36,    37,
      38,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    -1,    -1,    -1,    -1,    54,    55,    56,    -1,
      -1,    59,    36,    37,    38,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   118,     3,     4,    -1,   122,
      -1,    -1,    56,    -1,    -1,    59,    -1,    -1,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    36,
      37,    38,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     118,    -1,    -1,    -1,   122,    -1,    -1,    -1,    -1,    56,
      -1,    -1,    59,    -1,    -1,    -1,    -1,     3,   112,    -1,
      -1,    -1,    -1,    -1,   118,    -1,    -1,    -1,   122,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      -1,    -1,    -1,     3,    -1,    -1,    -1,    -1,    -1,    -1,
      36,    37,    38,    -1,    -1,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    -1,    -1,    -1,    -1,
      56,    -1,    -1,    59,    -1,   122,    36,    37,    38,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    48,     3,
      -1,    -1,    -1,    -1,    -1,    -1,    56,    -1,    -1,    59,
      -1,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    36,    37,    38,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   120,     3,   122,    -1,    -1,    -1,
      -1,    -1,    56,    -1,    -1,    59,    -1,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    -1,     3,
      -1,    -1,   122,    -1,    -1,    -1,    -1,    -1,    36,    37,
      38,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    -1,     3,    -1,    -1,    -1,    -1,    56,    -1,
      -1,    59,    36,    37,    38,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    -1,    -1,   122,    -1,
      -1,    -1,    56,    -1,     3,    59,    36,    37,    38,     8,
       9,     3,    11,    12,    13,    -1,     8,     9,    -1,    11,
      12,    13,    -1,    -1,    -1,    -1,    56,    26,    27,    59,
      -1,    -1,    -1,    -1,    26,    -1,    -1,     3,    -1,    -1,
      -1,    40,     8,     9,   122,    11,    12,    13,    40,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   122,    -1,
      36,    37,    38,    -1,    40,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   122,    59,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   115,    -1,    -1,    -1,
      -1,   120,    -1,   115,    -1,    -1,    -1,    -1,   120,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   115,
      -1,    -1,    -1,    -1,   120
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint16 yystos[] =
{
       0,   124,   125,     0,   126,   258,     1,     4,     5,     6,
      14,    29,    30,    31,    34,    41,    44,    46,    47,    48,
      49,    50,    51,    52,    53,    64,    69,    70,    71,    72,
      73,    74,    75,    76,    77,    79,    80,    81,    82,    83,
      84,    85,    86,    87,    88,    89,    90,    91,    92,    93,
      94,    95,    96,    97,    98,   101,   102,   107,   108,   109,
     127,   138,   139,   143,   145,   150,   178,   179,   185,   220,
     256,   258,     4,     3,    15,    16,    17,    18,    19,    20,
      21,    22,    23,    24,    25,    36,    37,    38,    56,    59,
     122,   164,   213,     7,     3,     4,     3,    58,     3,     3,
       7,   255,    26,     3,   255,   255,     3,     3,    26,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      36,    56,   164,   165,   213,    26,     4,   164,   213,     3,
       3,     3,    78,   119,   144,   144,     4,     3,   244,   244,
      26,    26,    29,    32,   255,     4,     7,   133,   164,   250,
     248,   250,     7,     7,     7,     7,     3,     7,    26,    32,
     257,     3,     3,     3,    56,   112,   118,   160,   161,   164,
     165,   213,    99,   122,   224,   258,    15,    17,    18,    21,
     167,   258,    15,   168,   258,   168,    15,    17,    18,    21,
     166,   258,   224,   164,     3,   172,   258,     3,     3,    26,
     160,   161,     3,    32,    32,   171,   258,     1,     7,    10,
      57,   149,   169,   170,   171,     3,    27,     3,    32,    39,
     246,   258,     3,   167,   168,   168,   166,   224,   164,     3,
     160,    26,     3,     3,   160,     3,     3,    26,   144,   246,
       3,    36,   247,     3,   127,     3,    26,    42,   112,   161,
     162,   251,   254,   258,    32,    29,    28,   249,   258,   245,
     258,   245,   245,   245,    29,    29,    35,    54,    55,   152,
     154,   155,   158,   159,   164,   258,    33,    26,    63,   223,
     224,   171,   172,     3,   161,   258,    26,     3,   160,    26,
       3,     3,   168,   168,   168,   168,    32,   118,   140,   162,
      26,    63,   209,   258,   183,   126,    28,    57,    57,     3,
       8,     9,    11,    12,    13,    26,    40,   115,   120,   177,
      27,   134,    29,   186,     7,     8,    27,    28,    26,   162,
     163,   258,   118,    27,    26,     3,   245,    28,    27,    27,
      26,   162,   254,   152,   161,    43,   177,   251,   251,   253,
     248,   250,    28,    35,    27,    28,   153,   258,   155,   158,
       3,    26,   112,   156,   161,   162,   258,     3,     3,   221,
     258,    29,    32,   152,    26,   122,   163,   118,    29,   209,
     136,   156,    28,   142,   258,   141,   118,     3,    60,    61,
      62,    65,   210,   211,   212,    32,     1,     3,    14,    29,
      46,    47,    48,    52,    53,    56,    60,    61,    62,    64,
      65,    66,    91,   120,   138,   139,   143,   164,   165,   188,
     192,   197,   213,   258,    33,     3,   122,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    36,   165,
     177,   213,    26,   177,   177,   110,   111,   112,   113,   114,
     115,   116,   117,   118,    14,    30,   150,   178,   115,   116,
     187,   192,   238,   258,     3,     3,   152,    39,    63,   157,
     258,   150,   152,    27,     3,   247,   248,    29,    32,   252,
      27,   251,   163,    43,   254,    33,   249,     3,    35,   257,
     154,   157,   162,   161,   156,   156,    27,   224,    32,   135,
      27,   152,     3,    67,   157,    32,     3,   143,   173,   174,
     258,    27,   160,   142,   156,     3,   212,    28,     3,    65,
     181,   191,    26,    26,    32,     3,    26,   172,    63,    63,
      63,   164,   120,   164,   195,     3,   112,   160,   161,   201,
     258,    26,    33,   188,     3,    32,     3,   167,   168,   168,
     166,   224,   164,    27,    27,     3,   164,   177,   177,   177,
     177,   177,   177,   177,   177,   177,   213,     7,   164,   213,
      26,   240,   258,   240,    33,   188,     1,    48,    52,   234,
     238,   258,   246,   246,    27,    32,   112,   169,     8,   129,
       3,   164,    27,    27,    29,    32,    39,   254,    27,   163,
     246,   153,   156,   224,     1,    48,   104,   105,   106,   164,
     225,   230,   231,   258,   173,    36,    68,   214,   258,    27,
      26,    29,   128,   180,    39,   174,    28,    33,    26,   142,
     162,    27,     3,   211,     3,   188,   188,   118,   152,     3,
     189,   246,     3,    32,   160,     3,   160,   192,    26,    26,
     157,   162,    26,    67,   118,   160,    29,    32,   199,   177,
      27,     3,   160,     3,   164,     3,     3,   237,    26,    32,
     234,    27,   151,   214,     3,    28,    29,   146,    29,   160,
     151,   214,   248,   250,    26,    27,   222,   229,    26,   226,
     227,   228,   160,    33,   225,    28,   233,   258,    33,    26,
     131,   151,   214,   152,   146,   188,   175,   174,     3,   152,
      26,    33,    27,    27,   188,    27,   196,    26,   194,    26,
      26,   152,   152,   193,   157,   184,   198,   160,    27,   161,
     242,   258,   242,   234,     3,   235,    32,   132,   160,    26,
      29,    32,    39,    29,   152,    26,   234,   225,     3,   225,
     225,   225,   162,   234,   160,    29,    29,   152,   146,   130,
      27,    33,    10,   176,   177,   137,    27,   152,   160,   214,
     215,    33,     3,     3,    48,   143,   207,   208,   258,   152,
      28,    29,   202,    27,   152,    27,    27,   202,   142,   160,
     200,   258,    29,    27,     3,    29,    32,    63,   239,   243,
     239,    27,   234,   146,    26,   163,   152,   250,    27,   152,
     103,    27,   103,   162,   233,    27,   146,    29,   142,    29,
      27,   182,    63,   216,   258,   190,   246,    39,    26,   208,
      28,    33,    27,   160,   205,   214,    27,   205,   205,    29,
      63,    26,   241,   258,   236,    33,   152,   157,    27,    29,
      27,   232,   233,    29,   142,     3,   217,   218,    29,    32,
     188,   176,     3,   208,    29,   205,   157,   162,    29,    32,
     206,   214,   154,     3,   234,    27,   147,    29,   231,    26,
      28,    27,   203,   157,    29,    32,    39,    27,   214,   146,
      27,   177,   219,   218,     3,   202,   204,   169,   148,    27,
      28,    39,   202,    29,   146,   177,   176
};

#define yyerrok		(yyerrstatus = 0)
#define yyclearin	(yychar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yyacceptlab
#define YYABORT		goto yyabortlab
#define YYERROR		goto yyerrorlab


/* Like YYERROR except do call yyerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  However,
   YYFAIL appears to be in use.  Nevertheless, it is formally deprecated
   in Bison 2.4.2's NEWS entry, where a plan to phase it out is
   discussed.  */

#define YYFAIL		goto yyerrlab
#if defined YYFAIL
  /* This is here to suppress warnings from the GCC cpp's
     -Wunused-macros.  Normally we don't worry about that warning, but
     some users do, and we want to make it easy for users to remove
     YYFAIL uses, which will produce warnings from Bison 2.5.  */
#endif

#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)					\
do								\
  if (yychar == YYEMPTY && yylen == 1)				\
    {								\
      yychar = (Token);						\
      yylval = (Value);						\
      YYPOPSTACK (1);						\
      goto yybackup;						\
    }								\
  else								\
    {								\
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))


#define YYTERROR	1
#define YYERRCODE	256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#define YYRHSLOC(Rhs, K) ((Rhs)[K])
#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)				\
    do									\
      if (YYID (N))                                                    \
	{								\
	  (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;	\
	  (Current).first_column = YYRHSLOC (Rhs, 1).first_column;	\
	  (Current).last_line    = YYRHSLOC (Rhs, N).last_line;		\
	  (Current).last_column  = YYRHSLOC (Rhs, N).last_column;	\
	}								\
      else								\
	{								\
	  (Current).first_line   = (Current).last_line   =		\
	    YYRHSLOC (Rhs, 0).last_line;				\
	  (Current).first_column = (Current).last_column =		\
	    YYRHSLOC (Rhs, 0).last_column;				\
	}								\
    while (YYID (0))
#endif


/* This macro is provided for backward compatibility. */

#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


/* YYLEX -- calling `yylex' with the right arguments.  */

#ifdef YYLEX_PARAM
# define YYLEX yylex (YYLEX_PARAM)
#else
# define YYLEX yylex ()
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yydebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yydebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_symbol_print (stderr,						  \
		  Type, Value); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_value_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# else
  YYUSE (yyoutput);
# endif
  switch (yytype)
    {
      default:
	break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (yytype < YYNTOKENS)
    YYFPRINTF (yyoutput, "token %s (", yytname[yytype]);
  else
    YYFPRINTF (yyoutput, "nterm %s (", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
#else
static void
yy_stack_print (yybottom, yytop)
    yytype_int16 *yybottom;
    yytype_int16 *yytop;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yydebug)							\
    yy_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_reduce_print (YYSTYPE *yyvsp, int yyrule)
#else
static void
yy_reduce_print (yyvsp, yyrule)
    YYSTYPE *yyvsp;
    int yyrule;
#endif
{
  int yynrhs = yyr2[yyrule];
  int yyi;
  unsigned long int yylno = yyrline[yyrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr, yyrhs[yyprhs[yyrule] + yyi],
		       &(yyvsp[(yyi + 1) - (yynrhs)])
		       		       );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yydebug)				\
    yy_reduce_print (yyvsp, Rule); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yystrlen (const char *yystr)
#else
static YYSIZE_T
yystrlen (yystr)
    const char *yystr;
#endif
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yystpcpy (char *yydest, const char *yysrc)
#else
static char *
yystpcpy (yydest, yysrc)
    char *yydest;
    const char *yysrc;
#endif
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
	switch (*++yyp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yyp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yyres)
	      yyres[yyn] = *yyp;
	    yyn++;
	    break;

	  case '"':
	    if (yyres)
	      yyres[yyn] = '\0';
	    return yyn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (0, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  YYSIZE_T yysize1;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = 0;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - Assume YYFAIL is not used.  It's too flawed to consider.  See
       <http://lists.gnu.org/archive/html/bison-patches/2009-12/msg00024.html>
       for details.  YYERROR is fine as it does not invoke this
       function.
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                yysize1 = yysize + yytnamerr (0, yytname[yyx]);
                if (! (yysize <= yysize1
                       && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                  return 2;
                yysize = yysize1;
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  yysize1 = yysize + yystrlen (yyformat);
  if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
    return 2;
  yysize = yysize1;

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
#else
static void
yydestruct (yymsg, yytype, yyvaluep)
    const char *yymsg;
    int yytype;
    YYSTYPE *yyvaluep;
#endif
{
  YYUSE (yyvaluep);

  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  switch (yytype)
    {

      default:
	break;
    }
}


/* Prevent warnings from -Wmissing-prototypes.  */
#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (void);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */


/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;

/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void *YYPARSE_PARAM)
#else
int
yyparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void)
#else
int
yyparse ()

#endif
#endif
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       `yyss': related to states.
       `yyvs': related to semantic values.

       Refer to the stacks thru separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yytoken = 0;
  yyss = yyssa;
  yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */

  /* Initialize stack pointers.
     Waste one element of value and location stack
     so that they stay on the same level as the state stack.
     The wasted elements are never initialized.  */
  yyssp = yyss;
  yyvsp = yyvs;

  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YYSTYPE *yyvs1 = yyvs;
	yytype_int16 *yyss1 = yyss;

	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yyoverflow is a macro.  */
	yyoverflow (YY_("memory exhausted"),
		    &yyss1, yysize * sizeof (*yyssp),
		    &yyvs1, yysize * sizeof (*yyvsp),
		    &yystacksize);

	yyss = yyss1;
	yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
	goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
	yystacksize = YYMAXDEPTH;

      {
	yytype_int16 *yyss1 = yyss;
	union yyalloc *yyptr =
	  (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
	if (! yyptr)
	  goto yyexhaustedlab;
	YYSTACK_RELOCATE (yyss_alloc, yyss);
	YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
	if (yyss1 != yyssa)
	  YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = YYLEX;
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  *++yyvsp = yylval;

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:

/* Line 1806 of yacc.c  */
#line 559 "parser.y"
    { 
                    {
		      int ii;
		      for (ii = 0; ii < 256; ii++) {
			handler_stack[ii] = 0;
		      }
		      handler_stack[0] = comment_handler;
		    }
                    doc_stack[0] = doctitle;
                 }
    break;

  case 3:

/* Line 1806 of yacc.c  */
#line 568 "parser.y"
    {
		   CommentHandler::cleanup();
                   cplus_cleanup();
		   doc_entry = doctitle;
		   if (lang_init) {
		     lang->close();
		   }
		   if (te_index) {
		     fprintf(stderr,"%s : EOF.  Missing #endif detected.\n", input_file);
		     FatalError();
		   }
               }
    break;

  case 4:

/* Line 1806 of yacc.c  */
#line 582 "parser.y"
    { 
		     scanner_clear_start();
                     Error = 0;
                }
    break;

  case 5:

/* Line 1806 of yacc.c  */
#line 586 "parser.y"
    {
	       }
    break;

  case 6:

/* Line 1806 of yacc.c  */
#line 590 "parser.y"
    {
                  if (allow) {
//		    init_language();
		    doc_entry = 0;
		    // comment_handler->clear();
		    include_file((yyvsp[(2) - (2)].id));
		  }
                }
    break;

  case 7:

/* Line 1806 of yacc.c  */
#line 601 "parser.y"
    {
		 if (allow) {
		   int oldextern = WrapExtern;
//		   init_language();
		   doc_entry = 0;
		   // comment_handler->clear();
		   WrapExtern = 1;
		   if (include_file((yyvsp[(2) - (2)].id)) >= 0) {
		     add_symbol("SWIGEXTERN",0,0);
		   } else {
		     WrapExtern = oldextern;
		   }
		 }
	       }
    break;

  case 8:

/* Line 1806 of yacc.c  */
#line 618 "parser.y"
    {
		  if (allow) {
		    int oldextern = WrapExtern;
		    init_language();
		    doc_entry = 0;
		    WrapExtern = 1;
		    if (include_file((yyvsp[(2) - (2)].id)) >= 0) {
		      add_symbol("SWIGEXTERN",0,0);
		      lang->import((yyvsp[(2) - (2)].id));
		    } else {
		      WrapExtern = oldextern;
		    }
		  }
                }
    break;

  case 9:

/* Line 1806 of yacc.c  */
#line 636 "parser.y"
    {
                  if (allow) {
                     if ((checkout_file((yyvsp[(2) - (2)].id),(yyvsp[(2) - (2)].id))) == 0) {
                       fprintf(stderr,"%s checked out from the SWIG library.\n",(yyvsp[(2) - (2)].id));
                      }
                  }
                }
    break;

  case 10:

/* Line 1806 of yacc.c  */
#line 646 "parser.y"
    {
		 if (allow) {
                  doc_entry = 0;
		  if (Verbose) {
		    fprintf(stderr,"%s : Line %d.  CPP %s ignored.\n", input_file, line_number,(yyvsp[(1) - (1)].id));
		  }
		 }
		}
    break;

  case 11:

/* Line 1806 of yacc.c  */
#line 657 "parser.y"
    {
		  if (allow) {
		    init_language();
		    if (Active_type) delete Active_type;
		    Active_type = new DataType((yyvsp[(2) - (5)].type));
		    Active_extern = (yyvsp[(1) - (5)].ivalue);
		    (yyvsp[(2) - (5)].type)->is_pointer += (yyvsp[(3) - (5)].decl).is_pointer;
		    if ((yyvsp[(4) - (5)].ivalue) > 0) {
		      (yyvsp[(2) - (5)].type)->is_pointer++;
		      (yyvsp[(2) - (5)].type)->status = STAT_READONLY;
                      (yyvsp[(2) - (5)].type)->arraystr = copy_string(ArrayString);
		    }
		    if ((yyvsp[(3) - (5)].decl).is_reference) {
		      fprintf(stderr,"%s : Line %d. Error. Linkage to C++ reference not allowed.\n", input_file, line_number);
		      FatalError();
		    } else {
		      if ((yyvsp[(2) - (5)].type)->qualifier) {
			if ((strcmp((yyvsp[(2) - (5)].type)->qualifier,"const") == 0)) {
			  if ((yyvsp[(5) - (5)].dtype).type != T_ERROR)
			    create_constant((yyvsp[(3) - (5)].decl).id, (yyvsp[(2) - (5)].type), (yyvsp[(5) - (5)].dtype).id);
			} else 
			  create_variable((yyvsp[(1) - (5)].ivalue),(yyvsp[(3) - (5)].decl).id,(yyvsp[(2) - (5)].type));
		      } else
			create_variable((yyvsp[(1) - (5)].ivalue),(yyvsp[(3) - (5)].decl).id,(yyvsp[(2) - (5)].type));
		    }
		  }
		  delete (yyvsp[(2) - (5)].type);
                }
    break;

  case 12:

/* Line 1806 of yacc.c  */
#line 684 "parser.y"
    { }
    break;

  case 13:

/* Line 1806 of yacc.c  */
#line 688 "parser.y"
    { 
                   skip_decl();
		   fprintf(stderr,"%s : Line %d. Function pointers not currently supported.\n",
			   input_file, line_number);
		}
    break;

  case 14:

/* Line 1806 of yacc.c  */
#line 696 "parser.y"
    {
		  if (Verbose) {
		    fprintf(stderr,"static variable %s ignored.\n",(yyvsp[(3) - (5)].decl).id);
		  }
		  Active_static = 1;
		  delete (yyvsp[(2) - (5)].type);
		}
    break;

  case 15:

/* Line 1806 of yacc.c  */
#line 702 "parser.y"
    {
		  Active_static = 0;
		}
    break;

  case 16:

/* Line 1806 of yacc.c  */
#line 708 "parser.y"
    { 
                   skip_decl();
		   fprintf(stderr,"%s : Line %d. Function pointers not currently supported.\n",
			   input_file, line_number);
		}
    break;

  case 17:

/* Line 1806 of yacc.c  */
#line 717 "parser.y"
    {
		  if (allow) {
		    init_language();
		    if (Active_type) delete Active_type;
		    Active_type = new DataType((yyvsp[(2) - (7)].type));
		    Active_extern = (yyvsp[(1) - (7)].ivalue);
		    (yyvsp[(2) - (7)].type)->is_pointer += (yyvsp[(3) - (7)].decl).is_pointer;
		    (yyvsp[(2) - (7)].type)->is_reference = (yyvsp[(3) - (7)].decl).is_reference;
		    create_function((yyvsp[(1) - (7)].ivalue), (yyvsp[(3) - (7)].decl).id, (yyvsp[(2) - (7)].type), (yyvsp[(5) - (7)].pl));
		  }
		  delete (yyvsp[(2) - (7)].type);
		  delete (yyvsp[(5) - (7)].pl);
		}
    break;

  case 18:

/* Line 1806 of yacc.c  */
#line 729 "parser.y"
    { }
    break;

  case 19:

/* Line 1806 of yacc.c  */
#line 733 "parser.y"
    {
		  if (allow) {
		    init_language();
		    (yyvsp[(2) - (7)].type)->is_pointer += (yyvsp[(3) - (7)].decl).is_pointer;
		    (yyvsp[(2) - (7)].type)->is_reference = (yyvsp[(3) - (7)].decl).is_reference;
		    create_function((yyvsp[(1) - (7)].ivalue), (yyvsp[(3) - (7)].decl).id, (yyvsp[(2) - (7)].type), (yyvsp[(5) - (7)].pl));
		  }
		  delete (yyvsp[(2) - (7)].type);
		  delete (yyvsp[(5) - (7)].pl);
		}
    break;

  case 20:

/* Line 1806 of yacc.c  */
#line 746 "parser.y"
    { 
		  if (allow) {
                    init_language();
		    DataType *t = new DataType(T_INT);
                    t->is_pointer += (yyvsp[(2) - (6)].decl).is_pointer;
		    t->is_reference = (yyvsp[(2) - (6)].decl).is_reference;
		    create_function((yyvsp[(1) - (6)].ivalue),(yyvsp[(2) - (6)].decl).id,t,(yyvsp[(4) - (6)].pl));
		    delete t;
		  }
                }
    break;

  case 21:

/* Line 1806 of yacc.c  */
#line 755 "parser.y"
    { }
    break;

  case 22:

/* Line 1806 of yacc.c  */
#line 759 "parser.y"
    {
		  if ((allow) && (Inline)) {
		    if (strlen(CCode.get())) {
		      init_language();
		      (yyvsp[(2) - (7)].type)->is_pointer += (yyvsp[(3) - (7)].decl).is_pointer;
		      (yyvsp[(2) - (7)].type)->is_reference = (yyvsp[(3) - (7)].decl).is_reference;
		      create_function(0, (yyvsp[(3) - (7)].decl).id, (yyvsp[(2) - (7)].type), (yyvsp[(5) - (7)].pl));
		    }
		  }
		  delete (yyvsp[(2) - (7)].type);
		  delete (yyvsp[(5) - (7)].pl);
		}
    break;

  case 23:

/* Line 1806 of yacc.c  */
#line 774 "parser.y"
    {
		  if (allow) {
		    init_language();
		    (yyvsp[(2) - (7)].type)->is_pointer += (yyvsp[(3) - (7)].decl).is_pointer;
		    (yyvsp[(2) - (7)].type)->is_reference = (yyvsp[(3) - (7)].decl).is_reference;
		    if (Inline) {
		      fprintf(stderr,"%s : Line %d. Repeated %%inline directive.\n",input_file,line_number);
		      FatalError();
		    } else {
		      if (strlen(CCode.get())) {
			fprintf(f_header,"static ");
			emit_extern_func((yyvsp[(3) - (7)].decl).id,(yyvsp[(2) - (7)].type),(yyvsp[(5) - (7)].pl),3,f_header);
			fprintf(f_header,"%s\n",CCode.get());
		      }
		      create_function(0, (yyvsp[(3) - (7)].decl).id, (yyvsp[(2) - (7)].type), (yyvsp[(5) - (7)].pl));
		    }
		  }
		  delete (yyvsp[(2) - (7)].type);
		  delete (yyvsp[(5) - (7)].pl);
		}
    break;

  case 24:

/* Line 1806 of yacc.c  */
#line 797 "parser.y"
    {
		  if (allow) {
		    if (Verbose) {
		      fprintf(stderr,"static function %s ignored.\n", (yyvsp[(3) - (7)].decl).id);
		    }
		  }
		  Active_static = 1;
		  delete (yyvsp[(2) - (7)].type);
		  delete (yyvsp[(5) - (7)].pl);
		}
    break;

  case 25:

/* Line 1806 of yacc.c  */
#line 806 "parser.y"
    {
		  Active_static = 0;
		 }
    break;

  case 26:

/* Line 1806 of yacc.c  */
#line 812 "parser.y"
    {
		  if (allow)
		    Status = Status | STAT_READONLY;
	       }
    break;

  case 27:

/* Line 1806 of yacc.c  */
#line 819 "parser.y"
    {
		 if (allow)
		   Status = Status & ~STAT_READONLY;
	       }
    break;

  case 28:

/* Line 1806 of yacc.c  */
#line 825 "parser.y"
    {
		 if (allow) {
                     strcpy(yy_rename,(yyvsp[(3) - (4)].id));
                     Rename_true = 1;
		 }
               }
    break;

  case 29:

/* Line 1806 of yacc.c  */
#line 833 "parser.y"
    { 
		 if (name_hash.lookup((yyvsp[(2) - (4)].id))) {
		   name_hash.remove((yyvsp[(2) - (4)].id));
		 }
		 name_hash.add((yyvsp[(2) - (4)].id),copy_string((yyvsp[(3) - (4)].id)));
	       }
    break;

  case 30:

/* Line 1806 of yacc.c  */
#line 842 "parser.y"
    {
                     NewObject = 1;
                }
    break;

  case 31:

/* Line 1806 of yacc.c  */
#line 844 "parser.y"
    {
                     NewObject = 0;
               }
    break;

  case 32:

/* Line 1806 of yacc.c  */
#line 850 "parser.y"
    {
		 if (allow) {
		   fprintf(stderr,"%s : Lind %d. Empty %%name() is no longer supported.\n",
			   input_file, line_number);
		   FatalError();
		 }
	       }
    break;

  case 33:

/* Line 1806 of yacc.c  */
#line 856 "parser.y"
    {
		 Rename_true = 0;
	       }
    break;

  case 34:

/* Line 1806 of yacc.c  */
#line 862 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   init_language();
		   if (add_symbol((yyvsp[(3) - (7)].id),(DataType *) 0, (char *) 0)) {
		     fprintf(stderr,"%s : Line %d. Name of native function %s conflicts with previous declaration (ignored)\n",
			     input_file, line_number, (yyvsp[(3) - (7)].id));
		   } else {
		     doc_entry = new DocDecl((yyvsp[(3) - (7)].id),doc_stack[doc_stack_top]);
		     lang->add_native((yyvsp[(3) - (7)].id),(yyvsp[(6) - (7)].id));
		   }
		 }
	       }
    break;

  case 35:

/* Line 1806 of yacc.c  */
#line 874 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   init_language();
		   (yyvsp[(6) - (11)].type)->is_pointer += (yyvsp[(7) - (11)].decl).is_pointer;
		   if (add_symbol((yyvsp[(3) - (11)].id),(DataType *) 0, (char *) 0)) {
		     fprintf(stderr,"%s : Line %d. Name of native function %s conflicts with previous declaration (ignored)\n",
			     input_file, line_number, (yyvsp[(3) - (11)].id));
		   } else {
		     if ((yyvsp[(5) - (11)].ivalue)) {
		       emit_extern_func((yyvsp[(7) - (11)].decl).id, (yyvsp[(6) - (11)].type), (yyvsp[(9) - (11)].pl), (yyvsp[(5) - (11)].ivalue), f_header);
		     }
		     doc_entry = new DocDecl((yyvsp[(3) - (11)].id),doc_stack[doc_stack_top]);
		     lang->add_native((yyvsp[(3) - (11)].id),(yyvsp[(7) - (11)].decl).id);
		   }
		 }
		 delete (yyvsp[(6) - (11)].type);
		 delete (yyvsp[(9) - (11)].pl);
	       }
    break;

  case 36:

/* Line 1806 of yacc.c  */
#line 895 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   if (!title_init) {
		     title_init = 1;
		     doc_init = 1;
		     if (!comment_handler) {
		       comment_handler = new CommentHandler();
		     }
		     { 
		       int ii;
		       for (ii = 0; ii < (yyvsp[(3) - (3)].dlist).count; ii++) {
			 comment_handler->style((yyvsp[(3) - (3)].dlist).names[ii],(yyvsp[(3) - (3)].dlist).values[ii]);
		       }
		     }
		     // Create a new title for documentation 
		     {
		       int temp = line_number;
		       line_number = (yyvsp[(1) - (3)].ivalue);
		       if (!doctitle)
			 doctitle = new DocTitle((yyvsp[(2) - (3)].id),0);
		       else {
			 doctitle->name = copy_string(title);
			 doctitle->line_number = (yyvsp[(1) - (3)].ivalue);
			 doctitle->end_line = (yyvsp[(1) - (3)].ivalue);
		       }
		       line_number = temp;
		     }
		     doctitle->usage = (yyvsp[(2) - (3)].id);
		     doc_entry = doctitle;
		     doc_stack[0] = doc_entry;
		     doc_stack_top = 0;
		     handler_stack[0] = comment_handler;
		     { 
		       int ii;
		       for (ii = 0; ii < (yyvsp[(3) - (3)].dlist).count; ii++) {
			 doc_stack[doc_stack_top]->style((yyvsp[(3) - (3)].dlist).names[ii],(yyvsp[(3) - (3)].dlist).values[ii]);
		       }
		     }

		   } else {
		     // Ignore it
		   }
		 }
	       }
    break;

  case 37:

/* Line 1806 of yacc.c  */
#line 943 "parser.y"
    {
		 if (allow && (!WrapExtern) && (!IgnoreDoc)) {
		   // Copy old comment handler
		   // if (handler_stack[1]) delete handler_stack[1];
		   handler_stack[1] = new CommentHandler(handler_stack[0]);  
		   comment_handler = handler_stack[1];
		   { 
		     int ii;
		     for (ii = 0; ii < (yyvsp[(3) - (3)].dlist).count; ii++) {
		       comment_handler->style((yyvsp[(3) - (3)].dlist).names[ii],(yyvsp[(3) - (3)].dlist).values[ii]);
		     }
		   }
		   {
		     int temp = line_number;
		     line_number = (yyvsp[(1) - (3)].ivalue);
		     doc_entry = new DocSection((yyvsp[(2) - (3)].id),doc_stack[0]);
		     line_number = temp;
		   }
		   doc_stack_top = 1;
		   doc_stack[1] = doc_entry;
		   { 
		     int ii;
		     for (ii = 0; ii < (yyvsp[(3) - (3)].dlist).count; ii++) {
		       doc_stack[doc_stack_top]->style((yyvsp[(3) - (3)].dlist).names[ii],(yyvsp[(3) - (3)].dlist).values[ii]);
		     }
		   }
		 }
	       }
    break;

  case 38:

/* Line 1806 of yacc.c  */
#line 973 "parser.y"
    {
		 if (allow && (!WrapExtern) && (!IgnoreDoc)) {
		   if (doc_stack_top < 1) {
		     fprintf(stderr,"%s : Line %d. Can't apply %%subsection here.\n", input_file,line_number);
		     FatalError();
		   } else {

		     // Copy old comment handler
		     // if (handler_stack[2]) delete handler_stack[2];
		     handler_stack[2] = new CommentHandler(handler_stack[1]);
		     comment_handler = handler_stack[2];
		     { 
		       int ii;
		       for (ii = 0; ii < (yyvsp[(3) - (3)].dlist).count; ii++) {
			 comment_handler->style((yyvsp[(3) - (3)].dlist).names[ii],(yyvsp[(3) - (3)].dlist).values[ii]);
		       }
		     }
		     {
		       int temp = line_number;
		       line_number = (yyvsp[(1) - (3)].ivalue);
		       doc_entry = new DocSection((yyvsp[(2) - (3)].id),doc_stack[1]);
		       line_number = temp;
		     }
		     doc_stack_top = 2;
		     doc_stack[2] = doc_entry;
		     { 
		       int ii;
		       for (ii = 0; ii < (yyvsp[(3) - (3)].dlist).count; ii++) {
			 doc_stack[doc_stack_top]->style((yyvsp[(3) - (3)].dlist).names[ii],(yyvsp[(3) - (3)].dlist).values[ii]);
		       }
		     }
		   }
		 }
	       }
    break;

  case 39:

/* Line 1806 of yacc.c  */
#line 1009 "parser.y"
    {
		 if (allow && (!WrapExtern) && (!IgnoreDoc)) {
		   if (doc_stack_top < 2) {
		     fprintf(stderr,"%s : Line %d. Can't apply %%subsubsection here.\n", input_file,line_number);
		     FatalError();
		   } else {

		     // Copy old comment handler

		     // if (handler_stack[3]) delete handler_stack[3];
		     handler_stack[3] = new CommentHandler(handler_stack[2]);
		     comment_handler = handler_stack[3];
		     { 
		       int ii;
		       for (ii = 0; ii < (yyvsp[(3) - (3)].dlist).count; ii++) {
			 comment_handler->style((yyvsp[(3) - (3)].dlist).names[ii],(yyvsp[(3) - (3)].dlist).values[ii]);
		       }
		     }
		     {
		       int temp = line_number;
		       line_number = (yyvsp[(1) - (3)].ivalue);
		       doc_entry = new DocSection((yyvsp[(2) - (3)].id),doc_stack[2]);
		       line_number = temp;
		     }
		     doc_stack_top = 3;
		     doc_stack[3] = doc_entry;
		     { 
		       int ii;
		       for (ii = 0; ii < (yyvsp[(3) - (3)].dlist).count; ii++) {
			 doc_stack[doc_stack_top]->style((yyvsp[(3) - (3)].dlist).names[ii],(yyvsp[(3) - (3)].dlist).values[ii]);
		       }
		     }
		   }
		 }
	       }
    break;

  case 40:

/* Line 1806 of yacc.c  */
#line 1046 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   fprintf(stderr,"%%alpha directive is obsolete.  Use '%%style sort' instead.\n");
		   handler_stack[0]->style("sort",0);
		   doc_stack[0]->style("sort",0);
		 }
	       }
    break;

  case 41:

/* Line 1806 of yacc.c  */
#line 1054 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   fprintf(stderr,"%%raw directive is obsolete. Use '%%style nosort' instead.\n");
		   handler_stack[0]->style("nosort",0);
		   doc_stack[0]->style("nosort",0);
		 }
	       }
    break;

  case 42:

/* Line 1806 of yacc.c  */
#line 1062 "parser.y"
    { }
    break;

  case 43:

/* Line 1806 of yacc.c  */
#line 1066 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   (yyvsp[(2) - (2)].id)[strlen((yyvsp[(2) - (2)].id)) - 1] = 0;
		   doc_entry = new DocText((yyvsp[(2) - (2)].id),doc_stack[doc_stack_top]);
		   doc_entry = 0;
		 }
	       }
    break;

  case 44:

/* Line 1806 of yacc.c  */
#line 1075 "parser.y"
    { }
    break;

  case 45:

/* Line 1806 of yacc.c  */
#line 1079 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   init_language();
		   (yyvsp[(1) - (1)].id)[strlen((yyvsp[(1) - (1)].id)) - 1] = 0;
//		   fprintf(f_header,"#line %d \"%s\"\n", start_line, input_file);
		   fprintf(f_header, "%s\n", (yyvsp[(1) - (1)].id));
		 }
	       }
    break;

  case 46:

/* Line 1806 of yacc.c  */
#line 1090 "parser.y"
    {
                 if (allow && (!WrapExtern)) {
		   init_language();
		   (yyvsp[(2) - (2)].id)[strlen((yyvsp[(2) - (2)].id)) - 1] = 0;
		   fprintf(f_wrappers,"%s\n",(yyvsp[(2) - (2)].id));
		 }
	       }
    break;

  case 47:

/* Line 1806 of yacc.c  */
#line 1100 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   init_language();
		   (yyvsp[(2) - (2)].id)[strlen((yyvsp[(2) - (2)].id)) -1] = 0;
		   fprintf(f_init,"%s\n", (yyvsp[(2) - (2)].id));
		 }
	       }
    break;

  case 48:

/* Line 1806 of yacc.c  */
#line 1109 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   init_language();
		   (yyvsp[(2) - (2)].id)[strlen((yyvsp[(2) - (2)].id)) - 1] = 0;
		   fprintf(f_header, "%s\n", (yyvsp[(2) - (2)].id));
		   start_inline((yyvsp[(2) - (2)].id),start_line);
		 }
	       }
    break;

  case 49:

/* Line 1806 of yacc.c  */
#line 1119 "parser.y"
    {
		 if (allow && (!WrapExtern)) {
		   fprintf(stderr,"%s\n", (yyvsp[(2) - (2)].id));
		 }
	       }
    break;

  case 50:

/* Line 1806 of yacc.c  */
#line 1125 "parser.y"
    {
                 if (allow && (!WrapExtern)) {
                   fprintf(stderr,"%s\n", (yyvsp[(2) - (2)].id));
                 }
               }
    break;

  case 51:

/* Line 1806 of yacc.c  */
#line 1132 "parser.y"
    {
                   DocOnly = 1;
               }
    break;

  case 52:

/* Line 1806 of yacc.c  */
#line 1138 "parser.y"
    {
		 if (allow) {
		   if (!module_init) {
		     lang->set_init((yyvsp[(2) - (3)].id));
		     module_init = 1;
		     init_language();
		   } else {
		     if (Verbose)
		       fprintf(stderr,"%s : Line %d. %%init %s ignored.\n",
			       input_file, line_number, (yyvsp[(2) - (3)].id));
		   }
		   if ((yyvsp[(3) - (3)].ilist).count > 0) {
		     fprintf(stderr,"%s : Line %d. Warning. Init list no longer supported.\n",
			     input_file,line_number);
		   }
		 }
		 for (i = 0; i < (yyvsp[(3) - (3)].ilist).count; i++)
		   if ((yyvsp[(3) - (3)].ilist).names[i]) delete [] (yyvsp[(3) - (3)].ilist).names[i];
		 delete [] (yyvsp[(3) - (3)].ilist).names;
	       }
    break;

  case 53:

/* Line 1806 of yacc.c  */
#line 1160 "parser.y"
    {
		 if (allow) {
		   if ((yyvsp[(3) - (3)].ilist).count)
		     lang->set_module((yyvsp[(2) - (3)].id),(yyvsp[(3) - (3)].ilist).names);
		   else
		     lang->set_module((yyvsp[(2) - (3)].id),0);
		   module_init = 1;
		   init_language();
		 }
		 for (i = 0; i < (yyvsp[(3) - (3)].ilist).count; i++)
		   if ((yyvsp[(3) - (3)].ilist).names[i]) delete [] (yyvsp[(3) - (3)].ilist).names[i];
		 delete [] (yyvsp[(3) - (3)].ilist).names;
	       }
    break;

  case 54:

/* Line 1806 of yacc.c  */
#line 1176 "parser.y"
    {
		 if (allow) {
		   if (((yyvsp[(3) - (3)].dtype).type != T_ERROR) && ((yyvsp[(3) - (3)].dtype).type != T_SYMBOL)) {
		     init_language();
		     temp_typeptr = new DataType((yyvsp[(3) - (3)].dtype).type);
		     create_constant((yyvsp[(2) - (3)].id), temp_typeptr, (yyvsp[(3) - (3)].dtype).id);
		     delete temp_typeptr;
		   } else if ((yyvsp[(3) - (3)].dtype).type == T_SYMBOL) {
		     // Add a symbol to the SWIG symbol table
		     if (add_symbol((yyvsp[(2) - (3)].id),(DataType *) 0, (char *) 0)) {
		       fprintf(stderr,"%s : Line %d. Warning. Symbol %s already defined.\n", 
			       input_file,line_number, (yyvsp[(2) - (3)].id));
		     }
		   }
		 }
	       }
    break;

  case 55:

/* Line 1806 of yacc.c  */
#line 1195 "parser.y"
    {
		 if (Verbose) {
		   fprintf(stderr,"%s : Line %d.  CPP Macro ignored.\n", input_file, line_number);
		 }
	       }
    break;

  case 56:

/* Line 1806 of yacc.c  */
#line 1202 "parser.y"
    {
		 remove_symbol((yyvsp[(2) - (2)].id));
	       }
    break;

  case 57:

/* Line 1806 of yacc.c  */
#line 1208 "parser.y"
    { scanner_clear_start(); }
    break;

  case 58:

/* Line 1806 of yacc.c  */
#line 1208 "parser.y"
    { 
		 if (allow) {
		   init_language();
		   if ((yyvsp[(3) - (8)].id)) {
		     temp_type.type = T_INT;
		     temp_type.is_pointer = 0;
		     temp_type.implicit_ptr = 0;
		     sprintf(temp_type.name,"int");
		     temp_type.typedef_add((yyvsp[(3) - (8)].id),1);
		   }
		 }
	       }
    break;

  case 59:

/* Line 1806 of yacc.c  */
#line 1223 "parser.y"
    { scanner_clear_start(); }
    break;

  case 60:

/* Line 1806 of yacc.c  */
#line 1223 "parser.y"
    {
		 if (allow) {
		   init_language();
		   temp_type.type = T_INT;
		   temp_type.is_pointer = 0;
		   temp_type.implicit_ptr = 0;
		   sprintf(temp_type.name,"int");
		   Active_typedef = new DataType(&temp_type);
		   temp_type.typedef_add((yyvsp[(8) - (8)].id),1);
		 }
	       }
    break;

  case 61:

/* Line 1806 of yacc.c  */
#line 1233 "parser.y"
    { }
    break;

  case 62:

/* Line 1806 of yacc.c  */
#line 1243 "parser.y"
    {
		   TMParm *p;
                   skip_brace();
		   p = (yyvsp[(7) - (8)].tmparm);
		   while (p) {
		     typemap_register((yyvsp[(5) - (8)].id),(yyvsp[(3) - (8)].id),p->p->t,p->p->name,CCode,p->args);
		     p = p->next;
                   }
		   delete (yyvsp[(3) - (8)].id);
		   delete (yyvsp[(5) - (8)].id);
	       }
    break;

  case 63:

/* Line 1806 of yacc.c  */
#line 1256 "parser.y"
    {
		 if (!typemap_lang) {
		   fprintf(stderr,"SWIG internal error. No typemap_lang specified.\n");
		   fprintf(stderr,"typemap on %s : Line %d. will be ignored.\n",input_file,line_number);
		   FatalError();
		 } else {
		   TMParm *p;
		   skip_brace();
		   p = (yyvsp[(5) - (6)].tmparm);
		   while (p) {
		     typemap_register((yyvsp[(3) - (6)].id),typemap_lang,p->p->t,p->p->name,CCode,p->args);
		     p = p->next;
		   }
		 }
		 delete (yyvsp[(3) - (6)].id);
	       }
    break;

  case 64:

/* Line 1806 of yacc.c  */
#line 1275 "parser.y"
    {
		 TMParm *p;
		 p = (yyvsp[(7) - (8)].tmparm);
		 while (p) {
                   typemap_clear((yyvsp[(5) - (8)].id),(yyvsp[(3) - (8)].id),p->p->t,p->p->name);
		   p = p->next;
		 }
		 delete (yyvsp[(3) - (8)].id);
		 delete (yyvsp[(5) - (8)].id);
	       }
    break;

  case 65:

/* Line 1806 of yacc.c  */
#line 1287 "parser.y"
    {
		 if (!typemap_lang) {
		   fprintf(stderr,"SWIG internal error. No typemap_lang specified.\n");
		   fprintf(stderr,"typemap on %s : Line %d. will be ignored.\n",input_file,line_number);
		   FatalError();
		 } else {
		   TMParm *p;
		   p = (yyvsp[(5) - (6)].tmparm);
		   while (p) {
		     typemap_clear((yyvsp[(3) - (6)].id),typemap_lang,p->p->t,p->p->name);
		     p = p->next;
		   }
		 }
		 delete (yyvsp[(3) - (6)].id);
	       }
    break;

  case 66:

/* Line 1806 of yacc.c  */
#line 1305 "parser.y"
    {
                   TMParm *p;
		   p = (yyvsp[(7) - (10)].tmparm);
		   while (p) {
		     typemap_copy((yyvsp[(5) - (10)].id),(yyvsp[(3) - (10)].id),(yyvsp[(9) - (10)].tmparm)->p->t,(yyvsp[(9) - (10)].tmparm)->p->name,p->p->t,p->p->name);
		     p = p->next;
		   }
		   delete (yyvsp[(3) - (10)].id);
		   delete (yyvsp[(5) - (10)].id);
		   delete (yyvsp[(9) - (10)].tmparm)->p;
		   delete (yyvsp[(9) - (10)].tmparm);
	       }
    break;

  case 67:

/* Line 1806 of yacc.c  */
#line 1320 "parser.y"
    {
		 if (!typemap_lang) {
		   fprintf(stderr,"SWIG internal error. No typemap_lang specified.\n");
		   fprintf(stderr,"typemap on %s : Line %d. will be ignored.\n",input_file,line_number);
		   FatalError();
		 } else {
                   TMParm *p;
		   p = (yyvsp[(5) - (8)].tmparm);
		   while (p) {
		     typemap_copy((yyvsp[(3) - (8)].id),typemap_lang,(yyvsp[(7) - (8)].tmparm)->p->t,(yyvsp[(7) - (8)].tmparm)->p->name,p->p->t,p->p->name);
		     p = p->next;
		   }
		 }
		 delete (yyvsp[(3) - (8)].id);
		 delete (yyvsp[(7) - (8)].tmparm)->p;
		 delete (yyvsp[(7) - (8)].tmparm);
	       }
    break;

  case 68:

/* Line 1806 of yacc.c  */
#line 1341 "parser.y"
    {
		 TMParm *p;
		 p = (yyvsp[(4) - (5)].tmparm);
		 while(p) {
		   typemap_apply((yyvsp[(2) - (5)].tmparm)->p->t,(yyvsp[(2) - (5)].tmparm)->p->name,p->p->t,p->p->name);
		   p = p->next;
		 }
		 delete (yyvsp[(4) - (5)].tmparm);
		 delete (yyvsp[(2) - (5)].tmparm)->args;
		 delete (yyvsp[(2) - (5)].tmparm);
               }
    break;

  case 69:

/* Line 1806 of yacc.c  */
#line 1352 "parser.y"
    {
		 TMParm *p;
		 p = (yyvsp[(2) - (3)].tmparm);
		 while (p) {
		   typemap_clear_apply(p->p->t, p->p->name);
		   p = p->next;
		 }
               }
    break;

  case 70:

/* Line 1806 of yacc.c  */
#line 1369 "parser.y"
    {
                    skip_brace();
                    fragment_register("except",(yyvsp[(3) - (5)].id), CCode);
		    delete (yyvsp[(3) - (5)].id);
	       }
    break;

  case 71:

/* Line 1806 of yacc.c  */
#line 1376 "parser.y"
    {
                    skip_brace();
                    fragment_register("except",typemap_lang, CCode);
               }
    break;

  case 72:

/* Line 1806 of yacc.c  */
#line 1383 "parser.y"
    {
                     fragment_clear("except",(yyvsp[(3) - (5)].id));
               }
    break;

  case 73:

/* Line 1806 of yacc.c  */
#line 1388 "parser.y"
    {
                     fragment_clear("except",typemap_lang);
	       }
    break;

  case 74:

/* Line 1806 of yacc.c  */
#line 1394 "parser.y"
    { }
    break;

  case 75:

/* Line 1806 of yacc.c  */
#line 1395 "parser.y"
    { }
    break;

  case 76:

/* Line 1806 of yacc.c  */
#line 1396 "parser.y"
    { }
    break;

  case 77:

/* Line 1806 of yacc.c  */
#line 1397 "parser.y"
    {
		 if (!Error) {
		   {
		     static int last_error_line = -1;
		     if (last_error_line != line_number) {
		       fprintf(stderr,"%s : Line %d. Syntax error in input.\n", input_file, line_number);
		       FatalError();
		       last_error_line = line_number;
                       // Try to make some kind of recovery.
		       skip_decl();
		     }
		     Error = 1;
		   }
		 }
	       }
    break;

  case 78:

/* Line 1806 of yacc.c  */
#line 1415 "parser.y"
    { }
    break;

  case 79:

/* Line 1806 of yacc.c  */
#line 1416 "parser.y"
    { }
    break;

  case 80:

/* Line 1806 of yacc.c  */
#line 1420 "parser.y"
    { }
    break;

  case 81:

/* Line 1806 of yacc.c  */
#line 1424 "parser.y"
    {
		 { 
		   int ii,jj;
		   for (ii = 0; ii < (yyvsp[(2) - (2)].dlist).count; ii++) {
		     comment_handler->style((yyvsp[(2) - (2)].dlist).names[ii],(yyvsp[(2) - (2)].dlist).values[ii]);
		     for (jj = 0; jj < doc_stack_top; jj++) 
		       doc_stack[jj]->style((yyvsp[(2) - (2)].dlist).names[ii],(yyvsp[(2) - (2)].dlist).values[ii]);
		     if (doctitle)
		       doctitle->style((yyvsp[(2) - (2)].dlist).names[ii],(yyvsp[(2) - (2)].dlist).values[ii]);
		     doc->style((yyvsp[(2) - (2)].dlist).names[ii],(yyvsp[(2) - (2)].dlist).values[ii]);
		   }
		 }
	       }
    break;

  case 82:

/* Line 1806 of yacc.c  */
#line 1440 "parser.y"
    {
		 { 
		   int ii;
		   for (ii = 0; ii < (yyvsp[(2) - (2)].dlist).count; ii++) {
		     comment_handler = new CommentHandler(comment_handler);
		     handler_stack[doc_stack_top] = comment_handler;
		     comment_handler->style((yyvsp[(2) - (2)].dlist).names[ii],(yyvsp[(2) - (2)].dlist).values[ii]);
		     doc_stack[doc_stack_top]->style((yyvsp[(2) - (2)].dlist).names[ii],(yyvsp[(2) - (2)].dlist).values[ii]);
		   }
		 }
	       }
    break;

  case 83:

/* Line 1806 of yacc.c  */
#line 1453 "parser.y"
    { }
    break;

  case 84:

/* Line 1806 of yacc.c  */
#line 1459 "parser.y"
    {
		 if (allow) {
		   if (IgnoreDoc) {
		     /* Already in a disabled documentation */
		     doc_scope++;
		   } else {
		     if (Verbose)
		       fprintf(stderr,"%s : Line %d. Documentation disabled.\n", input_file, line_number);
		     IgnoreDoc = 1;
		     doc_scope = 1;
		   }
		 }
	       }
    break;

  case 85:

/* Line 1806 of yacc.c  */
#line 1473 "parser.y"
    {
		 if (allow) {
		   if (IgnoreDoc) {
		     if (doc_scope > 1) {
		       doc_scope--;
		     } else {
		       if (Verbose)
			 fprintf(stderr,"%s : Line %d. Documentation enabled.\n", input_file, line_number);
		       IgnoreDoc = 0;
		       doc_scope = 0;
		     }
		   }
		 }
	       }
    break;

  case 86:

/* Line 1806 of yacc.c  */
#line 1492 "parser.y"
    {
		 if (allow) {
		   init_language();
		   /* Add a new typedef */
		   Active_typedef = new DataType((yyvsp[(2) - (3)].type));
		   (yyvsp[(2) - (3)].type)->is_pointer += (yyvsp[(3) - (3)].decl).is_pointer;
		   (yyvsp[(2) - (3)].type)->typedef_add((yyvsp[(3) - (3)].decl).id);
		   /* If this is %typedef, add it to the header */
		   if ((yyvsp[(1) - (3)].ivalue)) 
		     fprintf(f_header,"typedef %s %s;\n", (yyvsp[(2) - (3)].type)->print_full(), (yyvsp[(3) - (3)].decl).id);
		   cplus_register_type((yyvsp[(3) - (3)].decl).id);
		 }
	       }
    break;

  case 87:

/* Line 1806 of yacc.c  */
#line 1504 "parser.y"
    { }
    break;

  case 88:

/* Line 1806 of yacc.c  */
#line 1508 "parser.y"
    {
		 if (allow) {
		   init_language();
		   /* Typedef'd pointer */
		   if ((yyvsp[(1) - (10)].ivalue)) {
		     sprintf(temp_name,"(*%s)",(yyvsp[(5) - (10)].id));
		     fprintf(f_header,"typedef ");
		     emit_extern_func(temp_name, (yyvsp[(2) - (10)].type),(yyvsp[(8) - (10)].pl),0,f_header);
		   }
		   strcpy((yyvsp[(2) - (10)].type)->name,"<function ptr>");
		   (yyvsp[(2) - (10)].type)->type = T_USER;
		   (yyvsp[(2) - (10)].type)->is_pointer = 1;
		   (yyvsp[(2) - (10)].type)->typedef_add((yyvsp[(5) - (10)].id),1);
		   cplus_register_type((yyvsp[(5) - (10)].id));
		 }
		 delete (yyvsp[(2) - (10)].type);
		 delete (yyvsp[(5) - (10)].id);
		 delete (yyvsp[(8) - (10)].pl);
	       }
    break;

  case 89:

/* Line 1806 of yacc.c  */
#line 1530 "parser.y"
    {
		 if (allow) {
		   init_language();
		   if ((yyvsp[(1) - (11)].ivalue)) {
		     (yyvsp[(2) - (11)].type)->is_pointer += (yyvsp[(3) - (11)].ivalue);
		     sprintf(temp_name,"(*%s)",(yyvsp[(6) - (11)].id));
		     fprintf(f_header,"typedef ");
		     emit_extern_func(temp_name, (yyvsp[(2) - (11)].type),(yyvsp[(9) - (11)].pl),0,f_header);
		   }

		   /* Typedef'd pointer */
		   strcpy((yyvsp[(2) - (11)].type)->name,"<function ptr>");
		   (yyvsp[(2) - (11)].type)->type = T_USER;
		   (yyvsp[(2) - (11)].type)->is_pointer = 1;
		   (yyvsp[(2) - (11)].type)->typedef_add((yyvsp[(6) - (11)].id),1);
		   cplus_register_type((yyvsp[(6) - (11)].id));
		 }
		 delete (yyvsp[(2) - (11)].type);
		 delete (yyvsp[(6) - (11)].id);
		 delete (yyvsp[(9) - (11)].pl);
	       }
    break;

  case 90:

/* Line 1806 of yacc.c  */
#line 1554 "parser.y"
    {
		 if (allow) {
		   init_language();
		   Active_typedef = new DataType((yyvsp[(2) - (4)].type));
		   // This datatype is going to be readonly
			
		   (yyvsp[(2) - (4)].type)->status = STAT_READONLY | STAT_REPLACETYPE;
		   (yyvsp[(2) - (4)].type)->is_pointer += (yyvsp[(3) - (4)].decl).is_pointer;
		   // Turn this into a "pointer" corresponding to the array
		   (yyvsp[(2) - (4)].type)->is_pointer++;
		   (yyvsp[(2) - (4)].type)->arraystr = copy_string(ArrayString);
		   (yyvsp[(2) - (4)].type)->typedef_add((yyvsp[(3) - (4)].decl).id);
		   fprintf(stderr,"%s : Line %d. Warning. Array type %s will be read-only without a typemap\n",input_file,line_number, (yyvsp[(3) - (4)].decl).id);
		   cplus_register_type((yyvsp[(3) - (4)].decl).id);

		 }
	       }
    break;

  case 91:

/* Line 1806 of yacc.c  */
#line 1570 "parser.y"
    { }
    break;

  case 92:

/* Line 1806 of yacc.c  */
#line 1583 "parser.y"
    {
                if (allow) {
		  if (Active_typedef) {
		    DataType *t;
		    t = new DataType(Active_typedef);
		    t->is_pointer += (yyvsp[(2) - (3)].decl).is_pointer;
		    t->typedef_add((yyvsp[(2) - (3)].decl).id);
		    cplus_register_type((yyvsp[(2) - (3)].decl).id);
		    delete t;
		  }
		}
              }
    break;

  case 93:

/* Line 1806 of yacc.c  */
#line 1595 "parser.y"
    {
		    DataType *t;
		    t = new DataType(Active_typedef);
		    t->status = STAT_READONLY | STAT_REPLACETYPE;
		    t->is_pointer += (yyvsp[(2) - (3)].decl).is_pointer + 1;
		    t->arraystr = copy_string(ArrayString);
		    t->typedef_add((yyvsp[(2) - (3)].decl).id);
		    cplus_register_type((yyvsp[(2) - (3)].decl).id);
		    delete t;
    		    fprintf(stderr,"%s : Line %d. Warning. Array type %s will be read-only without a typemap.\n",input_file,line_number, (yyvsp[(2) - (3)].decl).id);
	      }
    break;

  case 94:

/* Line 1806 of yacc.c  */
#line 1606 "parser.y"
    { }
    break;

  case 95:

/* Line 1806 of yacc.c  */
#line 1626 "parser.y"
    {
		 /* Push old if-then-else status */
		 if_push();
		 /* Look a symbol up in the symbol table */
		 if (lookup_symbol((yyvsp[(2) - (2)].id))) {
		   in_then = 1;
		   in_else = 0;
		   allow = 1 & prev_allow;
		 } else {
		   /* Condition is false.   Skip over whatever is in this block */
		   in_else = skip_cond(1);
		   if (in_else == -1) {
		     /* Unrecoverable error */
		     SWIG_exit(1);
		   }
		   if (!in_else) {
		     if_pop();        // Pop out. Reached end of block
		   } else {
		     allow = prev_allow;
		     in_then = 0;
		   }
		 }
                }
    break;

  case 96:

/* Line 1806 of yacc.c  */
#line 1652 "parser.y"
    {
		 if_push();
		 if (lookup_symbol((yyvsp[(2) - (2)].id))) {
		   /* Condition is false.   Skip over whatever is in this block */
		   in_else = skip_cond(1);
		   if (in_else == -1) {
		     /* Unrecoverable error */
		     SWIG_exit(1);
		   }
		   if (!in_else) {
		     if_pop();        // Pop out. Reached end of block
		   } else {
		     allow = prev_allow;
		     in_then = 0;
		   }
		 } else {
		   in_then = 1;
		   in_else = 0;		   
		   allow = 1 & prev_allow;
		 }
	       }
    break;

  case 97:

/* Line 1806 of yacc.c  */
#line 1675 "parser.y"
    {
		 if ((!in_then) || (in_else)) {
		   fprintf(stderr,"%s : Line %d. Misplaced else\n", input_file, line_number);
		   FatalError();
		 } else {
		   in_then = 0;
		   in_else = 1;
		   if (allow) {
		     allow = 0;
		     /* Skip over rest of the conditional */
		     skip_cond(0);
		     if_pop();
		   } else {
		     allow = 1;
		   }
		   allow = allow & prev_allow;
		 }
	       }
    break;

  case 98:

/* Line 1806 of yacc.c  */
#line 1694 "parser.y"
    {
		 if ((!in_then) && (!in_else)) {
		   fprintf(stderr,"%s : Line %d. Misplaced endif\n", input_file, line_number);
		   FatalError();
		 } else {
		   if_pop();
		 }
	       }
    break;

  case 99:

/* Line 1806 of yacc.c  */
#line 1704 "parser.y"
    {
		 /* Push old if-then-else status */
		 if_push();
		 if ((yyvsp[(2) - (2)].ivalue)) {
		   in_then = 1;
		   in_else = 0;
		   allow = 1 & prev_allow;
		 } else {
		   /* Condition is false.   Skip over whatever is in this block */
		   in_else = skip_cond(1);
		   if (in_else == -1) {
		     /* Unrecoverable error */
		     SWIG_exit(1);
		   }
		   if (!in_else) {
		     if_pop();        // Pop out. Reached end of block
		   } else {
		     allow = prev_allow;
		     in_then = 0;
		   }
		 }
	       }
    break;

  case 100:

/* Line 1806 of yacc.c  */
#line 1730 "parser.y"
    {
		 /* have to pop old if clause off */
		 if_pop();

		 /* Push old if-then-else status */
		 if_push();
		 if ((yyvsp[(2) - (2)].ivalue)) {
		   in_then = 1;
		   in_else = 0;
		   allow = 1 & prev_allow;
		 } else {
		   /* Condition is false.   Skip over whatever is in this block */
		   in_else = skip_cond(1);
		   if (in_else == -1) {
		     /* Unrecoverable error */
		     SWIG_exit(1);
		   }
		   if (!in_else) {
		     if_pop();        // Pop out. Reached end of block
		   } else {
		     allow = prev_allow;
		     in_then = 0;
		   }
		 }
	       }
    break;

  case 101:

/* Line 1806 of yacc.c  */
#line 1759 "parser.y"
    {

                 /* Look ID up in the symbol table */
                    if (lookup_symbol((yyvsp[(3) - (4)].id))) {
		      (yyval.ivalue) = 1;
		    } else {
		      (yyval.ivalue) = 0;
		    }
               }
    break;

  case 102:

/* Line 1806 of yacc.c  */
#line 1768 "parser.y"
    {
		 if (lookup_symbol((yyvsp[(2) - (2)].id))) {
		   (yyval.ivalue) = 1;
		 } else {
		   (yyval.ivalue) = 0;
		 }
	       }
    break;

  case 103:

/* Line 1806 of yacc.c  */
#line 1775 "parser.y"
    {
                      if ((yyvsp[(2) - (2)].ivalue)) (yyval.ivalue) = 0;
		      else (yyval.ivalue) = 1;
	       }
    break;

  case 104:

/* Line 1806 of yacc.c  */
#line 1781 "parser.y"
    {
		 if (allow && (!WrapExtern))
		   lang->pragma((yyvsp[(3) - (7)].id),(yyvsp[(5) - (7)].id),(yyvsp[(6) - (7)].id));
		   fprintf(stderr,"%s : Line %d. Warning. '%%pragma(lang,opt=value)' syntax is obsolete.\n",
			   input_file,line_number);
		   fprintf(stderr,"        Use '%%pragma(lang) opt=value' instead.\n");
	       }
    break;

  case 105:

/* Line 1806 of yacc.c  */
#line 1789 "parser.y"
    {
                 if (allow && (!WrapExtern)) 
		   swig_pragma((yyvsp[(2) - (3)].id),(yyvsp[(3) - (3)].id));
    	       }
    break;

  case 106:

/* Line 1806 of yacc.c  */
#line 1793 "parser.y"
    {
		 if (allow && (!WrapExtern))
		   lang->pragma((yyvsp[(3) - (6)].id),(yyvsp[(5) - (6)].id),(yyvsp[(6) - (6)].id));
	       }
    break;

  case 107:

/* Line 1806 of yacc.c  */
#line 1801 "parser.y"
    { }
    break;

  case 108:

/* Line 1806 of yacc.c  */
#line 1802 "parser.y"
    {
		 if (allow) {
		   init_language();
		   temp_typeptr = new DataType(Active_type);
		   temp_typeptr->is_pointer += (yyvsp[(2) - (4)].decl).is_pointer;
		   if ((yyvsp[(3) - (4)].ivalue) > 0) {
		     temp_typeptr->is_pointer++;
		     temp_typeptr->status = STAT_READONLY;
		     temp_typeptr->arraystr = copy_string(ArrayString);
		   }
		   if ((yyvsp[(2) - (4)].decl).is_reference) {
		     fprintf(stderr,"%s : Line %d. Error. Linkage to C++ reference not allowed.\n", input_file, line_number);
		     FatalError();
		   } else {
		     if (temp_typeptr->qualifier) {
		       if ((strcmp(temp_typeptr->qualifier,"const") == 0)) {
			 /* Okay.  This is really some sort of C++ constant here. */
			 if ((yyvsp[(4) - (4)].dtype).type != T_ERROR)
			   create_constant((yyvsp[(2) - (4)].decl).id, temp_typeptr, (yyvsp[(4) - (4)].dtype).id);
		       } else 
			 create_variable(Active_extern,(yyvsp[(2) - (4)].decl).id, temp_typeptr);
		     } else
		       create_variable(Active_extern, (yyvsp[(2) - (4)].decl).id, temp_typeptr);
		   }
		   delete temp_typeptr;
		 }
	       }
    break;

  case 109:

/* Line 1806 of yacc.c  */
#line 1828 "parser.y"
    { }
    break;

  case 110:

/* Line 1806 of yacc.c  */
#line 1829 "parser.y"
    {
		 if (allow) {
		   init_language();
		   temp_typeptr = new DataType(Active_type);
		   temp_typeptr->is_pointer += (yyvsp[(2) - (6)].decl).is_pointer;
		   temp_typeptr->is_reference = (yyvsp[(2) - (6)].decl).is_reference;
		   create_function(Active_extern, (yyvsp[(2) - (6)].decl).id, temp_typeptr, (yyvsp[(4) - (6)].pl));
		   delete temp_typeptr;
		 }
		 delete (yyvsp[(4) - (6)].pl);
	       }
    break;

  case 111:

/* Line 1806 of yacc.c  */
#line 1839 "parser.y"
    { }
    break;

  case 112:

/* Line 1806 of yacc.c  */
#line 1842 "parser.y"
    {
                   (yyval.dtype) = (yyvsp[(1) - (2)].dtype);
                 }
    break;

  case 113:

/* Line 1806 of yacc.c  */
#line 1845 "parser.y"
    {
                   (yyval.dtype).type = T_SYMBOL;
	       }
    break;

  case 114:

/* Line 1806 of yacc.c  */
#line 1848 "parser.y"
    {
		 if (Verbose) 
		   fprintf(stderr,"%s : Line %d.  Warning. Unable to parse #define (ignored)\n", input_file, line_number);
		 (yyval.dtype).type = T_ERROR;
	       }
    break;

  case 115:

/* Line 1806 of yacc.c  */
#line 1856 "parser.y"
    { (yyval.ivalue) = 1; }
    break;

  case 116:

/* Line 1806 of yacc.c  */
#line 1857 "parser.y"
    {(yyval.ivalue) = 0; }
    break;

  case 117:

/* Line 1806 of yacc.c  */
#line 1858 "parser.y"
    {
		 if (strcmp((yyvsp[(2) - (2)].id),"C") == 0) {
		   (yyval.ivalue) = 2;
		 } else {
		   fprintf(stderr,"%s : Line %d.  Unrecognized extern type \"%s\" (ignored).\n", input_file, line_number, (yyvsp[(2) - (2)].id));
		   FatalError();
		 }
	       }
    break;

  case 118:

/* Line 1806 of yacc.c  */
#line 1870 "parser.y"
    { skip_brace(); }
    break;

  case 119:

/* Line 1806 of yacc.c  */
#line 1879 "parser.y"
    {
                 if (((yyvsp[(1) - (2)].p)->t->type != T_VOID) || ((yyvsp[(1) - (2)].p)->t->is_pointer))
		   (yyvsp[(2) - (2)].pl)->insert((yyvsp[(1) - (2)].p),0);
		 (yyval.pl) = (yyvsp[(2) - (2)].pl);
		 delete (yyvsp[(1) - (2)].p);
		}
    break;

  case 120:

/* Line 1806 of yacc.c  */
#line 1885 "parser.y"
    { (yyval.pl) = new ParmList;}
    break;

  case 121:

/* Line 1806 of yacc.c  */
#line 1888 "parser.y"
    {
		 (yyvsp[(3) - (3)].pl)->insert((yyvsp[(2) - (3)].p),0);
		 (yyval.pl) = (yyvsp[(3) - (3)].pl);
		 delete (yyvsp[(2) - (3)].p);
                }
    break;

  case 122:

/* Line 1806 of yacc.c  */
#line 1893 "parser.y"
    { (yyval.pl) = new ParmList;}
    break;

  case 123:

/* Line 1806 of yacc.c  */
#line 1896 "parser.y"
    {
                  (yyval.p) = (yyvsp[(1) - (1)].p);
		  if (typemap_check("ignore",typemap_lang,(yyval.p)->t,(yyval.p)->name))
		    (yyval.p)->ignore = 1;
               }
    break;

  case 124:

/* Line 1806 of yacc.c  */
#line 1901 "parser.y"
    {
                  (yyval.p) = (yyvsp[(2) - (2)].p);
                  (yyval.p)->call_type = (yyval.p)->call_type | (yyvsp[(1) - (2)].ivalue);
		  if (InArray && ((yyval.p)->call_type & CALL_VALUE)) {
		     fprintf(stderr,"%s : Line %d. Error. Can't use %%val with an array.\n", input_file, line_number);
		     FatalError();
		  }
		  if (!(yyval.p)->t->is_pointer) {
		     fprintf(stderr,"%s : Line %d. Error. Can't use %%val or %%out with a non-pointer argument.\n", input_file, line_number);
		     FatalError();
		  } else {
		    (yyval.p)->t->is_pointer--;
		  }
		}
    break;

  case 125:

/* Line 1806 of yacc.c  */
#line 1916 "parser.y"
    {
		    if (InArray) {
		      (yyvsp[(1) - (2)].type)->is_pointer++;
		      if (Verbose) {
			fprintf(stderr,"%s : Line %d. Warning. Array %s", input_file, line_number, (yyvsp[(1) - (2)].type)->print_type());
			print_array();
			fprintf(stderr," has been converted to %s.\n", (yyvsp[(1) - (2)].type)->print_type());
		      }
		      // Add array string to the type
		      (yyvsp[(1) - (2)].type)->arraystr = copy_string(ArrayString.get());
		    } 
		    (yyval.p) = new Parm((yyvsp[(1) - (2)].type),(yyvsp[(2) - (2)].id));
		    (yyval.p)->call_type = 0;
		    (yyval.p)->defvalue = DefArg;
		    if (((yyvsp[(1) - (2)].type)->type == T_USER) && !((yyvsp[(1) - (2)].type)->is_pointer)) {
		      if (Verbose)
			fprintf(stderr,"%s : Line %d. Warning : Parameter of type '%s'\nhas been remapped to '%s *' and will be called using *((%s *) ptr).\n",
				input_file, line_number, (yyvsp[(1) - (2)].type)->name, (yyvsp[(1) - (2)].type)->name, (yyvsp[(1) - (2)].type)->name);

		      (yyval.p)->call_type = CALL_REFERENCE;
		      (yyval.p)->t->is_pointer++;
		    }
		    delete (yyvsp[(1) - (2)].type);
		    delete (yyvsp[(2) - (2)].id);
                 }
    break;

  case 126:

/* Line 1806 of yacc.c  */
#line 1942 "parser.y"
    {
		   (yyval.p) = new Parm((yyvsp[(1) - (3)].type),(yyvsp[(3) - (3)].id));
		   (yyval.p)->t->is_pointer += (yyvsp[(2) - (3)].ivalue);
		   (yyval.p)->call_type = 0;
		   (yyval.p)->defvalue = DefArg;
		   if (InArray) {
		     (yyval.p)->t->is_pointer++;
		     if (Verbose) {
		       fprintf(stderr,"%s : Line %d. Warning. Array %s", input_file, line_number, (yyval.p)->t->print_type());
		       print_array();
		       fprintf(stderr," has been converted to %s.\n", (yyval.p)->t->print_type());
		     }
		     // Add array string to the type
		     (yyval.p)->t->arraystr = copy_string(ArrayString.get());
		    }
		   delete (yyvsp[(1) - (3)].type);
		   delete (yyvsp[(3) - (3)].id);
		}
    break;

  case 127:

/* Line 1806 of yacc.c  */
#line 1961 "parser.y"
    {
		  (yyval.p) = new Parm((yyvsp[(1) - (3)].type),(yyvsp[(3) - (3)].id));
		  (yyval.p)->t->is_reference = 1;
		  (yyval.p)->call_type = 0;
		  (yyval.p)->t->is_pointer++;
		  (yyval.p)->defvalue = DefArg;
		  if (!CPlusPlus) {
			fprintf(stderr,"%s : Line %d. Warning.  Use of C++ Reference detected.  Use the -c++ option.\n", input_file, line_number);
		  }
		  delete (yyvsp[(1) - (3)].type);
		  delete (yyvsp[(3) - (3)].id);
		}
    break;

  case 128:

/* Line 1806 of yacc.c  */
#line 1973 "parser.y"
    {
                  fprintf(stderr,"%s : Line %d. Error. Function pointer not allowed (remap with typedef).\n", input_file, line_number);
		  FatalError();
		  (yyval.p) = new Parm((yyvsp[(1) - (8)].type),(yyvsp[(4) - (8)].id));
		  (yyval.p)->t->type = T_ERROR;
		  (yyval.p)->name = copy_string((yyvsp[(4) - (8)].id));
		  strcpy((yyval.p)->t->name,"<function ptr>");
		  delete (yyvsp[(1) - (8)].type);
		  delete (yyvsp[(4) - (8)].id);
		  delete (yyvsp[(7) - (8)].pl);
		}
    break;

  case 129:

/* Line 1806 of yacc.c  */
#line 1984 "parser.y"
    {
                  fprintf(stderr,"%s : Line %d. Variable length arguments not supported (ignored).\n", input_file, line_number);
		  (yyval.p) = new Parm(new DataType(T_INT),(char*)"varargs");
		  (yyval.p)->t->type = T_ERROR;
		  (yyval.p)->name = copy_string("varargs");
		  strcpy((yyval.p)->t->name,"<varargs>");
		  FatalError();
		}
    break;

  case 130:

/* Line 1806 of yacc.c  */
#line 1994 "parser.y"
    {
                    (yyval.id) = (yyvsp[(1) - (2)].id); 
                    InArray = 0;
		    if ((yyvsp[(2) - (2)].dtype).type == T_CHAR)
		      DefArg = copy_string(ConstChar);
		    else
		      DefArg = copy_string((yyvsp[(2) - (2)].dtype).id);
                    if ((yyvsp[(2) - (2)].dtype).id) delete (yyvsp[(2) - (2)].dtype).id;
                }
    break;

  case 131:

/* Line 1806 of yacc.c  */
#line 2003 "parser.y"
    {
                    (yyval.id) = (yyvsp[(1) - (2)].id); 
                    InArray = (yyvsp[(2) - (2)].ivalue); 
                    DefArg = 0;
               }
    break;

  case 132:

/* Line 1806 of yacc.c  */
#line 2008 "parser.y"
    {
                         (yyval.id) = new char[1];
                         (yyval.id)[0] = 0;
                         InArray = (yyvsp[(1) - (1)].ivalue);
                         DefArg = 0;
               }
    break;

  case 133:

/* Line 1806 of yacc.c  */
#line 2014 "parser.y"
    { (yyval.id) = new char[1];
	                 (yyval.id)[0] = 0;
                         InArray = 0;
                         DefArg = 0;
               }
    break;

  case 134:

/* Line 1806 of yacc.c  */
#line 2021 "parser.y"
    { (yyval.dtype) = (yyvsp[(2) - (2)].dtype); }
    break;

  case 135:

/* Line 1806 of yacc.c  */
#line 2022 "parser.y"
    {
		 (yyval.dtype).id = new char[strlen((yyvsp[(3) - (3)].id))+2];
		 (yyval.dtype).id[0] = '&';
		 strcpy(&(yyval.dtype).id[1], (yyvsp[(3) - (3)].id));
		 (yyval.dtype).type = T_USER;
	       }
    break;

  case 136:

/* Line 1806 of yacc.c  */
#line 2028 "parser.y"
    {
		 skip_brace();
		 (yyval.dtype).id = 0; (yyval.dtype).type = T_INT;
	       }
    break;

  case 137:

/* Line 1806 of yacc.c  */
#line 2032 "parser.y"
    {
               }
    break;

  case 138:

/* Line 1806 of yacc.c  */
#line 2034 "parser.y"
    {(yyval.dtype).id = 0; (yyval.dtype).type = T_INT;}
    break;

  case 139:

/* Line 1806 of yacc.c  */
#line 2037 "parser.y"
    { (yyval.ivalue) = CALL_VALUE; }
    break;

  case 140:

/* Line 1806 of yacc.c  */
#line 2038 "parser.y"
    { (yyval.ivalue) = CALL_OUTPUT; }
    break;

  case 141:

/* Line 1806 of yacc.c  */
#line 2041 "parser.y"
    {
                 (yyval.ivalue) = (yyvsp[(1) - (2)].ivalue) | (yyvsp[(2) - (2)].ivalue);
               }
    break;

  case 142:

/* Line 1806 of yacc.c  */
#line 2044 "parser.y"
    {
                 (yyval.ivalue) = (yyvsp[(1) - (1)].ivalue);
	       }
    break;

  case 143:

/* Line 1806 of yacc.c  */
#line 2051 "parser.y"
    { (yyval.decl).id = (yyvsp[(1) - (1)].id);
                      (yyval.decl).is_pointer = 0;
		      (yyval.decl).is_reference = 0;
                }
    break;

  case 144:

/* Line 1806 of yacc.c  */
#line 2055 "parser.y"
    {
                      (yyval.decl).id = (yyvsp[(2) - (2)].id);
		      (yyval.decl).is_pointer = (yyvsp[(1) - (2)].ivalue);
		      (yyval.decl).is_reference = 0;
	       }
    break;

  case 145:

/* Line 1806 of yacc.c  */
#line 2060 "parser.y"
    {
		      (yyval.decl).id = (yyvsp[(2) - (2)].id);
		      (yyval.decl).is_pointer = 1;
		      (yyval.decl).is_reference = 1;
		      if (!CPlusPlus) {
			fprintf(stderr,"%s : Line %d. Warning.  Use of C++ Reference detected.  Use the -c++ option.\n", input_file, line_number);
		      }
	       }
    break;

  case 146:

/* Line 1806 of yacc.c  */
#line 2070 "parser.y"
    { (yyval.ivalue) = 1; }
    break;

  case 147:

/* Line 1806 of yacc.c  */
#line 2071 "parser.y"
    { (yyval.ivalue) = (yyvsp[(2) - (2)].ivalue) + 1;}
    break;

  case 148:

/* Line 1806 of yacc.c  */
#line 2075 "parser.y"
    {
		 (yyval.ivalue) = (yyvsp[(3) - (3)].ivalue) + 1;
		 "[]" >> ArrayString;
              }
    break;

  case 149:

/* Line 1806 of yacc.c  */
#line 2079 "parser.y"
    {
                 (yyval.ivalue) = (yyvsp[(4) - (4)].ivalue) + 1;
		 "]" >> ArrayString;
		 (yyvsp[(2) - (4)].dtype).id >> ArrayString;
		 "[" >> ArrayString;
              }
    break;

  case 150:

/* Line 1806 of yacc.c  */
#line 2086 "parser.y"
    {
                 (yyval.ivalue) = (yyvsp[(1) - (1)].ivalue);
              }
    break;

  case 151:

/* Line 1806 of yacc.c  */
#line 2089 "parser.y"
    { (yyval.ivalue) = 0;
                        ArrayString = "";
              }
    break;

  case 152:

/* Line 1806 of yacc.c  */
#line 2097 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
               }
    break;

  case 153:

/* Line 1806 of yacc.c  */
#line 2100 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (2)].type);
	       }
    break;

  case 154:

/* Line 1806 of yacc.c  */
#line 2103 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (2)].type);
	       }
    break;

  case 155:

/* Line 1806 of yacc.c  */
#line 2106 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 156:

/* Line 1806 of yacc.c  */
#line 2109 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 157:

/* Line 1806 of yacc.c  */
#line 2112 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 158:

/* Line 1806 of yacc.c  */
#line 2115 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 159:

/* Line 1806 of yacc.c  */
#line 2118 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 160:

/* Line 1806 of yacc.c  */
#line 2121 "parser.y"
    {
                   if ((yyvsp[(2) - (2)].type)) (yyval.type) = (yyvsp[(2) - (2)].type);
		   else (yyval.type) = (yyvsp[(1) - (2)].type);
	       }
    break;

  case 161:

/* Line 1806 of yacc.c  */
#line 2125 "parser.y"
    {
                   if ((yyvsp[(2) - (2)].type)) (yyval.type) = (yyvsp[(2) - (2)].type);
		   else (yyval.type) = (yyvsp[(1) - (2)].type);
	       }
    break;

  case 162:

/* Line 1806 of yacc.c  */
#line 2129 "parser.y"
    {
		 (yyval.type) = (yyvsp[(1) - (2)].type);
		 if (strlen((yyvsp[(2) - (2)].id)) > 0) {
		    if ((strlen((yyvsp[(2) - (2)].id)) + strlen((yyval.type)->name)) >= MAX_NAME) {
		      fprintf(stderr,"%s : Line %d. Fatal error. Type-name is too long!\n", 
			      input_file, line_number);
		    } else {
		      strcat((yyval.type)->name,(yyvsp[(2) - (2)].id));
		    }
		  }
	       }
    break;

  case 163:

/* Line 1806 of yacc.c  */
#line 2140 "parser.y"
    {
		  (yyval.type) = new DataType;
		  strcpy((yyval.type)->name,(yyvsp[(1) - (2)].id));
		  (yyval.type)->type = T_USER;
		  /* Do a typedef lookup */
		  (yyval.type)->typedef_resolve();
		  if (strlen((yyvsp[(2) - (2)].id)) > 0) {
		    if ((strlen((yyvsp[(2) - (2)].id)) + strlen((yyval.type)->name)) >= MAX_NAME) {
		      fprintf(stderr,"%s : Line %d. Fatal error. Type-name is too long!\n", 
			      input_file, line_number);
		    } else {
		      strcat((yyval.type)->name,(yyvsp[(2) - (2)].id));
		    }
		  }
	       }
    break;

  case 164:

/* Line 1806 of yacc.c  */
#line 2155 "parser.y"
    {
		  (yyval.type) = (yyvsp[(2) - (2)].type);
                  (yyval.type)->qualifier = new char[6];
		  strcpy((yyval.type)->qualifier,"const");
     	       }
    break;

  case 165:

/* Line 1806 of yacc.c  */
#line 2160 "parser.y"
    {
                  (yyval.type) = new DataType;
		  sprintf((yyval.type)->name,"%s %s",(yyvsp[(1) - (2)].id), (yyvsp[(2) - (2)].id));
		  (yyval.type)->type = T_USER;
	       }
    break;

  case 166:

/* Line 1806 of yacc.c  */
#line 2165 "parser.y"
    {
                  (yyval.type) = new DataType;
                  sprintf((yyval.type)->name,"%s::%s",(yyvsp[(1) - (3)].id),(yyvsp[(3) - (3)].id));
                  (yyval.type)->type = T_USER;
		  (yyval.type)->typedef_resolve();
               }
    break;

  case 167:

/* Line 1806 of yacc.c  */
#line 2174 "parser.y"
    {
                  (yyval.type) = new DataType;
                  sprintf((yyval.type)->name,"%s", (yyvsp[(2) - (2)].id));
                  (yyval.type)->type = T_USER;
                  (yyval.type)->typedef_resolve(1);
               }
    break;

  case 168:

/* Line 1806 of yacc.c  */
#line 2180 "parser.y"
    {
                  (yyval.type) = new DataType;
                  sprintf((yyval.type)->name,"enum %s", (yyvsp[(2) - (2)].id));
                  (yyval.type)->type = T_INT;
                  (yyval.type)->typedef_resolve(1);
               }
    break;

  case 169:

/* Line 1806 of yacc.c  */
#line 2190 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
               }
    break;

  case 170:

/* Line 1806 of yacc.c  */
#line 2193 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (2)].type);
	       }
    break;

  case 171:

/* Line 1806 of yacc.c  */
#line 2196 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (2)].type);
	       }
    break;

  case 172:

/* Line 1806 of yacc.c  */
#line 2199 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 173:

/* Line 1806 of yacc.c  */
#line 2202 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 174:

/* Line 1806 of yacc.c  */
#line 2205 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 175:

/* Line 1806 of yacc.c  */
#line 2208 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 176:

/* Line 1806 of yacc.c  */
#line 2211 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
	       }
    break;

  case 177:

/* Line 1806 of yacc.c  */
#line 2214 "parser.y"
    {
                   if ((yyvsp[(2) - (2)].type)) (yyval.type) = (yyvsp[(2) - (2)].type);
		   else (yyval.type) = (yyvsp[(1) - (2)].type);
	       }
    break;

  case 178:

/* Line 1806 of yacc.c  */
#line 2218 "parser.y"
    {
                   if ((yyvsp[(2) - (2)].type)) (yyval.type) = (yyvsp[(2) - (2)].type);
		   else (yyval.type) = (yyvsp[(1) - (2)].type);
	       }
    break;

  case 179:

/* Line 1806 of yacc.c  */
#line 2222 "parser.y"
    {
		   (yyval.type) = (yyvsp[(1) - (2)].type);
		   strcat((yyval.type)->name,(yyvsp[(2) - (2)].id));
	       }
    break;

  case 180:

/* Line 1806 of yacc.c  */
#line 2226 "parser.y"
    {
		  (yyval.type) = (yyvsp[(2) - (2)].type);
                  (yyval.type)->qualifier = new char[6];
		  strcpy((yyval.type)->qualifier,"const");
     	       }
    break;

  case 181:

/* Line 1806 of yacc.c  */
#line 2231 "parser.y"
    {
                  (yyval.type) = new DataType;
		  sprintf((yyval.type)->name,"%s %s",(yyvsp[(1) - (2)].id), (yyvsp[(2) - (2)].id));
		  (yyval.type)->type = T_USER;
	       }
    break;

  case 182:

/* Line 1806 of yacc.c  */
#line 2240 "parser.y"
    {
                   (yyval.type) = (DataType *) 0;
               }
    break;

  case 183:

/* Line 1806 of yacc.c  */
#line 2243 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
		   (yyval.type)->type = T_INT;
		   sprintf(temp_name,"signed %s",(yyvsp[(1) - (1)].type)->name);
		   strcpy((yyval.type)->name,temp_name);
	       }
    break;

  case 184:

/* Line 1806 of yacc.c  */
#line 2249 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (2)].type);
		   (yyval.type)->type = T_SHORT;
		   sprintf(temp_name,"signed %s",(yyvsp[(1) - (2)].type)->name);
		   strcpy((yyval.type)->name,temp_name);
	       }
    break;

  case 185:

/* Line 1806 of yacc.c  */
#line 2255 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (2)].type);
		   (yyval.type)->type = T_LONG;
		   sprintf(temp_name,"signed %s",(yyvsp[(1) - (2)].type)->name);
		   strcpy((yyval.type)->name,temp_name);
	       }
    break;

  case 186:

/* Line 1806 of yacc.c  */
#line 2261 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
		   (yyval.type)->type = T_SCHAR;
		   sprintf(temp_name,"signed %s",(yyvsp[(1) - (1)].type)->name);
		   strcpy((yyval.type)->name,temp_name);
	       }
    break;

  case 187:

/* Line 1806 of yacc.c  */
#line 2271 "parser.y"
    {
                   (yyval.type) = (DataType *) 0;
               }
    break;

  case 188:

/* Line 1806 of yacc.c  */
#line 2274 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
		   (yyval.type)->type = T_UINT;
		   sprintf(temp_name,"unsigned %s",(yyvsp[(1) - (1)].type)->name);
		   strcpy((yyval.type)->name,temp_name);
	       }
    break;

  case 189:

/* Line 1806 of yacc.c  */
#line 2280 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (2)].type);
		   (yyval.type)->type = T_USHORT;
		   sprintf(temp_name,"unsigned %s",(yyvsp[(1) - (2)].type)->name);
		   strcpy((yyval.type)->name,temp_name);
	       }
    break;

  case 190:

/* Line 1806 of yacc.c  */
#line 2286 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (2)].type);
		   (yyval.type)->type = T_ULONG;
		   sprintf(temp_name,"unsigned %s",(yyvsp[(1) - (2)].type)->name);
		   strcpy((yyval.type)->name,temp_name);
	       }
    break;

  case 191:

/* Line 1806 of yacc.c  */
#line 2292 "parser.y"
    {
                   (yyval.type) = (yyvsp[(1) - (1)].type);
		   (yyval.type)->type = T_UCHAR;
		   sprintf(temp_name,"unsigned %s",(yyvsp[(1) - (1)].type)->name);
		   strcpy((yyval.type)->name,temp_name);
	       }
    break;

  case 192:

/* Line 1806 of yacc.c  */
#line 2300 "parser.y"
    { }
    break;

  case 193:

/* Line 1806 of yacc.c  */
#line 2301 "parser.y"
    { }
    break;

  case 194:

/* Line 1806 of yacc.c  */
#line 2304 "parser.y"
    { scanner_check_typedef(); }
    break;

  case 195:

/* Line 1806 of yacc.c  */
#line 2304 "parser.y"
    {
                   (yyval.dtype) = (yyvsp[(2) - (2)].dtype);
		   scanner_ignore_typedef();
		   if (ConstChar) delete ConstChar;
		   ConstChar = 0;
                }
    break;

  case 196:

/* Line 1806 of yacc.c  */
#line 2310 "parser.y"
    {
                   (yyval.dtype).id = (yyvsp[(1) - (1)].id);
                   (yyval.dtype).type = T_CHAR;
		   if (ConstChar) delete ConstChar;
		   ConstChar = new char[strlen((yyvsp[(1) - (1)].id))+3];
		   sprintf(ConstChar,"\"%s\"",(yyvsp[(1) - (1)].id));
		}
    break;

  case 197:

/* Line 1806 of yacc.c  */
#line 2317 "parser.y"
    {
                   (yyval.dtype).id = (yyvsp[(1) - (1)].id);
		   (yyval.dtype).type = T_CHAR;
		   if (ConstChar) delete ConstChar;
		   ConstChar = new char[strlen((yyvsp[(1) - (1)].id))+3];
		   sprintf(ConstChar,"'%s'",(yyvsp[(1) - (1)].id));
		 }
    break;

  case 198:

/* Line 1806 of yacc.c  */
#line 2329 "parser.y"
    {
                 (yyval.ilist) = (yyvsp[(1) - (3)].ilist);
		 (yyval.ilist).names[(yyval.ilist).count] = copy_string((yyvsp[(3) - (3)].id));
		 (yyval.ilist).count++;
		 (yyval.ilist).names[(yyval.ilist).count] = (char *) 0;
                }
    break;

  case 199:

/* Line 1806 of yacc.c  */
#line 2335 "parser.y"
    {
                 (yyval.ilist).names = new char *[NI_NAMES];
		 (yyval.ilist).count = 0;
		 for (i = 0; i < NI_NAMES; i++) 
		   (yyval.ilist).names[i] = (char *) 0;
	       }
    break;

  case 200:

/* Line 1806 of yacc.c  */
#line 2345 "parser.y"
    { (yyval.id) = (yyvsp[(1) - (1)].id); }
    break;

  case 201:

/* Line 1806 of yacc.c  */
#line 2346 "parser.y"
    { (yyval.id) = (char *) 0;}
    break;

  case 202:

/* Line 1806 of yacc.c  */
#line 2352 "parser.y"
    {}
    break;

  case 203:

/* Line 1806 of yacc.c  */
#line 2353 "parser.y"
    {}
    break;

  case 204:

/* Line 1806 of yacc.c  */
#line 2357 "parser.y"
    {
		   temp_typeptr = new DataType(T_INT);
		   create_constant((yyvsp[(1) - (1)].id), temp_typeptr, (yyvsp[(1) - (1)].id));
		   delete temp_typeptr;
		 }
    break;

  case 205:

/* Line 1806 of yacc.c  */
#line 2362 "parser.y"
    { scanner_check_typedef();}
    break;

  case 206:

/* Line 1806 of yacc.c  */
#line 2362 "parser.y"
    {
		   temp_typeptr = new DataType((yyvsp[(4) - (4)].dtype).type);
// Use enum name instead of value
// OLD		   create_constant($1, temp_typeptr, $4.id);
                   create_constant((yyvsp[(1) - (4)].id), temp_typeptr, (yyvsp[(1) - (4)].id));
		   delete temp_typeptr;
                 }
    break;

  case 207:

/* Line 1806 of yacc.c  */
#line 2369 "parser.y"
    { }
    break;

  case 208:

/* Line 1806 of yacc.c  */
#line 2370 "parser.y"
    { }
    break;

  case 209:

/* Line 1806 of yacc.c  */
#line 2373 "parser.y"
    {
                   (yyval.dtype) = (yyvsp[(1) - (1)].dtype);
		   if (((yyval.dtype).type != T_INT) && ((yyval.dtype).type != T_UINT) &&
		       ((yyval.dtype).type != T_LONG) && ((yyval.dtype).type != T_ULONG) &&
		       ((yyval.dtype).type != T_SHORT) && ((yyval.dtype).type != T_USHORT) && 
		       ((yyval.dtype).type != T_SCHAR) && ((yyval.dtype).type != T_UCHAR)) {
		     fprintf(stderr,"%s : Lind %d. Type error. Expecting an int\n",
			     input_file, line_number);
		     FatalError();
		   }

                }
    break;

  case 210:

/* Line 1806 of yacc.c  */
#line 2385 "parser.y"
    {
                   (yyval.dtype).id = (yyvsp[(1) - (1)].id);
		   (yyval.dtype).type = T_CHAR;
		 }
    break;

  case 211:

/* Line 1806 of yacc.c  */
#line 2396 "parser.y"
    { 
                  (yyval.dtype).id = (yyvsp[(1) - (1)].id);
                  (yyval.dtype).type = T_INT;
                 }
    break;

  case 212:

/* Line 1806 of yacc.c  */
#line 2400 "parser.y"
    {
                  (yyval.dtype).id = (yyvsp[(1) - (1)].id);
                  (yyval.dtype).type = T_DOUBLE;
               }
    break;

  case 213:

/* Line 1806 of yacc.c  */
#line 2404 "parser.y"
    {
                  (yyval.dtype).id = (yyvsp[(1) - (1)].id);
		  (yyval.dtype).type = T_UINT;
	       }
    break;

  case 214:

/* Line 1806 of yacc.c  */
#line 2408 "parser.y"
    {
                  (yyval.dtype).id = (yyvsp[(1) - (1)].id);
		  (yyval.dtype).type = T_LONG;
	       }
    break;

  case 215:

/* Line 1806 of yacc.c  */
#line 2412 "parser.y"
    {
                  (yyval.dtype).id = (yyvsp[(1) - (1)].id);
		  (yyval.dtype).type = T_ULONG;
	       }
    break;

  case 216:

/* Line 1806 of yacc.c  */
#line 2416 "parser.y"
    {
	          (yyval.dtype).id = new char[strlen((yyvsp[(3) - (4)].type)->name)+9];
		  sprintf((yyval.dtype).id,"sizeof(%s)", (yyvsp[(3) - (4)].type)->name);
		  (yyval.dtype).type = T_INT;
	       }
    break;

  case 217:

/* Line 1806 of yacc.c  */
#line 2421 "parser.y"
    {
		  (yyval.dtype).id = new char[strlen((yyvsp[(4) - (4)].dtype).id)+strlen((yyvsp[(2) - (4)].type)->name)+3];
		  sprintf((yyval.dtype).id,"(%s)%s",(yyvsp[(2) - (4)].type)->name,(yyvsp[(4) - (4)].dtype).id);
		  (yyval.dtype).type = (yyvsp[(2) - (4)].type)->type;
	       }
    break;

  case 218:

/* Line 1806 of yacc.c  */
#line 2426 "parser.y"
    {
		 (yyval.dtype).id = lookup_symvalue((yyvsp[(1) - (1)].id));
		 if ((yyval.dtype).id == (char *) 0)
		   (yyval.dtype).id = (yyvsp[(1) - (1)].id);
		 else {
		   (yyval.dtype).id = new char[strlen((yyval.dtype).id)+3];
		   sprintf((yyval.dtype).id,"(%s)",lookup_symvalue((yyvsp[(1) - (1)].id)));
		 }
		 temp_typeptr = lookup_symtype((yyvsp[(1) - (1)].id));
		 if (temp_typeptr) (yyval.dtype).type = temp_typeptr->type;
		 else (yyval.dtype).type = T_INT;
               }
    break;

  case 219:

/* Line 1806 of yacc.c  */
#line 2438 "parser.y"
    {
                  (yyval.dtype).id = new char[strlen((yyvsp[(1) - (3)].id))+strlen((yyvsp[(3) - (3)].id))+3];
		  sprintf((yyval.dtype).id,"%s::%s",(yyvsp[(1) - (3)].id),(yyvsp[(3) - (3)].id));
                  (yyval.dtype).type = T_INT;
		  delete (yyvsp[(1) - (3)].id);
		  delete (yyvsp[(3) - (3)].id);
               }
    break;

  case 220:

/* Line 1806 of yacc.c  */
#line 2445 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,"+");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;
	       }
    break;

  case 221:

/* Line 1806 of yacc.c  */
#line 2451 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,"-");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;
	       }
    break;

  case 222:

/* Line 1806 of yacc.c  */
#line 2457 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,"*");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;

	       }
    break;

  case 223:

/* Line 1806 of yacc.c  */
#line 2464 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,"/");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;

	       }
    break;

  case 224:

/* Line 1806 of yacc.c  */
#line 2471 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,"&");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 if (((yyvsp[(1) - (3)].dtype).type == T_DOUBLE) || ((yyvsp[(3) - (3)].dtype).type == T_DOUBLE)) {
		   fprintf(stderr,"%s : Line %d. Type error in constant expression (expecting integers).\n", input_file, line_number);
		   FatalError();
		 }
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;

	       }
    break;

  case 225:

/* Line 1806 of yacc.c  */
#line 2482 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,"|");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 if (((yyvsp[(1) - (3)].dtype).type == T_DOUBLE) || ((yyvsp[(3) - (3)].dtype).type == T_DOUBLE)) {
		   fprintf(stderr,"%s : Line %d. Type error in constant expression (expecting integers).\n", input_file, line_number);
		   FatalError();
		 }
		 (yyval.dtype).type = T_INT;
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;

	       }
    break;

  case 226:

/* Line 1806 of yacc.c  */
#line 2494 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,"^");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 if (((yyvsp[(1) - (3)].dtype).type == T_DOUBLE) || ((yyvsp[(3) - (3)].dtype).type == T_DOUBLE)) {
		   fprintf(stderr,"%s : Line %d. Type error in constant expression (expecting integers).\n", input_file, line_number);
		   FatalError();
		 }
		 (yyval.dtype).type = T_INT;
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;

	       }
    break;

  case 227:

/* Line 1806 of yacc.c  */
#line 2506 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,"<<");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 if (((yyvsp[(1) - (3)].dtype).type == T_DOUBLE) || ((yyvsp[(3) - (3)].dtype).type == T_DOUBLE)) {
		   fprintf(stderr,"%s : Line %d. Type error in constant expression (expecting integers).\n", input_file, line_number);
		   FatalError();
		 }
		 (yyval.dtype).type = T_INT;
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;

	       }
    break;

  case 228:

/* Line 1806 of yacc.c  */
#line 2518 "parser.y"
    {
	         E_BINARY((yyval.dtype).id,(yyvsp[(1) - (3)].dtype).id,(yyvsp[(3) - (3)].dtype).id,">>");
		 (yyval.dtype).type = promote((yyvsp[(1) - (3)].dtype).type,(yyvsp[(3) - (3)].dtype).type);
		 if (((yyvsp[(1) - (3)].dtype).type == T_DOUBLE) || ((yyvsp[(3) - (3)].dtype).type == T_DOUBLE)) {
		   fprintf(stderr,"%s : Line %d. Type error in constant expression (expecting integers).\n", input_file, line_number);
		   FatalError();
		 }
		 (yyval.dtype).type = T_INT;
		 delete (yyvsp[(1) - (3)].dtype).id;
		 delete (yyvsp[(3) - (3)].dtype).id;

	       }
    break;

  case 229:

/* Line 1806 of yacc.c  */
#line 2530 "parser.y"
    {
	          (yyval.dtype).id = new char[strlen((yyvsp[(2) - (2)].dtype).id)+2];
		  sprintf((yyval.dtype).id,"-%s",(yyvsp[(2) - (2)].dtype).id);
		  (yyval.dtype).type = (yyvsp[(2) - (2)].dtype).type;
		 delete (yyvsp[(2) - (2)].dtype).id;

	       }
    break;

  case 230:

/* Line 1806 of yacc.c  */
#line 2537 "parser.y"
    {
	          (yyval.dtype).id = new char[strlen((yyvsp[(2) - (2)].dtype).id)+2];
		  sprintf((yyval.dtype).id,"~%s",(yyvsp[(2) - (2)].dtype).id);
		  if ((yyvsp[(2) - (2)].dtype).type == T_DOUBLE) {
		   fprintf(stderr,"%s : Line %d. Type error in constant expression (expecting integers).\n", input_file, line_number);
		   FatalError();
		  }
		  (yyval.dtype).type = (yyvsp[(2) - (2)].dtype).type;
		  delete (yyvsp[(2) - (2)].dtype).id;
	       }
    break;

  case 231:

/* Line 1806 of yacc.c  */
#line 2547 "parser.y"
    {
	          (yyval.dtype).id = new char[strlen((yyvsp[(2) - (3)].dtype).id)+3];
	          sprintf((yyval.dtype).id,"(%s)", (yyvsp[(2) - (3)].dtype).id);
		  (yyval.dtype).type = (yyvsp[(2) - (3)].dtype).type;
		  delete (yyvsp[(2) - (3)].dtype).id;
	       }
    break;

  case 232:

/* Line 1806 of yacc.c  */
#line 2558 "parser.y"
    { }
    break;

  case 233:

/* Line 1806 of yacc.c  */
#line 2559 "parser.y"
    {}
    break;

  case 234:

/* Line 1806 of yacc.c  */
#line 2565 "parser.y"
    {
	       char *iname;
	       if (allow) {
		 init_language();
		 DataType::new_scope();

		 sprintf(temp_name,"CPP_CLASS:%s\n",(yyvsp[(3) - (5)].id));
		 if (add_symbol(temp_name, (DataType *) 0, (char *) 0)) {
		   fprintf(stderr,"%s : Line %d. Error. %s %s is multiply defined.\n", input_file, line_number, (yyvsp[(2) - (5)].id), (yyvsp[(3) - (5)].id));
		   FatalError();
		 }
		 if ((!CPlusPlus) && (strcmp((yyvsp[(2) - (5)].id),"class") == 0))
		   fprintf(stderr,"%s : Line %d. *** WARNING ***. C++ mode is disabled (enable using -c++)\n", input_file, line_number);

		 iname = make_name((yyvsp[(3) - (5)].id));
		 doc_entry = new DocClass(iname, doc_parent());
		 if (iname == (yyvsp[(3) - (5)].id)) 
		   cplus_open_class((yyvsp[(3) - (5)].id), 0, (yyvsp[(2) - (5)].id));
		 else
		   cplus_open_class((yyvsp[(3) - (5)].id), iname, (yyvsp[(2) - (5)].id));
		 if (strcmp((yyvsp[(2) - (5)].id),"class") == 0)
		   cplus_mode = CPLUS_PRIVATE;
		 else
		   cplus_mode = CPLUS_PUBLIC;
		 doc_stack_top++;
		 doc_stack[doc_stack_top] = doc_entry;
		 scanner_clear_start();
		 nested_list = 0;
		 // Merge in scope from base classes
		 cplus_inherit_scope((yyvsp[(4) - (5)].ilist).count,(yyvsp[(4) - (5)].ilist).names);
	       }
              }
    break;

  case 235:

/* Line 1806 of yacc.c  */
#line 2596 "parser.y"
    {
		if (allow) {
		  if ((yyvsp[(4) - (8)].ilist).names) {
		    if (strcmp((yyvsp[(2) - (8)].id),"union") != 0)
		      cplus_inherit((yyvsp[(4) - (8)].ilist).count, (yyvsp[(4) - (8)].ilist).names);
		    else {
		      fprintf(stderr,"%s : Line %d.  Inheritance not allowed for unions.\n",input_file, line_number);
		      FatalError();
		    }
		  }
		  // Clean up the inheritance list
		  if ((yyvsp[(4) - (8)].ilist).names) {
		    int j;
		    for (j = 0; j < (yyvsp[(4) - (8)].ilist).count; j++) {
		      if ((yyvsp[(4) - (8)].ilist).names[j]) delete [] (yyvsp[(4) - (8)].ilist).names[j];
		    }
		    delete [] (yyvsp[(4) - (8)].ilist).names;
		  }

		  // Dumped nested declarations (if applicable)
		  dump_nested((yyvsp[(3) - (8)].id));

		  // Save and collapse current scope
		  cplus_register_scope(DataType::collapse_scope((yyvsp[(3) - (8)].id)));

		  // Restore the original doc entry for this class
		  doc_entry = doc_stack[doc_stack_top];
		  cplus_class_close((char *) 0); 
		  doc_entry = 0;
		  // Bump the documentation stack back down
		  doc_stack_top--;
		  cplus_mode = CPLUS_PUBLIC;
		}
	      }
    break;

  case 236:

/* Line 1806 of yacc.c  */
#line 2633 "parser.y"
    {
	       if (allow) {
		 char *iname;
		 init_language();
		 DataType::new_scope();

		 sprintf(temp_name,"CPP_CLASS:%s\n",(yyvsp[(3) - (5)].id));
		 if (add_symbol(temp_name, (DataType *) 0, (char *) 0)) {
		   fprintf(stderr,"%s : Line %d. Error. %s %s is multiply defined.\n", input_file, line_number, (yyvsp[(2) - (5)].id), (yyvsp[(3) - (5)].id));
		   FatalError();
		 }
		 if ((!CPlusPlus) && (strcmp((yyvsp[(2) - (5)].id),"class") == 0))
		   fprintf(stderr,"%s : Line %d. *** WARNING ***. C++ mode is disabled (enable using -c++)\n", input_file, line_number);
		 
		 iname = make_name((yyvsp[(3) - (5)].id));
		 doc_entry = new DocClass(iname, doc_parent());
		 if ((yyvsp[(3) - (5)].id) == iname) 
		   cplus_open_class((yyvsp[(3) - (5)].id), 0, (yyvsp[(2) - (5)].id));
		 else
		   cplus_open_class((yyvsp[(3) - (5)].id), iname, (yyvsp[(2) - (5)].id));
		 if (strcmp((yyvsp[(2) - (5)].id),"class") == 0)
		   cplus_mode = CPLUS_PRIVATE;
		 else
		   cplus_mode = CPLUS_PUBLIC;
		 // Create a documentation entry for the class
		 doc_stack_top++;
		 doc_stack[doc_stack_top] = doc_entry;
		 scanner_clear_start();
		 nested_list = 0;

		 // Merge in scope from base classes
		 cplus_inherit_scope((yyvsp[(4) - (5)].ilist).count,(yyvsp[(4) - (5)].ilist).names);

	       }
              }
    break;

  case 237:

/* Line 1806 of yacc.c  */
#line 2667 "parser.y"
    {
		if (allow) {
		  if ((yyvsp[(4) - (9)].ilist).names) {
		    if (strcmp((yyvsp[(2) - (9)].id),"union") != 0)
		      cplus_inherit((yyvsp[(4) - (9)].ilist).count, (yyvsp[(4) - (9)].ilist).names);
		    else {
		      fprintf(stderr,"%s : Line %d.  Inheritance not allowed for unions.\n",input_file, line_number);
		      FatalError();
		    }
		  }
		  // Create a datatype for correctly processing the typedef
		  Active_typedef = new DataType();
		  Active_typedef->type = T_USER;
		  sprintf(Active_typedef->name,"%s %s", (yyvsp[(2) - (9)].id),(yyvsp[(3) - (9)].id));
		  Active_typedef->is_pointer = 0;
		  Active_typedef->implicit_ptr = 0;

		  // Clean up the inheritance list
		  if ((yyvsp[(4) - (9)].ilist).names) {
		    int j;
		    for (j = 0; j < (yyvsp[(4) - (9)].ilist).count; j++) {
		      if ((yyvsp[(4) - (9)].ilist).names[j]) delete [] (yyvsp[(4) - (9)].ilist).names[j];
		    }
		    delete [] (yyvsp[(4) - (9)].ilist).names;
		  }

		  if ((yyvsp[(9) - (9)].decl).is_pointer > 0) {
		    fprintf(stderr,"%s : Line %d.  typedef struct { } *id not supported properly. Winging it...\n", input_file, line_number);

		  }
		  // Create dump nested class code
		  if ((yyvsp[(9) - (9)].decl).is_pointer > 0) {
		    dump_nested((yyvsp[(3) - (9)].id));
		  } else {
		    dump_nested((yyvsp[(9) - (9)].decl).id);
		  }
		    
		  // Collapse any datatypes created in the the class

		  cplus_register_scope(DataType::collapse_scope((yyvsp[(3) - (9)].id)));

		  doc_entry = doc_stack[doc_stack_top];
		  if ((yyvsp[(9) - (9)].decl).is_pointer > 0) {
		    cplus_class_close((yyvsp[(3) - (9)].id));
		  } else {
		    cplus_class_close((yyvsp[(9) - (9)].decl).id); 
		  }
		  doc_stack_top--;
		  doc_entry = 0;

		  // Create a typedef in global scope

		  if ((yyvsp[(9) - (9)].decl).is_pointer == 0)
		    Active_typedef->typedef_add((yyvsp[(9) - (9)].decl).id);
		  else {
		    DataType *t = new DataType(Active_typedef);
		    t->is_pointer += (yyvsp[(9) - (9)].decl).is_pointer;
		    t->typedef_add((yyvsp[(9) - (9)].decl).id);
		    cplus_register_type((yyvsp[(9) - (9)].decl).id);
		    delete t;
		  }
		  cplus_mode = CPLUS_PUBLIC;
		}
	      }
    break;

  case 238:

/* Line 1806 of yacc.c  */
#line 2730 "parser.y"
    { }
    break;

  case 239:

/* Line 1806 of yacc.c  */
#line 2734 "parser.y"
    {
	       char *iname;
	       if (allow) {
		 init_language();
		 DataType::new_scope();
		 if ((!CPlusPlus) && (strcmp((yyvsp[(2) - (3)].id),"class") == 0))
		   fprintf(stderr,"%s : Line %d. *** WARNING ***. C++ mode is disabled (enable using -c++)\n", input_file, line_number);
		 
		 iname = make_name((char*)"");
		 doc_entry = new DocClass(iname,doc_parent());
		 if (strlen(iname))
		   cplus_open_class("", iname, (yyvsp[(2) - (3)].id));
		 else
		   cplus_open_class("",0,(yyvsp[(2) - (3)].id));
		 if (strcmp((yyvsp[(2) - (3)].id),"class") == 0)
		   cplus_mode = CPLUS_PRIVATE;
		 else
		   cplus_mode = CPLUS_PUBLIC;
		 doc_stack_top++;
		 doc_stack[doc_stack_top] = doc_entry;
		 scanner_clear_start();
		 nested_list = 0;
	       }
              }
    break;

  case 240:

/* Line 1806 of yacc.c  */
#line 2757 "parser.y"
    {
		if (allow) {
		  if ((yyvsp[(7) - (7)].decl).is_pointer > 0) {
		    fprintf(stderr,"%s : Line %d. typedef %s {} *%s not supported correctly. Will be ignored.\n", input_file, line_number, (yyvsp[(2) - (7)].id), (yyvsp[(7) - (7)].decl).id);
		    cplus_abort();
		  } else {
		    sprintf(temp_name,"CPP_CLASS:%s\n",(yyvsp[(7) - (7)].decl).id);
		    if (add_symbol(temp_name, (DataType *) 0, (char *) 0)) {
		      fprintf(stderr,"%s : Line %d. Error. %s %s is multiply defined.\n", input_file, line_number, (yyvsp[(2) - (7)].id), (yyvsp[(7) - (7)].decl).id);
		      FatalError();
		    }
		  }
		  // Create a datatype for correctly processing the typedef
		  Active_typedef = new DataType();
		  Active_typedef->type = T_USER;
		  sprintf(Active_typedef->name,"%s",(yyvsp[(7) - (7)].decl).id);
		  Active_typedef->is_pointer = 0;
		  Active_typedef->implicit_ptr = 0;
		  
		  // Dump nested classes
		  if ((yyvsp[(7) - (7)].decl).is_pointer == 0)  
		    dump_nested((yyvsp[(7) - (7)].decl).id);

		  // Go back to previous scope

		  cplus_register_scope(DataType::collapse_scope((char *) 0));
		  
		  doc_entry = doc_stack[doc_stack_top];
		  // Change name of doc_entry
		  doc_entry->name = copy_string((yyvsp[(7) - (7)].decl).id);
		  if ((yyvsp[(7) - (7)].decl).is_pointer == 0) 
		    cplus_class_close((yyvsp[(7) - (7)].decl).id); 
		  doc_entry = 0;
		  doc_stack_top--;
		  cplus_mode = CPLUS_PUBLIC;
		}
	      }
    break;

  case 241:

/* Line 1806 of yacc.c  */
#line 2793 "parser.y"
    { }
    break;

  case 242:

/* Line 1806 of yacc.c  */
#line 2798 "parser.y"
    {
	       char *iname;
		 if (allow) {
		   init_language();
		   iname = make_name((yyvsp[(3) - (4)].id));
		   lang->cpp_class_decl((yyvsp[(3) - (4)].id),iname,(yyvsp[(2) - (4)].id));
		 }
	     }
    break;

  case 243:

/* Line 1806 of yacc.c  */
#line 2809 "parser.y"
    {
	       if (allow) {
		 init_language();
		 if (!CPlusPlus) 
		   fprintf(stderr,"%s : Line %d. *** WARNING ***. C++ mode is disabled (enable using -c++)\n", input_file, line_number);
		 
		 (yyvsp[(2) - (9)].type)->is_pointer += (yyvsp[(3) - (9)].decl).is_pointer;
		 (yyvsp[(2) - (9)].type)->is_reference = (yyvsp[(3) - (9)].decl).is_reference;
		 // Fix up the function name
		 sprintf(temp_name,"%s::%s",(yyvsp[(3) - (9)].decl).id,(yyvsp[(5) - (9)].id));
		 if (!Rename_true) {
		   Rename_true = 1;
		   sprintf(yy_rename,"%s_%s",(yyvsp[(3) - (9)].decl).id,(yyvsp[(5) - (9)].id));
		 }
		 create_function((yyvsp[(1) - (9)].ivalue), temp_name, (yyvsp[(2) - (9)].type), (yyvsp[(7) - (9)].pl));
	       }
	       delete (yyvsp[(2) - (9)].type);
	       delete (yyvsp[(7) - (9)].pl);
	      }
    break;

  case 244:

/* Line 1806 of yacc.c  */
#line 2830 "parser.y"
    {
	       if (allow) {
		 init_language();
		 if (!CPlusPlus) 
		   fprintf(stderr,"%s : Line %d. *** WARNING ***. C++ mode is disabled (enable using -c++)\n", input_file, line_number);

		 (yyvsp[(2) - (6)].type)->is_pointer += (yyvsp[(3) - (6)].decl).is_pointer;
		 // Fix up the function name
		 sprintf(temp_name,"%s::%s",(yyvsp[(3) - (6)].decl).id,(yyvsp[(5) - (6)].id));
		 if (!Rename_true) {
		   Rename_true = 1;
		   sprintf(yy_rename,"%s_%s",(yyvsp[(3) - (6)].decl).id,(yyvsp[(5) - (6)].id));
		 }
		 create_variable((yyvsp[(1) - (6)].ivalue),temp_name, (yyvsp[(2) - (6)].type));
	       }
	       delete (yyvsp[(2) - (6)].type);
	     }
    break;

  case 245:

/* Line 1806 of yacc.c  */
#line 2850 "parser.y"
    {
	       fprintf(stderr,"%s : Line %d. Operator overloading not supported (ignored).\n", input_file, line_number);
		skip_decl();
		delete (yyvsp[(2) - (5)].type);
	     }
    break;

  case 246:

/* Line 1806 of yacc.c  */
#line 2858 "parser.y"
    {
	       fprintf(stderr,"%s : Line %d. Templates not currently supported (ignored).\n",
		       input_file, line_number);
	       skip_decl();
	     }
    break;

  case 247:

/* Line 1806 of yacc.c  */
#line 2866 "parser.y"
    {
	       cplus_mode = CPLUS_PUBLIC;
               doc_entry = cplus_set_class((yyvsp[(2) - (3)].id));
	       if (!doc_entry) {
		 doc_entry = new DocClass((yyvsp[(2) - (3)].id),doc_parent());
	       };
	       doc_stack_top++;
	       doc_stack[doc_stack_top] = doc_entry;
	       scanner_clear_start();
	       AddMethods = 1;
	     }
    break;

  case 248:

/* Line 1806 of yacc.c  */
#line 2876 "parser.y"
    {
	       cplus_unset_class();
	       doc_entry = 0;
	       doc_stack_top--;
	       AddMethods = 0;
	     }
    break;

  case 249:

/* Line 1806 of yacc.c  */
#line 2884 "parser.y"
    { }
    break;

  case 250:

/* Line 1806 of yacc.c  */
#line 2885 "parser.y"
    { }
    break;

  case 251:

/* Line 1806 of yacc.c  */
#line 2886 "parser.y"
    { }
    break;

  case 252:

/* Line 1806 of yacc.c  */
#line 2889 "parser.y"
    {}
    break;

  case 253:

/* Line 1806 of yacc.c  */
#line 2890 "parser.y"
    {
	           AddMethods = 1;
	     }
    break;

  case 254:

/* Line 1806 of yacc.c  */
#line 2892 "parser.y"
    {
	           AddMethods = 0;
	     }
    break;

  case 255:

/* Line 1806 of yacc.c  */
#line 2894 "parser.y"
    { }
    break;

  case 256:

/* Line 1806 of yacc.c  */
#line 2895 "parser.y"
    {
	       skip_decl();
		   {
		     static int last_error_line = -1;
		     if (last_error_line != line_number) {
		       fprintf(stderr,"%s : Line %d. Syntax error in input.\n", input_file, line_number);
		       FatalError();
		       last_error_line = line_number;
		     }
		   }
	     }
    break;

  case 257:

/* Line 1806 of yacc.c  */
#line 2905 "parser.y"
    { }
    break;

  case 258:

/* Line 1806 of yacc.c  */
#line 2906 "parser.y"
    { }
    break;

  case 259:

/* Line 1806 of yacc.c  */
#line 2909 "parser.y"
    {
                char *iname;
                if (allow) {
		  init_language();
		  if (cplus_mode == CPLUS_PUBLIC) {
		    Stat_func++;
		    (yyvsp[(1) - (6)].type)->is_pointer += (yyvsp[(2) - (6)].decl).is_pointer;
		    (yyvsp[(1) - (6)].type)->is_reference = (yyvsp[(2) - (6)].decl).is_reference;
		    if (Verbose) {
		      fprintf(stderr,"Wrapping member function : %s\n",(yyvsp[(2) - (6)].decl).id);
		    }
		    iname = make_name((yyvsp[(2) - (6)].decl).id);
		    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		    if (iname == (yyvsp[(2) - (6)].decl).id) iname = 0;
		    cplus_member_func((yyvsp[(2) - (6)].decl).id, iname, (yyvsp[(1) - (6)].type),(yyvsp[(4) - (6)].pl),0);
		  }
		  scanner_clear_start();
		}
		delete (yyvsp[(1) - (6)].type);
		delete (yyvsp[(4) - (6)].pl);
              }
    break;

  case 260:

/* Line 1806 of yacc.c  */
#line 2933 "parser.y"
    {
	       char *iname;
	       if (allow) {
		 init_language();
		 if (cplus_mode == CPLUS_PUBLIC) {
		   Stat_func++;
		   (yyvsp[(2) - (7)].type)->is_pointer += (yyvsp[(3) - (7)].decl).is_pointer;
		   (yyvsp[(2) - (7)].type)->is_reference = (yyvsp[(3) - (7)].decl).is_reference;
		   if (Verbose) {
		     fprintf(stderr,"Wrapping virtual member function : %s\n",(yyvsp[(3) - (7)].decl).id);
		   }
		   iname = make_name((yyvsp[(3) - (7)].decl).id);
		   doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		   if (iname == (yyvsp[(3) - (7)].decl).id) iname = 0;
		   cplus_member_func((yyvsp[(3) - (7)].decl).id,iname,(yyvsp[(2) - (7)].type),(yyvsp[(5) - (7)].pl),1);
		 }
		 scanner_clear_start();
	       }
	       delete (yyvsp[(2) - (7)].type);
	       delete (yyvsp[(5) - (7)].pl);
	     }
    break;

  case 261:

/* Line 1806 of yacc.c  */
#line 2956 "parser.y"
    {
		char *iname;
		if (allow) {
		  init_language();
		  if (cplus_mode == CPLUS_PUBLIC) {
		    Stat_func++;
		    if (Verbose) {
		      fprintf(stderr,"Wrapping C++ constructor %s\n", (yyvsp[(1) - (5)].id));
		    }
		    iname = make_name((yyvsp[(1) - (5)].id));
		    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		    if (iname == (yyvsp[(1) - (5)].id)) iname = 0;
		    cplus_constructor((yyvsp[(1) - (5)].id),iname, (yyvsp[(3) - (5)].pl));
		  }
		  scanner_clear_start();
		}
		delete (yyvsp[(3) - (5)].pl);
	      }
    break;

  case 262:

/* Line 1806 of yacc.c  */
#line 2977 "parser.y"
    {
		char *iname;
		if (allow) {
		  init_language();
		  if (cplus_mode == CPLUS_PUBLIC) {
		    Stat_func++;
		    if (Verbose) {
		      fprintf(stderr,"Wrapping C++ destructor %s\n", (yyvsp[(2) - (6)].id));
		    }
		    iname = make_name((yyvsp[(2) - (6)].id));
		    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		    if (iname == (yyvsp[(2) - (6)].id)) iname = 0;
		    cplus_destructor((yyvsp[(2) - (6)].id),iname);
		  }
		}
		scanner_clear_start();
	      }
    break;

  case 263:

/* Line 1806 of yacc.c  */
#line 2997 "parser.y"
    {
 	        char *iname;
		if (allow) {
		  init_language();
		  if (cplus_mode == CPLUS_PUBLIC) {
		    Stat_func++;
		    if (Verbose) {
		      fprintf(stderr,"Wrapping C++ destructor %s\n", (yyvsp[(3) - (6)].id));
		    }
		    iname = make_name((yyvsp[(3) - (6)].id));
		    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		    if (iname == (yyvsp[(3) - (6)].id)) iname = 0;
		    cplus_destructor((yyvsp[(3) - (6)].id),iname);
		  }
		}
		scanner_clear_start();
	      }
    break;

  case 264:

/* Line 1806 of yacc.c  */
#line 3017 "parser.y"
    {
		if (allow) {
		  char *iname;
		  init_language();
		  if (cplus_mode == CPLUS_PUBLIC) {
		    if (Active_type) delete Active_type;
		    Active_type = new DataType((yyvsp[(1) - (3)].type));
		    (yyvsp[(1) - (3)].type)->is_pointer += (yyvsp[(2) - (3)].decl).is_pointer;
		    (yyvsp[(1) - (3)].type)->is_reference = (yyvsp[(2) - (3)].decl).is_reference;
		    if ((yyvsp[(1) - (3)].type)->qualifier) {
		      if ((strcmp((yyvsp[(1) - (3)].type)->qualifier,"const") == 0) && ((yyvsp[(1) - (3)].type)->is_pointer == 0)) {
			// Okay.  This is really some sort of C++ constant here.
	  	          if ((yyvsp[(3) - (3)].dtype).type != T_ERROR) {
			    iname = make_name((yyvsp[(2) - (3)].decl).id);
			    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
			    if (iname == (yyvsp[(2) - (3)].decl).id) iname = 0;
			    cplus_declare_const((yyvsp[(2) - (3)].decl).id,iname, (yyvsp[(1) - (3)].type), (yyvsp[(3) - (3)].dtype).id);
			  }
		      } else {
			int oldstatus = Status;
			char *tm;
			if ((yyvsp[(1) - (3)].type)->status & STAT_READONLY) {
			  if (!(tm = typemap_lookup("memberin",typemap_lang,(yyvsp[(1) - (3)].type),(yyvsp[(2) - (3)].decl).id,"",""))) 
			    Status = Status | STAT_READONLY;
			}
			iname = make_name((yyvsp[(2) - (3)].decl).id);
			doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
			if (iname == (yyvsp[(2) - (3)].decl).id) iname = 0;
			cplus_variable((yyvsp[(2) - (3)].decl).id,iname,(yyvsp[(1) - (3)].type));
			Status = oldstatus;
		      }
		    } else {
		      char *tm = 0;
		      int oldstatus = Status;
		      if ((yyvsp[(1) - (3)].type)->status & STAT_READONLY) {
			if (!(tm = typemap_lookup("memberin",typemap_lang,(yyvsp[(1) - (3)].type),(yyvsp[(2) - (3)].decl).id,"",""))) 
			  Status = Status | STAT_READONLY;
		      }
		      iname = make_name((yyvsp[(2) - (3)].decl).id);
		      doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		      if (iname == (yyvsp[(2) - (3)].decl).id) iname = 0;
		      cplus_variable((yyvsp[(2) - (3)].decl).id,iname,(yyvsp[(1) - (3)].type));
		      Status = oldstatus;
		      if (Verbose) {
			fprintf(stderr,"Wrapping member data %s\n", (yyvsp[(2) - (3)].decl).id);
		      }
		    }
		  }
		  scanner_clear_start();
		}
		delete (yyvsp[(1) - (3)].type);
	      }
    break;

  case 265:

/* Line 1806 of yacc.c  */
#line 3068 "parser.y"
    { }
    break;

  case 266:

/* Line 1806 of yacc.c  */
#line 3070 "parser.y"
    {
		char *iname;
		if (allow) {
		  int oldstatus = Status;
		  char *tm = 0;
		  init_language();
		  if (cplus_mode == CPLUS_PUBLIC) {
		    if (Active_type) delete Active_type;
		    Active_type = new DataType((yyvsp[(1) - (4)].type));
		    (yyvsp[(1) - (4)].type)->is_pointer += (yyvsp[(2) - (4)].decl).is_pointer + 1;
		    (yyvsp[(1) - (4)].type)->is_reference = (yyvsp[(2) - (4)].decl).is_reference;
		    (yyvsp[(1) - (4)].type)->arraystr = copy_string(ArrayString);
		    if (!(tm = typemap_lookup("memberin",typemap_lang,(yyvsp[(1) - (4)].type),(yyvsp[(2) - (4)].decl).id,"",""))) 
		      Status = STAT_READONLY;

		    iname = make_name((yyvsp[(2) - (4)].decl).id);
		    doc_entry = new DocDecl(iname, doc_stack[doc_stack_top]);
		    if (iname == (yyvsp[(2) - (4)].decl).id) iname = 0;
		    cplus_variable((yyvsp[(2) - (4)].decl).id,iname,(yyvsp[(1) - (4)].type));
		    Status = oldstatus;
		    if (!tm)
		      fprintf(stderr,"%s : Line %d. Warning. Array member will be read-only.\n",input_file,line_number);
		  }
		scanner_clear_start();
		}
		delete (yyvsp[(1) - (4)].type);
	      }
    break;

  case 267:

/* Line 1806 of yacc.c  */
#line 3101 "parser.y"
    {
		char *iname;
		if (allow) {
		  init_language();
		  if (cplus_mode == CPLUS_PUBLIC) {
		    (yyvsp[(2) - (3)].type)->is_pointer += (yyvsp[(3) - (3)].decl).is_pointer;
		    iname = make_name((yyvsp[(3) - (3)].decl).id);
		    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		    if (iname == (yyvsp[(3) - (3)].decl).id) iname = 0;
		    cplus_static_var((yyvsp[(3) - (3)].decl).id,iname,(yyvsp[(2) - (3)].type));
		    if (Active_type) delete Active_type;
		    Active_type = new DataType((yyvsp[(2) - (3)].type));
		    if (Verbose) {
		      fprintf(stderr,"Wrapping static member data %s\n", (yyvsp[(3) - (3)].decl).id);
		    }
		  }
		  scanner_clear_start();
		}
		delete (yyvsp[(2) - (3)].type);
	      }
    break;

  case 268:

/* Line 1806 of yacc.c  */
#line 3120 "parser.y"
    { }
    break;

  case 269:

/* Line 1806 of yacc.c  */
#line 3124 "parser.y"
    {
		char *iname;
		if (allow) {
		  (yyvsp[(2) - (7)].type)->is_pointer += (yyvsp[(3) - (7)].decl).is_pointer;
		  (yyvsp[(2) - (7)].type)->is_reference = (yyvsp[(3) - (7)].decl).is_reference;
		  if (cplus_mode == CPLUS_PUBLIC) {
		    iname = make_name((yyvsp[(3) - (7)].decl).id);
		    doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		    if (iname == (yyvsp[(3) - (7)].decl).id) iname = 0;
		    cplus_static_func((yyvsp[(3) - (7)].decl).id, iname, (yyvsp[(2) - (7)].type), (yyvsp[(5) - (7)].pl));
		    if (Verbose)
		      fprintf(stderr,"Wrapping static member function %s\n",(yyvsp[(3) - (7)].decl).id);
		  }
		  scanner_clear_start();
		}
		delete (yyvsp[(2) - (7)].type);
		delete (yyvsp[(5) - (7)].pl);
	      }
    break;

  case 270:

/* Line 1806 of yacc.c  */
#line 3144 "parser.y"
    {
		if (allow) {
		  cplus_mode = CPLUS_PUBLIC;
		  if (Verbose)
		    fprintf(stderr,"Public mode\n");
		  scanner_clear_start();
		}
	      }
    break;

  case 271:

/* Line 1806 of yacc.c  */
#line 3155 "parser.y"
    {
		if (allow) {
		  cplus_mode = CPLUS_PRIVATE;
		  if (Verbose)
		    fprintf(stderr,"Private mode\n");
		  scanner_clear_start();
		}
	      }
    break;

  case 272:

/* Line 1806 of yacc.c  */
#line 3166 "parser.y"
    {
		if (allow) {
		  cplus_mode = CPLUS_PROTECTED;
		  if (Verbose)
		    fprintf(stderr,"Protected mode\n");
		  scanner_clear_start();
		}
	      }
    break;

  case 273:

/* Line 1806 of yacc.c  */
#line 3177 "parser.y"
    {
	       if (allow) {
		 strcpy(yy_rename,(yyvsp[(3) - (4)].id));
		 Rename_true = 1;
	       }
	     }
    break;

  case 274:

/* Line 1806 of yacc.c  */
#line 3185 "parser.y"
    {
                 NewObject = 1;
             }
    break;

  case 275:

/* Line 1806 of yacc.c  */
#line 3187 "parser.y"
    {
                 NewObject = 0;
             }
    break;

  case 276:

/* Line 1806 of yacc.c  */
#line 3192 "parser.y"
    {scanner_clear_start();}
    break;

  case 277:

/* Line 1806 of yacc.c  */
#line 3192 "parser.y"
    {

		 // if ename was supplied.  Install it as a new integer datatype.

		if (allow) {
		  init_language();
		  if (cplus_mode == CPLUS_PUBLIC) {
		   if ((yyvsp[(2) - (7)].id)) {
		     cplus_register_type((yyvsp[(2) - (7)].id));
		     temp_type.type = T_INT;
		     temp_type.is_pointer = 0;
		     temp_type.implicit_ptr = 0;
		     sprintf(temp_type.name,"int");
		     temp_type.typedef_add((yyvsp[(2) - (7)].id),1); 
		   }
		 }
	       }
	      }
    break;

  case 278:

/* Line 1806 of yacc.c  */
#line 3210 "parser.y"
    {
		if (allow)
		  Status = Status | STAT_READONLY;
		scanner_clear_start();
              }
    break;

  case 279:

/* Line 1806 of yacc.c  */
#line 3215 "parser.y"
    {
		if (allow) 
		  Status = Status & ~(STAT_READONLY);
		scanner_clear_start();
	      }
    break;

  case 280:

/* Line 1806 of yacc.c  */
#line 3221 "parser.y"
    {
		if (allow)
		  fprintf(stderr,"%s : Line %d. Friends are not allowed--members only! (ignored)\n", input_file, line_number);
		skip_decl();
		scanner_clear_start();
	      }
    break;

  case 281:

/* Line 1806 of yacc.c  */
#line 3229 "parser.y"
    {
		if (allow)
		  fprintf(stderr,"%s : Line %d. Operator overloading not supported (ignored).\n", input_file, line_number);
		skip_decl();
		scanner_clear_start();
	      }
    break;

  case 282:

/* Line 1806 of yacc.c  */
#line 3235 "parser.y"
    { 
		scanner_clear_start();
	      }
    break;

  case 283:

/* Line 1806 of yacc.c  */
#line 3240 "parser.y"
    { }
    break;

  case 284:

/* Line 1806 of yacc.c  */
#line 3244 "parser.y"
    {
	      		scanner_clear_start();
	      }
    break;

  case 285:

/* Line 1806 of yacc.c  */
#line 3249 "parser.y"
    {
                 if (allow && (!WrapExtern)) { }
    	       }
    break;

  case 286:

/* Line 1806 of yacc.c  */
#line 3252 "parser.y"
    {
		 if (allow && (!WrapExtern))
                   cplus_add_pragma((yyvsp[(3) - (6)].id),(yyvsp[(5) - (6)].id),(yyvsp[(6) - (6)].id));
	       }
    break;

  case 287:

/* Line 1806 of yacc.c  */
#line 3275 "parser.y"
    { start_line = line_number; skip_brace(); 
	      }
    break;

  case 288:

/* Line 1806 of yacc.c  */
#line 3276 "parser.y"
    { 

		if (cplus_mode == CPLUS_PUBLIC) {
		  cplus_register_type((yyvsp[(2) - (6)].id));
		  if ((yyvsp[(5) - (6)].decl).id) {
		    if (strcmp((yyvsp[(1) - (6)].id),"class") == 0) {
		      fprintf(stderr,"%s : Line %d.  Warning. Nested classes not currently supported (ignored).\n", input_file, line_number);
		      /* Generate some code for a new class */
		    } else {
		      Nested *n = new Nested;
		      n->code << "typedef " << (yyvsp[(1) - (6)].id) << " " 
			      << CCode.get() << " $classname_" << (yyvsp[(5) - (6)].decl).id << ";\n";
		      n->name = copy_string((yyvsp[(5) - (6)].decl).id);
		      n->line = start_line;
		      n->type = new DataType;
		      n->type->type = T_USER;
		      n->type->is_pointer = (yyvsp[(5) - (6)].decl).is_pointer;
		      n->type->is_reference = (yyvsp[(5) - (6)].decl).is_reference;
		      n->next = 0;
		      add_nested(n);
		    }
		  }
		}
	      }
    break;

  case 289:

/* Line 1806 of yacc.c  */
#line 3301 "parser.y"
    { start_line = line_number; skip_brace();
              }
    break;

  case 290:

/* Line 1806 of yacc.c  */
#line 3302 "parser.y"
    { 
		if (cplus_mode == CPLUS_PUBLIC) {
		  if (strcmp((yyvsp[(1) - (5)].id),"class") == 0) {
		    fprintf(stderr,"%s : Line %d.  Warning. Nested classes not currently supported (ignored)\n", input_file, line_number);
		    /* Generate some code for a new class */
		  } else {
		    /* Generate some code for a new class */

		    Nested *n = new Nested;
		    n->code << "typedef " << (yyvsp[(1) - (5)].id) << " " 
			    << CCode.get() << " $classname_" << (yyvsp[(4) - (5)].decl).id << ";\n";
		    n->name = copy_string((yyvsp[(4) - (5)].decl).id);
		    n->line = start_line;
		    n->type = new DataType;
		    n->type->type = T_USER;
		    n->type->is_pointer = (yyvsp[(4) - (5)].decl).is_pointer;
		    n->type->is_reference = (yyvsp[(4) - (5)].decl).is_reference;
		    n->next = 0;
		    add_nested(n);

		  }
		}
	      }
    break;

  case 291:

/* Line 1806 of yacc.c  */
#line 3326 "parser.y"
    {
  		    if (cplus_mode == CPLUS_PUBLIC) {
                       cplus_register_type((yyvsp[(2) - (3)].id));
                    }
              }
    break;

  case 292:

/* Line 1806 of yacc.c  */
#line 3333 "parser.y"
    { 
                     skip_decl();
                     fprintf(stderr,"%s : Line %d. Function pointers not currently supported (ignored).\n", input_file, line_number);
		     
	      }
    break;

  case 293:

/* Line 1806 of yacc.c  */
#line 3338 "parser.y"
    {
                     skip_decl();
                     fprintf(stderr,"%s : Line %d. Function pointers not currently supported (ignored).\n", input_file, line_number);
		     
	      }
    break;

  case 294:

/* Line 1806 of yacc.c  */
#line 3343 "parser.y"
    { 
                     skip_decl();
                     fprintf(stderr,"%s : Line %d. Function pointers not currently supported (ignored).\n", input_file, line_number);
		     
	      }
    break;

  case 295:

/* Line 1806 of yacc.c  */
#line 3348 "parser.y"
    { }
    break;

  case 296:

/* Line 1806 of yacc.c  */
#line 3349 "parser.y"
    { }
    break;

  case 297:

/* Line 1806 of yacc.c  */
#line 3352 "parser.y"
    { (yyval.decl) = (yyvsp[(1) - (1)].decl);}
    break;

  case 298:

/* Line 1806 of yacc.c  */
#line 3353 "parser.y"
    { (yyval.decl).id = 0; }
    break;

  case 299:

/* Line 1806 of yacc.c  */
#line 3356 "parser.y"
    {}
    break;

  case 300:

/* Line 1806 of yacc.c  */
#line 3357 "parser.y"
    {}
    break;

  case 301:

/* Line 1806 of yacc.c  */
#line 3358 "parser.y"
    {}
    break;

  case 302:

/* Line 1806 of yacc.c  */
#line 3361 "parser.y"
    { }
    break;

  case 303:

/* Line 1806 of yacc.c  */
#line 3362 "parser.y"
    {
		 if (allow) {
		   int oldstatus = Status;
		   char *tm;

		   init_language();
		   if (cplus_mode == CPLUS_PUBLIC) {
		     temp_typeptr = new DataType(Active_type);
		     temp_typeptr->is_pointer += (yyvsp[(2) - (3)].decl).is_pointer;
		     if (Verbose) {
		       fprintf(stderr,"Wrapping member variable : %s\n",(yyvsp[(2) - (3)].decl).id);
		     }
		     Stat_var++;
		     doc_entry = new DocDecl((yyvsp[(2) - (3)].decl).id,doc_stack[doc_stack_top]);
		     if (temp_typeptr->status & STAT_READONLY) {
		       if (!(tm = typemap_lookup("memberin",typemap_lang,temp_typeptr,(yyvsp[(2) - (3)].decl).id,"",""))) 
			 Status = Status | STAT_READONLY;
		     }
		     cplus_variable((yyvsp[(2) - (3)].decl).id,(char *) 0,temp_typeptr);		
		     Status = oldstatus;
		     delete temp_typeptr;
		   }
		   scanner_clear_start();
		 }
	       }
    break;

  case 304:

/* Line 1806 of yacc.c  */
#line 3386 "parser.y"
    { }
    break;

  case 305:

/* Line 1806 of yacc.c  */
#line 3387 "parser.y"
    {
		 if (allow) {
		   int oldstatus = Status;
		   char *tm;

		   init_language();
		   if (cplus_mode == CPLUS_PUBLIC) {
		     temp_typeptr = new DataType(Active_type);
		     temp_typeptr->is_pointer += (yyvsp[(2) - (4)].decl).is_pointer;
		     if (Verbose) {
		       fprintf(stderr,"Wrapping member variable : %s\n",(yyvsp[(2) - (4)].decl).id);
		     }
		     Stat_var++;
		     if (!(tm = typemap_lookup("memberin",typemap_lang,temp_typeptr,(yyvsp[(2) - (4)].decl).id,"",""))) 
		       Status = Status | STAT_READONLY;
		     doc_entry = new DocDecl((yyvsp[(2) - (4)].decl).id,doc_stack[doc_stack_top]);
		     if (temp_typeptr->status & STAT_READONLY) Status = Status | STAT_READONLY;
		     cplus_variable((yyvsp[(2) - (4)].decl).id,(char *) 0,temp_typeptr);		
		     Status = oldstatus;
		     if (!tm)
		       fprintf(stderr,"%s : Line %d. Warning. Array member will be read-only.\n",input_file,line_number);
		     delete temp_typeptr;
		   }
		   scanner_clear_start();
		 }
	       }
    break;

  case 306:

/* Line 1806 of yacc.c  */
#line 3412 "parser.y"
    { }
    break;

  case 307:

/* Line 1806 of yacc.c  */
#line 3415 "parser.y"
    { 
                    CCode = "";
               }
    break;

  case 308:

/* Line 1806 of yacc.c  */
#line 3418 "parser.y"
    { skip_brace(); }
    break;

  case 309:

/* Line 1806 of yacc.c  */
#line 3421 "parser.y"
    { CCode = ""; }
    break;

  case 310:

/* Line 1806 of yacc.c  */
#line 3422 "parser.y"
    { CCode = ""; }
    break;

  case 311:

/* Line 1806 of yacc.c  */
#line 3423 "parser.y"
    { skip_brace(); }
    break;

  case 312:

/* Line 1806 of yacc.c  */
#line 3426 "parser.y"
    {}
    break;

  case 313:

/* Line 1806 of yacc.c  */
#line 3427 "parser.y"
    {}
    break;

  case 314:

/* Line 1806 of yacc.c  */
#line 3430 "parser.y"
    {
                    if (allow) {
		      if (cplus_mode == CPLUS_PUBLIC) {
			if (Verbose) {
			  fprintf(stderr,"Creating enum value %s\n", (yyvsp[(1) - (1)].id));
			}
			Stat_const++;
			temp_typeptr = new DataType(T_INT);
			doc_entry = new DocDecl((yyvsp[(1) - (1)].id),doc_stack[doc_stack_top]);
			cplus_declare_const((yyvsp[(1) - (1)].id), (char *) 0, temp_typeptr, (char *) 0);
			delete temp_typeptr;
			scanner_clear_start();
		      }
		    }
                  }
    break;

  case 315:

/* Line 1806 of yacc.c  */
#line 3445 "parser.y"
    {
		   if (allow) {
		     if (cplus_mode == CPLUS_PUBLIC) {
		       if (Verbose) {
			 fprintf(stderr, "Creating enum value %s = %s\n", (yyvsp[(1) - (3)].id), (yyvsp[(3) - (3)].dtype).id);
		       }
		       Stat_const++;
		       temp_typeptr = new DataType(T_INT);
		       doc_entry = new DocDecl((yyvsp[(1) - (3)].id),doc_stack[doc_stack_top]);
		       cplus_declare_const((yyvsp[(1) - (3)].id),(char *) 0, temp_typeptr,(char *) 0);
// OLD : Bug with value     cplus_declare_const($1,(char *) 0, temp_typeptr,$3.id);
		       delete temp_typeptr;
		       scanner_clear_start();
		     }
		   }
		 }
    break;

  case 316:

/* Line 1806 of yacc.c  */
#line 3461 "parser.y"
    {
		   if (allow) {
		     if (cplus_mode == CPLUS_PUBLIC) {
		       if (Verbose) {
			 fprintf(stderr,"Creating enum value %s\n", (yyvsp[(5) - (5)].id));
		       }
		       Stat_const++;
		       temp_typeptr = new DataType(T_INT);
		       doc_entry = new DocDecl((yyvsp[(3) - (5)].id),doc_stack[doc_stack_top]);
		       cplus_declare_const((yyvsp[(5) - (5)].id), (yyvsp[(3) - (5)].id), temp_typeptr, (char *) 0);
		       delete temp_typeptr;
		       scanner_clear_start();
		     }
		   }
		 }
    break;

  case 317:

/* Line 1806 of yacc.c  */
#line 3476 "parser.y"
    {
		   if (allow) {
		     if (cplus_mode == CPLUS_PUBLIC) {
		       if (Verbose) {
			 fprintf(stderr, "Creating enum value %s = %s\n", (yyvsp[(5) - (7)].id), (yyvsp[(7) - (7)].dtype).id);
		       }
		       Stat_const++;
		       temp_typeptr = new DataType(T_INT);
		       doc_entry = new DocDecl((yyvsp[(3) - (7)].id),doc_stack[doc_stack_top]);
		       cplus_declare_const((yyvsp[(5) - (7)].id),(yyvsp[(3) - (7)].id), temp_typeptr, (char *) 0);
// Old : bug with value	       cplus_declare_const($5,$3, temp_typeptr,$7.id);
		       delete temp_typeptr;
		       scanner_clear_start();
		     }
		   }
		 }
    break;

  case 318:

/* Line 1806 of yacc.c  */
#line 3492 "parser.y"
    { }
    break;

  case 319:

/* Line 1806 of yacc.c  */
#line 3493 "parser.y"
    { }
    break;

  case 320:

/* Line 1806 of yacc.c  */
#line 3496 "parser.y"
    {
		   (yyval.ilist) = (yyvsp[(2) - (2)].ilist);
                }
    break;

  case 321:

/* Line 1806 of yacc.c  */
#line 3499 "parser.y"
    {
                   (yyval.ilist).names = (char **) 0;
		   (yyval.ilist).count = 0;
                }
    break;

  case 322:

/* Line 1806 of yacc.c  */
#line 3505 "parser.y"
    { 
                   int i;
                   (yyval.ilist).names = new char *[NI_NAMES];
		   (yyval.ilist).count = 0;
		   for (i = 0; i < NI_NAMES; i++){
		     (yyval.ilist).names[i] = (char *) 0;
		   }
                   if ((yyvsp[(1) - (1)].id)) {
                       (yyval.ilist).names[(yyval.ilist).count] = copy_string((yyvsp[(1) - (1)].id));
                       (yyval.ilist).count++;
		   }
               }
    break;

  case 323:

/* Line 1806 of yacc.c  */
#line 3518 "parser.y"
    { 
                   (yyval.ilist) = (yyvsp[(1) - (3)].ilist);
                   if ((yyvsp[(3) - (3)].id)) {
		     (yyval.ilist).names[(yyval.ilist).count] = copy_string((yyvsp[(3) - (3)].id));
		     (yyval.ilist).count++;
		   }
               }
    break;

  case 324:

/* Line 1806 of yacc.c  */
#line 3527 "parser.y"
    {     
                  fprintf(stderr,"%s : Line %d. No access specifier given for base class %s (ignored).\n",
			  input_file,line_number,(yyvsp[(1) - (1)].id));
		  (yyval.id) = (char *) 0;
               }
    break;

  case 325:

/* Line 1806 of yacc.c  */
#line 3532 "parser.y"
    { 
                  fprintf(stderr,"%s : Line %d. No access specifier given for base class %s (ignored).\n",
			  input_file,line_number,(yyvsp[(2) - (2)].id));
		  (yyval.id) = (char *) 0;
	       }
    break;

  case 326:

/* Line 1806 of yacc.c  */
#line 3537 "parser.y"
    {
		 if (strcmp((yyvsp[(2) - (3)].id),"public") == 0) {
		   (yyval.id) = (yyvsp[(3) - (3)].id);
		 } else {
		   fprintf(stderr,"%s : Line %d. %s inheritance not supported (ignored).\n",
			   input_file,line_number,(yyvsp[(2) - (3)].id));
		   (yyval.id) = (char *) 0;
		 }
               }
    break;

  case 327:

/* Line 1806 of yacc.c  */
#line 3546 "parser.y"
    {
		 if (strcmp((yyvsp[(1) - (2)].id),"public") == 0) {
		   (yyval.id) = (yyvsp[(2) - (2)].id);
		 } else {
		   fprintf(stderr,"%s : Line %d. %s inheritance not supported (ignored).\n",
			   input_file,line_number,(yyvsp[(1) - (2)].id));
		   (yyval.id) = (char *) 0;
		 }
	       }
    break;

  case 328:

/* Line 1806 of yacc.c  */
#line 3555 "parser.y"
    {
                 if (strcmp((yyvsp[(1) - (3)].id),"public") == 0) {
		   (yyval.id) = (yyvsp[(3) - (3)].id);
		 } else {
		   fprintf(stderr,"%s : Line %d. %s inheritance not supported (ignored).\n",
			   input_file,line_number,(yyvsp[(1) - (3)].id));
		   (yyval.id) = (char *) 0;
		 }
               }
    break;

  case 329:

/* Line 1806 of yacc.c  */
#line 3566 "parser.y"
    { (yyval.id) = (char*)"public"; }
    break;

  case 330:

/* Line 1806 of yacc.c  */
#line 3567 "parser.y"
    { (yyval.id) = (char*)"private"; }
    break;

  case 331:

/* Line 1806 of yacc.c  */
#line 3568 "parser.y"
    { (yyval.id) = (char*)"protected"; }
    break;

  case 332:

/* Line 1806 of yacc.c  */
#line 3572 "parser.y"
    { (yyval.id) = (char*)"class"; }
    break;

  case 333:

/* Line 1806 of yacc.c  */
#line 3573 "parser.y"
    { (yyval.id) = (char*)"struct"; }
    break;

  case 334:

/* Line 1806 of yacc.c  */
#line 3574 "parser.y"
    {(yyval.id) = (char*)"union"; }
    break;

  case 335:

/* Line 1806 of yacc.c  */
#line 3577 "parser.y"
    {}
    break;

  case 336:

/* Line 1806 of yacc.c  */
#line 3578 "parser.y"
    { delete (yyvsp[(3) - (4)].pl);}
    break;

  case 337:

/* Line 1806 of yacc.c  */
#line 3579 "parser.y"
    {}
    break;

  case 338:

/* Line 1806 of yacc.c  */
#line 3584 "parser.y"
    { 
                    CCode = "";
               }
    break;

  case 339:

/* Line 1806 of yacc.c  */
#line 3587 "parser.y"
    { skip_brace(); }
    break;

  case 340:

/* Line 1806 of yacc.c  */
#line 3590 "parser.y"
    {}
    break;

  case 341:

/* Line 1806 of yacc.c  */
#line 3591 "parser.y"
    {}
    break;

  case 342:

/* Line 1806 of yacc.c  */
#line 3594 "parser.y"
    { }
    break;

  case 343:

/* Line 1806 of yacc.c  */
#line 3595 "parser.y"
    { }
    break;

  case 344:

/* Line 1806 of yacc.c  */
#line 3598 "parser.y"
    { }
    break;

  case 345:

/* Line 1806 of yacc.c  */
#line 3599 "parser.y"
    { }
    break;

  case 346:

/* Line 1806 of yacc.c  */
#line 3602 "parser.y"
    { }
    break;

  case 347:

/* Line 1806 of yacc.c  */
#line 3603 "parser.y"
    { }
    break;

  case 348:

/* Line 1806 of yacc.c  */
#line 3611 "parser.y"
    { 
                   ObjCClass = 1;
                   init_language();
		   cplus_mode = CPLUS_PROTECTED;
		   sprintf(temp_name,"CPP_CLASS:%s\n",(yyvsp[(2) - (3)].id));
		   if (add_symbol(temp_name,(DataType *) 0, (char *) 0)) {
		     fprintf(stderr,"%s : Line %d.  @interface %s is multiple defined.\n",
			     input_file,line_number,(yyvsp[(2) - (3)].id));
		     FatalError();
		   }
		   // Create a new documentation entry
		   doc_entry = new DocClass((yyvsp[(2) - (3)].id),doc_parent());
		   doc_stack_top++;
		   doc_stack[doc_stack_top] = doc_entry;
		   scanner_clear_start();
		   cplus_open_class((yyvsp[(2) - (3)].id), (char *) 0, "");     // Open up a new C++ class
                }
    break;

  case 349:

/* Line 1806 of yacc.c  */
#line 3627 "parser.y"
    { 
		  if ((yyvsp[(3) - (9)].id)) {
		      char *inames[1];
		      inames[0] = (yyvsp[(3) - (9)].id);
		      cplus_inherit(1,inames);
		  }
		  // Restore original doc entry for this class
		  doc_entry = doc_stack[doc_stack_top];
		  cplus_class_close((yyvsp[(2) - (9)].id));
		  doc_entry = 0;
		  doc_stack_top--;
		  cplus_mode = CPLUS_PUBLIC;
		  ObjCClass = 0;
		  delete (yyvsp[(2) - (9)].id);
		  delete (yyvsp[(3) - (9)].id);
                }
    break;

  case 350:

/* Line 1806 of yacc.c  */
#line 3644 "parser.y"
    {
                 ObjCClass = 1;
		 init_language();
                 cplus_mode = CPLUS_PROTECTED;
                 doc_entry = cplus_set_class((yyvsp[(2) - (6)].id));
		 if (!doc_entry) {
		   doc_entry = new DocClass((yyvsp[(2) - (6)].id),doc_parent());
		 }
		 doc_stack_top++;
		 doc_stack[doc_stack_top] = doc_entry;
		 scanner_clear_start();
	       }
    break;

  case 351:

/* Line 1806 of yacc.c  */
#line 3655 "parser.y"
    {
                 cplus_unset_class();
                 doc_entry = 0;
                 doc_stack_top--;
               }
    break;

  case 352:

/* Line 1806 of yacc.c  */
#line 3660 "parser.y"
    { skip_to_end(); }
    break;

  case 353:

/* Line 1806 of yacc.c  */
#line 3661 "parser.y"
    { skip_to_end(); }
    break;

  case 354:

/* Line 1806 of yacc.c  */
#line 3662 "parser.y"
    {
		 char *iname = make_name((yyvsp[(2) - (4)].id));
                 init_language();
                 lang->cpp_class_decl((yyvsp[(2) - (4)].id),iname,"");
		 for (int i = 0; i <(yyvsp[(3) - (4)].ilist).count; i++) {
		   if ((yyvsp[(3) - (4)].ilist).names[i]) {
		     iname = make_name((yyvsp[(3) - (4)].ilist).names[i]);
		     lang->cpp_class_decl((yyvsp[(3) - (4)].ilist).names[i],iname,"");
		     delete [] (yyvsp[(3) - (4)].ilist).names[i];
		   }
		 } 
		 delete [] (yyvsp[(3) - (4)].ilist).names;
	       }
    break;

  case 355:

/* Line 1806 of yacc.c  */
#line 3677 "parser.y"
    { (yyval.id) = (yyvsp[(2) - (3)].id);}
    break;

  case 356:

/* Line 1806 of yacc.c  */
#line 3678 "parser.y"
    { (yyval.id) = 0; }
    break;

  case 357:

/* Line 1806 of yacc.c  */
#line 3682 "parser.y"
    { skip_template(); 
                   CCode.strip();           // Strip whitespace
		   CCode.replace("<","< ");
		   CCode.replace(">"," >");
                   (yyval.id) = CCode.get();
                 }
    break;

  case 358:

/* Line 1806 of yacc.c  */
#line 3688 "parser.y"
    {
                   (yyval.id) =(char*) "";
               }
    break;

  case 359:

/* Line 1806 of yacc.c  */
#line 3693 "parser.y"
    { }
    break;

  case 360:

/* Line 1806 of yacc.c  */
#line 3694 "parser.y"
    { 
                    cplus_mode = CPLUS_PUBLIC;
                 }
    break;

  case 361:

/* Line 1806 of yacc.c  */
#line 3696 "parser.y"
    { }
    break;

  case 362:

/* Line 1806 of yacc.c  */
#line 3697 "parser.y"
    {
                    cplus_mode = CPLUS_PRIVATE;
                 }
    break;

  case 363:

/* Line 1806 of yacc.c  */
#line 3699 "parser.y"
    { }
    break;

  case 364:

/* Line 1806 of yacc.c  */
#line 3700 "parser.y"
    { 
                    cplus_mode = CPLUS_PROTECTED;
                 }
    break;

  case 365:

/* Line 1806 of yacc.c  */
#line 3702 "parser.y"
    { }
    break;

  case 366:

/* Line 1806 of yacc.c  */
#line 3703 "parser.y"
    {
		 if (!Error) {
		   skip_decl();
		   {
		     static int last_error_line = -1;
		     if (last_error_line != line_number) {
		       fprintf(stderr,"%s : Line %d. Syntax error in input.\n", input_file, line_number);
		       FatalError();
		       last_error_line = line_number;
		     }
		     Error = 1;
		   }
		 }
	       }
    break;

  case 367:

/* Line 1806 of yacc.c  */
#line 3716 "parser.y"
    { }
    break;

  case 368:

/* Line 1806 of yacc.c  */
#line 3717 "parser.y"
    { }
    break;

  case 369:

/* Line 1806 of yacc.c  */
#line 3720 "parser.y"
    {
  
                }
    break;

  case 370:

/* Line 1806 of yacc.c  */
#line 3727 "parser.y"
    { 
                 if (cplus_mode == CPLUS_PUBLIC) {
		   int oldstatus = Status;
		   char *tm;
		   char *iname;
		   if (Active_type) delete Active_type;
		   Active_type = new DataType((yyvsp[(1) - (2)].type));
		   (yyvsp[(1) - (2)].type)->is_pointer += (yyvsp[(2) - (2)].decl).is_pointer;
		   (yyvsp[(1) - (2)].type)->is_reference = (yyvsp[(2) - (2)].decl).is_reference;
		   if ((yyvsp[(1) - (2)].type)->status & STAT_READONLY) {
		     if (!(tm = typemap_lookup("memberin",typemap_lang,(yyvsp[(1) - (2)].type),(yyvsp[(2) - (2)].decl).id,"",""))) 
		       Status = Status | STAT_READONLY;
		   }
		   iname = make_name((yyvsp[(2) - (2)].decl).id);
		   doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		   if (iname == (yyvsp[(2) - (2)].decl).id) iname = 0;
		   cplus_variable((yyvsp[(2) - (2)].decl).id,iname,(yyvsp[(1) - (2)].type));
		   Status = oldstatus; 
		 }
		 scanner_clear_start();
		 delete (yyvsp[(1) - (2)].type);
               }
    break;

  case 371:

/* Line 1806 of yacc.c  */
#line 3749 "parser.y"
    { 
		 if (cplus_mode == CPLUS_PUBLIC) {
		   int oldstatus = Status;
		   char *tm, *iname;
		   if (Active_type) delete Active_type;
		   Active_type = new DataType((yyvsp[(1) - (3)].type));
		   (yyvsp[(1) - (3)].type)->is_pointer += (yyvsp[(2) - (3)].decl).is_pointer;
		   (yyvsp[(1) - (3)].type)->is_reference = (yyvsp[(2) - (3)].decl).is_reference;
		   (yyvsp[(1) - (3)].type)->arraystr = copy_string(ArrayString);
		   if ((yyvsp[(1) - (3)].type)->status & STAT_READONLY) {
		     if (!(tm = typemap_lookup("memberin",typemap_lang,(yyvsp[(1) - (3)].type),(yyvsp[(2) - (3)].decl).id,"",""))) 
		       Status = Status | STAT_READONLY;
		   }
		   iname = make_name((yyvsp[(2) - (3)].decl).id);
		   doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		   if (iname == (yyvsp[(2) - (3)].decl).id) iname = 0;
		   cplus_variable((yyvsp[(2) - (3)].decl).id,iname,(yyvsp[(1) - (3)].type));
		   Status = oldstatus; 
		 }
		 scanner_clear_start();
		 delete (yyvsp[(1) - (3)].type);
	       }
    break;

  case 372:

/* Line 1806 of yacc.c  */
#line 3771 "parser.y"
    {
                    strcpy(yy_rename,(yyvsp[(3) - (4)].id));
                    Rename_true = 1;
	       }
    break;

  case 373:

/* Line 1806 of yacc.c  */
#line 3774 "parser.y"
    { }
    break;

  case 374:

/* Line 1806 of yacc.c  */
#line 3776 "parser.y"
    { 
                 if (cplus_mode == CPLUS_PUBLIC) {
		   int oldstatus = Status;
		   char *tm, *iname;
		   DataType *t = new DataType (Active_type);
		   t->is_pointer += (yyvsp[(2) - (3)].decl).is_pointer;
		   t->is_reference = (yyvsp[(2) - (3)].decl).is_reference;
		   if (t->status & STAT_READONLY) {
		     if (!(tm = typemap_lookup("memberin",typemap_lang,t,(yyvsp[(2) - (3)].decl).id,"",""))) 
		       Status = Status | STAT_READONLY;
		   }
		   iname = make_name((yyvsp[(2) - (3)].decl).id);
		   doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		   if (iname == (yyvsp[(2) - (3)].decl).id) iname = 0;
		   cplus_variable((yyvsp[(2) - (3)].decl).id,iname,t);
		   Status = oldstatus; 
		   delete t;
		 }
		 scanner_clear_start();
               }
    break;

  case 375:

/* Line 1806 of yacc.c  */
#line 3796 "parser.y"
    {
		 char *iname;
                 if (cplus_mode == CPLUS_PUBLIC) {
		   int oldstatus = Status;
		   char *tm;
		   DataType *t = new DataType (Active_type);
		   t->is_pointer += (yyvsp[(2) - (4)].decl).is_pointer;
		   t->is_reference = (yyvsp[(2) - (4)].decl).is_reference;
		   t->arraystr = copy_string(ArrayString);
		   if (t->status & STAT_READONLY) {
		     if (!(tm = typemap_lookup("memberin",typemap_lang,t,(yyvsp[(2) - (4)].decl).id,"",""))) 
		       Status = Status | STAT_READONLY;
		   }
		   iname = make_name((yyvsp[(2) - (4)].decl).id);
		   doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		   if (iname == (yyvsp[(2) - (4)].decl).id) iname = 0;
		   cplus_variable((yyvsp[(2) - (4)].decl).id,iname,t);
		   Status = oldstatus; 
		   delete t;
		 }
		 scanner_clear_start();
               }
    break;

  case 376:

/* Line 1806 of yacc.c  */
#line 3818 "parser.y"
    { }
    break;

  case 377:

/* Line 1806 of yacc.c  */
#line 3821 "parser.y"
    { }
    break;

  case 378:

/* Line 1806 of yacc.c  */
#line 3822 "parser.y"
    {
                   AddMethods = 1;
	       }
    break;

  case 379:

/* Line 1806 of yacc.c  */
#line 3824 "parser.y"
    {
                   AddMethods = 0;
               }
    break;

  case 380:

/* Line 1806 of yacc.c  */
#line 3827 "parser.y"
    {
                     strcpy(yy_rename,(yyvsp[(3) - (4)].id));
                     Rename_true = 1;
	       }
    break;

  case 381:

/* Line 1806 of yacc.c  */
#line 3830 "parser.y"
    { }
    break;

  case 382:

/* Line 1806 of yacc.c  */
#line 3831 "parser.y"
    {
                 skip_decl();		                
		 if (!Error) {
		   {
		     static int last_error_line = -1;
		     if (last_error_line != line_number) {
		       fprintf(stderr,"%s : Line %d. Syntax error in input.\n", input_file, line_number);
		       FatalError();
		       last_error_line = line_number;
		     }
		     Error = 1;
		   }
		 }
	       }
    break;

  case 383:

/* Line 1806 of yacc.c  */
#line 3844 "parser.y"
    { }
    break;

  case 384:

/* Line 1806 of yacc.c  */
#line 3845 "parser.y"
    { }
    break;

  case 385:

/* Line 1806 of yacc.c  */
#line 3848 "parser.y"
    {
                 char *iname;
                 // An objective-C instance function
                 // This is like a C++ member function

		 if (strcmp((yyvsp[(3) - (5)].id),objc_destruct) == 0) {
		   // This is an objective C destructor
                   doc_entry = new DocDecl((yyvsp[(3) - (5)].id),doc_stack[doc_stack_top]);
                   cplus_destructor((yyvsp[(3) - (5)].id),(char *) 0);
		 } else {
		   iname = make_name((yyvsp[(3) - (5)].id));
		   doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		   if (iname == (yyvsp[(3) - (5)].id)) iname = 0;
		   cplus_member_func((yyvsp[(3) - (5)].id),iname,(yyvsp[(2) - (5)].type),(yyvsp[(4) - (5)].pl),0);
		   scanner_clear_start();
		   delete (yyvsp[(2) - (5)].type);
		   delete (yyvsp[(3) - (5)].id);
		   delete (yyvsp[(4) - (5)].pl);
		 }
               }
    break;

  case 386:

/* Line 1806 of yacc.c  */
#line 3868 "parser.y"
    { 
                 char *iname;
                 // An objective-C class function
                 // This is like a c++ static member function
                 if (strcmp((yyvsp[(3) - (5)].id),objc_construct) == 0) {
		   // This is an objective C constructor
		   doc_entry = new DocDecl((yyvsp[(3) - (5)].id),doc_stack[doc_stack_top]);
                   cplus_constructor((yyvsp[(3) - (5)].id),0,(yyvsp[(4) - (5)].pl));
		 } else {
		   iname = make_name((yyvsp[(3) - (5)].id));
		   doc_entry = new DocDecl(iname,doc_stack[doc_stack_top]);
		   if (iname == (yyvsp[(3) - (5)].id)) iname = 0;
		   cplus_static_func((yyvsp[(3) - (5)].id),iname,(yyvsp[(2) - (5)].type),(yyvsp[(4) - (5)].pl));
		 }
                 scanner_clear_start();
                 delete (yyvsp[(2) - (5)].type);
                 delete (yyvsp[(3) - (5)].id);
                 delete (yyvsp[(4) - (5)].pl);
               }
    break;

  case 387:

/* Line 1806 of yacc.c  */
#line 3889 "parser.y"
    { CCode = ""; }
    break;

  case 388:

/* Line 1806 of yacc.c  */
#line 3890 "parser.y"
    { skip_brace(); }
    break;

  case 389:

/* Line 1806 of yacc.c  */
#line 3893 "parser.y"
    { 
                  (yyval.type) = (yyvsp[(2) - (3)].type);
                }
    break;

  case 390:

/* Line 1806 of yacc.c  */
#line 3896 "parser.y"
    { 
                  (yyval.type) = (yyvsp[(2) - (4)].type);
                  (yyval.type)->is_pointer += (yyvsp[(3) - (4)].ivalue);
               }
    break;

  case 391:

/* Line 1806 of yacc.c  */
#line 3900 "parser.y"
    {       /* Empty type means "id" type */
                  (yyval.type) = new DataType(T_VOID);
		  sprintf((yyval.type)->name,"id");
                  (yyval.type)->is_pointer = 1;
                  (yyval.type)->implicit_ptr = 1;
               }
    break;

  case 392:

/* Line 1806 of yacc.c  */
#line 3908 "parser.y"
    { 
                  (yyval.type) = new DataType((yyvsp[(2) - (3)].p)->t);
                  delete (yyvsp[(2) - (3)].p);
                 }
    break;

  case 393:

/* Line 1806 of yacc.c  */
#line 3912 "parser.y"
    { 
                  (yyval.type) = new DataType(T_VOID);
		  sprintf((yyval.type)->name,"id");
                  (yyval.type)->is_pointer = 1;
                  (yyval.type)->implicit_ptr = 1;
               }
    break;

  case 394:

/* Line 1806 of yacc.c  */
#line 3920 "parser.y"
    { 
                   Parm *p= new Parm((yyvsp[(3) - (4)].type),(yyvsp[(4) - (4)].id));
		   p->objc_separator = (yyvsp[(2) - (4)].id);
                   (yyval.pl) = (yyvsp[(1) - (4)].pl);
                   (yyval.pl)->append(p);
               }
    break;

  case 395:

/* Line 1806 of yacc.c  */
#line 3926 "parser.y"
    { 
                 (yyval.pl) = new ParmList;
               }
    break;

  case 396:

/* Line 1806 of yacc.c  */
#line 3931 "parser.y"
    { (yyval.id) = copy_string(":"); }
    break;

  case 397:

/* Line 1806 of yacc.c  */
#line 3932 "parser.y"
    { (yyval.id) = new char[strlen((yyvsp[(1) - (2)].id))+2]; 
                    strcpy((yyval.id),(yyvsp[(1) - (2)].id));
		    strcat((yyval.id),":");
		    delete (yyvsp[(1) - (2)].id);
	        }
    break;

  case 398:

/* Line 1806 of yacc.c  */
#line 3943 "parser.y"
    {
                    (yyval.dlist) = (yyvsp[(3) - (3)].dlist);
		    (yyval.dlist).names[(yyval.dlist).count] = copy_string((yyvsp[(1) - (3)].id));
		    (yyval.dlist).values[(yyval.dlist).count] = copy_string((yyvsp[(2) - (3)].id));
		    format_string((yyval.dlist).values[(yyval.dlist).count]);
		    (yyval.dlist).count++;
                 }
    break;

  case 399:

/* Line 1806 of yacc.c  */
#line 3953 "parser.y"
    {
                    (yyval.dlist) = (yyvsp[(1) - (4)].dlist);
		    (yyval.dlist).names[(yyval.dlist).count] = copy_string((yyvsp[(3) - (4)].id));
		    (yyval.dlist).values[(yyval.dlist).count] = copy_string((yyvsp[(4) - (4)].id));
		    format_string((yyval.dlist).values[(yyval.dlist).count]);
		    (yyval.dlist).count++;
                 }
    break;

  case 400:

/* Line 1806 of yacc.c  */
#line 3960 "parser.y"
    {
                    (yyval.dlist).names = new char *[NI_NAMES];
		    (yyval.dlist).values = new char *[NI_NAMES];
		    (yyval.dlist).count = 0;
	       }
    break;

  case 401:

/* Line 1806 of yacc.c  */
#line 3967 "parser.y"
    {
                     (yyval.id) = (yyvsp[(2) - (2)].id);
                 }
    break;

  case 402:

/* Line 1806 of yacc.c  */
#line 3970 "parser.y"
    {
                     (yyval.id) = (yyvsp[(2) - (2)].id);
	       }
    break;

  case 403:

/* Line 1806 of yacc.c  */
#line 3973 "parser.y"
    { 
                     (yyval.id) = 0;
                }
    break;

  case 404:

/* Line 1806 of yacc.c  */
#line 3983 "parser.y"
    {
                 (yyval.id) = (yyvsp[(1) - (1)].id);
               }
    break;

  case 405:

/* Line 1806 of yacc.c  */
#line 3986 "parser.y"
    {
                 (yyval.id) = copy_string("const");
               }
    break;

  case 406:

/* Line 1806 of yacc.c  */
#line 3991 "parser.y"
    {
                 (yyval.tmparm) = (yyvsp[(1) - (2)].tmparm);
                 (yyval.tmparm)->next = (yyvsp[(2) - (2)].tmparm);
		}
    break;

  case 407:

/* Line 1806 of yacc.c  */
#line 3997 "parser.y"
    {
                 (yyval.tmparm) = (yyvsp[(2) - (3)].tmparm);
                 (yyval.tmparm)->next = (yyvsp[(3) - (3)].tmparm);
                }
    break;

  case 408:

/* Line 1806 of yacc.c  */
#line 4001 "parser.y"
    { (yyval.tmparm) = 0;}
    break;

  case 409:

/* Line 1806 of yacc.c  */
#line 4004 "parser.y"
    {
		    if (InArray) {
		      (yyvsp[(1) - (2)].type)->is_pointer++;
		      (yyvsp[(1) - (2)].type)->arraystr = copy_string(ArrayString);
		    }
		    (yyval.tmparm) = new TMParm;
                    (yyval.tmparm)->p = new Parm((yyvsp[(1) - (2)].type),(yyvsp[(2) - (2)].id));
		    (yyval.tmparm)->p->call_type = 0;
		    (yyval.tmparm)->args = tm_parm;
		    delete (yyvsp[(1) - (2)].type);
		    delete (yyvsp[(2) - (2)].id);
                 }
    break;

  case 410:

/* Line 1806 of yacc.c  */
#line 4017 "parser.y"
    {
		  (yyval.tmparm) = new TMParm;
		   (yyval.tmparm)->p = new Parm((yyvsp[(1) - (3)].type),(yyvsp[(3) - (3)].id));
		   (yyval.tmparm)->p->t->is_pointer += (yyvsp[(2) - (3)].ivalue);
		   (yyval.tmparm)->p->call_type = 0;
		   if (InArray) {
		     (yyval.tmparm)->p->t->is_pointer++;
		     (yyval.tmparm)->p->t->arraystr = copy_string(ArrayString);
		    }
		   (yyval.tmparm)->args = tm_parm;
		   delete (yyvsp[(1) - (3)].type);
		   delete (yyvsp[(3) - (3)].id);
		}
    break;

  case 411:

/* Line 1806 of yacc.c  */
#line 4031 "parser.y"
    {
                  (yyval.tmparm) = new TMParm;
		  (yyval.tmparm)->p = new Parm((yyvsp[(1) - (3)].type),(yyvsp[(3) - (3)].id));
		  (yyval.tmparm)->p->t->is_reference = 1;
		  (yyval.tmparm)->p->call_type = 0;
		  (yyval.tmparm)->p->t->is_pointer++;
		  if (!CPlusPlus) {
			fprintf(stderr,"%s : Line %d. Warning.  Use of C++ Reference detected.  Use the -c++ option.\n", input_file, line_number);
		  }
		  (yyval.tmparm)->args = tm_parm;
		  delete (yyvsp[(1) - (3)].type);
		  delete (yyvsp[(3) - (3)].id);
		}
    break;

  case 412:

/* Line 1806 of yacc.c  */
#line 4044 "parser.y"
    {
                  fprintf(stderr,"%s : Line %d. Error. Function pointer not allowed (remap with typedef).\n", input_file, line_number);
		  FatalError();
                  (yyval.tmparm) = new TMParm;
		  (yyval.tmparm)->p = new Parm((yyvsp[(1) - (8)].type),(yyvsp[(4) - (8)].id));
		  (yyval.tmparm)->p->t->type = T_ERROR;
		  (yyval.tmparm)->p->name = copy_string((yyvsp[(4) - (8)].id));
		  strcpy((yyval.tmparm)->p->t->name,"<function ptr>");
		  (yyval.tmparm)->args = tm_parm;
		  delete (yyvsp[(1) - (8)].type);
		  delete (yyvsp[(4) - (8)].id);
		  delete (yyvsp[(7) - (8)].pl);
		}
    break;

  case 413:

/* Line 1806 of yacc.c  */
#line 4059 "parser.y"
    {
                    (yyval.id) = (yyvsp[(1) - (2)].id); 
                    InArray = 0;
                }
    break;

  case 414:

/* Line 1806 of yacc.c  */
#line 4063 "parser.y"
    { 
                    ArrayBackup = "";
		    ArrayBackup << ArrayString;
                  }
    break;

  case 415:

/* Line 1806 of yacc.c  */
#line 4066 "parser.y"
    {
                    (yyval.id) = (yyvsp[(1) - (4)].id);
                    InArray = (yyvsp[(2) - (4)].ivalue);
                    ArrayString = "";
		    ArrayString << ArrayBackup;
                }
    break;

  case 416:

/* Line 1806 of yacc.c  */
#line 4072 "parser.y"
    { 
                    ArrayBackup = "";
		    ArrayBackup << ArrayString;
		}
    break;

  case 417:

/* Line 1806 of yacc.c  */
#line 4075 "parser.y"
    {
		    (yyval.id) = new char[1];
		    (yyval.id)[0] = 0;
		    InArray = (yyvsp[(1) - (3)].ivalue);
                    ArrayString = "";
                    ArrayString << ArrayBackup;
		}
    break;

  case 418:

/* Line 1806 of yacc.c  */
#line 4082 "parser.y"
    { (yyval.id) = new char[1];
  	                  (yyval.id)[0] = 0;
                          InArray = 0;
                }
    break;

  case 419:

/* Line 1806 of yacc.c  */
#line 4088 "parser.y"
    {
                  tm_parm = (yyvsp[(2) - (3)].pl);
                }
    break;

  case 420:

/* Line 1806 of yacc.c  */
#line 4091 "parser.y"
    {
                  tm_parm = 0;
                }
    break;

  case 421:

/* Line 1806 of yacc.c  */
#line 4096 "parser.y"
    {(yyval.id) = (yyvsp[(1) - (1)].id);}
    break;

  case 422:

/* Line 1806 of yacc.c  */
#line 4097 "parser.y"
    { (yyval.id) = (yyvsp[(1) - (1)].id);}
    break;

  case 423:

/* Line 1806 of yacc.c  */
#line 4103 "parser.y"
    { }
    break;

  case 424:

/* Line 1806 of yacc.c  */
#line 4104 "parser.y"
    { }
    break;

  case 425:

/* Line 1806 of yacc.c  */
#line 4107 "parser.y"
    { }
    break;

  case 426:

/* Line 1806 of yacc.c  */
#line 4108 "parser.y"
    { }
    break;

  case 427:

/* Line 1806 of yacc.c  */
#line 4109 "parser.y"
    { }
    break;



/* Line 1806 of yacc.c  */
#line 8756 "y.tab.c"
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*------------------------------------.
| yyerrlab -- here on detecting error |
`------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
	 error, discard it.  */

      if (yychar <= YYEOF)
	{
	  /* Return failure if at end of input.  */
	  if (yychar == YYEOF)
	    YYABORT;
	}
      else
	{
	  yydestruct ("Error: discarding",
		      yytoken, &yylval);
	  yychar = YYEMPTY;
	}
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
	{
	  yyn += YYTERROR;
	  if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
	    {
	      yyn = yytable[yyn];
	      if (0 < yyn)
		break;
	    }
	}

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
	YYABORT;


      yydestruct ("Error: popping",
		  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  *++yyvsp = yylval;


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined(yyoverflow) || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
		  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yyresult);
}



/* Line 2067 of yacc.c  */
#line 4143 "parser.y"


void error_recover() {
  int c;
  c = yylex();
  while ((c > 0) && (c != SEMI)) 
    c = yylex();
}

/* Called by the parser (yyparse) when an error is found.*/
void yyerror (const char *) {
  //  Fprintf(stderr,"%s : Line %d. Syntax error.\n", input_file, line_number);
  //  error_recover();
}


