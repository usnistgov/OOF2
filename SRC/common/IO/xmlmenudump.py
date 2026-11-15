# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common import oofenum
from ooflib.common import labeltree
from ooflib.common.IO import parameter
import sys

enumdict = {}
regclassdict = {}

# Keep track of which parameter types need to be documented.  This
# function is called on every parameter that appears in a menu item.

def process_param(param):
    global regclassdict
    global enumdict
    # Check for RegisteredParameters
    if isinstance(param, parameter.RegisteredParameter):
        processRegClass(param.reg)  # recursively includes reg. class params
    # Check for EnumParameters
    if isinstance(param, oofenum.EnumParameter):
        enumdict[param.enumclass.__name__] = param.enumclass
    elif isinstance(param, oofenum.ListOfEnumsParameter):
        for enumclass in param.enumclasses:
            enumdict[enumclass.__name__] = enumclass

def processRegClass(regclass):
    try:
        if regclass.secret:
            return
    except AttributeError:
        pass
    regclassdict[regclass.__name__] = regclass
    for r in regclass.registry:
        for p in r.params:
            process_param(p)

# Registered (base) classes that need to be documented but for some
# reason aren't picked up by looping over menu items and their
# parameters should be identified by calling addRegisteredClass.  We
# don't immediately call processRegClass on them, because the registry
# might not be filled yet.

otherregclasses = []
def addRegisteredClass(regclass):
    otherregclasses.append(regclass)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

indexItems = []

def xmlIndexEntry(name, category, xmlid):
    indexItems.append((name, category, xmlid))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
        
def regclassID(regclass):
    # xml id string to mark the definition of a base RegisteredClass
    return f"RegisteredClass-{regclass.__name__}"
def regID(reg):
    return f"RegisteredClass-{reg.subclass.__name__}"

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##

# xrefListing converts a list of docbook ids to a list of xref links
# for the "See Also" sections of menuitems and registeredclasses.  The
# input list items are either docbook ids (strings) or a tuple (id,
# text).

def xrefListing(xrefs):
    assert len(xrefs) > 0
    xrefs.sort(key=sectionsorter)
    texts = []
    done = []                   # check for duplicates
    for xref in xrefs:
        if xref not in done:
            if isinstance(xref, str):
                texts.append(f'<xref linkend="{xref}"/>')
            elif isinstance(xref, tuple):
                texts.append(f'<xref linkend="{xref[0]}" endterm="{xref[1]}"/>')
            else:
                raise ooferror.PyErrPyProgrammingError(f"bad xref: {xref}")
            done.append(xref)

    listitems = [f'<listitem><simpara>{t}</simpara></listitem>' for t in texts]
    return ("<itemizedlist>" +
            "\n".join(listitems) +
            "</itemizedlist>")
        
# Sorting key function for docbook ids. iddict is populated when
# xmlmenudump() is called.  It is a dictionary whose keys are the
# docbook ids of the xref targets that are *not* created automatically
# by xmlmenudump, and whose values are the sorting order of those
# targets.  It's computed by the manual-generating script,
# MAN_OOF2/xmldump.py, before it calls xmlmenudump.

iddict = {}                     # iddict[docbook_id] = sorting_order

def sectionsorter(xmlid):
    # A tuple of the form (id, text) is sorted on the id, even though
    # the replacement text will be printed.  I'm not sure this is a
    # good idea, but I'm also not sure we use it.
    if isinstance(xmlid, (tuple, list)):
        return sectionsorter(xmlid[0])

    # Sections of the manual with ids in iddict are listed first, in
    # the order in which the targets appear in the manual.
    try:
        return (0, iddict[xmlid])
    except KeyError:
        pass
    # MenuItems, RegisteredClasses, etc, are listed in alphabetical
    # order within their category.  This relies on all of the ids
    # starting with the proper prefix.
    if xmlid.startswith("MenuItem-"):
        return (1, xmlid)
    if xmlid.startswith("RegisteredClass-"):
        return (2, xmlid)
    if xmlid.startswith("Property-"):
        return (3, xmlid)
    if xmlid.startswith("Enum-"):
        return (4, xmlid)
    if xmlid.startswith("Object-"):
        return (5, xmlid)
    if xmlid.startswith("Figure-"):
        return (6, xmlid)

    print(f"*** xmlmenudump: Uncategorized docbook id {xmlid}",
          file=sys.stderr)
    return (100, xmlid)
   

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##

