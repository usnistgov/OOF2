# -*- python -*-
# $RCSfile: adaptive.py,v $
# $Revision: 1.18 $
# $Author: langer $
# $Date: 2014/09/27 21:41:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.tutorials import tutorial
TutoringItem = tutorial.TutoringItem
TutorialClass = tutorial.TutorialClass

TutorialClass(
    subject = "Adaptive Mesh Refinement",
    ordering = 6,
    lessons = [
    
    TutoringItem(
    subject="Introduction",
    comments=

    """OOF2 provides a rudimentary adaptive mesh refinement tool via
    BOLD(a Posteriori) error estimation scheme that utilizes the
    BOLD(Superconvergent Patch Recovery) of BOLD(Zienkiewicz) and
    BOLD(Zhu) -- more discussion of the subject can be found in the
    OOF2 manual.

    In this tutorial, the adaptive mesh refinement will be briefly
    demonstrated.

    """),

    TutoringItem(
    subject="Loading a Skeleton",
    comments=
    
    """Open a graphics window, if none has been opened yet, with
    the BOLD(Graphics/New) command in the BOLD(Windows) menu.

    Locate the file BOLD(el_shape.mesh) within the share/oof2/examples
    directory in your OOF2 installation.

    A data file can be loaded from the BOLD(File) menu in the main OOF2
    window (BOLD(File -> Load -> Data)).
    Select the example file (BOLD(el_shape.mesh)) in the file selector,
    and click BOLD(OK).
    """,
    signal = ("new who", "Skeleton")
    ),
    
    TutoringItem(
    subject="L-shaped Domain",
    comments=

    """If you have finished the tutorial for BOLD(Non-rectangular Domain),
    you should be familiar with this Mesh.
    The Mesh looks rectangular but Material has been assigned only to
    the BOLD(green) part of the Mesh, which simulates an effective
    BOLD(L)-shaped domain.
    
    Move on to the next slide.
    """ ),

    TutoringItem(
    subject="Boundary Conditions",
    comments="""The Mesh is ready to be solved.

    The applied boundary conditions (all BOLD(Dirichlet)) are:

    BOLD(1.) u_x = 0 on the BOLD(left) side
    
    BOLD(2.) u_y = 0 on the BOLD(left) side

    BOLD(3.) u_x = 0 on the BOLD(top) side

    BOLD(4.) u_y = 0 on the BOLD(top) side

    BOLD(5.) u_y = -2 on the BOLD(right) side"""
    ),

    TutoringItem(
    subject="Solution",
    comments=
    
    """Open the BOLD(Solver) page and just click BOLD(Solve).
    A deformed Mesh will be displayed in the graphics window.
    Note that dummy elements (BOLD(ivory) part) are BOLD(NOT) displayed
    in the deformed Mesh.

    For a clearer view, hide the Skeleton layer.  Navigate to the
    bottom of the graphics window and find a layer labeled
    BOLD(Skeleton(skeleton)) and uncheck the leftmost square box to
    hide the layer.

    Due to the shape of the domain, it is obvious that stresses are
    highly concentrated in the region surrounding the corner.
    It is also safe to assume that errors in this region would be higher
    than in other regions.

    Move on to the next slide to start the process for adaptive mesh
    refinement.
    """,
    signal = "mesh solved"
    ),

    TutoringItem(
    subject="Adaptive Mesh Refinement",
    comments=

    """Go to the BOLD(Skeleton) page.  (In earlier versions of OOF2,
    adaptive mesh refinement was a Mesh modification method.  As of
    version 2.1, it's part of BOLD(Skeleton) refinement.)

    Choose the BOLD(Refine) Skeleton Modification method, and set
    BOLD(targets) to BOLD(Adaptive Mesh Refinement). 

    The BOLD(subproblem) parameter determines which subproblem's
    elements and fields will be used to determine which elements will
    be refined.  Leave it set to BOLD(el_shape.png/skeleton/mesh/default).

    The BOLD(estimator) parameter determines which error estimator to
    use. Elements with high error estimates will be refined.
    Currently, OOF2 only provides one estimator, the BOLD(Z-Z
    Estimator).  Set its parameters to BOLD(norm)=BOLD(L2 Error Norm),
    BOLD(flux)=BOLD(Stress), and BOLD(threshold)=BOLD(10).  This means
    that the L2 norm of the difference between the computed flux and
    the "recovered" flux will be computed, and that any elements in
    which this difference is greater than 10 percent of the L2 norm of
    the flux will be refined.

    The remaining parameters are the same as for other Skeleton
    refinement methods.  Set BOLD(criterion) to BOLD(Unconditional),
    BOLD(degree) to BOLD(Bisection/liberal) and BOLD(alpha) to 0.3.

    Click BOLD(OK).
""",
    
#     """Go back to the BOLD(FEMesh) page.

#     Select BOLD(Adaptive Mesh Refinement).
#     As of now, we have only one error estimator, BOLD(Z-Z Estimator).
#     Select BOLD(L2 Error Norm) for error estimating BOLD(method).
#     Select BOLD(stress), which is the only entity,
#     for the BOLD(flux) parameter.
#     Set BOLD(threshold) to be BOLD(10).

#     For each element, an L2 error norm will be computed
#     with stresses computed from the finite element solution and their
#     recovered counterparts, which act as exact stresses.
#     If the relative error exceeds 10 percent, the element will be refined.

#     The next three parameters, BOLD(criterion), BOLD(degree) and, BOLD(alpha)
#     take care of actual refinement. Don't bother with these parameters
#     for this tutorial (See BOLD(skeleton) tutorial for details).

#     Sometimes, refinement could create badly-shaped elements. These elements
#     can be removed by turning on the BOLD(rationalize) option.

#     By default, field values are transferred to the refined mesh.
#     This, however, is just a
#     projection of the previous solution onto the refined mesh --
#     you need to re-solve the problem for improved solution.

#     Leave these options as they are for now and click BOLD(OK).
#     """,
    signal = "Skeleton modified"
    ),

    TutoringItem(
        subject="Rebuild the Mesh",
        comments=
        """Go back to the Graphics window and use the left hand
        checkboxes in the layer list to hide the Mesh and show the
        Skeleton.  Notice that the Mesh wasn't refined, although the
        Skeleton was.  Skeleton modifications are NOT automatically
        transferred to Meshes, because doing so can be computationally
        expensive.  

        Toggle the layers in the graphics window so that the Mesh is
        visible again.

        Go to the BOLD(FE Mesh) page and make sure that the
        BOLD(Method) widget in the BOLD(Mesh Operations) pane is set
        to BOLD(Rebuild).  Click BOLD(OK).  Now the Mesh has been
        updated to match the Skeleton.
        """,
        signal="Mesh modified"
        ),

    TutoringItem(
    subject="Refined Mesh",
    comments=
    
    """As expected, elements surrounding the corner have been refined.

    The Displacement values from the old Mesh have been transferred to
    the refined Mesh.  This, however, is just a projection of the
    previous solution onto the refined mesh.  You need to re-solve the
    problem to get an improved solution.

    Go to the BOLD(Solver) page.  BOLD(Solve) the problem again with
    the refined mesh.
    """,
    signal = "mesh solved"
    ),

    TutoringItem(
    subject="Refine Again",
    comments=
    
    """
    Go back to the BOLD(Skeleton) page and refine the Skeleton again
    (just click BOLD(OK)), and rebuild the Mesh by clicking
    BOLD(OK) in the BOLD(FE Mesh) page again.
    
    The corner has been refined more. For a better view, use
    BOLD(ctrl)+BOLD(.) or BOLD(Settings)->BOLD(Zoom)->BOLD(In) from
    the graphics window.

    This process (BOLD(Refine) + BOLD(Rebuild) + BOLD(Solve)) can be
    repeated until you're satisfied.  If a Mesh is out of sync with
    its Skeleton, it's not possible to solve it or use it as a basis
    for refining the Skeleton until it's been rebuilt.

    Thanks for trying out the tutorial.
    """,
    signal = "mesh changed"
    )
    
    ])
