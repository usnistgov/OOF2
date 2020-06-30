# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# A GfxWindow always has a current MouseHandler, which knows what to
# do with mouse events on the canvas.  The window's toolboxes can
# install new MouseHandlers.  The base class defined here does
# nothing.


class MouseHandler:
    def acceptEvent(self, eventtype):
        # eventtype is either 'up', 'down', 'move', or 'scroll'.
        # Return True if it can be handled.
        return False
    def up(self, x, y, button, shift, ctrl, data):
        pass
    def down(self, x, y, button, shift, ctrl, data):
        pass
    def move(self, x, y, button, shift, ctrl, data):
        pass
    def scroll(self, x, y, button, shift, ctrl, data):
        pass

    
nullHandler = MouseHandler()            # doesn't do anything
