# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Menu commands for reading a Mesh from a file.  To be precise, a Mesh
# is re-created from a read Skeleton, and then the Fields, Equations,
# BoundaryConditions, etc. are read.


from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import masterelement
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import labeltree
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import datafile
from ooflib.common.IO import filenameparam
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.engine import bdycondition
from ooflib.engine import fieldinit
from ooflib.engine import meshcrosssection
from ooflib.engine import meshstatus
from ooflib.engine import outputschedule
from ooflib.engine import skeletonboundary
from ooflib.engine import skeletoncontext
from ooflib.engine import solvermode
from ooflib.engine import subproblemtype
if config.dimension() == 2:
    from ooflib.engine import skeletonelement
elif config.dimension() == 3:
    from ooflib.engine import skeletonelement3d as skeletonelement
from ooflib.engine.IO import meshparameters
from ooflib.engine.IO import outputdestination
from ooflib.engine.IO import scheduledoutput
from ooflib.engine.IO.skeletonIO import rearrangeEdges
import ooflib.SWIG.engine.equation
import ooflib.SWIG.engine.field
import ooflib.engine.mesh
import ooflib.engine.subproblemcontext

from ooflib.common.IO import microstructureIO
from ooflib.engine.IO import skeletonIO

import ooflib.engine.IO.meshmenu
import ooflib.engine.IO.boundaryconditionmenu

OOFMenuItem = oofmenu.OOFMenuItem

OOF = mainmenu.OOF

meshmenu = OOF.LoadData.addItem(
    OOFMenuItem(
        'Mesh',
        help="Load a Mesh from a data file.",
        discussion="""<para>
        This menu contains commands for constructing a &mesh;.  It is
        used internally in data files and not invoked directly by the
        &oof2; user interface.</para>"""
))

subpmenu = OOF.LoadData.addItem(
    OOFMenuItem(
        'Subproblem',
        help="Load a Subproblem from a data file.",
        discussion="""<para>
        This menu contains commands for constructing a &subproblem;.
        It is used internally in data files and not invoked directly
        by the &oof2; user interface.</para>"""
    ))

def getNodeSets(femesh):
    nodesets = {}               # lists of nodes keyed by fieldSetID.
    for node in femesh.funcnodes():
        fieldsetid = node.fieldSetID()
        try:
            nodesets[fieldsetid].append(node)
        except KeyError:
            nodesets[fieldsetid] = [node]
    # Make sure that Fields are always listed in the same order, to
    # facilitate testing.  Since fieldSetIDs are integers, we just
    # sort the set of IDs.
    ids = sorted(list(nodesets.keys()))
    return ids, nodesets

def writeFields(dfile, meshcontext):
    # Field values
    # fields = ["Displacement", "Temperature"] : ListOfStrings
    # field_values = [(node_index, fvalue0, fvalue1, fvalue2), ....]
    # : ListOfTuplesOfIntFloats

    # When a Mesh is created from a Skeleton, its nodes are created in
    # some (seemingly) arbitrary order, which depends on the order of
    # the nodes and elements in the Skeleton and on the way in which
    # Skeleton and SkeletonElement conspire to build the Mesh.  The
    # order in which the Field values are saved in the data file
    # depends on the order of the Mesh nodes, which depends on this
    # confusing creation history.  But everything is ok, because
    # Meshes are *always* created from Skeletons, and always created
    # the same way.  As long as the Skeleton in the Mesh file has been
    # saved with its nodes in the right order, the Mesh will be
    # created with its nodes in the right order, and the data file
    # will list the Fields in the right order.

    # Since different Nodes may contain different sets of Fields
    # (being in different sets of SubProblems), we need to list which
    # Fields are defined at each Node.  It's not sufficient to use the
    # SubProblem data for this, because Fields may be defined in more
    # than one SubProblem on a Node.  So we need to save a list of
    # Fields for each Node, but in order to save space in the data
    # file, we first create sets of Nodes that contain the same
    # Fields.  Then the list of Fields just has to be saved once for
    # each set of Nodes.  The Fields defined on a Node are determined
    # by the Node's FieldSet, so we can use the fieldSetID.

    femesh = meshcontext.getObject()
    ids, nodesets = getNodeSets(femesh)
    for fieldsetID in ids:
        nodelist= nodesets[fieldsetID]
        fieldnames = sorted(femesh.getFieldSetByID(fieldsetID))
        fields = [getFieldObj(name) for name in fieldnames]
        values = []
        for node in nodelist:
            fv = [node.index()]
            for field in fields:
                for i in range(field.ndof()):
                    fv.append(field.value(femesh, node, i))
            values.append(tuple(fv))
