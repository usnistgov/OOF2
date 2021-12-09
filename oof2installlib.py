# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Modify the "install_lib" command so that it runs "install_name_tool" on Macs.

from distutils.command import install_lib
from distutils import log
from distutils.sysconfig import get_config_var
from distutils.errors import DistutilsExecError
import os
import subprocess
import sys

class oof_install_lib(install_lib.install_lib):
    def install(self):
        outfiles = install_lib.install_lib.install(self)

        if sys.platform == 'darwin':
            # Find the names of the shared libraries and where they've
            # been installed (or will be installed).
            install_shlib = self.get_finalized_command("install_shlib")
            # install_dir is <root>/<prefix>/lib
            install_dir = install_shlib.install_dir
            root = self.get_finalized_command("install").root
            if root is not None:
                install_dir = os.path.relpath(install_dir, root)
                install_dir = os.path.join(os.sep, install_dir) 
            
            shared_libs = [lib.name for lib in install_shlib.shlibs]
            
            installed_names = {}        # new path keyed by lib name
            for lib in shared_libs:
                installed_names["lib%s.dylib"%lib] = \
                    os.path.join(install_dir, "lib%s.dylib"%lib)

            # The names of the files to be modified end with
            # SHLIB_EXT.
            suffix = get_config_var('SHLIB_EXT')
            if suffix is not None:
                suffix = suffix[1:-1] # SHLIB has quotation marks.
            else:
                suffix = get_config_var('SO')
                assert suffix is not None
                
            for phile in outfiles:
                # phile is a file in destroot
                if phile.endswith(suffix): # Is it a library?
                    # See which dylibs it links to by running otool -L
                    cmd = ("otool", "-L", phile)
                    log.info(" ".join(cmd))
                    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
                    stdoutdata, stderrdata = proc.communicate()
                    if stderrdata:
                        print >> sys.stderr, stderrdata
                        raise DistutilsExecError(
                            "Command failed: " + " ".join(cmd))

                    # Loop over output lines from otool -L
                    for line in stdoutdata.splitlines():
                        l = line.lstrip()
                        # dylib is the uninstalled path to a library
                        # that phile links to, but it needs to refer
                        # to the installed path.
                        dylib = l.split()[0]
                        libname = os.path.split(dylib)[1]
                        try:
                            # Look for the installed path
                            newname = installed_names[libname]
                        except KeyError:
                            # It's not a library we know about.
                            pass
                        else:
                            # Fix the name, if it needs fixing.
                            if newname != dylib:
                                cmd = ("install_name_tool", "-change",
                                       dylib, newname, phile)
                                log.info(" ".join(cmd))
                                errorcode = subprocess.call(cmd)
                                if errorcode:
                                    raise DistutilsExecError(
                                        "Command failed:" + " ".join(cmd))
                                    
                        
        return outfiles
        

