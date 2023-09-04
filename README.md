This is the README file for OOF2, describing how to build and install
it with the Python distutils utility.

This README file is for OOF2 version 2.3.0 or later.

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
software, you first contact the authors at oof_manager@nist.gov.

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

The executive summary of steps (to be typed in a terminal window) is:

```
mkdir oof2
cd oof2
tar -xzf oof2-<version>.tar.gz
mkdir build
cd build
cmake ../oof2-<version>
make install
```

but please read the rest of this file before proceeding.

If something goes wrong, your system adminstrator may be able to help
you, or you can contact the oof developers at oof_manager@nist.gov.
It's diagnostically useful to include all of the output from the
installation commands.

OOF2 has been built and tested on Debian Linux and macOS 13 (Ventura).
It ought to work on other varieties of Linux.

## Prerequisites

A computer running a variant of the Unix operating system, including
Linux and Macintosh. OOF2 currently does *not* run on Microsoft
Windows.

The following external programs and libraries must be present
before you can run OOF2.  To compile OOF2 from sources, you will
also require the header files ("includes") associated with these
programs and libraries.  These are usually available as part of a
"development" version of the library software.

- [Python 3 (3.8 or later)](http://www.python.org)
- [Swig (4.0 or 4.1)] (https://www.swig.org)
- [Magick++](http://www.imagemagick.org/www/Magick++/index.html)
- [gtk3 (3.22 or later)](http://www.gtk.org/download/)
- [pygobject (3.28 or later)](https://pypi.org/project/PyGObject/)
- [cairomm (1.12 or later)](https://www.cairographics.org/cairomm/)
- [pango (1.40 or later)](https://pango.gnome.org/)
- [pangocairo (1.40 or later)](https://gnome.pages.gitlab.gnome.org/pango/PangoCairo/) 
- [oofcanvas (1.1 or later)](http://www.ctcms.nist.gov/oof/oofcanvas)

Please note that the words "or later" do not include later major
versions.  OOF2 will not work with gtk 4.x.  It is recommended that
you use a package manager to install the prerequisites, rather than
compiling them yourself.

Macintosh users can install either native Quartz or X11 versions of
gtk3, cairo, and pango.  If using X11, they will have to also install
an X11 server to run OOF2. But there seem to be some problems with
gtk3 and X11 on Macs, so Quartz is recommended.

You should also have the ability to run *lapack* and the *"blas"* basic
linear algebra subroutines.  On maCOS no special libraries are
required.  On Linux and commercial Unix systems, they may have to
be installed, and you may require headers (sometimes provided as
part of a "-dev" package).

Detailed instructions for installing the OOF2 prerequisites on a
number of different operating systems can be found at
http://www.ctcms.nist.gov/oof/oof2/prerequisites.html.

## Installation Procedure

Commands in the following steps should be typed into a terminal
window.  Type everything after the initial "%".

### 0. Download

Download the latest OOF2 source distribution from
http://www.ctcms.nist.gov/oof/oof2/  It will create a file called
something like oof2-2.3.0.tar.gz.

### 1. Create a working directory and move to it

In your home directory or some other convenient location, enter

    % mkdir oof2
    % cd oof2

### 2. Unpack

Unpack the .tar.gz file.  The usual way is to run `tar -xf` on the
file you want to unpack.  If the file is in your Downloads directory,
type

    % tar -xf ~/Downloads/oof2-2.3.0.tar.gz
    
This will create a subdirectory named "oof2-<version>" in the
directory where you run tar.
    
### 3. Configure

Create a build directory. 

    % mkdir build
    % cd build

If you want to use the default settings, run `cmake`.

    % cmake ../oof2-2.3.0
    
but beware that this will cause OOF2 to be installed in a system
directory like `/usr` or `/usr/local`, where you might not have
permission to create files.  It's better to use `ccmake`, which will
let you edit settings:

    % ccmake ../oof2-2.3.0
    
See https://cmake.org/cmake/help/latest/manual/ccmake.1.html for
full instructions on how to use ccmake.  At a minimum

- Type `c` to do the initial configuration
- Use the arrow keys to navigate to `CMAKE_INSTALL_PREFIX`, which is
  where OOF2 will be installed.
- Type `<return>`, edit the prefix, and type `<return>` again.
  Set the prefix to a directory where you can write, such as your home
  directory.
- Similarly, change `DESIRED_PYTHON_VERSION` to a version of python3
  that you have installed, and `DESIRED_SWIG_VERSION` to the version
  of swig4.
- Type `c` to update the configuration.
- Type `g` to generate the build scripts and exit.

### 4. Build and install

Run

    % make install

If your computer's version of `make` can run in parallel, you can
build OOF2 faster by including the `-j` option

    % make -j 10 install
    
Replace `10` by however many compilation processes you can run
simultaneously. 

If you need superuser permissions to create files in the installation
directory (possibly because you didn't change `CMAKE_INSTALL_PREFIX`
in step 3) you should run the build and installation steps separately
so that you can use superuser privileges for installation:

    % make
    % sudo make install
    
The installation procedure will create an executable script called
`oof2` in `<prefix>/bin`, a bunch of shared libraries called
`liboof2*.so` or `liboof2*.dylib` in `<prefix>/lib`, a directory
called `oof2` in `<prefix>/lib/python3.x/site-packages` (where 3.x is
your python version number), and some example files in
`<prefix>/share/oof2/examples`.

### 5. Set environment variables

If `<prefix>/bin` is not in your Unix command path, you'll need to add
it to the `PATH` environment variable, or create a symbolic link from a
directory that is in your path (or start OOF2 the hard way by by
typing `<prefix>/bin/oof2`).  (Typing `echo $path` will print the
current value of your path.  The method for setting environment
variables depends on which Unix shell you're using.)

If `<prefix>/lib` is not in the list of directories that the dynamic
linker searches for libraries, you'll have to add it by setting the
`LD_LIBRARY_PATH` environment variable.  This should *not* be necessary
on Macintosh.
    
If `<prefix>/lib/python3.x/site-packages` is not in your Python path,
you'll have to add it to the `PYTHONPATH` environment variable. Running
`python -c "import sys; print sys.path"` will print your Python path.
   
### 4. Test 

If you want to test the installation, run `oof2-test` and
`oof2-guitest`.

`oof2-test` runs a variety of tests that don't depend on the GUI.  It
can take a long time to complete.  `oof2-guitest` runs GUI-dependent
tests.  It doesn't takes as long but it can get confused if you
accidentally click or type in one of its windows, so it's best to just
sit back and watch it run.

The test files are installed into
`<prefix>/lib/python3.x/site-packages/oof2/TEST` and
`<prefix>/lib/python3.x/site-packages/oof2/TEST/GUI`.  Each of those
directories has a `README` file that may be helpful.

In version 2.3.0 there is something wrong with the GUI testing
apparatus that makes a few of the tests fail erratically.  If
`oof2-guitest` fails, note the name of the failed test file and
restart the test with `oof2-guitest --from <name of failed test>`.
You may have to do this more than once.

# Running OOF2

At this point, you should have an executable file named `oof2` in a
`bin` directory in your execution path.  You can now simply type `oof2`
at your shell prompt, and OOF2 will start up.

OOF2 also has many options, and you can get a summary of them by typing
`oof2 --help`.

By default, OOF2 runs in graphics mode, opening a couple of windows to
get you started.  If you don't want this, you can use the `--text`
option to run it in command-line mode.

Be sure to read the [OOF manual](http://www.ctcms.nist.gov/~langer/oof2man/) 
and to go through the tutorials provided in the OOF2 Help menu.


# Contact Us

If you encounter bugs in the program, please send e-mail to
`oof_bugs@nist.gov`.  Tell us what version of OOF2 you're using, what
operating system you're using, and *exactly* what you did to encounter
the error.  It is helpful to include an OOF2 script (which you can
save with the "File/Save/Python Log" menu item) and a copy of any
input files (images, oof data files, etc) required to run the script.
It is extremely difficult for us to fix a bug if we can't reproduce it
ourselves. 

Other communications, including requests for help and suggestions for
new features, can be sent to oof_manager@nist.gov.



