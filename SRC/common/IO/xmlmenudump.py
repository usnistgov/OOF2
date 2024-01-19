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
from ooflib.common import labeltree
from ooflib.common import utils
from ooflib.common.IO import parameter

enumdict = {}
regclassdict = {}

#################

# Keep track of which parameter types need to be documented.  This
# function is called on every parameter that appears in a menu item.

def process_param(param):
    global regclassdict
    global enumdict
    # Check for RegisteredParameters
    if isinstance(param, parameter.RegisteredParameter):
        processRegClass(param.reg)  # recursively includes reg. class params
    # Check for EnumParameters
    if isinstance(param, enum.EnumParameter):
        enumdict[param.enumclass.__name__] = param.enumclass
    elif isinstance(param, enum.ListOfEnumsParameter):
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

##################

indexItems = []

def xmlIndexEntry(name, category, xmlid):
    indexItems.append((name, category, xmlid))

##################
        
def regclassID(regclass):
    # xml id string to mark the definition of a base RegisteredClass
    return "RegisteredClass-%s" % regclass.__name__
def registrationID(reg):
    return "RegisteredClass-%s" % reg.subclass.__name__

###################

# Convert a list of xml ids to a list of links for the "See Also"
# sections of menuitems and registeredclasses.  The list items are
# either xml ids (strings) or a tuple (xmlid, text). 

def xrefListing(xrefs):
    texts = []
    done = []                   # check for duplicates
    for xref in xrefs:
        if xref not in done:
            if isinstance(xref, str):
                texts.append(f'<xref linkend="{xref}"/>')
            elif isinstance(xref, tuple):
                texts.append(f'<xref linkend="{xref[0]}" endterm="{xref[1]}"/>')
            done.append(xref)
    return ", ".join(texts)
        
    

###################

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
                return whelp
            return whelp.read(obj)
    raise AttributeError(obj, "helpstr, help, or tip")

emptyDiscussion = DiscussionFile(None, None)

##################    

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

###################

def dumpMenu(phile, menu, toplevel):
    if menu.getOption('no_doc'):
        return
    path = menu.path()
    if not toplevel:
        print('<section xreflabel="%s" id="MenuItem-%s" role="Menu">' \
              % (path, path), file=phile)
        print("<title>%s</title>" % path, file=phile)
        xmlIndexEntry(path, "Menu", "MenuItem-%s" % path)
    try:
        print("<subtitle>%s</subtitle>" % getHelp(menu), file=phile)
    except AttributeError:
        pass
    try:
        discus = getDiscussion(menu)
    except AttributeError:
        print(f"<para>MISSING MENU DISCUSSION: {path}</para>", file=phile)
    else:
        if discus is not emptyDiscussion:
            print(discus, file=phile)

    if not toplevel:
        print("<simpara>Parent Menu: <xref linkend='MenuItem-%s'/></simpara>" \
              % menu.parent.path(), file=phile)

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
            itempath = item.path()
            print(" <listitem><simpara>", file=phile)
            print(f"  <link linkend='MenuItem-{itempath}'><command>{itempath}</command></link>",
                  file=phile)
            try:
                help = getHelp(item)
                if help:
                    print("&emdash;", help, file=phile)
            except AttributeError:
                pass
            print(" </simpara></listitem>", file=phile)
        print("</itemizedlist>", file=phile)

    if commands:
        print("<itemizedlist spacing='compact'>", file=phile)
        print(f" <title>{path} Commands</title>", file=phile)
        for command in commands:
            item = menu.getItem(command)
            itempath = item.path()
            print(" <listitem><simpara>", file=phile)
            print(f"  <xref linkend='MenuItem-{itempath}'/>", file=phile)
            try:
                help = getHelp(item)
                if help:
                    print("&emdash;", help, file=phile)
            except AttributeError:
                pass
            print(" </simpara></listitem>", file=phile)
        print("</itemizedlist>", file=phile)

    xrefs = menu.xmlXRefs()
    if xrefs:
        print(" <simplesect>", file=phile)
        print("   <title>See Also</title>", file=phile)
        print(f"   <simpara>{xrefs}</simpara>", file=phile)
        print(" </simplesect>", file=phile)

    if not toplevel:
        print("</section> <!-- %s -->" % path, file=phile)


    for submenu in submenus:
        dumpMenu(phile, menu.getItem(submenu), toplevel=0)
    for command in commands:
        dumpMenuItem(phile, menu.getItem(command))


