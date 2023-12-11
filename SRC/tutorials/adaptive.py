# -*- python -*-

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
    tip="Improving a Mesh where necessary.",
    discussion="""<para>
    This example shows how to use <xref
    linkend="RegisteredClass-AdaptiveMeshRefine"/> to create a finer
    &mesh; where the finite element solution requires more accuracy.
    </para>""",
    lessons = [
    
    TutoringItem(
    subject="Introduction",
    comments=

"""OOF2 provides a rudimentary adaptive mesh refinement tool via <b>a Posteriori</b> error estimation scheme that utilizes the <b>Superconvergent Patch Recovery</b> of <b>Zienkiewicz</b> and <b>Zhu</b> -- more discussion of the subject can be found in the OOF2 manual.

In this tutorial, the adaptive mesh refinement will be briefly demonstrated.

    """),

    TutoringItem(
    subject="Loading a Skeleton",
    comments=
    
"""Open a graphics window, if none has been opened yet, with the <b>Graphics/New</b> command in the <b>Windows</b> menu.  Set <b>New Layer Policy</b> to <b>Single</b> in the <b>Settings</b> menu.

Locate the file <b>el_shape.mesh</b> within the share/oof2/examples directory in your OOF2 installation.

Use the menu item <b>File/Load/Data</b> in the main OOF2 window to load the file.
    """
    ),
    
    TutoringItem(
    subject="L-shaped Domain",
    comments=

"""If you have finished the tutorial for <b>Non-rectangular Domain</b>, you should be familiar with this Mesh.  The Mesh looks rectangular but a Material has been assigned only to the <b>green</b> part of the Mesh, which simulates an effective <b>L</b>-shaped domain.
    
Move on to the next slide. """
    ),

    TutoringItem(
    subject="Boundary Conditions",
    comments=
"""The Mesh is ready to be solved.

The applied boundary conditions (all <b>Dirichlet</b>) are:

<b>1.</b> u_x = 0 on the <b>left</b> side
    
<b>2.</b> u_y = 0 on the <b>left</b> side

<b>3.</b> u_x = 0 on the <b>top</b> side

<b>4.</b> u_y = 0 on the <b>top</b> side

<b>5.</b> u_y = -2 on the <b>right</b> side"""
    ),

    TutoringItem(
    subject="Solution",
    comments=
    
"""Open the <b>Solver</b> page and just click <b>Solve</b>. A deformed Mesh will be displayed in the graphics window. Note that dummy elements (<b>ivory</b> part) are <b>NOT</b> displayed in the deformed Mesh.

For a clearer view, hide the Skeleton layer.  Navigate to the bottom of the graphics window and find a layer labeled <b>Skeleton(skeleton)</b> and uncheck the leftmost square box to hide the layer.

Due to the shape of the domain, it is obvious that stresses are highly concentrated in the region surrounding the corner. It is also safe to assume that errors in this region would be higher than in other regions.

Move on to the next slide to start the process for adaptive mesh refinement."""
    ),

    TutoringItem(
    subject="Adaptive Mesh Refinement",
    comments=

"""Go to the <b>Skeleton</b> page.  (In earlier versions of OOF2, adaptive mesh refinement was a Mesh modification method.  As of version 2.1, it's part of <b>Skeleton</b> refinement.)

Choose the <b>Refine</b> Skeleton Modification method, and set <b>targets</b> to <b>Adaptive Mesh Refinement</b>. 

The <b>subproblem</b> parameter determines which subproblem's elements and fields will be used to determine which elements will be refined.  Leave it set to <b>el_shape.png/skeleton/mesh/default</b>.

The <b>estimator</b> parameter determines which error estimator to use. Elements with high error estimates will be refined. Currently, OOF2 only provides one estimator, the <b>Z-Z Estimator</b>.  Set its parameters to <b>norm</b>=<b>L2 Error Norm</b>, <b>flux</b>=<b>Stress</b>, and <b>threshold</b>=<b>10</b>.  This means that the L2 norm of the difference between the computed flux and the "recovered" flux will be computed, and that any elements in which this difference is greater than 10 percent of the L2 norm of the flux will be refined.

The remaining parameters are the same as for other Skeleton refinement methods.  Set <b>criterion</b> to <b>Unconditional</b>, <b>degree</b> to <b>Bisection/liberal</b> and <b>alpha</b> to 0.3.

Click <b>OK</b>. """,
    
#     """Go back to the <b>FEMesh</b> page.

#     Select <b>Adaptive Mesh Refinement</b>.
#     As of now, we have only one error estimator, <b>Z-Z Estimator</b>.
#     Select <b>L2 Error Norm</b> for error estimating <b>method</b>.
#     Select <b>stress</b>, which is the only entity,
#     for the <b>flux</b> parameter.
#     Set <b>threshold</b> to be <b>10</b>.

#     For each element, an L2 error norm will be computed
#     with stresses computed from the finite element solution and their
#     recovered counterparts, which act as exact stresses.
#     If the relative error exceeds 10 percent, the element will be refined.

#     The next three parameters, <b>criterion</b>, <b>degree</b> and, <b>alpha</b>
#     take care of actual refinement. Don't bother with these parameters
#     for this tutorial (See <b>skeleton</b> tutorial for details).

#     Sometimes, refinement could create badly-shaped elements. These elements
#     can be removed by turning on the <b>rationalize</b> option.

#     By default, field values are transferred to the refined mesh.
#     This, however, is just a
#     projection of the previous solution onto the refined mesh --
#     you need to re-solve the problem for improved solution.

#     Leave these options as they are for now and click <b>OK</b>.
#     """,
    ),

    TutoringItem(
        subject="Rebuild the Mesh",
        comments=
"""Go back to the Graphics window and use the left hand checkboxes in the layer list to hide the Mesh and show the Skeleton.  Notice that the Mesh wasn't refined, although the Skeleton was.  Skeleton modifications are NOT automatically transferred to Meshes, because doing so can be computationally expensive.  

Toggle the layers in the graphics window so that the Mesh is visible again.

Go to the <b>FE Mesh</b> page and make sure that the <b>Method</b> widget in the <b>Mesh Operations</b> pane is set to <b>Rebuild</b>.  Click <b>OK</b>.  Now the Mesh has been updated to match the Skeleton.
        """,
        ),

    TutoringItem(
    subject="Refined Mesh",
    comments=
    
"""As expected, elements surrounding the corner have been refined.

The Displacement values from the old Mesh have been transferred to the refined Mesh.  This, however, is just a projection of the previous solution onto the refined mesh.  You need to re-solve the problem to get an improved solution.

Go to the <b>Solver</b> page.  <b>Solve</b> the problem again with the refined mesh.  If you get an convergence error, edit the <b>Solver</b> and switch the <b>symmetric_solver</b> to <b>BiCG</b>, which seems to work better here, or increase the tolerance of <b>CG</b> to 1.e-08.  After you change the Solver, click <b>Solve</b> again.  """,
    ),

    TutoringItem(
    subject="Refine Again",
    comments=
    
"""Go back to the <b>Skeleton</b> page and refine the Skeleton again (just click <b>OK</b>), and rebuild the Mesh by clicking <b>OK</b> in the <b>FE Mesh</b> page again.
    
The corner has been refined more. For a better view, use <b>ctrl-.</b> or <b>Settings/Zoom/In</b> from the graphics window.

This process (<b>Refine</b> + <b>Rebuild</b> + <b>Solve</b>) can be repeated until you're satisfied.  If a Mesh is out of sync with its Skeleton, it's not possible to solve it or use it as a basis for refining the Skeleton until it's been rebuilt.

Thanks for trying out the tutorial. """,
    )
    
    ])
