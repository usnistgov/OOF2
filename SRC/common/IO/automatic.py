# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Parameters can take the value 'automatic' to indicate that they
# should be set automatically.

from ooflib.common import utils

class Automatic:
    def __repr__(self):
        return 'automatic'
    def __eq__(self, other):
        # All Automatics are equal to each other, but don't equal
        # anything else.  Menu callbacks will be checking to see if
        # parameters are automatic, so it's convenient to define
        # __eq__.
        return isinstance(other, self.__class__)
    def __hash__(self):
        return hash(id(self.__class__))

automatic = Automatic()

utils.OOFdefine('automatic', automatic)

#####################

# AutomaticNames look just like strings, but when an object with an
# automatically generated name is redefined, its AutomaticName can be
# redefined too.  Code can use isisntance(name, AutomaticName) to
# distinguish AutomaticNames from plain strings.  The 'resolver'
# function of an AutomaticNameParameter should return an
# AutomaticName, if appropriate.  See OutputSchedule.replace() and
# scheduledoutputmenu.outputNameResolver() for examples.

class AutomaticName(str):
    # Here we redefine __repr__ to include 'AutomaticName', but don't
    # redefine __str__.  Doing it this way means that AutomaticNames
    # that appear in scripts are labelled as such, but they aren't
    # labelled in the GUI. 
    def __repr__(self):
        return "AutomaticName('%s')" % str.__str__(self)
    def __hash__(self):
        return str.__hash__(self)

utils.OOFdefine('AutomaticName', AutomaticName)
