OBSOLETE 
# -*- python -*-
# $RCSfile: profileIO.py,v $
# $Revision: 1.13 $
# $Author: langer $
# $Date: 2010/12/04 03:50:03 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Save and load named profiles -- these objects live in the
# ProfileManager, and are defined in engine/profile.py.
# Meshes which have boundary conditions which use named profiles
# should autosave the relevant named profiles.


from ooflib.SWIG.common import switchboard
from ooflib.common import enum
from ooflib.common.IO import datafile
from ooflib.common.IO import filenameparam
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.engine import profile
AllProfiles = profile.AllProfiles

savemenu = mainmenu.OOF.File.Save

# We can call the loaddata menu item "Profile" safely, because
# only named profiles can be saved.
profile_data_menu = mainmenu.OOF.LoadData.addItem(
    oofmenu.OOFMenuItem('Profile'))

def _newNamedProfile(menuitem, name, profile):
    # Setting the name does the dictionary insertion and bookkeeping.
    profile.set_name(name)

profile_data_menu.addItem(oofmenu.OOFMenuItem(
    'New',
    callback=_newNamedProfile,
    params=[parameter.StringParameter('name', tip="Name of the profile."),
            parameter.RegisteredParameter('profile', profile.CoreProfile,
                                          tip=parameter.emptyTipString)],
    help="Create a new named profile from a data file.",
    discussion="""<para>

    Load a <link
    linkend='Section-Concepts-Mesh-BoundaryCondition-NamedProfile'>named
    <classname>Profile</classname></link>.  This command is only used
    in data files.

    </para>"""))
            

# This function is called from saveprofile, below, and optionally also
# from the mesh, when it has to save profiles.
def writeprofile(datafile, profile_name, profile_object):
    datafile.startCmd(mainmenu.OOF.LoadData.Profile.New)
    datafile.argument('name', profile_name)
    datafile.argument('profile', profile_object)
    datafile.endCmd()
    
def saveprofile(menuitem, filename, mode, format, profile):
    profile_obj = AllProfiles[profile]
    dfile = datafile.writeDataFile(filename, mode.string(), format)
    writeprofile(dfile, profile, profile_obj)
    dfile.close()

# This item is "secret" because it's only invoked either from
# a script or from the boundary condition page's "Save" button.
profile_save = savemenu.addItem(oofmenu.OOFMenuItem(
    'Profile',
    secret=0,
    ordering=90,
    callback=saveprofile,
    threadable=oofmenu.THREADABLE,
    params = [
    filenameparam.WriteFileNameParameter('filename', tip="File name."),
    filenameparam.WriteModeParameter(
                'mode', tip="'w' to (over)write and 'a' to append."),
    enum.EnumParameter('format', datafile.DataFileFormat, datafile.ASCII,
                       tip="File format."),
    profile.ProfileNameParameter('profile', tip="Profile to save.")],
    help="Save a named profile to a file.",
    discussion="""<para>

    Save a <link
    linkend='Section-Concepts-Mesh-BoundaryCondition-NamedProfile'>named
    <classname>Profile</classname></link> to a data file.  The
    available file <varname>formats</varname> are discussed in <xref
    linkend='Section-Concepts-FileFormats'/>.

    </para>"""))

def enable_profile_save(*args):
    if AllProfiles:
        savemenu.Profile.enable()
    else:
        savemenu.Profile.disable()

switchboard.requestCallback("profiles changed", enable_profile_save)
enable_profile_save()
