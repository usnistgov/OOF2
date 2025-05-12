# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# ScriptLoader loads and executes a python file.  It provides hooks
# that can be redefined in a derived class to update a progress bar
# and to halt processing.
from ooflib.common import debug
from ooflib.common import excepthook
from ooflib.SWIG.common import ooferror
import ast
import sys

# class _ScriptExceptHook(excepthook.OOFexceptHook):
#     def __init__(self, scriptloader):
#         self.scriptloader = scriptloader
#     def __call__(self, e_type, e_value, tback):
#         self.scriptloader.error = (e_type, e_value, tback)
#         self.scriptloader.progress.stop()
#         self.scriptloader.errhandler(*self.scriptloader.error)
#         oldhook = excepthook.remove_excepthook(self)

# # This flag is used to switch between different versions of
# # ScriptLoader.run().  The flag is available as a global variable so
# # that test programs know which version is being used, if the format
# # of the output (error messages, in particular) depends on the version
# # of run().
# #  Loader types are
# #    basic: Uses exec(lines), does not do progress bars, can't be interrupted
# #    ast:   Uses Abstract Syntax Tree to evaluate blocks of code
# #    trace: Uses sys.settrace to keep track line execution. May be slow?
# _loaderType = "ast"

# def isLoaderType(lt):
#     assert lt in ("basic", "ast", "trace")
#     return _loaderType == lt

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## TODO: Use chained exceptions?  raise exc from otherexc? 

class _ScriptException(Exception):
    def __init__(self, depth=0):
        self.depth = depth
    # def reraise(self, exc_info):
    #     self.exc_info.append(exc_info)
    #     self.depth -= 1
    #     return self

class ScriptInterrupt(_ScriptException):
    pass

class ScriptException(_ScriptException):
    pass

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ScriptLoader:
    def __init__(self, filename, locals=None, errhandler=None):
        self.filename = filename
        self.error = None

        # When this is used in SRC/common/IO/mainmenu.py, via the
        # PScriptLoader class, locals is set to the main OOF
        # namespace, sys.modules['__main__'].__dict__.
        self.locals = locals

        # self.errhandler is set this way, and not via a default
        # argument, because excepthook.displayTraceBack may change
        # between class definition and instantiation.

        # In GUI mode, displayTraceBack is set to gui_printTraceBack
        # when reporter_GUI.py is loaded.  In text mode, it's an
        # OOFexceptHook instance, defined in excepthook.py.
        self.errhandler = errhandler or excepthook.displayTraceBack

    def get_lines(self, filename):
        fileobj = None
        try:
            fileobj = open(filename, "r")
            lines = fileobj.read()
        except Exception as exc:
            raise ooferror.PyErrUserError(f"Script {filename} not found!")
        finally:
            if fileobj is not None:
                fileobj.close()
        return lines

    # The following methods can be redefined in derived classes.
    
    def progress(self, current, total): # Called to update progress bar
        pass

    def stop(self):     # Called to see if execution should be stopped
        return False

    def done(self):             # Called when execution is complete
        pass

    # def show_error(self, filename): # Called when an error is found
    #     pass
    #self.error = sys.exc_info()

    def run(self):
        debug.fmsg()
        
        # Loop over top-level nodes of the python Abstract Symbol
        # Tree. Run one node at a time by replacing the list of nodes
        # in the AST with a list containing just the one node.  (This
        # appears to work, but I have no idea if it's legal.)
        lines = self.get_lines(self.filename)
        try:
            self.tree = ast.parse(lines, filename=self.filename)
        except SyntaxError as exc:
            raise ScriptException(exc) from exc
            # self.error = sys.exc_info()
            # print(f"Caught SyntaxError: {self.error}")
            # self.errhandler(*self.error)
            # self.show_error(self.filename) # sets self.error
        codebody = self.tree.body

        # Create a globals dict for the script environment. Adding
        # locals to it ensures that if a script defines variables
        # outside a function, that they're available inside the
        # function.
        #
        # TODO: Does this mean that the script can't actually change
        # variables in the main oof namespace?  It's not actually
        # using the main namespace's dictionary.  That does not seem
        # to be the case.

        # Script depth for the script being loaded here is one more
        # than the depth for the script that's loading it, if any. If
        # there is an outer script, then it has defined _scriptdepth_
        # in globals.  If there isn't an outer script, set
        # _scriptdepth_ to 0.
        globs = globals()
        globs['_scriptdepth_'] = globs.get('_scriptdepth_', -1) + 1
        
        if len(codebody) > 0:
            try:
                # self.excepthook = excepthook.assign_excepthook(
                #     _ScriptExceptHook(self))
                lastline = codebody[-1].end_lineno
                for snippet in codebody:
                    # debug.fmsg(f"Running snippet {snippet.lineno}")
                    self.tree.body = [snippet]
                    code = compile(self.tree, self.filename, "exec")
                    globs = globs | self.locals
                    exec(code, globs, self.locals)
                    self.progress(snippet.lineno, lastline) 
                    if self.stop():
                        raise ScriptInterrupt()
            except ScriptInterrupt as exc:
                # This script was interrupted.
                debug.fmsg("Interrupted!")
                raise ScriptInterrupt(exc.depth-1) from exc
            except ScriptException as exc:
                # An exception was raised by a sub-script.
                debug.fmsg("ScriptException!")
                raise ScriptException(exc.depth-1) from exc
            except Exception as exc:
                #debug.fmsg("Exception occured!", exc)
                raise ScriptException() from exc

                # debug.fmsg(f"Caught Exception {exc}")
                # self.error = sys.exc_info()
                # debug.fmsg(f"Calling {self.errhandler}")
                # debug.fmsg(f"   with {self.error=}")
                # # The exception is *not* re-raised explicitly
                # # here.  self.errhandler() can raise it if
                # # necessary.
                # self.errhandler(*self.error)
                # excepthook.remove_excepthook(self.excepthook)
            finally:
                self.done()
        debug.fmsg("done")


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Attempt to use sys.settrace to write a version of ScriptLoader that
# might be less hacky that the AST version above.  However, by adding
# a callback to every Python line, it might be slow.  This may be
# using obsolete error handling.