## TODO: figure out what's wrong with this version, and if it's faster
## when fixed:
#             values = [
#                 tuple(
#                     [node.index()] + [field.value(femesh, node, i)
#                                       for i in range(field.ndof())
#                                       for field in fields]
#                     )
#                 for node in nodelist]
        dfile.startCmd(meshmenu.Load_Field)
        dfile.argument('mesh', meshcontext.path())
        dfile.argument('fields', fieldnames)
        dfile.argument('field_values', values)
        dfile.endCmd()

def writeAndCacheFields(dfile, meshcontext, time):
    writeFields(dfile, meshcontext)
    dfile.startCmd(meshmenu.Cache_Fields)
    dfile.argument('mesh', meshcontext.path())
    dfile.argument('time', time)
    dfile.endCmd()

def writeMesh(dfile, meshcontext, includeFields=True):
    skelcontext = meshcontext.getParent()
    skelpath = skelcontext.path()
    femesh = meshcontext.femesh()

    # Create mesh.
    dfile.startCmd(meshmenu.New)
    dfile.argument('name', meshcontext.name())
    masterelems = [repr(ename) for ename in list(meshcontext.elementdict.values())]
    dfile.argument('masterelems', masterelems)
    dfile.argument('skeleton', skelpath)
    dfile.endCmd()

    # Create subproblems
    anyfields = False  # used later to decide if field values must be saved
    for subpctxt in meshcontext.subproblems():
        subp = subpctxt.subptype
        subpobj = subpctxt.getObject()
        if subpctxt.name() != ooflib.engine.mesh.defaultSubProblemName:
            dfile.startCmd(subpmenu.New)
            dfile.argument('name', subpctxt.name())
            dfile.argument('subproblem', subp)
            dfile.argument('mesh', meshcontext.path())
            dfile.endCmd()
        # Define and activate Fields on subproblems
        definedfields = [field.name() for field in
                         subpctxt.all_compound_fields()]
        activefields = [field.name() for field in
                        subpctxt.all_compound_fields()
                        if subpobj.is_active_field(field)]
        inplanefields = [field.name() for field in
                         subpctxt.all_compound_fields()
                         if femesh.in_plane(field)]
        if definedfields:
            anyfields = True
            dfile.startCmd(subpmenu.Fields)
            dfile.argument('subproblem', subpctxt.path())
            dfile.argument('defined', definedfields)
            dfile.argument('active', activefields)
            dfile.argument('inplane', inplanefields)
            dfile.endCmd()
        # Time derivative fields have a separate menu item to preserve
        # backwards compatibiltiy from the pre-time-dependence days.
        timederivfields = [field.name() for field in
                           subpctxt.all_compound_fields() if
                           subpctxt.is_defined_field(field.time_derivative())]
        if timederivfields:
            dfile.startCmd(subpmenu.Time_Derivative_Fields)
            dfile.argument('subproblem', subpctxt.path())
            dfile.argument('fields', timederivfields)
            dfile.endCmd()

        # Equations
        equations = [eqn.name() for eqn in subpctxt.all_equations()]
        if equations:
            dfile.startCmd(subpmenu.Equations)
            dfile.argument('subproblem', subpctxt.path())
            dfile.argument('equations', equations)
            dfile.endCmd()

        # Solver
        if subpctxt.time_stepper is not None:
            dfile.startCmd(subpmenu.Solver)
            dfile.argument('subproblem', subpctxt.path())
            dfile.argument('solver_mode', subpctxt.solver_mode)
            dfile.endCmd()

    # End loop over subproblems

    # Field initializers
    for field in meshcontext.all_subproblem_fields():
        init = meshcontext.get_initializer(field)
        if init:
            dfile.startCmd(meshmenu.Initialize_Field)
            dfile.argument('mesh', meshcontext.path())
            dfile.argument('field', field)
            dfile.argument('initializer', init)
            dfile.endCmd()

    # Boundary conditions
    bcnames = sorted(meshcontext.allBndyCondNames())
    for bcname in bcnames:
        bc = meshcontext.getBdyCondition(bcname)
        # bc's that are invisible in the gui are generally created by
        # internal processes.  Explicity saving and loading them can
        # lead to conflicts.
        if bc.isVisible():
            dfile.startCmd(meshmenu.Boundary_Condition)
            dfile.argument('mesh', meshcontext.path())
            dfile.argument('bcname', bcname)
            dfile.argument('bc', bc)
            dfile.endCmd()

    # Boundary condition initializers
    bcnames = [bc.name() for bc in meshcontext.initialized_bcs()]
    bcnames.sort()
    for bcname in bcnames:
        dfile.startCmd(meshmenu.Set_BC_Initializer)
        dfile.argument('mesh', meshcontext.path())
        dfile.argument('bc', bcname)
        dfile.argument('initializer', meshcontext.get_bc_initializer(bcname))
        dfile.endCmd()
        

    if anyfields and includeFields:
        # Cached data.  Cached data must be stored before the current
        # data, so that when it's reloaded, the current data isn't
        # overwritten.
        curtime = meshcontext.getCurrentTime()
        latest = meshcontext.atLatest()
        times = sorted(meshcontext.cachedTimes())
        for time in times:
            meshcontext.restoreCachedData(time)
            writeAndCacheFields(dfile, meshcontext, time)
            meshcontext.releaseCachedData()
        # Restore the mesh to its current state.    
        if latest:
            meshcontext.restoreLatestData()
            meshcontext.releaseLatestData() # allow overwriting
        else:
            meshcontext.restoreCachedData(curtime)
            meshcontext.releaseCachedData()

        # Save the current state, if it hasn't been cached.
        if curtime not in times:
            writeFields(dfile, meshcontext)
            dfile.startCmd(meshmenu.Time)
            dfile.argument('mesh', meshcontext.path())
            dfile.argument('time', meshcontext.getCurrentTime())
            dfile.endCmd()

    # If there are no Fields, the time isn't defined.  It will have
    # been initialized to 0 when the Mesh was created.

    # Cross sections:
    for csname in meshcontext.cross_sections.all_names(): # already ordered
        cs = meshcontext.cross_sections[csname]
        dfile.startCmd(meshmenu.CrossSection)
        dfile.argument('mesh', meshcontext.path())
        dfile.argument('name', csname)
        dfile.argument('cs', cs)
        dfile.endCmd()

    # Scheduled outputs
    meshcontext.outputSchedule.saveAll(dfile, meshcontext)

    # Status. This should be the last thing written.
    dfile.startCmd(meshmenu.Status)
    dfile.argument('mesh', meshcontext.path())
    if isinstance(meshcontext.status, meshstatus.Unsolved):
        # Since the order in which mesh attributes were written to the
        # data file is somewhat arbitrary, the details of an
        # "Unsolved" status aren't terribly meaningful.  Use generic
        # details.
        dfile.argument('status', meshstatus.Unsolved("Newly loaded."))
    else:
        dfile.argument('status', meshcontext.status)
    dfile.endCmd()