# RegisteredClasses, Registrations, MenuItems, and Enums (and possibly
# other classes) have 'discussion' strings, which go into the xml
# manual.  If these strings are long, it's a pain to have them inside
# the source code (especially because editing xml in emacs's
# python-mode is a nuisance).  So those strings live in files in the
# MAN_OOF2 directory.  The xml menu dump command only works when OOF2
# is run in the MAN_OOF2 directory.  The loadFile function allows
# discussion strings stored in files to be associated with the
# appropriate objects without actually reading the files until
# xmlmenudump is run.  func is an optional function for processing the
# string in the file before inserting it into the xml.
#
# The discussion section can be suppressed by setting discussion to
# emptyDiscussion. 

def loadFile(filename, func=None):
    return DiscussionFile(filename, func)

class DiscussionFile:
    def __init__(self, filename=None, func=None):
        self.filename = filename
        self.func = func
    def read(self, obj):
        # This comment makes it easier to find the source file in case
        # the xml processor reports errors in the combined file.
        namecomment = f"<!-- FILE: {self.filename} -->\n"
        if self.filename:
            phile = open(self.filename, 'r')
            text = phile.read()
        else:
            text = None
        if self.func:
            return namecomment + self.func(text, obj)
        return namecomment + text

class DiscussionFunc:
    def __init__(self, func):
        # func is a function that returns a string or a DiscussionFile
        self.func = func
    def read(self, obj):
        return self.func(obj)

def getDiscussion(obj):
    ## Raises AttributeError if the object doesn't have a discussion
    ## or if its discussion isn't either a string or a DiscussionFile.
    if isinstance(obj.discussion, (str, bytes)):
        return obj.discussion
    if obj.discussion is emptyDiscussion:
        return emptyDiscussion
    return obj.discussion.read(obj)

def getHelp(obj):                       # get help, helpstr, or tip
    for helpattr in ("helpstr", "help", "tip"):
        try:
            whelp = getattr(obj, helpattr)
        except AttributeError:
            pass
        else:
            if isinstance(whelp, (str, bytes)):
                if not whelp.endswith('.'):
                    whelp = whelp + '.'
                return whelp
            return whelp.read(obj)
    raise AttributeError(obj, "helpstr, help, or tip")

emptyDiscussion = DiscussionFile(None, None)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#    

# Keep track of other objects that need to be documented -- this
# includes anything except for RegisteredClasses, Enums, Outputs, and
# MenuItems. Every file that defines such objects must create an
# XMLObjectDoc object for each object type.  The 'discussion' argument
# should be a complete docbook refentry element or a DiscussionFile
# object containing a refentry.  The refentry id should be
# 'Object-name' where 'name' is the name of the object.

objDocs = labeltree.LabelTree()

class XMLObjectDoc:
    def __init__(self, name, discussion, ordering=0):
        self.name = name
        self.discussion = discussion
        objDocs.__setitem__(name, self, ordering)

# Other parts of the code that want to add a complete Section to the
# reference manual can register a callback here.  The callback will be
# called with a file argument.

otherSections = []

