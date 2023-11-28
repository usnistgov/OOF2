# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import utils
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter

indent =  "      "
indent2 = "           "

paramdict = {}                          # all parameter types that are used
regclassdict = {}                       # Every registered class we see.
enumdict = {}                           # All Enum types that are used

def textdumper(menuitem, file):
    if menuitem.items or menuitem.getOption('no_doc'):
        return                      # skip submenus, only do actual commands
    print(menuitem.path(), file=file)
    if menuitem.callback:
        funcname, modulename = menuitem.getcallbackname()
        print(indent, "callback: Function '%s' in module '%s'" % \
              (funcname, modulename), file=file)
    if menuitem.helpstr:
        print(indent, "help:", menuitem.helpstr, file=file)
    else:
        print(indent, "MISSING HELP STRING.", file=file)
    if menuitem.secret:
        print(indent, "secret:", menuitem.secret, file=file)
    print(indent, "threadability:", menuitem.threadable, file=file)
    if menuitem.options:
        print(indent, "options:", end=' ', file=file)
        for key,val in menuitem.options.items():
            print(key, "=", val, end=' ', file=file)
        print(file=file)
    if menuitem.params:
        print(indent, "Parameters:", file=file)
        for param in menuitem.params:
            tip = param.tip or "MISSING TIP"
            print(indent2, "'%s'\t%s\t%s" \
                  %(param.name, param.classRepr(), tip), file=file)
            add_params(param)
    print(file=file)
            # v = param.valueRepr()
            # if v:
            #     paramdict[param.classRepr()] = v


# Recursively add parameters amd registered classes to the dictionaries.
def add_params(param):
    global enumdict
    global paramdict
    global regclassdict
    
    v = param.valueRepr()
    if v:
        paramdict[param.classRepr()] = param
    # Check for RegisteredParameters
    try:
        rlist = param.registry
    except AttributeError:
        pass
    else:
        for r in rlist:
            regclassdict[r.subclass.__name__] = r
            for p in r.params:
                add_params(p)
    # Check for EnumParameters
    if isinstance(param, enum.EnumParameter):
        enumdict[param.enumclass] = 1


def textmenudump(file):
    global paramdict
    global enumdict
    paramdict = {}
    enumdict = {}
    mainmenu.OOF.apply(textdumper, file)
    
    print("\n\n------------ Registered Classes -------------\n", file=file)
    rlist = sorted(list(regclassdict.items()))
    for rname, reg in rlist:
        basenames = [regclass.__name__ for regclass in reg.registeredclasses]
        print(indent, rname, "(%s)" % ",".join(basenames), file=file)
        if reg.tip:
            print(indent, "tip:", reg.tip, file=file)
        else:
            print(indent, "MISSING TIP STRING.", file=file)
        for p in reg.params:
            print(indent2, "'%s'\t%s" % (p.name, p.classRepr()), file=file)
        print(file=file)

    print("\n\n------------ Enum Classes ------------\n", file=file)
    elist = list(enumdict.keys())
    elist.sort()
    for enum in elist:
        print(indent, enum.__name__, file=file)
        for name in enum.names:
            try:
                helpstr = enum.helpdict[name]
                print(indent2, name, ": ", helpstr, file=file)
            except KeyError:
                print(indent2, name, ": MISSING HELP STRING", file=file)
        print(file=file)

    print("\n\n------------ Parameter Classes ------------\n", file=file)
    plist = list(paramdict.items())
    plist.sort()
    for name, p in plist:
        print(indent, name, file=file) #, v
        if p.tip:
            print(indent2, "tip:", p.tip, file=file)
        else:
            print(indent2, "MISSING TIP STRING", file=file)
        vlist = p.valueRepr().split('\n')
        for vv in vlist:
            print(indent2, vv, file=file)
        print(file=file)
    file.close()


########################

class MenuDumpFormat(enum.EnumClass("text", "xml")):
    tip = "File formats for the &oof2; API dump."
    discussion = """<para>
    <classname>MenuDumpFormat</classname> objects are used by <xref
    linkend='MenuItem-OOF.Help.API_Listing'/> to specify the output
    format.
    </para>"""

from ooflib.common.IO import xmlmenudump

def menudump(menuitem, filename, format):
    file = open(filename, 'w')
    if file:
        try:
            if format=="text":
                textmenudump(file)
            elif format=="xml":
                xmlmenudump.xmlmenudump(file)
        finally:
            file.close()

mainmenu.OOF.Help.addItem(oofmenu.OOFMenuItem(
    'API_Listing',
    callback=menudump,
    threadable = oofmenu.UNTHREADABLE,
    secret = not debug.debug(),
    params=[
    parameter.StringParameter('filename', 'oof2_api.txt', tip="File name."),
    enum.EnumParameter('format', MenuDumpFormat, value="text",
                       tip="Format for the api listing, 'text' or 'xml'.")
    ],
    help="Create a verbose listing of all OOF menu commands.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/menu/api_listing.xml')
    ))