def getMyMasterElementDict(masterelems):
    edict = {}
    masterdict = masterelement.getMasterElementDict()
    for ename in masterelems:
        try:
            master = masterdict[ename]
            edict[master.ncorners()] = master
        except KeyError:
            raise ooferror.PyErrUserError("Element type \"%s\" is unknown."
                                          % ename)
    return edict

def _newMesh(menuitem, name, masterelems, skeleton):
    skel = skeletoncontext.skeletonContexts[skeleton].getObject()
    edict = getMyMasterElementDict(masterelems)
    # This hard-codes the realmaterial material factory
    # function. There's not much chance of ever wanting to store
    # Meshes that use other factory functions.
    femesh = skel.femesh(edict, skeletonelement.SkeletonElement.realmaterial,
                         skeleton) #Interface branch, pass skeleton path to femesh
    meshctxt = ooflib.engine.mesh.meshes.add(
        labeltree.makePath(skeleton)+[name], femesh,
        parent=skeletoncontext.skeletonContexts[skeleton],
        elementdict=edict,
        materialfactory=skeletonelement.SkeletonElement.realmaterial)
    meshctxt.createDefaultSubProblem()

meshmenu.addItem(OOFMenuItem(
    'New',
    callback=_newMesh,
    params=[parameter.StringParameter('name', tip="Name for the Mesh."),
            parameter.ListOfStringsParameter('masterelems',
                                             tip="Names of Master Elements."),
            whoville.WhoParameter('skeleton',
                                  skeletoncontext.skeletonContexts,
                                  tip=parameter.emptyTipString)
            ],
    help="Create a Mesh.",
    discussion="""<para>
    Create a &mesh;.  This command is similar to <xref
    linkend="MenuItem-OOF.Mesh.New"/>, but is run from within a data
    file, and not directly by the &oof2; user interface.
    </para>"""
    ))

def _newSubProblem(menuitem, mesh, name, subproblem):
    meshcontext = ooflib.engine.mesh.meshes[mesh]
    meshcontext.reserve()
    meshcontext.begin_writing()
    try:
        subpobj = subproblem.create()
        meshcontext.newSubProblem(subpobj, subproblem,
                                  labeltree.makePath(mesh)+[name])
    finally:
        meshcontext.end_writing()
        meshcontext.cancel_reservation()

subpmenu.addItem(OOFMenuItem(
    'New',
    callback=_newSubProblem,
    params=[parameter.StringParameter('name', tip='Name for the SubProblem'),
            parameter.RegisteredParameter('subproblem',
                                          subproblemtype.SubProblemType,
                                          tip=parameter.emptyTipString),
            whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString)],
    help="Define a Subproblem.",
    discussion="""<para>
    Create a &subproblem;. This command is similar to <xref
    linkend="MenuItem-OOF.Subproblem.New"/>, but is run from within a
    data file, and not directly by the &oof2; user interface.
    </para>"""
    ))

