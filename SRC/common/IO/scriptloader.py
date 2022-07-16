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

import ast

class ScriptLoader:
    def __init__(self, filename, locals=None, errhandler=None):
        self.filename = filename
        self.locals = locals
        fileobj = open(self.filename)
        self.tree = ast.parse(fileobj.read()) # get the Abstract Syntax Tree
        fileobj.close()
            
    def run(self):
        # Loop over top-level nodes of the AST. Run one node at a time
        # by replacing the list of nodes in the AST with a list
        # containing just the one node.  (This appears to work, but I
        # have no idea if it's legal.)
        codebody = self.tree.body
        lastline = codebody[-1].end_lineno
        for snippet in codebody:
            self.tree.body = [snippet]
            code = compile(self.tree, self.filename, "exec")
            exec(code, globals(), self.locals)
            self.progress(snippet.lineno, lastline) 
            if self.stop():
                break

    def progress(self, current, total): # May be redefined in subclasses
        pass

    def stop(self):             # May be redefined in subclasses
        return False