# import os

# class ScriptLoader:
#     ...
#     def __run__(self):
#         debug.fmsg()
#         lines = self.get_lines(self.filename)
#         sys.settrace(Tracer(self))
#         try:
#             # This sets frame.f_code.co_filename to '<string>'.  Can
#             # we distinguish that from any other exec lines that might
#             # be run by the script?
#             exec(lines, globals()|self.locals, self.locals())
#             # exec(lines, globals(), self.locals)            
#         except _StopLoading:
#             return
#         except SyntaxError as exc:
#             sys.settrace(None)
#             self.show_error(self.filename)
#             raise
#         except Exception as exc:
#             sys.settrace(None)
#             self.error = sys.exc_info()
#             self.errhandler(*self.error)
#         finally:
#             sys.settrace(None)
#             self.done()

# class _StopLoading(Exception):
#     pass

# class Tracer:
#     def __init__(self, loader):
#         self.loader = loader
#         self.fname = os.path.abspath(loader.filename)
#         self.lineno = 0
#     def __call__(self, frame, event, arg):
#         if event == 'line':
#             # print("Tracer:", self.fname, frame.f_lineno)
#             if frame.f_code.co_filename == self.fname:
#                 if self.lineno < frame.f_lineno:
#                     self.lineno = frame.f_lineno
#                     self.loader.progress.progress(self.lineno,
#                                                   self.loader.lastline)
#                     if self.loader.stop():
#                         sys.settrace(None)
#                         raise _StopLoading
#         return self
        
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Simple version of ScriptLoader, that doesn't support progress bars.
# This may be using obsolete error handling.

# class ScriptLoader:
#     ...
#     def run_basic(self):
#         debug.fmsg()
#         lines = self.get_lines(self.filename)
#         try:
#             exec(lines, globals()|locals(), None)
#         except SyntaxError as exc:
#             self.show_error(self.filename)
#             debug.fmsg("run_no_progress: caught", exc)
#             raise
#         except Exception as exc:
#             self.error = sys.exc_info()
#             self.errhandler(*self.error)
#         finally:
#             self.done()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