getFieldObj = ooflib.SWIG.engine.field.getField
getEquationObj = ooflib.SWIG.engine.equation.getEquation

def _subpFields(menuitem, subproblem, defined, active, inplane):
    subpctxt = ooflib.engine.subproblemcontext.subproblems[subproblem]
    meshctxt = subpctxt.getParent()
    meshname = meshctxt.path()
    subpname = subpctxt.path()
    subp = subpctxt.getObject()

    for fname in defined:
        field = getFieldObj(fname)
        subp.define_field(field)
        switchboard.notify("field defined", subpname, field.name(), 1)

    for fname in active:
        field = getFieldObj(fname)
        subp.activate_field(field)
        switchboard.notify("field activated", subpname, field.name(), 1)

    for fname in inplane:
        field = getFieldObj(fname)
        meshctxt.set_in_plane_field(field, True)
        switchboard.notify("field inplane", meshname, field.name(), 1)

    subpctxt.changed("Fields loaded.")

subpmenu.addItem(OOFMenuItem(
    'Fields',
    callback=_subpFields,
    params=[whoville.WhoParameter('subproblem',
                                  ooflib.engine.subproblemcontext.subproblems,
                                  tip=parameter.emptyTipString),
            parameter.ListOfStringsParameter('defined', tip="Defined Fields."),
            parameter.ListOfStringsParameter('active', tip="Active Fields."),
            parameter.ListOfStringsParameter('inplane', tip="In-plane Fields.")
            ],
    help="Load subproblem Field definitions.",
    discussion="""<para>
    Load the list of the names of the defined &fields; for a
    &subproblem;, excluding the time derivative &fields;.  Auxiliary
    time derivative &fields; are handled by <xref
    linkend="MenuItem-OOF.LoadData.Subproblem.Time_Derivative_Fields"/>.
    </para><para> This command is used within data files and is not
    invoked directly by the &oof2; user interface.
    </para>"""
    ))

# Time derivative fields are handled separately for backwards
# compatibility.  Adding them to _subpFields would break
# pre-time-dependence data files.

def _subpTimeDerivFields(menuitem, subproblem, fields):
    subpctxt = ooflib.engine.subproblemcontext.subproblems[subproblem]
    meshctxt = subpctxt.getParent()
    meshname = meshctxt.path()
    subpname = subpctxt.path()
    subp = subpctxt.getObject()
    for fname in fields:
        field = getFieldObj(fname)
        subp.define_field(field.time_derivative())
        subp.define_field(field.out_of_plane_time_derivative())
    subpctxt.changed("Time-derivative fields defined.")

subpmenu.addItem(OOFMenuItem(
    'Time_Derivative_Fields',
    callback=_subpTimeDerivFields,
    params=[whoville.WhoParameter('subproblem',
                                  ooflib.engine.subproblemcontext.subproblems,
                                  tip=parameter.emptyTipString),
            parameter.ListOfStringsParameter('fields',
                           tip="Fields with auxiliary time-derivative Fields.")
            ],
    help="Load subproblem Field definitions.",
    discussion="""<para>
    Load the list of the names of the defined time-derivative &fields;
    for a &subproblem;.  These are treated separately from the other
    &fields; for backwards compatibility with old data files.  See
    <xref
    linkend="MenuItem-OOF.LoadData.Subproblem.Fields"/>.</para><para>
    This command is used within data files and is not invoked directly
    by the &oof2; user interface.
    </para>"""
    ))

def _loadFieldValues(menuitem, mesh, fields, field_values):
    meshctxt = ooflib.engine.mesh.meshes[mesh]
    femesh = meshctxt.getObject()
    fieldlist = [getFieldObj(fld) for fld in fields] # get objects from names
    for fv in field_values:
        index = fv[0]
        node = femesh.getNode(index)
        pointer = 1
        for field in fieldlist:
            for i in range(field.ndof()):
                field.setvalue(femesh, node, i, fv[pointer])
                pointer += 1

    # Field values can change the appearance of a newly-loaded mesh.
    switchboard.notify("mesh data changed", meshctxt)
    switchboard.notify("redraw")

meshmenu.addItem(OOFMenuItem(
    'Load_Field',
    callback = _loadFieldValues,
    params=[whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString),
            parameter.ListOfStringsParameter('fields',
                                             tip="Names of Fields."),
            parameter.ListOfTuplesOfIntFloatsParameter('field_values',
                                                       tip="Values of Fields.")],
    help="Load Field values into a Mesh.",
    discussion="""<para>

    Load values for a &field; at the &nodes; of a saved &mesh;.  This
    command is used internally in data files and not invoked directly
    by the &oof2; user interface.</para>

    <para> The <varname>fields</varname> parameter is a <link
    linkend='Object-list'>list</link> of the names of the &fields;
    that are defined on the &mesh;.  The
    <varname>field_values</varname> parameter is a list of tuples
    containing an integer node number, followed by the components of
    the listed fields in the listed order.</para>

    <para> Because different &nodes; may have different sets of
    &fields; defined on them, more than one call to
    <command>Load_Field</command> may be needed to load all of the
    &fields; on a &mesh;.
    
    </para>"""
    ))