def addSection(callback, ordering):
    otherSections.append((ordering, callback))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def dumpMenu(phile, menu, parent, sectiontitle=None):
    # parent is passed in as an argument so that the LoadData menu,
    # which has no parent data, can still be listed as a submenu of
    # the main menu.  Not giving it a parent makes it harder for data
    # files to escape the LoadMenu submenu, but logically to the user
    # it's still a submenu.
    if menu.getOption('no_doc'):
        return
    path = menu.path()
    role = 'Menu' if parent else 'RootMenu'
    attrs = f'xreflabel="{path}" id="MenuItem-{path}" role="{role}"'
    print(f"<section {attrs}>", file=phile)
    print(f"<title>{sectiontitle or path}</title>", file=phile)
    
    xmlIndexEntry(path, "Menu", f"MenuItem-{path}")
    try:
        print(f"<subtitle>{getHelp(menu)}</subtitle>", file=phile)
    except AttributeError:
        pass
    try:
        discus = getDiscussion(menu)
    except AttributeError:
        print(f"<para>MISSING MENU DISCUSSION: {path}</para>", file=phile)
    else:
        if discus is not emptyDiscussion:
            print(discus, file=phile)

    if parent is not None:
        linkend = f"MenuItem-{parent.path()}"
        print(f"<simpara>Parent Menu: <xref linkend='{linkend}'/></simpara>",
              file=phile)

    # Create alphabetical lists of submenus and commands.  It's more
    # convenient to find things in alphabetical lists in the manual,
    # even if they're not presented alphabetically in the GUI.
    # Sorting can be suppressed by setting alphabetize=False in the
    # OOFMenuItem constructor.
    commands = []
    submenus = []
    for item in menu.items:
        if not item.getOption('no_doc'):
            if item.items:
                submenus.append(item.name)
            else:
                commands.append(item.name)
    if menu.alphabetize:
        submenus.sort()
        commands.sort()

    if submenus:
        print("<itemizedlist spacing='compact'>", file=phile)
        print(f" <title>{path} Submenus</title>", file=phile)
        for submenu in submenus:
            item = menu.getItem(submenu)
            if item.getOption('no_doc'):
                continue
            itempath = item.path()
            print(" <listitem><simpara>", file=phile)
            print(f"  <link linkend='MenuItem-{itempath}'><command>{itempath}</command></link>",
                  file=phile)
            try:
                helpstr = getHelp(item)
                if helpstr:
                    print("&emdash;", helpstr, file=phile)
            except AttributeError:
                pass
            print(" </simpara></listitem>", file=phile)
        print("</itemizedlist>", file=phile)

    if commands:
        print("<itemizedlist spacing='compact'>", file=phile)
        print(f" <title>{path} Commands</title>", file=phile)
        for command in commands:
            item = menu.getItem(command)
            if item.getOption('no_doc'):
                continue
            itempath = item.path()
            print(" <listitem><simpara>", file=phile)
            print(f"  <xref linkend='MenuItem-{itempath}'/>", file=phile)
            try:
                helpstr = getHelp(item)
                if helpstr:
                    print("&emdash;", helpstr, file=phile)
            except AttributeError:
                pass
            print(" </simpara></listitem>", file=phile)
        print("</itemizedlist>", file=phile)

    xrefs = menu.xmlXRefs()
    if xrefs:
        print(" <simplesect>", file=phile)
        print("   <title>See Also</title>", file=phile)
        print(f"   <para>{xrefListing(xrefs)}</para>", file=phile)
        print(" </simplesect>", file=phile)

    for submenu in submenus:
        dumpMenu(phile, menu.getItem(submenu), menu)
    for command in commands:
        dumpMenuItem(phile, menu.getItem(command))

    print(f"</section> <!-- {path} -->", file=phile)


