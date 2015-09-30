This is the README file for OOF2, describing how to build and install
it with the Python distutils utility.

This README file is for OOF2 version 2.1.12 or later.

# What is OOF2

[OOF2](http://www.ctcms.nist.gov/oof/) is designed to help materials
scientists calculate macroscopic properties from images of real or
simulated microstructures. It reads an image, assigns material
properties to features in the image, and conducts virtual experiments
to determine the macroscopic properties of the microstructure.

The programs are written in C++ and Python and benefit from an
object-oriented design. The underlying numerical solutions rely on
finite element technology.  Hence the name OOF, for object-oriented
finite element analysis.

# Disclaimer

This software provided is provided by NIST as a public service. You
may use, copy and distribute copies of the software in any medium,
provided that you keep intact this entire notice. You may improve,
modify and create derivative works of the software or any portion of
the software, and you may copy and distribute such modifications or
works. Modified works should carry a notice stating that you changed
the software and should note the date and nature of any such
change. Please explicitly acknowledge the National Institute of
Standards and Technology as the source of the software.  To facilitate
maintenance we ask that before distributing modified versions of this
software, you first contact the authors at oof manager@nist.gov.

The software is expressly provided "AS IS". NIST MAKES NO WARRANTY OF
ANY KIND, EXPRESS, IMPLIED, IN FACT OR ARISING BY OPERATION OF LAW,
INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTY OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT
AND DATA ACCURACY. NIST NEITHER REPRESENTS NOR WARRANTS THAT THE
OPERATION OF THE SOFTWARE WILL BE UNINTERRUPTED OR ERROR-FREE, OR THAT
ANY DEFECTS WILL BE CORRECTED. NIST DOES NOT WARRANT OR MAKE ANY
REPRESENTATIONS REGARDING THE USE OF THE SOFTWARE OR THE RESULTS
THEREOF, INCLUDING BUT NOT LIMITED TO THE CORRECTNESS, ACCURACY,
RELIABILITY, OR USEFULNESS OF THE SOFTWARE.

You are solely responsible for determining the appropriateness of
using and distributing the software and you assume all risks
associated with its use, including but not limited to the risks and
costs of program errors, compliance with applicable laws, damage to or
loss of data, programs or equipment, and the unavailability or
interruption of operation. This software is not intended to be used in
any situation where a failure could cause risk of injury or damage to
property. The software was developed by NIST employees. NIST employee
contributions are not subject to copyright protection within the
United States.

# Installation

Installation is similar to other Python libraries.  If your system is
well-set-up, and has the required libraries, there should be no
difficulties.

The executive summary of steps is:

```
tar -xzf oof-<version>.tar.gz
cd oof-<version>
python setup.py build
python setup.py install
```

but please read the rest of this file before proceeding.

If something goes wrong, your system adminstrator may be able to help
you, or you can contact the oof developers at oof manager@nist.gov.
It's diagnostically useful to include all the output from setup.py.

OOF2 has been built and tested on Linux (Debian, CentOS, Ubuntu, and,
OpenSUSE), and Macintosh OS X.

## Prerequisites

A computer running a variant of the Unix operating system,
including Linux and Macintosh OS X, and an X11 server. OOF2
currently does *not* run on Microsoft Windows.

The following external programs and libraries must be present
before you can run OOF2.  To compile OOF2 from sources, you will
also require the header files ("includes") associated with these
programs and libraries.  These are usually available as part of a
"development" version of the library software.

- [Python (2.6 or 2.7)](http://www.python.org)
- [Magick++](http://www.imagemagick.org/www/Magick++/index.html)
- [gtk+-2.0 (2.6 or later. Not 3.x)](http://www.gtk.org/download/)   
- [libgnomecanvas2](http://directory.fsf.org/graphics/misc/libgnomecanvas.html)
- [pygtk2 (2.6 or later)](http://www.pygtk.org)

Please note that the words "or later" do not include later major
versions.  OOF2 will not work with Python 3.x or gtk+ 3.x.

Macintosh OS X users will need to install an [*X11 server*](
http://xquartz.macosforge.org/).

You should also have the ability to run *lapack* and the *"blas"* basic
linear algebra subroutines.  On Macintosh OS X, they are built in
to the Accelerate framework in the OS, and no special libraries are
required.  On Linux and commercial Unix systems, they may have to
be installed, and you may require headers (sometimes provided as
part of a "-dev" package).

OOF2 will use the *tcmalloc* library for efficient memory allocation
if it is available, but it will also work without it (although it
will be slower).  It can be obtained from 
https://github.com/gperftools/gperftools and many package managers.

Detailed instructions for installing the OOF2 prerequisites on a
number of different operating systems can be found at
http://www.ctcms.nist.gov/oof/oof2/prerequisites.html.

## Procedure

   (Macintosh OS X users can install OOF2 from either a Terminal or
   xterm window, or the equivalent.)

### 1. Unpack

   Unpack the .tar.gz file.  The usual way is to run `tar -xzf` on the
   file you want to unpack.  This will create a subdirectory named
   "oof2-<version>" in the directory where you run tar.

### 2. Build the OOF2 libraries and Python extension modules

   Switch to the newly-created directory, and run

     % python setup.py build

   The build_ext command will create a "build" subdirectory in the top
   OOF2 directory.  Within "build" it will create a subdirectory with
   a system-dependent name.

#### 2.1 Getting more control over the build

   You can ignore this section unless something went wrong when
   building OOF2 in step 1.  setup.py tries to be intelligent about
   choosing options, but it's not perfect.

   The distutils "build" command actually runs a bunch of separate
   subcommands, each of which has its own options.  The relevant
   subcommands are "build_shlib", "build_ext", "build_scripts", and
   "build_py".  "build_shlib" builds the shared libraries,
   liboof2common.so, etc, that contain most of the low-level OOF2
   machinery. "build_ext" builds the OOF2 Python extension modules
   that provide the interface betweeen C++ and Python.  "build_py"
   copies the Python files from the source directory to the build
   directory, and "build_scripts" copies the start-up script into the
   build directory and makes it executable.  OOF2 installers will
   probably only have to worry about "build_shlib" and "build_ext".

   The four commands must be run in order: build_shlib must precede
   build_ext, and build_ext must precede build_py.

   Each command can be run separately, for example

    % python setup.py build_ext

   or in combination

    % python setup.py build_shlib build_ext

   and options can be provided to each one
  
    % python setup.py build_shlib --debug build_ext --include_dirs=/sw/include

   You can see the full set of options by running

    % python setup.py --help <command name>

   Here are the options most likely to be useful:

   For "build_shlib" or "build":

   * --library-dirs   
   
      Specify a non-standard location for libraries.  Multiple
      directories should be separated by colons, like this:
      --library-dirs=/strange/spot:/out/of/theway

   * --libraries       
   
      Specify libraries to load. Due to a bug in distutils, it's only
      possible to specify a single library. For example
      --libraries=abc will load libabc.so.  If you need to load more
      than one library in this way, please contact us.
      
   * --blas-libraries
   
      Specify libraries to use for blas and lapack.  Multiple library
      names should be separated by spaces, like this:
      --blas-libraries="myblas mylapack"

   * --blas-link-args  
        
      Specify additional link arguments required by blas and lapack,
      for example: --blas-link-args="-faltivec -framework vecLib"

The following arguments can appear anywhere after "setup.py" in the
command line, and apply to both the build and install steps.  Tf
you run the build and install steps separately, you must provide
these arguments in *both* steps if you provide them in one.

   * --disable-gui
   
      Don't include any components of the graphical user interface.
      When this option is used, it's not necessary to have the gtk,
      pygtk, or libgnomecanvas libraries installed.

   * --enable-openmp   
   
      Turn on OpenMP code in OOF2 for parallel execution.  This will
      only work if your compiler supports OpenMP, which the
      Macintosh clang compiler does not.  (In OOF2 2.1.12 only the
      matrix construction and pixel autogroup operations are
      parallelized.)

Prior to version 2.1.12, setup.py accepted the arguments
--skip-swig and --with-swig to control swig, which is used to
generate some of the OOF2 code.  The OOF2 distribution now includes
its own copy of swig, and those arguments are unnecessary.
             

### 3. Install

   To install OOF2, run

   ```
   % python setup.py install
   ```

   This will install OOF2 in the standard location for Python
   extensions on your system.  This is good, because then you won't
   have to do anything special to get OOF2 to run.  It's also bad,
   because unless you are the system administrator, you probably don't
   have permission to install anything in that directory.  You have
   two options:

   1. Get a system administrator to run the installation step.

   2. Tell distutils to install oof2 in a different place, like this:
      ```
      % python setup.py install --prefix=<prefix>
      ```
   
      where \<prefix> is a directory that you can write to.  The default
      value of \<prefix> is usually */usr/local*.  On OS X it may be
      something like */Library/Frameworks/Python.framework/Versions/2.7*
      if you're using the system Python, or */sw* or */opt/local* if you're
      using fink or macports.

      The installation procedure will create an executable script called
      "oof2" in \<prefix>/bin, a bunch of shared libraries called
      "liboof2*.so" or "liboof2\*.dylib" in \<prefix>/lib, a directory
      called "oof2" in \<prefix>/lib/python2.x/site-packages (where 2.x
      is your python version number), and some example files in
      \<prefix>/share/oof2/ examples. 

      (It's possible to use --home=\<home> instead of --prefix when
      installing oof2.  The only difference is that --home will put the
      python libraries in \<home>/lib/python instead of
      \<prefix>/lib/python2.x/site-packages.)

#### 3.1. Set environment variables

   If \<prefix>/bin is not in your Unix command path, you'll need to
   add it to the PATH environment variable, or create a symbolic link
   from a directory that is in your path (or start OOF2 the hard way
   by by typing \<prefix>/bin/oof2).  (Typing `echo $path` will print
   the current value of your path.  The method for setting
   environment variables depends on which Unix shell you're using.)

   If \<prefix>/lib is not in the list of directories that the dynamic
   linker searches for libraries, you'll have to add it by setting
   the LD_LIBRARY_PATH environment variable.  This should *not* be
   necessary on Macintosh OS X.

   If \<prefix>/lib/python2.x/site-packages is not in your Python
   path, you'll have to add it to the PYTHONPATH environment
   variable. Running the following command will print your Python
   path. `python -c "import sys; print sys.path"` will print your
   Python path.


# Running OOF2

At this point, you should have an executable file named "oof2" in a
bin directory in your execution path.  You can now simply type `oof2`
at your shell prompt, and OOF2 will start up.

OOF also has many options, and you can get a summary of them by typing
`oof2 --help`.

By default, OOF runs in graphics mode, opening a couple of windows to
get you started.  If you don't want this, you can use the `--text`
option to run it in command-line mode.

Be sure to read the [OOF manual](http://www.ctcms.nist.gov/~langer/oof2man/) 
and to go through the tutorials provided in the OOF2 help menu.


# Contact Us

If you encounter bugs in the program, please send e-mail to
oof_bugs@nist.gov.  Tell us what version of OOF2 you're using, what
operating system you're using, and *exactly* what you did to encounter
the error.  It is helpful to include an OOF2 script (which you can
save with the "File/Save/Python Log" menu item) and a copy of any
input files (images, oof data files, etc) required to run the script.
It is extremely difficult for us to fix a bug if we can't reproduce it
here. 

Other communications, including requests for help and suggestions for
new features, can be sent to oof_manager@nist.gov.



