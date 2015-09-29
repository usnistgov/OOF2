# -*- python -*-
# $RCSfile: relaxation.py,v $
# $Revision: 1.71 $
# $Author: langer $
# $Date: 2011/03/22 14:59:09 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import progress
from ooflib.SWIG.common import threadstate
from ooflib.SWIG.engine import equation
from ooflib.SWIG.engine import field
from ooflib.SWIG.engine import masterelement
from ooflib.SWIG.engine import material
from ooflib.SWIG.engine import preconditioner
from ooflib.SWIG.engine.property.elasticity.iso import iso
from ooflib.SWIG.engine.property.skeletonrelaxationrate \
    import skeletonrelaxationrate
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import bdycondition
from ooflib.engine import evolve
from ooflib.engine import fieldinit
from ooflib.engine import nonlinearsolver
from ooflib.engine import materialmanager
from ooflib.engine import matrixmethod
from ooflib.engine import profile
from ooflib.engine import propertyregistration
from ooflib.engine import solvermode
from ooflib.engine import skeletonmodifier
from ooflib.engine import staticstep
from ooflib.engine.IO import isocijkl
from ooflib.engine.IO import meshmenu
import ooflib.engine.mesh


class Relax(skeletonmodifier.SkeletonModifier):

    materialName = '__bone_marrow__'

    def __init__(self, alpha, gamma, iterations):
        self.alpha = alpha
        self.gamma = gamma
        self.iterations = iterations
        self.count = 0
        self.solver_converged = True
        self.meshname = None

        threadno = threadstate.findThreadNumber()

        ## create material
        materialmanager.materialmanager.add_secret(self.materialName)
        ## SkeletonRelaxationRateTensor is the PropertyRegistration for the
        ## SkeletonRelaxationRate property.
        relaxPropReg = skeletonrelaxationrate.SkeletonRelaxationRateTensor.\
            named_copy("__relaxationrate%d__" % threadno, secret=True)
        relaxPropReg.getParameter("gamma").value = self.gamma
        relaxPropReg.getParameter("alpha").value = self.alpha
        self.skelRelRate = relaxPropReg()
        # gamma_parameter = \
        #     skeletonrelaxationrate.SkeletonRelaxationRateTensor.getParameter(
        #     'gamma')
        # gamma_parameter.value = self.gamma
        # alpha_parameter = \
        #     skeletonrelaxationrate.SkeletonRelaxationRateTensor.getParameter(
        #     'alpha')
        # alpha_parameter.value = self.alpha
        # self.skelRelRate = skeletonrelaxationrate.SkeletonRelaxationRateTensor()
        materialmanager.materialmanager.add_prop(self.materialName,
                                                 self.skelRelRate.name())


        # isotropic elasticity
        stiffnessPropReg = iso.IsotropicElasticity.named_copy(
            "__stiffness%d__" % threadno, secret=True)
        stiffnessPropReg.getParameter('cijkl').value = \
            isocijkl.IsotropicRank4TensorCij(c11=1.0, c12=0.5)
        self.stiffness = stiffnessPropReg()
        materialmanager.materialmanager.add_prop(
            self.materialName, self.stiffness.name())

    def material(self):
        return materialmanager.getMaterial(self.materialName)

    def goodToGo(self, skeleton):
        skeleton.checkIllegality()
        return (not skeleton.illegal()
                and self.count < self.iterations
                and self.solver_converged)
    def updateIteration(self):
        self.count +=1
    def set_fakematerial(self, skelelement, skeleton):
        return self.material()
    def create_mesh(self, context):
        ## context is a skeleton context
        ## setup element types
        edict = {}
        # get linear isoparametric master elements
        if config.dimension() == 2:
            edict[3] = masterelement.getMasterElementDict()['T3_3']
            edict[4] = masterelement.getMasterElementDict()['Q4_4']
        elif config.dimension() == 3:
            edict[4] = masterelement.getMasterElementDict()['T4_4']
        skel = context.getObject()
        ## returns a Mesh (Who) object
        self.meshname = context.path() + ":__internal_mesh__"
        #Interface branch, pass skeleton path to femesh
        femesh = skel.femesh(edict, self.set_fakematerial, context.path())
        meshcontext = ooflib.engine.mesh.meshes.add(
            self.meshname, femesh,
            parent=context,
            skeleton=skel, elementdict=edict)
        meshcontext.createDefaultSubProblem()

        return meshcontext

    def define_fields(self, meshctxt):
        femesh = meshctxt.femesh()
        subp = meshctxt.get_default_subproblem().getObject()
        displacement = field.getField('Displacement')
        subp.define_field(displacement)
        subp.activate_field(displacement)
        if config.dimension() == 2:
            meshctxt.set_in_plane_field(displacement, True)

    def activate_equations(self, meshctxt):
        meshctxt.get_default_subproblem().getObject().activate_equation(
            equation.getEquation('Force_Balance'))
    def set_boundary_conditions(self, mesh):
        ## here, mesh is a Mesh (Who) object
        displacement = field.getField('Displacement')
        if config.dimension() == 2:
            ## left boundary
            self.leftBoundaryCondition = \
                 bdycondition.DirichletBC(displacement,
                                          'x',
                                          equation.getEquation('Force_Balance'),
                                          'x',
                                          profile.ConstantProfile(0),
                                          'left'
                                          )
            self.leftBoundaryCondition.add_to_mesh('left', mesh.path())

            ## right boundary
            self.rightBoundaryCondition = \
                 bdycondition.DirichletBC(displacement,
                                          'x',
                                          equation.getEquation('Force_Balance'),
                                          'x',
                                          profile.ConstantProfile(0),
                                          'right'
                                          )
            self.rightBoundaryCondition.add_to_mesh('right', mesh.path())

            ## top boundary
            self.topBoundaryCondition = \
                 bdycondition.DirichletBC(displacement,
                                          'y',
                                          equation.getEquation('Force_Balance'),
                                          'y',
                                          profile.ConstantProfile(0),
                                          'top'
                                          )
            self.topBoundaryCondition.add_to_mesh('top', mesh.path())

            ## bottom boundary
            self.bottomBoundaryCondition = \
                 bdycondition.DirichletBC(displacement,
                                          'y',
                                          equation.getEquation('Force_Balance'),
                                          'y',
                                          profile.ConstantProfile(0),
                                          'bottom'
                                          )
            self.bottomBoundaryCondition.add_to_mesh('bottom', mesh.path())

    def update_node_positions(self, skeleton, mesh):
        skeleton.timestamp.increment()
        ## mesh is a Mesh Who object
        femesh = mesh.getObject()
        displacement = field.getField('Displacement')
        for node in skeleton.nodes:

            #Interface branch