def dumpMenuItem(phile, menuitem):
    if menuitem.getOption('no_doc'):
        return
    path = menuitem.path()
    xmlIndexEntry(path, "Menu Item", f"MenuItem-{path}")
    print(f'<refentry xreflabel="{path}" id="MenuItem-{path}" role="MenuItem">',
          file=phile)
    print(" <refnamediv>", file=phile)
    print(f"  <refname>{path}</refname>", file=phile)
    try:
        helpstr = getHelp(menuitem)
        if helpstr:
            print(f"  <refpurpose>{helpstr}</refpurpose>", file=phile)
        else:
            print("  <refpurpose></refpurpose>", file=phile)
    except AttributeError:
        print(f"  <refpurpose>MISSING HELP STRING: {path}</refpurpose>",
              file=phile)
    print(" </refnamediv>", file=phile)

    menuitem.xmlSynopsis(phile)

    print(" <refsect1>", file=phile)
    print("   <title>Details</title>", file=phile)
    print("   <itemizedlist>", file=phile)
    print(
        f"""
        <listitem>
          <simpara>
            Parent Menu: <xref linkend='MenuItem-{menuitem.parent.path()}'/>
          </simpara>
        </listitem>""",
        file=phile)
    if menuitem.callback:
        fname, mname = menuitem.getcallbackname()
        print(
          f"""
          <listitem>
             <simpara>
                Callback: function <function>{fname}</function> in module <filename>{mname}</filename>
             </simpara>
          </listitem>""",
        file=phile)

    # Menu items are enabled and disabled dynamically, so the current
    # state of the flag isn't relevant to the documentation. Don't
    # print options unless the option list contains something other
    # than "disabled".
    if menuitem.options and list(menuitem.options.keys()) != ['disabled']:
        print("  <listitem><simpara>", file=phile)
        print("   Options:", file=phile)
        for key, val in list(menuitem.options.items()):
            if key != "disabled":
                print(
                  f" <varname>{key}</varname>=<constant>{repr(val)}</constant>",
                  file=phile)
        print("  </simpara></listitem>", file=phile)

    menuitem.xmlParams(phile)

    print("   </itemizedlist>", file=phile)
    print(" </refsect1>", file=phile) # details section

    try:
        discus = getDiscussion(menuitem)
    except AttributeError:
        print(" <refsect1>", file=phile)
        print("  <title>Description</title>", file=phile)
        print(f"  <para>MISSING MENUITEM DISCUSSION: {path}</para>", file=phile)
        print(" </refsect1>", file=phile)
    else:
        if discus is not emptyDiscussion:
            print(" <refsect1>", file=phile)
            print("  <title>Description</title>", file=phile)
            print(f"  {discus}", file=phile)
            print(" </refsect1>", file=phile)

    xrefs = menuitem.xmlXRefs() 
    if xrefs:
        print(" <refsect1>", file=phile)
        print("   <title>See Also</title>", file=phile)
        print(f"   <para>{xrefListing(xrefs)}</para>", file=phile)
        print(" </refsect1>", file=phile)
    
    print("</refentry>", file=phile)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def xmlmenudump(phile, xmlids):
    global iddict
    iddict = xmlids

    # Clear global dictionaries, in case this isn't the first time
    # this function has been run.
    global enumdict
    global regclassdict
    regclassdict = {}
    enumdict = {}

    print("<!-- This file is generated by xmlmenudump.  DO NOT EDIT IT. -->", file=phile)
    print(file=phile)
    print("<chapter id='Chapter-Reference'><title>User Reference</title>", file=phile)
    print("""
    <section id="Section-Reference-HowTo">
    <title>How to Use This Section</title>
      <para>
      This chapter consists of sets of reference pages for some of
      the important objects that appear in &oof2; scripts. Since all
      &oof2; operations can be scripted, these reference pages are the
      penultimate source for details on how everything works in
      &oof2;.<footnote><para>The ultimate source is the code itself,
      naturally.</para></footnote>
      </para>
      <para>
      Each &oof2; operation, and each line in an &oof2; script, is a
      single command from the &oof2; <link
      linkend='MenuItem-OOF'>menus</link>.  The menus are
      hierarchical, and the reference page for each menu item contains
      a link to page for its parent menu.
      <tip><para><emphasis>Read the parent
      page!</emphasis> Often it contains useful information that
      applies to all of the commands in the menu.</para></tip>
      </para>
      <para>
      The same advice applies to the pages for the <link
      linkend='Section-RegisteredClasses'><classname>RegisteredClass</classname></link>
      objects. A <classname>RegisteredClass</classname> <link
      linkend='Section-RegisteredBaseClasses'>base class</link>
      describes a <emphasis>category</emphasis> of object which is
      used as an argument in menu commands.  For example, a command
      that creates a boundary condition will have an argument whose
      value must be one of the members of the <xref
      linkend='RegisteredClass-BC'/> category.  Each base class
      contains many different <emphasis>subclasses</emphasis>,
      representing different varieties of things in the base class
      category.  For example, the <xref linkend='RegisteredClass-BC'/>
      class contains <xref linkend='RegisteredClass-DirichletBC'/> and
      <xref linkend='RegisteredClass-NeumannBC'/>, and other boundary
      condition types.  Each subclass has its own reference page,
      which contains a link to the base class's page.  Read both
      pages!  The base class page often contains important information
      relevant to all of the subclasses.
      </para>
    </section>
    """, file=phile)

    ## Add sections defined elsewhere.
    otherSections.sort()
    for ordering, otherSectionCB in otherSections:
        otherSectionCB(phile)

    ########

    print("<section id='Section-OtherObjects' role='toc-never'>", file=phile)
    print(" <title>Other Objects</title>", file=phile)
    print(""" <para>

    This section covers other objects that are used as arguments to
    &oof2; commands.

    </para>""", file=phile)

    # TODO: Sort alphabetically?
    objDocs.apply2(function=printObjDocs, postfunc=postPrintObjDocs,
                   phile=phile)
    print("</section>", file=phile)         # end of other objects section

    #########

    # List of all objects that have reference pages.

    indexItems.sort(key=lambda x: x[0].lower())
    print("<section id='Section-Reference-Index'>", file=phile)
    print(" <title>Searchable Index of Reference Pages</title>", file=phile)
    print(""" 
 <para>This index is simply an alphabetical list of all of the menu
 items, <classname>RegisteredClasses</classname>,
 <foreignphrase>etc.</foreignphrase> that are described in <xref
 linkend='Chapter-Reference'/>.  Each entry links to its reference
 page. The hope is that putting them all in one list makes it easy to
 find what you're looking for.  Use your browser's Find command.</para>""", file=phile)
    
    print('<table rowsep="0" colsep="0" frame="none" pgwide="0">', file=phile)
    print('<tgroup cols="2"><tbody>', file=phile)
    for name, category, xmlid in indexItems:
        print(f"""
        <row>
          <entry>
            <simpara>
              <link linkend='{xmlid}'>{name}</link>
            </simpara>
          </entry>
          <entry>
            <simpara>{category}</simpara>
          </entry>
        </row>
        """,
        file=phile)
    print("</tbody></tgroup></table>", file=phile)
    print("</section>", file=phile)

    print("</chapter>", file=phile)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def mainMenuSection(phile):
    from ooflib.common.IO import mainmenu      # delayed, to avoid import loop
    dumpMenu(phile, mainmenu.OOF, None, sectiontitle="The Main OOF Menu")

