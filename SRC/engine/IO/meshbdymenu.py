# -*- python -*-
# $RCSfile: meshbdymenu.py,v $
# $Revision: 1.29 $
# $Author: langer $
# $Date: 2011/04/22 18:52:48 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Menu items for post-solution actions on boundaries.

from ooflib.SWIG.common import switchboard
from ooflib.common import enum
from ooflib.common.IO import automatic
from ooflib.common.IO import datafile
from ooflib.common.IO import filenameparam
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import placeholder
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.engine import meshbdyanalysis
from ooflib.engine import namedanalysis
from ooflib.engine.IO import analyzemenu
from ooflib.engine.IO import meshmenu
from ooflib.engine.IO import meshparameters
from ooflib.engine.IO import outputdestination
import ooflib.engine.mesh
import string
import types

bdyanalysismenu = meshmenu.meshmenu.addItem(
    oofmenu.OOFMenuItem(
        'Boundary_Analysis',
        help="Compute properties of the solution on boundaries."))

mesh_param = whoville.WhoParameter(
    'mesh', ooflib.engine.mesh.meshes,
    tip="The mesh on which to perform the analysis.")

time_param = placeholder.TimeParameter(
    'time', tip='Time at which to perform the analysis.')

bdy_param = meshparameters.MeshEdgeBdyParameter(
    'boundary', tip="The boundary to analyze.")

analyzer_param = parameter.RegisteredParameter(
    'analyzer', meshbdyanalysis.MeshBdyAnalyzer,
    tip="Operation to perform on the boundary.")

destination_param = outputdestination.OutputDestinationParameter(
    'destination',
    value=outputdestination.msgWindowOutputDestination,
    tip="Where the data should be written.")

def _meshBdyAnalyze(menuitem, mesh, time, boundary, analyzer, destination):
    meshctxt = ooflib.engine.mesh.meshes[mesh]
    meshctxt.begin_reading()
    try:
        meshctxt.precompute_all_subproblems()
        t = meshctxt.getTime(time)
        meshctxt.restoreCachedData(t)
        try:
            destination.open()
            destination.printHeadersIfNeeded(analyzer, boundary)
            analyzer.analyze(meshctxt, t, boundary, destination)
            destination.close()
        finally:
            meshctxt.releaseCachedData()
    finally:
        meshctxt.end_reading()
    
bdyanalysismenu.addItem(oofmenu.OOFMenuItem(
    'Analyze',
    secret=1,
    callback=_meshBdyAnalyze,
    params = [mesh_param, time_param, bdy_param, analyzer_param,
              destination_param],
    help="Post-solution analysis of boundaries.",
    discussion="""<para>
    The <command>OOF.Mesh.Boundary_Analysis</command> command runs
    post-solution analyses on the &mesh; boundaries.  Compare to <xref
    linkend='MenuItem-OOF.Mesh.Analyze'/>, which contains commands
    that operate on the interior of the &mesh;.
    </para>"""
    ))

############################

## TODO: The command hierarchies for named bulk analyses and named
## boundary analyses are different, for no apparent reason. The bulk
## commands are in OOF.Named_Analysis while the boundary commands are
## in OOF.Mesh.Boundary_Analysis.  Both should be in
## OOF.Named_Analysis.

def _nameAnalysis(menuitem, name, boundary, analyzer):
    namedanalysis.NamedBdyAnalysis(name, boundary, analyzer)
    switchboard.notify("named boundary analyses changed")

bdyanalysismenu.addItem(oofmenu.OOFMenuItem(
    "Create",
    callback=_nameAnalysis,
    params=[
        parameter.AutomaticNameParameter(
            'name', resolver=namedanalysis.bdynameResolver,
            value=automatic.automatic,
            tip="The name of the analysis."),
        bdy_param,
        analyzer_param],
    help="Assign a name to a set of boundary analysis parameters.",
    discussion=xmlmenudump.loadFile(
            'DISCUSSIONS/engine/menu/newnamedbdyanal.xml')
    ))

mainmenu.OOF.LoadData.addItem(oofmenu.OOFMenuItem(
        'NamedBdyAnalysis',
        callback=_nameAnalysis,
        params=[
            parameter.StringParameter('name', tip=parameter.emptyTipString),
            bdy_param,
            analyzer_param],
        help="Create a named boundary analysis. Used internally in data files.",
        discussion="<para>Create a named boundary analysis.</para>"  
        ))

def _deleteAnalysis(menuitem, name):
    namedanalysis.getNamedBdyAnalysis(name).destroy()
    switchboard.notify("named boundary analyses changed")

bdyanalysismenu.addItem(oofmenu.OOFMenuItem(
    "Delete",
    callback=_deleteAnalysis,
    params=[namedanalysis.BdyAnalysisNameParameter(
            'name', tip='Name of the analysis operation to delete')],
    help="Delete a named set of boundary analysis parameters.",
    discussion=xmlmenudump.loadFile(
                'DISCUSSIONS/engine/menu/delnamedbdyanal.xml')
    ))
           
def _saveAnalysis(menuitem, filename, mode, format, names):
    dfile = datafile.writeDataFile(filename, mode.string(), format)
    for analysisname in names:
        analysis = namedanalysis.getNamedBdyAnalysis(analysisname)
        dfile.startCmd(mainmenu.OOF.LoadData.NamedBdyAnalysis)
        dfile.argument('name', analysisname)
        dfile.argument('boundary', analysis.boundary)
        dfile.argument('analyzer', analysis.analyzer)
        dfile.endCmd()

bdyanalysismenu.addItem(oofmenu.OOFMenuItem(
    "SaveAnalysisDefs",
    callback=_saveAnalysis,
    params=[
        filenameparam.WriteFileNameParameter('filename',
                                             tip='Name of the file.'),
        filenameparam.WriteModeParameter(
            'mode', tip="'w' to (over)write, 'a' to append."),
        enum.EnumParameter('format', datafile.DataFileFormat, datafile.ASCII,
                           tip="Format of the file."),
        namedanalysis.BdyAnalysisNamesParameter(
            'names', tip="Names of the analyses to be saved.")],
    help="Save the definitions of named boundary analysis operations in a file.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/savebdyanal.xml')
    ))

def _retrieveNamedAnalyis(menutiem, name):
    switchboard.notify("retrieve boundary analysis", name)

bdyanalysismenu.addItem(oofmenu.OOFMenuItem(
        "RetrieveNamedAnalysis",
        callback=_retrieveNamedAnalyis,
        params=[namedanalysis.BdyAnalysisNameParameter(
                "name", tip="Name of the boundary analysis to be retrieved")],
        help="Set the Boundary Analysis Page widgets to the parameters of a stored analysis operation.",
        discussion=xmlmenudump.loadFile(
            'DISCUSSIONS/engine/menu/retrievebdyanal.xml')
        ))
        
