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

## TODO: The typography in this tutorial should be made consistent
## with the others.  This one uses the bold tag a lot less.

tutorial.TutorialClass(
    subject = "Solving Time Dependent Systems",
    ordering=7,
    lessons=[
        TutoringItem(
            subject="Introduction",
            comments=
"""OOF2 can compute the time evolution of a system if:

(1) The material properties define the coefficients of at least one time derivative in at least one active equation, and

(2) A non-static time stepping method is selected in the <b>Solver</b> page.

In addition, it helps if at least one output quantity is selected on the the <b>Scheduled Output</b> page.

This tutorial demonstrates how to solve a damped elasticity problem. It assumes that you already know how to create a Microstructure, define Material Properties, and all the other operations involved in setting up an OOF2 problem. """
        ),

        TutoringItem(
            subject="Create a Microstructure",
            comments=
"""We'll first create a simple uniform microstructure.  Go to the <b>Microstructure</b> page and click <b>New</b> to create a Microstructure.  Use the default values for the parameters and click <b>OK</b>. """,
        ),

        TutoringItem(
            subject="Define a Material",
            comments=
"""Go to the <b>Materials</b> page and create a <b>New</b> bulk material.

Add the following Properties to the Material:

<b>Mechanical:Elasticity:Isotropic</b> with bulk modulus 0.5 and shear modulus 0.25.

<b>Mechanical:ForceDensity:ConstantForceDensity</b> with gx=0 and gy=-0.3.  This simulates gravity.  Since we haven't specified what units we're using in this toy problem, we can choose whatever value we like for g.

<b>Mechanical:MassDensity:ConstantMassDensity</b> with rho=1.0.  This gives the material inertia and will allow us to solve F=ma.

<b>Mechanical:Viscosity:Isotropic</b> with bulk=0.07 and shear=0.25. Viscosity has the same form as an elastic modulus, so we parametrize it the same way.

Assign the new Material to all of the pixels in the Microstructure.
""",
        ),

        TutoringItem(
            subject="Create a Skeleton and a Mesh",
            comments=
"""Go to the <b>Skeleton</b> page and create an 8x8 quadrilateral nonperiodic Skeleton.

Go to the <b>FE Mesh</b> page and create a Mesh, using the default parameters. """,
        ),

        TutoringItem(
            subject="Define Fields and Equations",
            comments=
"""Go to the <b>Fields &amp; Equations</b> page.

Check all three boxes next to <b>Displacement</b>, making the displacement field defined, active, and in-plane.  Make the <b>Force Balance</b> equation active. """
        ),

        TutoringItem(
            subject="Set Boundary Conditions",
            comments=
"""Go to the <b>Boundary Conditions</b> page and create two boundary conditions, one Dirichlet condition setting the x component of Displacement to 0 on the bottom boundary, and one setting the y component to 0. """,
        ),

        TutoringItem(
            subject="Schedule Outputs",
            comments=
"""Go to the <b>Scheduled Output</b> page.  This page controls what output quantities will be computed while OOF2 is solving a time-dependent system.  All of the quantities that can be computed by the <b>Analysis</b> and <b>Boundary Analysis</b> pages are available to be computed during a time evolution.

Each Scheduled Output consists of three parts:

<b>1.</b> The <b>Output</b>, which is the quantity to be computed. "Quantity" is interpreted loosely here.  It includes quantities from the Analysis and Boundary Analysis pages, as well as graphics window updates and mesh data files.

<b>2.</b> The <b>Schedule</b>, which determines when the output operation takes place.

<b>3.</b> The <b>Destination</b>, which determines where the output is written. """
        ),

        TutoringItem(
            subject="Schedule Graphics Output",
            comments=
"""We'll first add a Scheduled Output that determines how often the <b>Graphics Window</b> will be updated.

Click the <b>New</b> button at the top of the page.  A dialog window will open allowing you to choose one of a number of kinds of Outputs.  Set the <b>output</b> parameter to <b>Update Graphics</b> and leave the <b>name</b> parameter set to <i>&lt;automatic&gt;</i>.  Click <b>OK</b>.

The new Output is listed in the window.  If we had given a value to the <b>name</b> parameter in the dialog box, then that name would appear in the Output column.  Instead, it contains the generic name, "GraphicsUpdate". """
        ),

        TutoringItem(
            subject="Schedule Graphics Output, continued",
            comments=
"""The <b>Schedule</b> column contains "---" because no schedule has been assigned to the GraphicsUpdate operation.  Make sure that the "---" is selected and click on the <b>Edit</b> button under the label <b>Schedule</b> at the bottom of the page, or double click on "---" in the <b>Schedule</b> column.

The dialog box asks you to pick a <b>scheduletype</b> and a <b>schedule</b>.  The types are <b>Absolute</b> (operations will be performed at given times), <b>Relative</b> (operations will be performed at given times, but those times are relative to the starting point of the time evolution), and <b>Conditional</b> (times aren't determined in advance -- operations take place when some other criteria are satisfied).  Leave "scheduletype" set to "Absolute".

Set "schedule" to "Periodic" with delay=0.0 and interval=0.1.  This means that the graphics windows will be updated whenever the time is 0.0 + 0.1*k, for integers k.  Click <b>OK</b>.

The <b>Destination</b> column contains <b>&lt;Graphics Window&gt;</b> because that's the only destination that makes sense when updating graphics. """
        ),

        TutoringItem(
            subject="Schedule Data Output",
            comments=
"""Now we'll define an output operation that stores the average position of the top boundary of the mesh in a file. 

Click the <b>New</b> button to define a new output operation.  This time, in the dialog box set "output" to "Boundary Analysis".  For "operation", choose "Average Field" with "field" set to "Displacement".  For "boundary", choose "top".  Click <b>OK</b>.

The new Output is now selected in the list.  Both its Schedule and Destination show up as "---" because they haven't been set.  Unlike GraphicsUpdate, there is no default destination for boundary analysis outputs.  We could set the schedule the same way we did for GraphicsUpdate, but it's easier to copy the GraphicsUpdate schedule. Click on "GraphicsUpdate" to select it, then click on the <b>Copy</b> button under the label <b>Schedule</b> at the bottom of the page.  In the dialog box, change "target" to "Average Displacement on top" and click <b>OK</b>.  The two Outputs now have the same Schedule.

To determine where the output data goes, select the "Average Displacement" Output again, and click the <b>Edit</b> button in the <b>Destination</b> column.  There are two choices: "Message Window" writes to the OOF2 Message Window, and "Output Stream" writes to a file.  Choose "Output Stream" and enter a file name.  Click <b>OK</b>. """
        ),

        TutoringItem(
            subject="Schedule Data Output, continued",
            comments=
"""Sometimes you'll want to save and re-use an Output definition, especially ones that have a lot of parameters, such as those listed in the "Bulk Analysis" submenu of the New Output dialog box.  These outputs are the same as those performed on the <b>Analysis</b> page. OOF2 lets you give a name to these analysis operations and refer to them by name in either the <b>Analysis</b> page or the New Output dialog on the <b>Scheduled Output</b> page.

Go to the <b>Analysis Page</b> and set the <b>Output</b>, <b>Operation</b>, <b>Domain</b> and <b>Sampling</b> widgets for the quantity you want to examine.  For example, to compute y displacement averaged over the whole mesh, set <b>Output</b> to "Scalar/Field/Component/Displacement/y", set <b>Operation</b> to "Average", set <b>Domain</b> to "Entire Mesh", and <b>Sampling</b> to "Element Set".

Note that the available options in a given pane on this page can depend on what has been selected in another pane.  You have to select the"Average" operation before the "Element Set" sampling is available.

To give these settings a name, click the <b>New</b> button in the <b>Named Analysis</b> box.  Either click <b>OK</b> to accept the default name (which is "analysis"), or click the checkbox next to the name and type a new name.  Click <b>OK</b> to accept the new name. """,
        ),

        TutoringItem(
            subject="Schedule Data Output, part 3",
            comments=
"""Go back to the <b>Scheduled Output</b> page.  Click on the <b>New</b> button to create a new Output.  This time, leave "name" set to <i>&lt;automatic&gt;</i> and set <b>output</b> to "Named Analysis".  The name you used appears in a pull down menu for the "analysis" parameter.  Click <b>OK</b>.  The new Output now appears in the lists.  Its name is the name that you assigned to the Named Analyis.

Again, copy the Schedule from the other outputs by selecting one of them and clicking on the <b>Copy</b> button in the <b>Schedule</b> column.

Finally, click the <b>Edit</b> button in the <b>Destination</b> column. (Remember to reselect the new Output first.)  Select "Output Stream" and enter the same file name that you chose earlier for the Boundary Analysis data.  Both sets of data will go to the same file. """,
        ),
        
        TutoringItem(
            subject="The Solver Page",
            comments=
"""Go to the <b>Solver</b> page.

The page consists of three regions.  In the <b>Subproblems</b> pane you can assign a Solver to a Subproblem and choose which Subproblems to solve and in which order.

The <b>Field Initialization</b> pane allows you to choose how Fields will be initialized and to apply the initializers.  It also allows an initial <b>time</b> to be assigned to the Mesh.

At the bottom of the page are boxes for the time, the <b>Solve</b> button itself, and a <b>Status</b> box.  The <b>current time</b> box shows the Mesh's current time, which is determined by the time evolution.  It can be reset when Fields are initialized.

<b>end time</b> is the target time for a time-dependent solution.  You should set it before clicking <b>Solve</b>. 

The <b>Status</b> box briefly describes the state of the solution of the current Mesh.  Clicking the <b>Details</b> button will sometimes display a bit more information in the Message window."""
        ),

        TutoringItem(
            subject="Choose a Solver",
            comments=
"""The <b>Subproblems</b> list contains one line, for the "default" Subproblem that is defined on all Meshes.  If you define other Subproblems on the <b>FE Mesh</b> page, they will also appear in the list. 

The checkboxes in the <b>Solve?</b> column indicate whether or not OOF2 should solve each Subproblem.  Make sure that the checkbox is checked.

The <b>Solver</b> column shows the solution method that will be used on each Subproblem.  If it says <b>&lt;none&gt;</b> that Subproblem won't be solved, even if its <b>Solve?</b> checkbox is checked.  Click on the "default" Subproblem line to select it, and click the <b>Set Solver</b> button (or double-click the line).  A dialog box opens that lets you choose a solution method.

The solver can be specified either in <b>Basic</b> mode or <b>Advanced</b> mode.  In Basic mode, OOF2 makes many decisions for you.  Set the "solver_mode" parameter to <b>Advanced</b>.

The "time_stepper" parameter determines which time-stepping algorithm to use.  If it's set to "Static" no time stepping will be done, (although if the end time is greater than the start time, the system will be solved quasistaticly).  "Uniform" takes time steps with a fixed size, and "Adaptive" adjusts the time steps to achieve a given accuracy.  Set "time stepper" to "Adaptive", with tolerance=0.0001, initialstep=0.1, minstep=1.e-5, errorscaling=Absolute, and stepper=TwoStep.  Set the TwoStep parameters to singlestep=SS22 with both theta1 and theta2 equal to 0.5.

Leave the "nonlinear_solver" parameter set to "None".  You'd only use a different value if you were solving a microstructure that had nonlinear material properties.

The "symmetric_solver" parameter governs how OOF2 solves the symmetric matrix equations that arise from discretizing the equations of motion. Set it to "CG" (conjugate gradient) with preconditioner=ILU, tolerance=1e-13, and max_iterations=1000.

The "asymmetric_solver" parameter governs how OOF2 solves asymmetric matrix equations, if they arise.  This example won't create any asymmetric matrices, so the setting of this parameter is unimportant.

Click <b>OK</b>. """,
        ),

        TutoringItem(
            subject="Set Field Initializers",
            comments=
"""The <b>Field Initialization</b> pane in the <b>Solver</b> page lists all of the fields defined on the Mesh.  Displacement appears because it was defined on the <b>Fields &amp; Equations</b> page.  Its time derivative, Displacement_t, appears because the Force_Balance equation is second order in time (the material has a MassDensity property) and we've chosen a non-static time stepping method.  If we had set time_stepping=Static in the previous tutorial page, then Displacement_t would not need to be initialized.

Select the "Displacement" link in the <b>Field Initialization</b> list and click on the <b>Set</b> button, or double click on the line.  A dialog box appears for setting the initialization method for the components of the field.  The components can be initialized to constant values, to functions of x and y, or by copying from another Mesh.  For this example, choose "XYTFunction" and set "fx" to 0.0 and "fy" to 0.1*x*y.  Click <b>OK</b>.

Initialize the time derivative field, Displacement_t, to "Constant" with "cx" and "cy" set to 0.0. """,
        ),

        TutoringItem(
            subject="Initialize Fields",
            comments=
"""Assigning initializers to the fields doesn't actually initialize the fields.  That has to be done in a separate step.  First, open a graphics window and add a layer that displays the Mesh edges at their actual positions (not their original positions!).

Click the <b>Apply</b> button in the <b>Field Initialization</b> pane and observe the changes in the graphics window.

Notice that the Mesh nodes have moved because the displacement field has been initialized. 

Optional: Add a display layer that shows either the Skeleton edges or the Mesh edges at their original positions.  To make the display easier to read, give the edges in the new layer a different color. Light gray works well.  """
        ),

        TutoringItem(
            subject="Solve",
            comments=
"""Type "6" into the <b>end time</b> box at the bottom of the <b>Solver</b> page.  You can leave <b>initial step size</b> set to "None" because the adaptive stepping algorithm will automatically choose a step size.  If you think you know a good guess for the step size, you can type it in.

Click the <b>Solve</b> button to compute the time evolution.

The progress of the solution can be monitored by observing the <b>current time</b> field in the <b>Solver</b> page, the progress bar in the <b>Activity Viewer</b> window, and the updates in the graphics window.  The progress bar and the current time are updated more frequently than the graphics window as long as the adaptive stepper is taking steps that are smaller than the graphics update interval that was specified on the <b>Scheduled Output</b> page.

When the solution is finished, the <b>Status</b> pane in the <b>Solver</b> page will say "Solved".  Note that the <b>end time</b> is now 12 and the <b>Solve</b> button has changed to a <b>Continue</b> button.  If you want to extend the time evolution, you only have to click <b>Continue</b>. """
        ),

        TutoringItem(
            subject="Animate the Solution",
            comments=
"""Watching the graphics window as the solution was calculated was possibly not very exciting because the computation was slow.  Or perhaps you just weren't paying attention and missed it.  In either case, you'd like to be able to replay it without repeating all of the calculations.

Go to the graphics window, and choose <b>Animate</b> from the <b>File</b> menu.  Click <b>OK</b> in the dialog box, and pay better attention to the graphics window this time. """
        ),

        TutoringItem(
            subject="Output Files",
            comments=
"""Examine the output file that you created.  It'll be in the directory that you were using when you started OOF2, unless you specified another directory when you chose the file name.  Notice that each line of data in the file is preceded by a bunch of comment lines, beginning with a '#' character.  The comments describe the contents of the data lines.  If you had directed only one output to the file, the comments would only appear at the top, and the file would be more readable. """
        ),

        TutoringItem(
            subject="Start Over",
            comments=
"""The motion of the microstructure wasn't very dramatic. Let's change the material parameters and try again.

Go to the <b>Materials</b> page.  Select the material's Viscosity property by clicking on it in the <b>Material</b> pane.  Click <b>Parametrize</b> in the <b>Property</b> pane and change "shear" to 0.01.  Click <b>OK</b>.

Go back to the <b>Solver</b> page.  Note that the <b>Status</b> pane says "Unsolved", because the computed solution is now invalid.  Also note the the current time is still 6, and that the end time is still 12.  To recompute the time evolution, we need to reinitialize the fields and the times as well.  To do that, click <b>Apply at time</b> in the <b>Field Initialization</b> page.  In the dialog box, set "time" to 0.0 and click <b>OK</b>.  Change <b>end time</b> back to 6.

Click <b>Solve</b> again to recompute the time evolution with the new parameters. """
        ),

        ## TODO GTK3: Break this up into smaller pages, now that the
        ## tutorial window isn't scrollable.
        TutoringItem(
            subject="Undiscussed Topics",
            comments=
"""You've finished the tutorial on time dependent systems.  The tutorial didn't go into great detail, so please play around with the options to see what their effects are.  (As a last resort, read the manual! It may or may not be up to date.)  Here are some comments on a few topics that weren't covered in the tutorial:

<b>Time Steps</b>: Whether the time stepper is Uniform or Adaptive, the step size is always adjusted so that it hits the output times exactly. For example, if the start time is 0, the output time interval is 1 and the uniform step size is 0.75, then the size of the first step will be 0.75, but the size of the second step will be only 0.25, to attain the output time of 1.0.  The third step will be 0.75 again.

<b>Choosing a Matrix Method</b>: The finite element solution process always includes the solution of a matrix equation.  OOF2 offers a number of solution methods.  If the matrix is symmetric, the Conjugate Gradient method (CG) is almost always the best method.  If the matrix is not symmetric, use BiCG or GMRES instead.  These methods are all preconditioned sparse iterative methods, meaning that they approach a solution gradually and approximately and don't require extra memory to store the parts of the matrix that are zero.  The preconditioner is a way of guessing the answer beforehand so as to start the iteration close to the solution.  The ILU preconditioner seems to work well in most cases, but you might want to try the others if the solution is taking a long time.

The Direct matrix method is not iterative or sparse.  It may give better answers, but may also run out of memory if you're solving a large problem.  It may or may not be faster than the sparse iterative methods.

<b>Uniform and Adaptive Time Stepping</b>: Uniform steppers take steps of a constant predetermined size.  Adaptive steppers adjust the step size to keep an error estimate below a specified tolerance.  They do more work per step than the uniform steppers, but (a) may take fewer step and (b) provide some confidence that the answer is correct.  When this tutorial was written, there was only one Adaptive time stepper in OOF2, TwoStep. This method uses a Uniform Stepper to take one step, then repeats that step with two smaller steps, and compares the results.  The choices for the "singlestep" parameter for the TwoStep stepper are the same as the choices for the "stepper" parameter for the Uniform stepping method.

<b>Error Scaling</b>: The adaptive methods require you to set an "errorscaling" parameter which determines how errors are compared to the tolerance.  Relative errors are scaled by the value of the solution, so if a component of the solution passes through zero, the relative error will be very large, and the adaptive method will attempt to take very small time steps (and probably fail).  Absolute errors aren't scaled, and so will be a better choice for solutions containing zeros, but may be too restrictive for large values. Cross-over (XOver) errors are a sort of compromise.  If an adaptive stepper is failing because the step size is too small, try changing the error scaling.

<b>Choosing a Stepper</b>: Forward Euler is the simplest time stepper and has very little computational overhead, but tends to be unstable and require very small time steps.  Its error is proportional to the square of the time step.  Usually it's better to pick a more sophisticated method that can take larger time steps.  Backward Euler has little overhead and is more stable than Forward Euler, but its error scales the same way. Crank-Nicolson has an error that scales with the cube of the time step, so it's more accurate and doesn't have much more overhead than Backward Euler.  Liniger and Galerkin are variants of Crank-Nicolson.  All of the aforementioned methods are designed for equations with only first order time derivatives.  If solving an equation with second order time derivatives, OOF2 can use these methods if it augments the system of equations with additional equations for the first derivatives.  This increases the number of equations and also makes the resulting matrices asymmetric, so CG can't be used.

<b>SS22</b> works directly on equations with second order time derivatives without requiring auxiliary equations, so it can be used with the CG matrix solver.

<b>Solving Multiple Subproblems</b>: If more than one subproblem is being solved with an adaptive stepper, each will use its own time step.  If the fields in the two subproblems are changing on different time scales, putting them in separate subproblems allows the steppers to work more efficiently.  If the fields in one subproblem instantaneously reach equilibrium, solve that problem with the Static time stepping, which will compute the quasistatic solution at each instant in time.

<b>Animation Options</b>: The start time and finish time can be chosen from any of the times at which output was computed by clicking on the arrows on either side of the entry boxes in the the Animate dialog. Times between those times can be entered directly in the boxes, and interpolated solutions will be computed.  If "style" is set to "Loop" or "Back and Forth" the animation will continue forever or until you click the "Stop" button in the Activity Viewer window, whichever comes first.

<b>Mesh Data Cache</b>: The data for all the fields at all the nodes at all the time steps can take up a lot of memory.  If your computer doesn't have enough memory, you can tell OOF2 to cache this data in temporary files on disk instead.  In the main OOF2 window, choose Mesh Defaults/Data Cache Type in the Settings menu to set the cache to Disk for all new meshes.  To change the cache type for an existing mesh, use the Set Data Cache method in the Mesh Operations pane on the FE Mesh page. """
        )
        ]
)