addSection(mainMenuSection, 0)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## RegisteredClasses

def regClassSection(phile):

    for regclass in otherregclasses:
        processRegClass(regclass)
    
    print("<section id='Section-RegisteredClasses' role='toc-always'>",
          file=phile)
    print(" <title>Registered Classes</title>", file=phile)
    print("""<para>

Many command arguments in &oof2; require the user to choose one of a
set of related objects.  These sets are called
<classname>RegisteredClasses</classname>, because the objects are
constructed from <classname>Registrations</classname>, stored in a
<classname>Registry</classname>, which provide the information needed
to create the objects.  All of that is completely irrelevant to you,
the &oof2; user, but helps to explain the title of this section.
</para>

<para> Section <xref linkend='Section-RegisteredBaseClasses'/> lists
the <classname>RegisteredClasses</classname> and the choices
(subclasses) available for each class.  Section <xref
linkend='Section-RegisteredSubclasses'/> describes the subclasses and
lists the parameters required to create the objects.  Some subclasses
may be members of more than one
<classname>RegisteredClass</classname>.

    </para>""", file=phile)
    regclassnames = sorted(list(regclassdict.keys()))
    registrationdict = {}
    print("<section id='Section-RegisteredBaseClasses' role='toc-never'>",
          file=phile)
    print(" <title>RegisteredClass Base Classes</title>", file=phile)
    print(" <itemizedlist spacing='compact'>", file=phile)

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    ## List of RegisteredClass base classes
    
    for regclassname in regclassnames:
        regclass = regclassdict[regclassname]
        for reg in regclass.registry:
            registrationdict[reg.subclass.__name__] = reg
        try:
            tip = getHelp(regclass)
        except AttributeError:
            tip = f"MISSING TIP STRING: {regclassname}"
        print(f"""
        <listitem>
          <simpara>
            <xref linkend='{regclassID(regclass)}'/>  &emdash; {tip}
          </simpara>
        </listitem>
        """,
              file=phile)
            
    print("  </itemizedlist>", file=phile)
    print("</section>", file=phile)
    
    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    ## List of subclasses for all base classes, sorted by name.

    subclassnames = sorted(list(registrationdict.keys()))

    print("<section id='Section-RegisteredSubclasses' role='toc-never'>", file=phile)
    print(" <title>RegisteredClass Subclasses</title>", file=phile)
    print(" <itemizedlist spacing='compact'>", file=phile)
    for name in subclassnames:
        try:
            reg = registrationdict[name]
        except KeyError:
            continue
        print("  <listitem><simpara>", file=phile)
        try:
            tip = getHelp(reg)
        except AttributeError:
            tip = f"MISSING TIP STRING: {name}"
        print(f"    <xref linkend='{regID(reg)}'/> &emdash; {tip}",
              file=phile)
        print("  </simpara></listitem>", file=phile)
    print(" </itemizedlist>", file=phile)
    print("</section>", file=phile)

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    ## Reference pages for each base class and subclass.

    for regclassname in regclassnames:
        regclass = regclassdict[regclassname]
        xmlIndexEntry(regclassname,"RegisteredClass base class",
                      regclassID(regclass))

        # Reference page for the base class
        try:
            tip = getHelp(regclass)
        except AttributeError:
            tip = f"MISSING TIP STRING: {regclassname}"
        print(f"""
<refentry xreflabel='{regclassname}' id='{regclassID(regclass)}' role='RegisteredClass'>
  <refnamediv>
    <refname>{regclassname}</refname>
    <refpurpose>{tip}</refpurpose>
  </refnamediv>
  <refsect1>
    <title>Subclasses</title>
      <para>
         Subclasses are listed as they appear in the GUI and (in
         parentheses) as they appear in scripts.
      </para>
      <itemizedlist spacing='compact'>""",
      file=phile)

        # Don't sort.  Registrations are listed on the base class page
        # in the order in which they appear in the GUI.
        for reg in regclass.registry:
            if reg.secret:
                continue
            registrationdict[reg.subclass.__name__] = reg
            try:
                tip = getHelp(reg)
            except AttributeError:
                tip = f"MISSING TIP STRING: {reg.subclass.__name__}"
            print(f"""
            <listitem>
              <simpara>
                <link linkend='{regID(reg)}'>{reg.name()}</link>   (<classname>{reg.subclass.__name__}</classname>) &emdash; {tip}
              </simpara>
            </listitem>
            """,
                  file=phile)
        print(
            """
        </itemizedlist>
      </refsect1>""", file=phile)

        try:
            discus = getDiscussion(regclass)
        except AttributeError:
            print("  <refsect1>", file=phile)
            print("   <title>Description</title>", file=phile)
            print(f"<para>MISSING REGCLASS DISCUSSION: {regclassname}</para>",
                  file=phile)
            print("  </refsect1>", file=phile)
        else:
            if discus is not emptyDiscussion:
                print("  <refsect1>", file=phile)
                print("   <title>Description</title>", file=phile)
                print(f"    {discus}", file=phile)
                print("  </refsect1>", file=phile)
        xrefs = getattr(regclass, "xrefs", [])
        if xrefs:
            print("<refsect1>", file=phile)
            print("<title>See Also</title>", file=phile)
            print(f"<para>{xrefListing(xrefs)}</para>", file=phile)
            print("</refsect1>", file=phile)

        print(f" </refentry> <!-- {regID(reg)} -->", file=phile)

        # Loop over subclasses of regclass

        for reg in regclass.registry:
            if reg.secret:
                continue
            name = reg.subclass.__name__
            xmlIndexEntry(name, "RegisteredClass subclass",
                              regID(reg))
            try:
                tip = getHelp(reg)
            except AttributeError:
                tip = f"MISSING TIP STRING: {name}"
            args = ', '.join([f'<varname>{p.name}</varname>'
                              for p in reg.params])
            print(f"""
<refentry xreflabel='{name}' id='{regID(reg)}' role='RegisteredClass'>
  <refnamediv>
    <refname>{reg.name()} ({name})</refname>
    <refpurpose>{tip}</refpurpose>
  </refnamediv>
  <refsynopsisdiv>
     <simpara>
       <classname>{name}</classname>({args})
     </simpara>
   </refsynopsisdiv>
   <refsect1>
     <title>Details</title>
     <itemizedlist>
       <listitem>
         <simpara>
            Base class{'es' if len(reg.registeredclasses)>1 else ''}:
                """, file=phile)
            # List base classes of this subclass
            for regclass in reg.registeredclasses:
                print(
                    f""" <link linkend='{regclassID(regclass)}'>
                    <classname>{regclass.__name__}</classname>
                    </link>""",
                    file=phile)
            print(" </simpara>\n</listitem>", file=phile)
            # List parameters
            if reg.params:
                print("""
                <listitem>
                   <para>
                     Parameters:
                     <variablelist>
                """, file=phile)
                for param in reg.params:
                    try:
                        tip = getHelp(param)
                    except AttributeError:
                        tip = f"MISSING TIP STRING: {name, param.name}"
                    print(f"""
                       <varlistentry>
                         <term><varname>{param.name}</varname></term>
                         <listitem>
                            <simpara>{tip} <emphasis>Type</emphasis>: {param.valueDesc()}</simpara>
                         </listitem>
                        </varlistentry>""", file=phile)
                print("""
                     </variablelist> <!-- End of parameter list -->
                   </para>
                </listitem>""", file=phile)
                # end if there are parameters
            # Discussion section
            try:
                discus = getDiscussion(reg)
            except AttributeError:
                discus = f"<para>MISSING REGCLASS DISCUSSION: {name}</para>"
            print(f"""
            </itemizedlist>
            </refsect1> <!-- End of details section -->
            <refsect1>
              <title>Description</title>
            {discus}
            </refsect1>
            """, file=phile)
            # Cross references
            if reg.xrefs:
                print(f"""
                <refsect1>
                  <title>See Also</title>
                  <para>{xrefListing(reg.xrefs)}</para>
                </refsect1>
                """, file=phile)
            print("</refentry>", file=phile)

    # End loop over base RegisteredClasses
    print("</section> <!-- End of RegisteredClass section -->", file=phile)