def _loadTime(menuitem, mesh, time):
    meshctxt = ooflib.engine.mesh.meshes[mesh]
    meshctxt.setCurrentTime(time)
    switchboard.notify("mesh changed", meshctxt)

meshmenu.addItem(OOFMenuItem(
    'Time',
    callback=_loadTime,
    params=[whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString),
            parameter.FloatParameter('time', tip=parameter.emptyTipString)],
    help="Set the current time for a saved Mesh.",
    discussion="""<para>
    Set the time for the current &field; values.  This command is used
    within data files and not invoked directly by the &oof2; user
    interface.
    </para>"""))

def _cacheFields(menuitem, mesh, time):
    meshctxt = ooflib.engine.mesh.meshes[mesh]
    meshctxt.setCurrentTime(time)
    meshctxt.cacheCurrentData()
    switchboard.notify("mesh changed", meshctxt)
    switchboard.notify("mesh data changed", meshctxt) # ???

meshmenu.addItem(OOFMenuItem(
    'Cache_Fields',
    callback=_cacheFields,
    params=[whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString),
            parameter.FloatParameter('time', tip=parameter.emptyTipString)],
    help="Store Field values in the Mesh's cache.",
    discussion="""<para>

    Store the current Field values in the data cache. This command is
    used internally in data files not invoked directly by the &oof2;
    user interface.</para>

    <para>Cached fields are stored in a data file as a series of <xref
    linkend="MenuItem-OOF.LoadData.Mesh.Load_Field"/> commands
    followed by a call to <command>Cache_Fields</command>, which moves
    the data into the cache.
    
    </para>"""
    ))

def _subpEqns(menuitem, subproblem, equations):
    subpctxt = ooflib.engine.subproblemcontext.subproblems[subproblem]
    subpname = subpctxt.path()
    subp = subpctxt.getObject()
    for eqn in equations:
        equation = getEquationObj(eqn)
        subp.activate_equation(equation)
        switchboard.notify('equation activated', subpname, equation.name(), 1)

subpmenu.addItem(OOFMenuItem(
    'Equations',
    callback=_subpEqns,
    params=[whoville.WhoParameter('subproblem',
                                  ooflib.engine.subproblemcontext.subproblems,
                                  tip=parameter.emptyTipString),
            parameter.ListOfStringsParameter('equations',
                                             tip="Active equations.")],
    help="Load subproblem Equations.",
    discussion="""<para>
    Load the list of active &equations; from a saved &mesh;.  This
    command is unsed internally in data files and not invoked directly
    by the &oof2; user interface.
    </para>"""
    ))

def _subpSolver(menuitem, subproblem, solver_mode):
    subpctxt = ooflib.engine.subproblemcontext.subproblems[subproblem]
    subpctxt.solver_mode = solver_mode
    switchboard.notify("subproblem solver changed", subpctxt.path())

subpmenu.addItem(OOFMenuItem(
    'Solver',
    callback=_subpSolver,
    params=[whoville.WhoParameter('subproblem',
                                  ooflib.engine.subproblemcontext.subproblems,
                                  tip=parameter.emptyTipString),
            parameter.RegisteredParameter('solver_mode', solvermode.SolverMode,
                                          tip="The solver.")
            ],
    help="Assign a solver to a subproblem.",
    discussion="""<para>

    Assign a solver to a subproblem. This command is used internally
    in data files and not invoked directly by the &oof2; user
    interface.

    </para>"""
    ))


def _meshBoundary_Conditions(menuitem, mesh, bcname, bc):
    bc.add_to_mesh(bcname, mesh)

meshmenu.addItem(OOFMenuItem(
    'Boundary_Condition',
    callback = _meshBoundary_Conditions,
    params=[whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString),
            parameter.StringParameter('bcname',
                                      tip="Name of the boundary condition."),
            parameter.RegisteredParameter('bc', bdycondition.BC,
                                          tip=parameter.emptyTipString)],
    help="Load a boundary conditon.",
    discussion="""<para>
    Load a <link linkend='Section-Tasks-BoundaryCondition'>boundary
    condition</link> from a saved &mesh;.  This command is used within
    data files and not invoked directly by the &oof2; user interface.
    </para>"""
    ))