def dumpMenuItem(phile, menuitem):
    if menuitem.getOption('no_doc'):
        return
    path = menuitem.path()
    xmlIndexEntry(path, "Menu Item", "MenuItem-%s" % path)
    print('<refentry xreflabel="%s" id="MenuItem-%s" role="MenuItem">'\
          % (path, path), file=phile)
    print(" <refnamediv>", file=phile)
    print("  <refname>%s</refname>" % path, file=phile)
    try:
        help = getHelp(menuitem)
        if help:
            print("  <refpurpose>%s</refpurpose>" % help, file=phile)
        else:
            print("   <refpurpose></refpurpose>", file=phile)
    except AttributeError:
        print("  <refpurpose>MISSING HELP STRING: %s</refpurpose>" \
              % path, file=phile)
    print(" </refnamediv>", file=phile)

    menuitem.xmlSynopsis(phile)

    print(" <refsect1>", file=phile)
    print("   <title>Details</title>", file=phile)
    print("   <itemizedlist>", file=phile)
    print("    <listitem><simpara>Parent Menu: <xref linkend='MenuItem-%s'/></simpara></listitem>" % menuitem.parent.path(), file=phile)
    if menuitem.callback:
        fname, mname = menuitem.getcallbackname()
        print("  <listitem><simpara>", file=phile)
        print("   Callback: function <function>%s</function> in module <filename>%s</filename>" % (fname, mname), file=phile)
        print("  </simpara></listitem>", file=phile)

    # Menu items are enabled and disabled dynamically, so the current
    # state of the flag isn't relevant to the documentation.
    ## TODO: "disabled" shouldn't be an OOFMenuItem option.
    if menuitem.options and list(menuitem.options.keys()) != ['disabled']:
        print("  <listitem><simpara>", file=phile)
        print("   Options:", file=phile)
        for key, val in list(menuitem.options.items()):
            if key != "disabled":
                print(" <varname>%s</varname>=<constant>%s</constant>"
                      %(key, repr(val)), file=phile)
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
        print(f"   <simpara>{xrefs}</simpara>", file=phile)
        print(" </refsect1>", file=phile)
    
    print("</refentry>", file=phile)

###################        