# This section has a large ordering value so that it comes *after* any
# section that calls process_param, ensuring that all RegisteredClass
# definitions have been found.

addSection(regClassSection, ordering=1000)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def enumSection(phile):
    print("<section id='Section-Enums' role='toc-never'>", file=phile)
    print(" <title>Enumerated Types</title>", file=phile)
    print(""" <para>

    Many command arguments in &oof2; require the user to choose from a
    small set of predetermined constant values, called
    <classname>Enums</classname>.<footnote><simpara>This
    <classname>Enum</classname> is not the same as the builtin Python
    <classname>enum.Enum</classname> class.</simpara></footnote> These
    <classname>Enums</classname> differ from <link
    linkend='Section-RegisteredClasses'><classname>RegisteredClasses</classname></link>
    in that they are much simpler objects, and never require any
    parameters.  This section describes all of the
    <classname>Enum</classname> classes and lists their allowed
    values.  </para>

    <para>

     In the GUI, <classname>Enum</classname> parameters are chosen
     from a pull-down menu.  In scripts, <classname>Enum</classname>
     parameters can be set to the <emphasis>name</emphasis> of the
     <classname>Enum</classname> object, in quotation marks.  For
     example, if you want to change the default <link
     linkend="Section-Graphics-New-Layer-Policy">New Layer
     Policy</link>, you could put the following line in the <link
     linkend="Section-oof2rc"><filename>.oof2rc</filename></link> in
     your home directory:
    
    <blockquote><simpara><userinput>
    <link linkend="MenuItem-OOF.Settings.Graphics_Defaults.New_Layer_Policy">OOF.Settings.Graphics_Defaults.New_Layer_Policy</link>(policy=<link linkend="Enum-NewLayerPolicy">'Single'</link>)
    </userinput></simpara></blockquote>
    
    Here, <varname>policy</varname> is a parameter that requires an object from the <xref linkend="Enum-NewLayerPolicy"/> class.

    </para>""", file=phile)

    enumnames = sorted(list(enumdict.keys()))

    print("<itemizedlist spacing='compact'>", file=phile)
    for enumname in enumnames:
        enumclass = enumdict[enumname]
        try:
            tip = getHelp(enumclass)
        except AttributeError:
            tip = f"MISSING ENUM TIP STRING: {enumname}"
        print("<listitem><simpara>", file=phile)
        print(f" <xref linkend='Enum-{enumname}'/> &emdash; {tip}", file=phile)
        print("</simpara></listitem>", file=phile)        
    print("</itemizedlist>", file=phile)
    
    for enumname in enumnames:
        enumclass = enumdict[enumname]
        xmlIndexEntry(enumname, f"Enum class", f"Enum-{enumname}")
        print(
         f" <refentry xreflabel='{enumname}' id='Enum-{enumname}' role='Enum'>",
         file=phile)
        print("  <refnamediv>", file=phile)
        print(f"   <refname>{enumname}</refname>", file=phile)
        try:
            tip = getHelp(enumclass)
        except AttributeError:
            tip = f"MISSING ENUM TIP STRING: {enumname}"
        print(f"   <refpurpose>{tip}</refpurpose>", file=phile)
        print("  </refnamediv>", file=phile)        

        try:
            discus = getDiscussion(enumclass)
        except AttributeError:
            print(" <refsect1>", file=phile)
            print("  <title>Description</title>", file=phile)
            print(f"<para>MISSING ENUM DISCUSSION: {enumname}</para>",
                  file=phile)
            print(" </refsect1>", file=phile)
        else:
            if discus is not emptyDiscussion:
                print(" <refsect1>", file=phile)
                print("  <title>Description</title>", file=phile)
                print(f"  {discus}", file=phile)
                print(" </refsect1>", file=phile)
        print(" <refsect1>", file=phile)
        print("  <title>Values</title>", file=phile)
        print("  <itemizedlist spacing='compact'>", file=phile)
        for name in enumclass.names:
            try:
                helpstr = ": " + enumclass.helpdict[name]
            except KeyError:
                helpstr = ""
            print("   <listitem><simpara>", file=phile)
            # The missing space before {helpstr} is intentional.
            print(f"   <userinput>{name}</userinput>{helpstr}", file=phile)
            print("   </simpara></listitem>", file=phile)
        print("  </itemizedlist>", file=phile)
            
        print("  </refsect1>", file=phile)
        xrefs = getattr(enumclass, "xrefs", [])
        if xrefs:
            print("<refsect1>", file=phile)
            print("<title>See Also</title>", file=phile)
            print(f"<para>{xrefListing(xrefs)}</para>", file=phile)
            print("</refsect1>", file=phile)
        print("</refentry>", file=phile)
    print("</section>", file=phile)         # end of enum section

