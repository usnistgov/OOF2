# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.common import strfunction
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
import struct

# String-based function object used by boundary profiles -- user types
# in a string, and one of these objects gets built.  Profiles'
# __call__ methods provide the relevant arguments.

class ProfileFunctionXT(strfunction.StrFunction):
    def __init__(self, funcstr):
        # x and y are the current location and is guaranteed to be
        # provided. All others are provided if applicable.  nx and ny
        # are the unit-vector components of the boundary normal at
        # this location. i is the node index, s is the arc length,
        # alpha is the fractional arc length.
        strfunction.StrFunction.__init__(
            self, 'x, y, t, nx, ny, i, s, alpha', funcstr)
    def __repr__(self):
        # ProfileFunctions only have to write their values when they
        # are used in ProfileFunctionParameters, which can set
        # themselves from a string. So just write the string.
        return "'%s'" % self.funcstr

class ProfileFunctionX(strfunction.StrFunction):
    def __init__(self, funcstr):
        # x and y are the current location and is guaranteed to be
        # provided. All others are provided if applicable.  nx and ny
        # are the unit-vector components of the boundary normal at
        # this location. i is the node index, s is the arc length,
        # alpha is the fractional arc length.
        strfunction.StrFunction.__init__(
            self, 'x, y, nx, ny, i, s, alpha', funcstr)
    def __repr__(self):
        # ProfileFunctions only have to write their values when they
        # are used in ProfileFunctionParameters, which can set
        # themselves from a string. So just write the string.
        return "'%s'" % self.funcstr

xmlmenudump.XMLObjectDoc(
    'ProfileFunction',
    xmlmenudump.loadFile('DISCUSSIONS/engine/object/profilefunction.xml'))

# The ProfileFunctionParameter can accept either a string or a
# ProfileFunction object, but it only stores a ProfileFunction object.
# Like XYStrFunctionParameter, it needs a special "set" function.

class ProfileFunctionParameterBase(parameter.Parameter):
    def __init__(self, name, value=None, default=None, tip=None):
        parameter.Parameter.__init__(self, name,
                                         value=value,
                                         default=default, tip=tip)
    def set(self, value):
        if isinstance(value, (str, bytes)):
            self._value = self.profileClass(value)
        elif isinstance(value, self.profileClass):
            self._value = value
        elif value is None:
            self._value = None
        else:
            raise parameter.ParameterMismatch(
                'Got ' + repr(value) + ' for Parameter ' + self.name)
        self.timestamp.increment()
    def binaryRepr(self, datafile, value):
        length = len(value.funcstr)
        return struct.pack('>i', length) + bytes(value.funcstr, "UTF-8")
    def binaryRead(self, parser):
        b = parser.getBytes(struct.calcsize('>i'))
        (length,) = struct.unpack('>i', b)
        return self.profileClass(parser.getBytes(length).decode())
    def valueDesc(self):
        return ("A <link linkend='Object-ProfileFunction'><classname>" +
                self.profileClass.__name__ + "</classname></link> object.")

class ProfileFunctionXParameter(ProfileFunctionParameterBase):
    profileClass = ProfileFunctionX

class ProfileFunctionXTParameter(ProfileFunctionParameterBase):
    profileClass = ProfileFunctionXT

utils.OOFdefine('ProfileFunctionX', ProfileFunctionX)
utils.OOFdefine('ProfileFunctionXT', ProfileFunctionXT)

