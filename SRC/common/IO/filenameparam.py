# -*- python -*-
# $RCSfile: filenameparam.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2011/04/29 20:22:42 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import enum
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

class FileNameParameter(parameter.StringParameter):
    def __init__(self, name, value=None, default="", tip=None, ident=None):
        self.ident = ident
        parameter.StringParameter.__init__(self, name, value, default, tip)

class WriteFileNameParameter(FileNameParameter):
    action='w'

class ReadFileNameParameter(FileNameParameter):
    action='r'

class WriteMode(enum.EnumClass("w", "a")):
    tip="Write or append?"
    discussion=xmlmenudump.loadFile("DISCUSSIONS/common/enum/writemode.xml")

class WriteModeParameter(enum.EnumParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        enum.EnumParameter.__init__(self, name, WriteMode, value, default, tip)

class OverwriteParameter(parameter.BooleanParameter):
    pass