# This section has a large ordering value so that it comes *after* any
# section that calls process_param, ensuring that all Enum definitions
# have been found.

addSection(enumSection, ordering=1001)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Callbacks used by LabelTree.apply2 when printing the contents of the
# objDocs tree.

# The <refentry>s for these items set role='OtherObj', which keeps
# them from being listed in tables of contents (per a template in
# oofhtml.xml).

def printObjDocs(path, obj, phile):
    if obj is not None:
        try:
            discus = getDiscussion(obj)
        except AttributeError:
            print(f"<para>MISSING OBJ DISCUSSION: {path} {obj}</para>",
                  file=phile)
        else:
            if discus is not emptyDiscussion:
                print(discus, file=phile)
    else:
        # obj is None, meaning that this is a meta section.  Print toc.
        if path:    # no path means we're at the top level of the tree
            print(f"<section id='Object-{path}' role='toc-never'>", file=phile)
            print(f"  <title>{path}</title>", file=phile)
        print("  <itemizedlist spacing='compact'>", file=phile)
        node = objDocs[path]
        for subnode in node.nodes:
            # Only print leaf nodes of the LabelTree.  The other nodes
            # are in the automatically generated table of
            # contents.
            if not subnode.nodes:
                name = subnode.name
                print("<listitem><simpara>", file=phile)
                print(f"<link linkend='Object-{name}'>{name}</link>",
                      file=phile)
                print("</simpara></listitem>", file=phile)
                xmlIndexEntry(subnode.name, "Object", f"Object-{name}")
        print("  </itemizedlist>", file=phile)

def postPrintObjDocs(path, obj, phile):
    if obj is None:
        if path:
            print(f"</section> <!-- {path} -->", file=phile)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

XMLObjectDoc('list', loadFile('DISCUSSIONS/common/object/list.xml'))
