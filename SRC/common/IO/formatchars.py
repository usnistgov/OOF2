# -*- python -*-
# $RCSfile: formatchars.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2012/03/09 20:28:17 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Settable parameters controlling the output format

from ooflib.common import enum
from ooflib.common import registeredclass
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

settingsmenu = mainmenu.OOF.Settings.addItem(oofmenu.OOFMenuItem(
    'Output_Formatting',
    help="Formatting options for post-processing analysis output."))

# The menuitems just set the parameter values, so they just have a
# dummy callback function.

def _dummy(*args, **kwargs):
    pass

class Separator(enum.EnumClass("space", "comma", "tab")):
    tip="Characters used between columns in output files."
    discussion="""<para>
    The commands in the <xref linkend='MenuItem-OOF.Mesh.Analyze'/>
    menu write columns of data to output files.  The commands have a
    <varname>separator</varname> argument that sets the character that
    divides one column of data from the next.  The
    <classname>Separator</classname> contains all of the allowed
    separators.
    </para>"""

_separator_strings = {
    Separator("space") : " ",
    Separator("comma") : ", ",
    Separator("tab") : "\t"}

separator_param = enum.EnumParameter(
    'separator', Separator,
    'comma', default='comma',
    tip="The character to appear between columns in output.")

def getSeparator(*args):
    if not args:
        return _separator_strings[separator_param.value]
    return _separator_strings[args[0].string()]

settingsmenu.addItem(oofmenu.OOFMenuItem(
    'Separator',
    callback=_dummy,
    params=[separator_param],
    help="Set the character to appear between columns in output files.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/common/menu/separator.xml")
    ))



comment_char_param = parameter.StringParameter(
    "comment_character", "#", default="#",
    tip="The string used to mark comments in output files.")

def getCommentChar():
    return comment_char_param.value

settingsmenu.addItem(oofmenu.OOFMenuItem(
    'Comment_Character',
    callback=_dummy,
    params=[comment_char_param],
    help="Set the string used to mark comments in output files.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/common/menu/commentchar.xml")
))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# When reading external input files, we want to be able to read any
# weird separator that some other program uses, we don't need to
# distinguish between spaces and tabs, and the discussion string for
# the Separator class is inapplicable.  So here's a separate class to
# use when reading input files.

class InputSeparator(registeredclass.RegisteredClass):
    registry = []
    def split(self, line):
        return line.split(self.character)

class WhiteSpaceSeparator(InputSeparator):
    character = None

registeredclass.Registration(
    'White Space',
    InputSeparator,
    WhiteSpaceSeparator,
    ordering=0,
    tip="Any combination of blanks and tabs.")

class CommaSeparator(InputSeparator):
    character = ','

registeredclass.Registration(
    "Comma",
    InputSeparator,
    CommaSeparator,
    ordering=1,
    tip="A comma.")

class OtherSeparator(InputSeparator):
    def __init__(self, character):
        self.character = character

registeredclass.Registration(
    "Other",
    InputSeparator,
    OtherSeparator,
    ordering=2,
    params=[
        parameter.StringParameter('character', ',', 
                                  tip="The separator character(s).")],
    tip="Any specified character or string of characters.")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## TODO: This should be obsolete, or at least not in this file. 

def showTime():
    return settingsmenu.Show_Time.value

settingsmenu.addItem(oofmenu.CheckOOFMenuItem(
    'Show_Time',
    value=True,
    callback=_dummy,
    help="Show or hide the time column in output files.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/common/menu/showtime.xml")
))
    