def xmlmenudump(phile):

    # Clear global dictionaries, in case this isn't the first time
    # this function has been run.
    global enumdict
    global regclassdict
    regclassdict = {}
    enumdict = {}

    print("<!-- This file is generated by xmlmenudump.  DO NOT EDIT IT. -->", file=phile)
    print(file=phile)
    print("<chapter id='Chapter-Reference'><title>Reference</title>", file=phile)
    print("""

    <section id="Section-Reference:HowTo">
      <title>How to use this Chapter</title>
      <para>
      
      This chapter consists of a set of reference pages for some of
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

    ## Add other sections defined elsewhere.  (Misleading comment!
    ## Sections defined here are also in otherSections.)
    otherSections.sort()
    for ordering, otherSectionCB in otherSections:
        otherSectionCB(phile)

    ########

    print("<section id='Section-OtherObjects'>", file=phile)
    print(" <title>Other Objects</title>", file=phile)
    print(""" <para>

    This section covers objects that can occur in &oof2; commands but
    aren't included in the above sections, for various reasons.

    </para>""", file=phile)

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
        print("<row>", file=phile)
        print("<entry><simpara><link linkend='%s'>%s</link></simpara></entry>" % (xmlid, name), file=phile)
        print("<entry><simpara>%s</simpara></entry>" % category, file=phile)
        print("</row>", file=phile)
    print("</tbody></tgroup></table>", file=phile)
    print("</section>", file=phile)

    print("</chapter>", file=phile)

def mainMenuSection(phile):
    # The section containing the main menu is handled differently from
    # all the other menus.  Its id is MenuItem-OOF so that
    # automatically generated references to root menu go to it.
    print("<section id='MenuItem-OOF' xreflabel='The Main OOF Menu'>", file=phile)
    print("  <title>Menus</title>", file=phile)

    from ooflib.common.IO import mainmenu      # delayed, to avoid import loop
    dumpMenu(phile, mainmenu.OOF, toplevel=1)
    print("</section>", file=phile)         # end of menu item listing

addSection(mainMenuSection, 0)

def regClassSection(phile):
    ## RegisteredClasses

    for regclass in otherregclasses:
        processRegClass(regclass)
    
    print("<section id='Section-RegisteredClasses'>", file=phile)
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
    print("<section id='Section-RegisteredBaseClasses'>", file=phile)
    print(" <title>Base RegisteredClasses</title>", file=phile)
    print(" <itemizedlist spacing='compact'>", file=phile)

    ## List of RegisteredClass base classes
    for regclassname in regclassnames:
        regclass = regclassdict[regclassname]
        try:
            tip = getHelp(regclass)
        except AttributeError:
            tip = "MISSING TIP STRING: %s" % regclassname
        print(" <listitem><simpara>", file=phile)
        print("  <xref linkend='%s'/> &#x2014; %s" % (regclassID(regclass),\
                                                         tip), file=phile)
        print(" </simpara></listitem>", file=phile)        
    print(" </itemizedlist>", file=phile)

    ## Reference pages for each base class
    for regclassname in regclassnames:
        regclass = regclassdict[regclassname]
        xmlIndexEntry(regclassname,"RegisteredClass base class",
                      regclassID(regclass))
        print(" <refentry xreflabel='%s' id='%s' role='RegisteredClass'>" % \
              (regclassname, regclassID(regclass)), file=phile)
        print("  <refnamediv>", file=phile)
        print("   <refname>%s</refname>" % regclassname, file=phile)
        try:
            tip = getHelp(regclass)
        except AttributeError:
            tip = "MISSING TIP STRING: %s" % regclassname
        print("   <refpurpose>%s</refpurpose>" % tip, file=phile)
        print("  </refnamediv>", file=phile)
        print("  <refsect1>", file=phile)
        print("   <title>Subclasses</title>", file=phile)
        print("""   <para>
        Subclasses are listed as they appear in the GUI and (in
        parentheses) as they appear in scripts.
        </para>""", file=phile)
        print("   <itemizedlist spacing='compact'>", file=phile)
        # Don't sort... registrations are listed in the order in which
        # they appear in the GUI.
        for reg in regclass.registry:
            if not reg.secret:
                registrationdict[reg.subclass.__name__] = reg
                try:
                    tip = getHelp(reg)
                except AttributeError:
                    tip = "MISSING TIP STRING: %s" % reg.subclass.__name__
                print("   <listitem><simpara>", file=phile)
                print("    <link linkend='%s'>%s (<classname>%s</classname>)</link> &#x2014; %s" % \
                      (registrationID(reg), reg.name(), reg.subclass.__name__,
                       tip), file=phile)
                print("   </simpara></listitem>", file=phile)
        print("   </itemizedlist>", file=phile)        
        print("  </refsect1>", file=phile)
        
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
            print(f"<simpara>{xrefListing(xrefs)}</simpara>", file=phile)
            print("</refsect1>", file=phile)

        print(" </refentry>", file=phile) # end refentry for registered base class

    print("</section>", file=phile)

    subclassnames = sorted(list(registrationdict.keys()))

    print("<section id='Section-RegisteredSubclasses'>", file=phile)
    print(" <title>Subclasses</title>", file=phile)

    ## List of subclasses
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
            tip = "MISSING TIP STRING: %s" % name
        print("    <xref linkend='%s'/> &#x2014; %s" % \
              (registrationID(reg), tip), file=phile)
        print("  </simpara></listitem>", file=phile)
    print(" </itemizedlist>", file=phile)

    ## Reference page for each subclass
    for name in subclassnames:
        try:
            reg = registrationdict[name]
        except KeyError:
            continue
        xmlIndexEntry(name, "RegisteredClass subclass", registrationID(reg))
        print(" <refentry xreflabel='%s' id='%s' role='Registration'>"\
              % (name, registrationID(reg)), file=phile)
        print("  <refnamediv>", file=phile)
        print("    <refname>%s (%s)</refname>" % (reg.name(), name), file=phile)
        try:
            tip = getHelp(reg)
        except AttributeError:
            tip = "MISSING TIP STRING: %s" % name
        print("     <refpurpose>%s</refpurpose>" % tip, file=phile)
        print("  </refnamediv>", file=phile)

        print("  <refsynopsisdiv><simpara>", file=phile)
        args = utils.stringjoin(['<varname>%s</varname>' % p.name
             for p in reg.params], ', ')
        print("   <classname>%s</classname>(%s)" % (name, args), file=phile)
        print("  </simpara></refsynopsisdiv>", file=phile)
        
        print("  <refsect1>", file=phile)
        print("    <title>Details</title>", file=phile)
        print("    <itemizedlist>", file=phile)
        print("     <listitem><simpara>", file=phile)
        print("      Base class%s:"%("es"*(len(reg.registeredclasses)>1)), file=phile)
        for regclass in reg.registeredclasses:
            print("      <link linkend='%s'><classname>%s</classname></link>" \
            % (regclassID(regclass), regclass.__name__), file=phile)
        print("     </simpara></listitem>", file=phile)
        if reg.params:
            print("     <listitem><para>", file=phile)
            print("      Parameters:", file=phile)
            print("      <variablelist>", file=phile)
            for param in reg.params:
                print("       <varlistentry>", file=phile)
                print("        <term><varname>%s</varname></term>" \
                      % param.name, file=phile)
                print("         <listitem>", file=phile)
                try:
                    tip = getHelp(param)
                except AttributeError:
                    tip = "MISSING TIP STRING: %s:%s" % (name, param.name)
                print("          <simpara>%s <emphasis>Type</emphasis>: %s</simpara>" \
                      % (tip, param.valueDesc()), file=phile)
                print("         </listitem>", file=phile)
                print("       </varlistentry>", file=phile)
            print("      </variablelist>", file=phile) # end of parameter list
            print("     </para></listitem>", file=phile)
        print("    </itemizedlist>", file=phile) # end of Details list
        print("  </refsect1>", file=phile) # end of Details section
        print("  <refsect1>", file=phile)
        print("   <title>Description</title>", file=phile)
        try:
            discus = getDiscussion(reg)
        except AttributeError:
            print(f"<para>MISSING REGCLASS DISCUSSION: {name}</para>",
                  file=phile)
        else:
            print(f"   {discus}", file=phile)
        print("  </refsect1>", file=phile)
        if reg.xrefs:
            print("   <refsect1>", file=phile)
            print("   <title>See Also</title>", file=phile)
            print(f"   <simpara>{xrefListing(reg.xrefs)}</simpara>",
                  file=phile)
            print("   </refsect1>", file=phile)
        print(" </refentry>", file=phile)

    print("</section>", file=phile)         # end of registered subclasses

    print("</section>", file=phile)         # end of registered classes section

# This section has a large ordering value so that it comes *after* any
# section that calls process_param, ensuring that all RegisteredClass
# definitions have been found.

addSection(regClassSection, ordering=1000)

def enumSection(phile):
    print("<section id='Section-Enums'>", file=phile)
    print(" <title>Enumerated Types</title>", file=phile)
    print(""" <para>

    Many command arguments in &oof2; require the user to choose from a
    small set of predetermined constant values, called
    <classname>Enums</classname>.  These <classname>Enums</classname>
    differ from <link
    linkend='Section-RegisteredClasses'><classname>RegisteredClasses</classname></link>
    in that they are much simpler objects, and never require any
    parameters.  This section describes all of the
    <classname>Enum</classname> classes and lists their allowed
    values.
    </para>

    <para>

     In the GUI, <classname>Enum</classname> parameters are chosen
     from a pull-down menu.  In scripts, <classname>Enum</classname>
     parameters can be set to the <emphasis>name</emphasis> of the
     <classname>Enum</classname> object, in quotation marks.
     For example, this documentation was generated by
     <blockquote><simpara><userinput>
       <link linkend='MenuItem-OOF.Help.API_Listing'>
        OOF.Help.API_Listing</link>(filename='oof2_api.xml',
        format=<link linkend='Enum-MenuDumpFormat'>'xml'</link>)
      </userinput></simpara></blockquote>
      Here, <varname>format</varname> is a parameter that requires an
      object from the <xref linkend='Enum-MenuDumpFormat'/> class.
    
    </para>""", file=phile)

    enumnames = sorted(list(enumdict.keys()))

    print("<itemizedlist spacing='compact'>", file=phile)
    for enumname in enumnames:
        enumclass = enumdict[enumname]
        try:
            tip = getHelp(enumclass)
        except AttributeError:
            tip = "MISSING ENUM TIP STRING: %s" % enumname
        print("<listitem><simpara>", file=phile)
        print(" <xref linkend='Enum-%s'/> &#x2014; %s" % (enumname, tip), file=phile)
        print("</simpara></listitem>", file=phile)        
    print("</itemizedlist>", file=phile)
    
    for enumname in enumnames:
        enumclass = enumdict[enumname]
        xmlIndexEntry(enumname, "Enum class", 'Enum-%s' % enumname)
        print(" <refentry xreflabel='%s' id='Enum-%s' role='Enum'>" \
              % (enumname, enumname), file=phile)
        print("  <refnamediv>", file=phile)
        print("   <refname>%s</refname>" % enumname, file=phile)
        try:
            tip = getHelp(enumclass)
        except AttributeError:
            tip = "MISSING ENUM TIP STRING: %s" % enumname
        print("   <refpurpose>%s</refpurpose>" % tip, file=phile)
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
            print("   <userinput>%s</userinput>%s" % (name, helpstr), file=phile)
            print("   </simpara></listitem>", file=phile)
        print("  </itemizedlist>", file=phile)
            
        print("  </refsect1>", file=phile)
        print("</refentry>", file=phile)
    print("</section>", file=phile)         # end of enum section

# This section has a large ordering value so that it comes *after* any
# section that calls process_param, ensuring that all Enum definitions
# have been found.

addSection(enumSection, ordering=1001)

    
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
        if path:                        # no path means we're at the top level
            print("<section id='Object-%s'>" % path, file=phile)
            print("  <title>%s</title>" % path, file=phile)
        print("  <itemizedlist spacing='compact'>", file=phile)
        node = objDocs[path]
        for subnode in node.nodes:
            print("<listitem><simpara>", file=phile)
            print("<link linkend='Object-%(name)s'>%(name)s</link>" \
                  % {'name':subnode.name}, file=phile)
            print("</simpara></listitem>", file=phile)
            xmlIndexEntry(subnode.name, "Object", "Object-%s" % subnode.name)
        print("  </itemizedlist>", file=phile)

def postPrintObjDocs(path, obj, phile):
    if obj is None:
        if path:
            print("</section> <!-- %s -->" % path, file=phile)

###############################

XMLObjectDoc('list', loadFile('DISCUSSIONS/common/object/list.xml'))