meshmenu.addItem(OOFMenuItem(
        'Set_BC_Initializer',
        callback=ooflib.engine.IO.boundaryconditionmenu.setBCInit,
        params=[whoville.WhoParameter(
                'mesh', ooflib.engine.mesh.meshes,
                tip=parameter.emptyTipString),
            parameter.StringParameter(
                'bc',
                tip="Name of the boundary condition to initialize"),
            parameter.RegisteredParameter(
                'initializer',
                bdycondition.FloatBCInitMethod,
                tip='How the initial value is to be interpreted.')],
        help="Load a FloatBC initializer.",
        discussion="""<para>
        Load an initializer for a floating boundary condition from a
        saved &mesh;.  This command is used within data files and not
        invoked directly by the &oof2; user interface.
        </para>"""
        ))

meshmenu.addItem(OOFMenuItem(
    'Initialize_Field',
    callback=ooflib.engine.IO.meshmenu.initField,
    params=[
    whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                          tip=parameter.emptyTipString),
    meshparameters.FieldParameter('field', tip=parameter.emptyTipString,
                                  outofplane=True),
    fieldinit.FieldInitParameter('initializer', tip=parameter.emptyTipString)
    ],
    help="Initialize a Field.",
    discussion="""<para>
    Initialize a &field; on a saved &mesh;.  If <link
    linkend='MenuItem-OOF.LoadData.Mesh.Load_Field'>field data</link>
    is saved as well, it will overwrite the &fields; from the
    initializer.  This command is used within data files and not
    invoked directly by the &oof2; user interface.
    </para>"""))



def _crossSection(menuitem, mesh, name, cs):
    meshcontext = ooflib.engine.mesh.meshes[mesh]
    meshcontext.reserve()
    meshcontext.begin_writing()
    try:
        meshcontext.addCrossSection(name, cs)
    finally:
        meshcontext.end_writing()
        meshcontext.cancel_reservation()

meshmenu.addItem(OOFMenuItem(
    'CrossSection',
    callback=_crossSection,
    params=[
    whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                          tip=parameter.emptyTipString),
    parameter.StringParameter('name', tip="Name of the cross section."),
    parameter.RegisteredParameter('cs', meshcrosssection.MeshCrossSection,
                                  tip=parameter.emptyTipString)],
    help="Load a Cross Section.",
    discussion="""<para>
    Load a <link linkend='RegisteredClass-MeshCrossSection'>cross
    section</link>.  This command is used within data files and not
    invoked directly by the &oof2; user interface.
    </para>"""
    ))


def _assignMat(menuitem, mesh, elements, material):
    reporter.warn(
       "Explicit material assignments to mesh elements are no longer supported!"
    )

meshmenu.addItem(OOFMenuItem(
    'AssignMaterial',
    callback=_assignMat,
    params=[whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString),
            parameter.ListOfIntsParameter('elements',
                                          tip='Indices of the elements'),
            parameter.StringParameter('material',
                                      tip='Material to assign to the elements')
            ],
    help="Load explicitly assigned Materials into a Mesh",
    no_doc=1
    ))

def _status(menuitem, mesh, status):
    meshcontext = ooflib.engine.mesh.meshes[mesh]
    meshcontext.setStatus(status)

meshmenu.addItem(OOFMenuItem(
    'Status',
    callback=_status,
    params=[
            whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString),
            parameter.RegisteredParameter('status',
                                          meshstatus.MeshStatus,
                                          tip=parameter.emptyTipString)],
    help="Set the Mesh status.",
    discussion="""<para>
    Set a Mesh's status.  This command is used within data files and
    not invoked directly by the &oof2; user interface.
    </para>"""
))

##########################################################

## Old menu items to support mesh files written before the advent of
## SubProblems.

def _meshFields(menuitem, mesh, defined, active, inplane):
    meshctxt = ooflib.engine.mesh.meshes[mesh]
    subpname = meshctxt.get_default_subproblem().path()

    for fname in defined:
        field = getFieldObj(fname)
        meshctxt.get_default_subproblem().getObject().define_field(field)
        switchboard.notify("field defined", subpname, field.name(), 1)

    for fname in active:
        field = getFieldObj(fname)
        meshctxt.get_default_subproblem().getObject().activate_field(field)
        switchboard.notify("field activated", subpname, field.name(), 1)

    for fname in inplane:
        field = getFieldObj(fname)
        meshctxt.set_in_plane_field(field, True)
        switchboard.notify("field inplane", mesh, field.name(), 1)

    switchboard.notify("mesh changed", meshctxt)

meshmenu.addItem(OOFMenuItem(
    'Field',
    callback=_meshFields,
    params=[whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString),
            parameter.ListOfStringsParameter('defined',
                                             tip="Defined Fields."),
            parameter.ListOfStringsParameter('active', tip="Active Fields."),
            parameter.ListOfStringsParameter('inplane', tip="In-plane Fields.")],
    help="Load Fields, the old way",
    discussion="""<para>
    Load the list of defined &fields; from a saved &mesh;.  This
    command is used within <emphasis>old</emphasis> data files, from
    before the invention of &subproblems;, and not invoked directly by
    the &oof2; user interface.
    </para>"""
    ))


