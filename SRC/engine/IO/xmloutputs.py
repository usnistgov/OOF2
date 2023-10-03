# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common.IO import xmlmenudump
from ooflib.engine.IO import output
from ooflib.common import debug
import sys

def _catalogPaths(outputlist, xmlids, prefix):
    for o in outputlist:
        if o not in xmlids:
            xmlids[o] = prefix + o.getPath().replace(':', '-')

def outputDump(file):
    scalars = output.scalarOutputs.getObjects()
    positions = output.positionOutputs.getObjects()
    aggregates = output.aggregateOutputs.getObjects()
    allOutputs = scalars + positions + aggregates
    # # allOutputs contains duplicates...
    # allOutputs.sort(lambda x, y: cmp(x.getPath(), y.getPath()))
    xmlids = {}
    _catalogPaths(scalars, xmlids, 'Output-Scalar-')
    _catalogPaths(positions, xmlids, 'Output-Position-')
    _catalogPaths(aggregates, xmlids, 'Output-Aggregates-')

    print("<section id='Section-Output'>", file=file)
    print(" <title>Outputs</title>", file=file)
    print("<!--this section produced by SRC/engine/IO/xmloutputs.py-->", file=file)
    print("""
    <para>
     The <classname>Output</classname> classes provide ways of
     extracting data from <link
     linkend='Section-Concepts-Mesh'>Meshes</link>.  Different kinds
     of <classname>Outputs</classname> produce different kinds of
     data.  <link
     linkend='RegisteredClass-FilledContourDisplay'>Contour
     plots</link>, for example, display the results of a <link
     linkend='Section-Output-Scalar'>Scalar Output</link> at
     locations determined by a <link
     linkend='Section-Output-Position'>Position Output</link>.
    </para>
    <para>
      <classname>Outputs</classname> are used for graphical output by
      some <xref linkend="RegisteredClass-DisplayMethod"/> classes,
      for post-processing on the <link
      linkend="Section-Tasks-Analysis">Analysis</link> and <link
      linkend="Section-Tasks-BdyAnalysis">Boundary Analysis</link> pages,
      and as data for
      <link linkend="MenuItem-OOF.Mesh.Scheduled_Output">scheduled
      outputs</link>.
    </para>
    <para>
     The three categories of outputs are
     <itemizedlist>
      <listitem><para id='Section-Output-Scalar'>
       <classname>ScalarOutputs</classname>:
       These are Outputs whose result is a single number at each evaluation
       point.  They are used as the <varname>what</varname> argument
       in the contour plotting commands, for example.
       <itemizedlist spacing='compact'>
       """, file=file)
    paths = sorted([(o.getPath(),o) for o in scalars])
    for path,o in paths:
        xmlmenudump.xmlIndexEntry(path, "Scalar Output", xmlids[o])
        print(" <listitem><simpara><link linkend='%s'>" % xmlids[o], file=file)
        print("  <classname>%s</classname>" % path, file=file)
        print(" </link></simpara></listitem>", file=file)
    print("""
       </itemizedlist>
      </para></listitem>
      <listitem><para id='Section-Output-Position'>
       <classname>PositionOutputs</classname>:
       These are Outputs whose result is a position.  They are used as the
       <varname>where</varname> argument in plotting commands.
        <itemizedlist spacing='compact'>""", file=file)
    paths = [(o.getPath(),o) for o in positions]
    paths.sort()
    for path,o in paths:
        xmlmenudump.xmlIndexEntry(path, "Position Output", xmlids[o])
        print(" <listitem><simpara><link linkend='%s'>" % xmlids[o], file=file)
        print("  <classname>%s</classname>" % path, file=file)
        print(" </link></simpara></listitem>", file=file)
    print("""
       </itemizedlist>
      </para></listitem>
      <listitem><para id='Section-Output-Aggregate'>
       <classname>AggregateOutputs</classname>:

       These are Outputs whose result is a (possibly) multidimensional
       object, such as a &field; or &flux;.
       They are used when interactively querying &mesh; data with the
       <link
       linkend='Section-Graphics-MeshInfo-DataViewer'>Data
       Viewer</link>.  Many of the <link
       linkend='Section-Output-Scalar'><classname>ScalarOutputs</classname></link>
       are also <classname>AggregateOutputs</classname>.
       <itemizedlist spacing='compact'> """, file=file)
    paths = [(o.getPath(),o) for o in aggregates]
    paths.sort()
    for path,o in paths:
        xmlmenudump.xmlIndexEntry(path, "Aggregate Output", xmlids[o])
        print("<listitem><simpara><link linkend='%s'>" % xmlids[o], file=file)
        print(" <classname>%s</classname>" % path, file=file)
        print(" </link></simpara></listitem>", file=file)
    print("""
       </itemizedlist>

      </para></listitem>
     </itemizedlist>
     
    </para>
    """, file=file)

    for o,xmlid in list(xmlids.items()):
        path = o.getPath()
        print("<refentry id='%s' role='Output'>" % xmlid, file=file)
        print(" <refnamediv>", file=file)
        print("  <refname>%s</refname>" % path, file=file)
        try:
            print(" <refpurpose>%s</refpurpose>" % xmlmenudump.getHelp(o), file=file)
        except AttributeError as ax:
            print(" <refpurpose>MISSING HELP STRING: %s</refpurpose>" % xmlid, file=file)
        print(" </refnamediv>", file=file)
        print(" <refsynopsisdiv>", file=file)
        print("  <title>Output Categories</title>", file=file)
        print("  <itemizedlist spacing='compact'>", file=file)
        if o in scalars:
            print("<listitem><simpara><link linkend='Section-Output-Scalar'><classname>ScalarOutput</classname></link></simpara></listitem>", file=file)
        if o in positions:
            print("<listitem><simpara><link linkend='Section-Output-Position'><classname>PositionOutput</classname></link></simpara></listitem>", file=file)
        if o in aggregates:
            print("<listitem><simpara><link linkend='Section-Output-Aggregate'><classname>AggregateOutput</classname></link></simpara></listitem>", file=file)
        print("  </itemizedlist>", file=file)
        print(" </refsynopsisdiv>", file=file)
        params = list(o.getSettableParams().values())
        if params:
            print(" <refsect1>", file=file)
            print("  <title>Parameters</title>", file=file)
            print("  <variablelist>", file=file)
            for param in params:
                xmlmenudump.process_param(param)
                print("   <varlistentry>", file=file)
                print("    <term><varname>%s</varname></term>" \
                      % param.name, file=file)
                print("    <listitem>", file=file)
                try:
                    tip = xmlmenudump.getHelp(param)
                except AttributeError:
                    tip = "MISSING HELP STRING: %s" % param.name
                print("     <simpara>%s <emphasis>Type</emphasis>: %s</simpara>" 
                          % (tip, param.valueDesc()), file=file)
                print("     </listitem>", file=file)
                print("   </varlistentry>", file=file)
            print("  </variablelist>", file=file)
            print(" </refsect1>", file=file)
        print(" <refsect1>", file=file)
        print("  <title>Description</title>", file=file)
        try:
            print(xmlmenudump.getDiscussion(o), file=file)
        except AttributeError:
            print("<simpara>MISSING DISCUSSION: Output %s</simpara>" % path, file=file)
        print(" </refsect1>", file=file)
        print("</refentry>", file=file)
            
    print("</section>", file=file)         # End of Outputs 

xmlmenudump.addSection(outputDump, 2)