##            realnode = femesh.getNode(node.meshindex)
            #TODO: Do we have to update all the realmesh nodes
            #that correspond to node?
            skelel = node.neighborElements()[0]
            realel = femesh.getElement(skelel.meshindex)
            realnode = realel.getCornerNode(skelel.getNodeIndexIntoList(node))

            dx = displacement.value(femesh, realnode, 0)
            dy = displacement.value(femesh, realnode, 1)
            if config.dimension() == 2:
                skeleton.moveNodeBy(node, primitives.Point(dx, dy))
            elif config.dimension() == 3:
                dz = displacement.value(femesh, realnode, 2)
                skeleton.moveNodeBy(node, primitives.Point(dx, dy, dz))

    def apply(self, oldskeleton, context):
        prog = progress.getProgress("Relax", progress.DEFINITE)
        prog.setMessage("Preparing to relax...")
        return oldskeleton.deputyCopy()
    def initialize_fields(self, mesh):
        if config.dimension() == 2:
            initializer = fieldinit.ConstTwoVectorFieldInit(cx=0.0,cy=0.0)
        elif config.dimension() == 3:
            initializer = fieldinit.ConstTwoVectorFieldInit(cx=0.0,cy=0.0,cz=0.0)
        meshmenu.initField(self, self.meshname, field.getField('Displacement'),
                           initializer)
        meshmenu.applyFieldInits(self, self.meshname)
    def postProcess(self, context):
        ## This function first creates a mesh with custom-made properties,
        ## then assigns "temporary" properties to pixels
        ## and specifies BCs and equations.
        ## Next, iterates for the solution using the specified solver,
        ## accepts all node moves and redraws skeleton.
        ## It repeats these steps until iteration criteria has been met.
        ## Finally, the (temporary) mesh and the rest  of the temporary
        ## objects are cleaned up.

        ## create progress bar
        prog = progress.getProgress("Relax", progress.DEFINITE)

        ## get skeleton and calculate energy
        skeleton = context.getObject()
        before = skeleton.energyTotal(self.alpha)
        self.count = 0

        while self.goodToGo(skeleton) and not prog.stopped():
            ## femesh is created and properties are assigned
            mesh = self.create_mesh(context) # mesh context object

            ## define displacement field
            self.define_fields(mesh)
            ## activate the mechanical balance equation
            self.activate_equations(mesh)
            mesh.changed("Relaxing")
            ## constrain the nodes on the boundaries to only slide
            ## along the edge
            self.set_boundary_conditions(mesh)

            # solve linear system.
            self.coreProcess(mesh, mesh.get_default_subproblem())
            if prog.stopped():
                break

            # Update positions of nodes in the Skeleton
            context.begin_writing()
            try:
                self.update_node_positions(skeleton, mesh)
            finally:
                context.end_writing()

            mesh.lockAndDelete()

            switchboard.notify("skeleton nodes moved", context)
            switchboard.notify("redraw")

            self.updateIteration() ## update iteration manager machinery
            prog.setFraction(1.0*self.count/self.iterations)
            prog.setMessage("%d/%d iterations" % (self.count, self.iterations))

        prog.finish()

        ## calculate total energy improvement, if any.
        after = skeleton.energyTotal(self.alpha)
        if before:
            rate = 100.0*(before-after)/before
        else:
            rate = 0.0
        diffE = after - before
        reporter.report("Relaxation complete: deltaE = %10.4e (%6.3f%%)"
                        % (diffE, rate))

        if config.dimension() == 2:
            del self.topBoundaryCondition
            del self.leftBoundaryCondition
            del self.bottomBoundaryCondition
            del self.rightBoundaryCondition

        materialmanager.materialmanager.delete_prop(self.stiffness.name())
        materialmanager.materialmanager.delete_prop(self.skelRelRate.name())
        propertyregistration.AllProperties.delete(self.stiffness.name())
        propertyregistration.AllProperties.delete(self.skelRelRate.name())
        materialmanager.materialmanager.delete_secret(self.materialName)

    def coreProcess(self, meshctxt, subp):
        subp.solver_mode = solvermode.AdvancedSolverMode(
            time_stepper=staticstep.StaticDriver(),
            nonlinear_solver=nonlinearsolver.NoNonlinearSolver(),
            symmetric_solver=matrixmethod.ConjugateGradient(
                preconditioner.ILUPreconditioner(),
                1.e-5,          # tolerance
                1000            # max_iterations
                ),
            asymmetric_solver=matrixmethod.BiConjugateGradient(
                preconditioner.ILUPreconditioner(),
                1.e-5,          # tolerance
                1000            # max_iterations
                )
            )
        meshctxt.begin_writing()
        try:
            try:
                evolve.evolve(meshctxt, 0.0)
            except:
                # TODO: Be more explicit about what exceptions
                # should be handled here, to distinguish actual
                # convergence failures from programming errors.
                self.solver_converged = False
            else:
                self.solver_converged = True
        finally:
            meshctxt.end_writing()

#################################################

registeredclass.Registration(
    'Relax',
    skeletonmodifier.SkeletonModifier,
    Relax,
    ordering=0.5,
    params=[
        skeletonmodifier.alphaParameter,
        parameter.FloatParameter(name = 'gamma', value = 0.5,
                                 tip='Node mobility'),
        parameter.IntParameter('iterations', value = 1, tip='number of steps')
        ],
    tip='Improve a skeleton by solving a finite element system where the properties are functions of the underlying homogeneity and shape',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/relax.xml')
    )


# Old tip for gamma:
#    tip='Coefficient of mesh expansion or rate of
#    expansion/contraction per inhomogeneity or per deviation from
#    ideal shape. A small positive value is recommended for meshes
#    where element edges want to be made coincide with pixel group
#    edges.'