def _meshEquations(menuitem, mesh, equations):
    meshctxt = ooflib.engine.mesh.meshes[mesh]
    subpname = meshctxt.get_default_subproblem().path()
    subp = meshctxt.get_default_subproblem().getObject()

    for eqn in equations:
        equation = getEquationObj(eqn)
        subp.activate_equation(equation)
        switchboard.notify('equation activated', subpname, equation.name(), 1)

meshmenu.addItem(OOFMenuItem(
    'Equation',
    callback=_meshEquations,
    params=[whoville.WhoParameter('mesh', ooflib.engine.mesh.meshes,
                                  tip=parameter.emptyTipString),
            parameter.ListOfStringsParameter('equations',
                                             tip="Names of Equations.")],
    help="Load Equations.",
    discussion="""<para>
    Load the list of active &equations; from a saved &mesh;.  This
    command is used within <emphasis>old</emphasis> data files, from
    before the invention of &subproblems;, and not invoked directly by
    the &oof2; user interface.
    </para>"""
    ))



#################################################################

# Scheduled output of field data during time evolution.

class MeshFileOutput(scheduledoutput.ScheduledOutput):
    def start(self, meshcontext, time, continuing):
        # ScheduledOutput.start() opens the file and resets 'rewound'.
        writeskel = self.destination.rewound or not continuing
        scheduledoutput.ScheduledOutput.start(self, meshcontext, time,
                                              continuing)
        if writeskel:
            skelcontext = meshcontext.getParent()
            mscontext = skelcontext.getParent()
            microstructureIO.writeMicrostructure(self.destination.dfile(),
                                                 mscontext)
            skeletonIO.writeSkeleton(self.destination.dfile(), skelcontext)
            writeMesh(self.destination.dfile(), meshcontext,
                      includeFields=False)
    def perform(self, meshcontext, time):
        writeAndCacheFields(self.destination.dfile(), meshcontext, time)

registeredclass.Registration(
    'Mesh File',
    scheduledoutput.ScheduledOutput,
    MeshFileOutput,
    ordering=1,
    destinationClass=outputdestination.DataFileOutput,
    tip="Save a complete Mesh data file containing field data at each output time.",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/meshfileoutput.xml'))

#################################################################

##########
# ABAQUS #
##########

import datetime

def writeABAQUSfromMesh(filename, mode, meshcontext):
    femesh=meshcontext.femesh()

    buffer=["*HEADING\nABAQUS-style file created by OOF2 on %s from a mesh of the microstructure %s.\n "
        % (datetime.datetime.today(), meshcontext.getSkeleton().MS.name())]

    # Build dictionaries of elements and nodes, giving each one a
    # unique index. Elements and nodes already have indices, but the
    # sets of indices may have gaps.  Abaqus require a contiguous set
    # starting at 1.  The element dict is keyed by the oof2 element
    # index, but the node dict is keyed by *position* so that split
    # nodes don't appear in the abaqus output.  All oof2 nodes at the
    # same position are represented by a single abaqus node.

    nodedict = utils.OrderedDict()
    i = 1
    # use only those nodes that are associated with elements that have
    # a material
    for el in femesh.elements():
        if el.material():
            for node in el.node_iterator():
                if nodedict.setdefault(node.position(), i) == i:
                    i += 1

    # same for elements
    elementdict = utils.OrderedDict()
    i = 1
    # In the same loop, get the list of materials and masterelements
    # directly from the elements (i.e. straight from the horses'
    # mouths. May be inefficient.)
    materiallist=utils.OrderedDict()
    masterElementDict=utils.OrderedDict()
    for el in femesh.elements():
        ematerial = el.material()
        emasterelement = el.masterelement()
        if ematerial:
            matname = ematerial.name()
            if matname not in materiallist:
                materiallist[matname] = ematerial
            melname = emasterelement.name()
            if melname not in masterElementDict:
                masterElementDict[melname] = emasterelement
            elementdict[el.get_index()] = i
            i += 1

    buffer.append("** Materials defined by OOF2:\n")
    for matname, details in materiallist.items():
        buffer.append("**   %s:\n" % (matname))
        for prop in details.properties:
            for param in prop.registration().params:
                buffer.append("**     %s: %s\n" % (param.name,param.value))

    # Note that meshcontext.elementdict is different from elementdict
    # we constructed above!
    buffer.append("** Master elements used in OOF2:\n")
    for ekey, ename in meshcontext.elementdict.items():
        buffer.append("**   %s: %s, %s\n"
                      % (ekey, ename.name(), ename.description()))

    buffer.append("** Boundary Conditions:\n")
    for bcname in meshcontext.allBndyCondNames():
        bc=meshcontext.getBdyCondition(bcname)
        buffer.append("**   %s: %s\n" % (bcname,repr(bc)))

    buffer.append("""** Notes:
**   The set of nodes and elements may be different from the set
**    created from a skeleton depending on the element type and if the
**    mesh was refined.
** The materials and boundary conditions provided by OOF2 may be
**   translated into ABAQUS by the user.
** The element type provided below should be verified and modified
**   accordingly.
** Only elements (and nodes of such elements) that have an associated
**   material are included in this file.
""")

    listbuf=["*NODE\n"]
    # Get nodes that are associated with elements that have a material
    # definition.  Other nodes aren't in nodedict.
    for (position, index) in nodedict.items():
        listbuf.append("%d, %s, %s\n" % (index, position.x, position.y))
    buffer.extend(listbuf)

    for ename in meshcontext.elementdict.values():
        ## TODO OPT: Use a separate buffer for each element type, and
        ## only loop over the elements once!  Concatenate the buffers
        ## at the end.
        try:
            # Group the elements according to element type
            listbuf=[
"""** The OOF2 element type is %s. The type provided for ABAQUS is only a guess
** and may have to be modified by the user to be meaningful.
*ELEMENT, TYPE=CPS%d
"""
% (repr(ename),masterElementDict[ename.name()].nnodes())]
            # Trivia: C stands for Continuum, PS for Plane Stress (PE
            # - Plane strain)
            for el in femesh.elements():
                if el.material():
                    if el.masterelement().name()==ename.name():
                        listbuf2=["%d" % (elementdict[el.get_index()])]
                        cornernodelist=[]
                        # List corner nodes first, as preferred by ABAQUS
                        for node in el.cornernode_iterator():
                            listbuf2.append("%d" % (nodedict[node.position()]))
                            cornernodelist.append(node.index())
                        # List the non-corner nodes (midpoints and
                        # center point of a Q9_9)
                        for node in el.node_iterator():
                            if node.index() not in cornernodelist:
                                listbuf2.append(
                                    "%d" % (nodedict[node.position()]))
                        listbuf.append(utils.stringjoin(listbuf2,", ")+"\n")
            buffer.extend(listbuf)
        except KeyError:
            ## TODO: Which KeyError are we ignoring here?  Use
            ## try/except/else to put the 'except' closer to the
            ## exception.
            pass

    buffer.append("** Point boundaries in OOF2\n")
    pbnames = meshcontext.pointBoundaryNames()
    pbnames.sort()
    for pbname in pbnames:
        buffer.append("*NSET, NSET=%s\n" % (pbname))
        listbuf=[]
        i=0
        for node in femesh.getBoundary(pbname).nodeset:
            try:
                somevalue=nodedict[node.position()]
            except KeyError:
                pass
            else:
                if i>0 and i%16==0:
                    # Just in case the list does contain more than 16 nodes:)
                    listbuf.append("\n%d" % (somevalue))
                else:
                    listbuf.append("%d" % (somevalue))
                i+=1
        buffer.append(utils.stringjoin(listbuf,", ")+"\n")

    buffer.append("** Edge boundaries in OOF2\n")
    ebnames = meshcontext.edgeBoundaryNames()
    ebnames.sort()
    for ebname in ebnames:
        buffer+="*NSET, NSET=%s\n" % (ebname)
        listbuf=[]
        i=0
        for node in femesh.getBoundary(ebname).edgeset.nodes():
            try:
                somevalue=nodedict[node.position()]
            except KeyError:
                pass
            else:
                # Respect the 16 item-per-row-limit of ABAQUS
                if i>0 and i%16==0:
                    listbuf.append("\n%d" % (somevalue))
                else:
                    listbuf.append("%d" % (somevalue))
                i+=1
        buffer.append(utils.stringjoin(listbuf,", ")+"\n")

    for matname in materiallist:
        ## TODO OPT: Use a separate buffer for each material, and only
        ## loop over elements once.
        buffer+="*ELSET, ELSET=%s\n" % matname
        listbuf=[]
        i=0
        for el in femesh.elements():
            if el.material():
                if el.material().name()==matname:
                    if i>0 and i%16==0:
                        listbuf.append("\n%d" % elementdict[el.get_index()])
                    else:
                        listbuf.append("%d" % elementdict[el.get_index()])
                    i+=1
        buffer.append(utils.stringjoin(listbuf,", ") +
                      "\n*SOLID SECTION, ELSET=%s, MATERIAL=%s\n" % (matname,
                                                                     matname))

    for matname in materiallist:
        buffer.append("*MATERIAL, NAME=%s\n** Use the information in the header to complete these fields under MATERIAL\n" % matname)

    # Save/Commit to file. Perhaps should be done outside the current method.
    fp=open(filename,mode)
    fp.write("".join(buffer))
    fp.close()

