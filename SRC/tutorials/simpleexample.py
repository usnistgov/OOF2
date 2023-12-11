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
    subject="A Simple Example",
    ordering=0.1,
    tip="A complete but minimal example.",
    discussion="""<para>
    This tutorial works through a simple example problem from
    beginning to end, illustrating some of the most important features
    of &oof2;.
    </para>""",
    lessons = [
        TutoringItem(
            subject="Introduction",
            comments=
"""This tutorial is designed to familiarize users with OOF2 by guiding them through a simple but complete project.

We assume that you run this tutorial from a fresh start of OOF2. Whether you run it this way or not doesn't make any significant difference but it simplifies things in a few places.

<b>Objective</b>: A simple finite element analysis of a fictitious microstructure under uniaxial tension.  The microstructure is composed of two fictitious materials named <b>yellow</b> and <b>cyan</b> with linear elastic properties given by:

<b>yellow</b> : E=1.0, nu=0.3

<b>cyan</b> : E=0.5. nu=0.3 """
        ),

    TutoringItem(
        subject="Graphics Window",
        comments=
"""Open a graphics window, if none has been opened yet, with the <b>Graphics/New</b> command in the <b>Windows</b> menu in any OOF2 window.  Graphical representations of entities such as Microstructure, Skeleton, and Mesh, are displayed in the graphics window.

(New!) The graphics window doesn't automatically display objects unless you add a new graphics layer.  It can be told to automatically add layers, though.  In the Settings menu, select <b>New Layer Policy</b>, and in the dialog box set <b>policy</b> to <b>Single</b>.  Click <b>OK</b>.  This makes the window automatically display new Images, Meshes, and Skeletons if only one such object exists."""
    ),

    TutoringItem(
        subject="Get the Image",
        comments=
"""Locate the file <b>cyallow.png</b> within the share/oof2/examples directory in your OOF2 installation. """
    ),

    TutoringItem(
        subject="Loading a Microstructure and an Image",
        comments=
"""Open the <b>Microstructure</b> page from the <b>Task</b> menu in the main OOF2 window.

Create a new Microstructure from an existing image file by clicking the <b>New from Image File</b> button.

In the file selector, navigate to <b>cyallow.png</b>.  For now, leave the <b>microstructure_name</b>, <b>width</b> and <b>height</b> values set to <i>&lt;automatic&gt;</i>.  Click <b>OK</b>.

You should see an image -- cyan on top of yellow -- displayed on the graphics window.  Also, the <b>Microstructure</b> pull down menu at the top of the Microstructure page now contains a single entry, "cyallow.png", which is the automatically generated name for the Microstructure that was created by the <b>New from Image File</b> command. """,
    ),

    TutoringItem(
        subject="Categorizing Pixels",
        comments=
"""At this point, a microstructure has been created but it contains no useful information other than its size.

We need to let the microstructure know that it has two different materials and they are represented by the two different colors in the Image.

Generally, this is a fairly complicated process, but the sample microstructure in this tutorial can be automatically categorized with a single click of a button, since the base image features only two distinct colors.

Open the <b>Image</b> page in the main OOF2 window.

Click the <b>Group</b> button, and click <b>OK</b> in the dialog box.

Go back to the <b>Microstructure</b> page, and notice that two pixel groups have been created.""",
    ),

    TutoringItem(
        subject="Renaming Pixel Groups",
        comments=
"""The automatically generated names of the pixel groups are the hexadecimal values of the colors and are not terribly convenient. The groups can be renamed.

Select the first pixel group, <b>#00ffff (2160 pixels meshable)</b>.

Once it's been highlighted, click <b>Rename</b>, in the buttons to
the left of the group list. (The buttons above the group list act
on the Microstructure, not the groups).

Delete the old name and type in <b>cyan</b>, which is the actual
color of the group. 

Click <b>OK</b> to finalize the change. """,
    ),

    TutoringItem(
        subject="Renaming Pixel Groups -- continued",
        comments=
"""Select the second pixel group and <b>Rename</b> it to <b>yellow</b>.

Now you're ready to create materials for each pixel group. """,
    ),        

    TutoringItem(
        subject="Adding Materials",
        comments=
"""Open the <b>Materials</b> page in the main OOF2 window.

The page contains two panes.  The left hand <b>Property</b> pane allows you to define material properties.  The right hand <b>Material</b> pane allows you to combine properties into a Material.

Create a new material by clicking on the <b>New</b> button in the <b>Material</b> pane.

The <b>name</b> field contains the text <i>&lt;automatic&gt;</i> in italics. If you don't change it, OOF2 will generate an automatic name for the material.  If you type anything in the field, it will replace <i>&lt;automatic&gt;</i>, and what you've typed will be used for the name of the material.  If you delete everything that you've typed, <i>&lt;automatic&gt;</i> will reappear.  Whenever OOF2 is able to automatically generate an input value, it uses a widget like this, where typing anything turns off the automatic behavior and deleting everything turns it back on. 

Type <b>yellow-material</b> in the text entry field.  (You can use any name you like for the material, including names that you've used for other objects.  To avoid confusion in this tutorial, though, don't use the name "yellow" since it's already been used for the pixel group.)

Leave "material_type" set to "bulk".
    
Click <b>OK</b>. """,
    ),

    TutoringItem(
        subject="Adding Materials -- continued",
        comments=
"""Create a second <b>New</b> material with the name <b>cyan-material</b>.""",
    ),

    TutoringItem(
        subject="Creating a Property",
        comments=
"""We now need to make materials meaningful by adding properties to them.

The <b>Property</b> pane on the left side of the Materials page hierarchically lists all of the Property types that are installed in OOF2.  Clicking on a triangle pointing RIGHT will expand a level, and clicking on a triangle pointing DOWN will collapse a level of the hierarchy.

Start creating a property for <b>yellow-material</b> by selecting <b>Isotropic</b> from <b>Elasticity</b> in the <b>Mechanical</b> property hierarchy.

Click <b>Copy</b> and give the Property a user-defined name. (This is another automatic widget.  Use the Copy button in the Property pane, not the one in the Material pane!)

Type in <b>yellow_elasticity</b> and click <b>OK</b>.  Note that Property names must begin with a letter and can only contain letters, numerals, and underscores (they must be legal Python variable names). """,
    ),
        
    TutoringItem(
        subject="Parametrizing a Property",
        comments=
"""Select <b>yellow_elasticity</b> from the Property hierarchy and either double click it or click the <b>Parametrize...</b> button to input actual values.

The elasticity parameters can be entered in a variety of formats. The default format is <b>Cij</b>.  Change it to <b>E and nu</b> with the pull down menu at the top of the Parametrize dialog box.

Set the Young's modulus (<b>young</b>) to 1.0 and Poisson's ratio (<b>poisson</b>) to 0.3.

Click <b>OK</b> to finish up. """,
    ),

    TutoringItem(
        subject="Adding a Property to a Material",
        comments=
"""Below the <b>New</b> button in the <b>Material</b> pane is a pull-down menu that lists all of the Materials that have been defined.  Select the <b>yellow-material</b> that you defined earlier.

Make sure that the <b>yellow_elasticity</b> Property is still selected.

Click <b>Add Property to Material</b> in the <b>Property</b> pane to add the Property to the Material.

The addition should immediately appear in the <b>Material</b> pane, in the list of Properties below the Material selector. """,
    ),

    TutoringItem(
        subject="Creating Another Property",
        comments=
"""Make another <b>Copy</b> of <b>Isotropic</b> and name it <b>cyan_elasticity</b>.""",
    ),

    TutoringItem(
        subject="Parametrizing Another Property",
        comments=
"""<b>Parametrize</b> the property <b>cyan_elasticity</b> with these values: <b>young</b>=0.5, <b>poisson</b>=0.3.""",
    ),

    TutoringItem(
        subject="Adding Another Property to a Material",
        comments=
"""Select <b>cyan-material</b> in the Material selector in the <b>Material</b> pane, and add the Property <b>cyan_elasticity</b> by clicking on the <b>Add Property to Material</b> button.

Make sure that the Materials contain the correct Properties before you move on.  Select a Property in the <b>Material</b> pane and use the <b>Remove Property from Material</b> button if you've made a mistake.  """,
    ),

    TutoringItem(
        subject="Adding Colors to Materials",
        comments=
"""Although it's not necessary mathematically, it's convenient to assign colors to Materials so that the Microstructure can be displayed.

<b>Copy</b> the <b>Color</b> property in the <b>Property</b> pane, giving the copy the name <b>yellow</b>.

<b>Parametrize</b> the <b>yellow</b> Property.  The color of the Material doesn't have to be the same as the color in the Image, but might be confusing if it's different.  In the Parametrize dialog box, switch from <b>TranslucentGray</b> to <b>RGBAColor</b>, and set the <b>red</b>, <b>green</b>, <b>blue</b>, and <b>alpha</b> sliders to something yellowish, say <b>red</b>=1, <b>green=0.8</b>, and <b>blue</b>=0.  <b>Alpha</b> is the opacity.  Leave it at 1.0. (You can change the values either by sliding the sliders or typing in the text boxes on the right.)  Click <b>OK</b>.

Add the <b>yellow</b> Property to the <b>yellow-material</b>.

Similarly create a <b>Color</b> property for <b>cyan</b> and add it to the <b>cyan-material</b>.  Parametrize it with <b>Red</b>=0, <b>Green</b>=0.8, and <b>Blue</b>=1. """,
    ),

    TutoringItem(
        subject="Assigning a Material to Pixels",
        
    comments=
"""Now that we have defined Materials and created pixel groups in the Microstructure, we can assign Materials to the microstructure.

Select the material <b>yellow-material</b> and click on the button labelled <b>Assign to Pixels...</b> in the <b>Material</b> pane.

The pop-up window lets you choose the Microstructure to which the Material will be assigned (currently we only have one, "cyallow.png"), and the pixels within the Microstructure.  Choose the pixel group <b>yellow</b> in the <b>pixels</b> pull-down menu.

Click <b>OK</b> to finish. """,
    ),

    TutoringItem(
        subject="Displaying a Microstructure",
        comments=
"""The graphics window can display some things automatically, but if you want to view a Microstructure you must do it explicitly by adding a new <b>Display Layer</b>.

Dig up the Graphics window that you opened earlier by choosing <b>Graphics/Graphics 1</b> in the <b>Windows</b> menu on any OOF2 window.

Select <b>New</b> from the <b>Layer</b> menu in the Graphics window. Earlier versions of OOF2 used a really awkward graphics layer editor window here.  Fortunately, it's been eliminated.

The dialog box for creating a new graphics layer asks you to specify three things: <b>category</b>, <b>what</b>, and <b>how</b>.

<b>category</b> is what kind of thing is to be displayed by the layer: <b>Microstructure</b>, <b>Image</b>, <b>Skeleton</b>, etc. Click on the pulldown menu and select <b>Microstructure</b>.

<b>what</b> is the name of the particular object that is to be displayed.  Select <b>cyallow.png</b>, the name of the Microstructure, in the pulldown menu.  (The other two items in the menu refer to the Microstructures displayed in other layers, but there are no relevant layers at the moment, so ignore them.)

<b>how</b> is the way in which the object will be displayed. Different kinds of objects have different kinds of display methods.  Leave the pull-down menu at the top of the <b>how</b> field set to <b>Material</b>, which draws the Microstructure by coloring each pixel with the color of the Material assigned to the pixel.  This display method has two parameters: <b>no_material</b>, the color to use for pixels that have no associated Material; and <b>no_color</b>, the color to use for pixels that have a Material which has no ColorProperty.  Ignore both parameters for now and click the <b>OK</b> button. """
    ),

    TutoringItem(
        subject="Layer List",
        comments=
"""The Microstructure Material Display appears in the Graphics window. Pixels to which you assigned the yellow-material are drawn in yellow.  The remaining pixels are black because they have no Material, and the default value for <b>no_material</b> is black.

The Layer List at the bottom of the Graphics Window now shows two layers: a Microstructure layer on top of an Image layer.  You may have to scroll the list to see both layers.  Because the Microstructure and the Image are the same size, you can only see one of them at a time.  The buttons in the column labelled <b>Show</b> in the Layer List allow you to choose which layers will actually be displayed.  If you un-check the <b>Show</b> button for the Microstructure layer you will see the Image layer below it. 

The order of the layers can be changed by selecting a layer and using the commands in the <b>Layer</b> menu, or right-clicking on a layer and using the pop-up menu. (Clicking and dragging layers might also work.) """
    ),

    TutoringItem(
        subject="Assigning a Material to Pixels -- continued",
        comments=
"""Select the <b>cyan-material</b> in the <b>Material</b> pane in the main OOF2 window and assign it to the pixel group named <b>cyan</b>.

Make the Microstructure display layer visible in the graphics window, and note that the black pixels have turned cyan, since they now have a Material assigned to them.""",
    ),


    TutoringItem(
        subject="Creating a Skeleton",
        comments=
"""OOF2 doesn't create a finite element mesh directly from a Microstructure.  Instead, it creates a <b>Skeleton</b>, which specifies the mesh geometry and nothing else.  One Skeleton can be used to create many different meshes, with different element types and different physical fields.  One Microstructure can contain many Skeletons.

Open the <b>Skeleton</b> page in the main OOF2 window.

Since we have such a simple microstructure, creating a reasonable skeleton is going to be easy.

Click the <b>New</b> button to open up a skeleton initializer.

To keep things simple, just click <b>OK</b> to create a 4x4 grid of quadrilateral skeleton elements.""",
    ),

    TutoringItem(
        subject="Snapping Nodes to Material Boundaries",
        comments=
"""The Skeleton is now displayed on top of the Microstructure in the graphics window.

The second row of elements (from the bottom) contains both <b>cyan</b> and <b>yellow</b>, while other elements contain only one Material.

The Skeleton will be a better representation of the Microstructure if each element contains only one Material.  In this case, moving the nodes of the third row to the material boundary will fix the Skeleton.
    
Click on the chooser widget for the <b>method</b> parameter in the <b>Skeleton Modification</b> pane and select <b>Snap Nodes</b>.

Set <b>alpha</b> to 1.0.  Place the mouse over the labels and menu items to see an explanation of what the parameters mean.
    
Click <b>OK</b> to modify the skeleton.

All the elements in the skeleton are now completely homogeneous. """,
    ),

    TutoringItem(
        subject="Creating a Finite Element Mesh",
        comments=
"""It's time to create an FE mesh based on this skeleton.

Open the <b>FE Mesh</b> page.

Click the <b>New</b> button to get a dialog box for creating a new Mesh.  Here you must specify which types of mesh elements to use for triangular and quadrilateral skeleton elements.  The <b>mapping order</b> and <b>interpolation order</b> pull-down menus specify what order polynomials will be used for positioning the elements (mapping) and for interpolating within them.  Leave these set to <b>1</b> to use linear elements.

The pull-down menus labelled <b>2-cornered element</b>, <b>3-cornered element</b> and <b>4-cornered element</b> list the available element types that are consistent with the polynomial orders chosen.  There's only one choice for each: <b>D2_2</b>, <b>T3_3</b> and <b>Q4_4</b>.  Positioning the mouse over the menus will bring up a tooltip describing the element type.

Click <b>OK</b> to create an FE Mesh.  The new mesh is displayed in the graphics window, but at the moment it looks just like the Skeleton, so it's hard to see. """,
        ## TODO GTK3: there are supposed to be tooltips for the
        ## element types
    ),

    TutoringItem(
        subject="Defining Fields",
        comments=
"""Proceed to the <b>Fields &amp; Equations</b> page.
        
Here, we need to tell OOF2 about the (known) unknowns of the problem that we're trying to solve.

Fields are <b>defined</b> if they have been given values on the Mesh.

Fields are <b>active</b> if the solver will find their values. Only defined fields can be active.

Fields are <b>in-plane</b> if they have no out-of-plane derivatives. (This is a generalization of plane-strain.)

We're solving a uniaxial tension problem, so <b>displacement</b> is the only (known) unknown.

Check all three boxes for the <b>Displacement</b> field. """
    ),

    TutoringItem(
        subject="Activating Equations",
        comments=
"""We're solving the <b>Force_Balance</b> equation, so check the corresponding box on the right hand side of the <b>Fields &amp; Equations</b> page. """
    ),

    TutoringItem(
        subject="Applying Boundary Conditions",
        comments=
"""Now, move to the <b>Boundary Conditions</b> page.

The boundary conditions we're going to apply are:

<b>1.</b> u_x = 0 on the <b>left</b> side
    
<b>2.</b> u_y = 0 on the <b>bottom</b> side

<b>3.</b> u_x = 10.0 on the <b>right</b> side

To set fixed boundary conditions in OOF2, you must specify not only the Field that is to be fixed, but the Equation that is constrained by fixing the Field.  This is because OOF2 handles general couplings between Fields, so it's not always obvious which Equation should be constrained.  For the problem we're solving now, we'll make the simplest choice.

Since only one Field is defined and only one Equation is active for this example, the <b>field</b> and <b>equation</b> will have only one choice each, <b>Displacement</b> for field and <b>Force_Balance</b> for equation.

Go to the next slide to really set the boundary conditions. """
    ),

    TutoringItem(
        subject="Applying Boundary Conditions -- continued",
        comments=
"""Click the <b>New...</b> button in the <b>Condition</b> pane to bring up a boundary condition builder. 
    
Give the boundary condition a name, or leave the name field set to <i>&lt;automatic&gt;</i>.

The pull-down menu below the name allows you to choose the type of boundary condition.  Leave it set to <b>Dirichlet</b> boundary conditions, which gives Fields fixed values at the boundaries.

The first B.C. deals with displacement in the <b>x</b>-direction, so select <b>x</b> for both <b>Displacement</b> and <b>Force_Balance</b> components.

The <b>profile</b> is the functional form of the Field along the boundary.  The predefined boundaries in OOF2 (top, left, bottom, right) go counterclockwise around the microstructure.  Set the <b>profile</b> to <b>Constant Profile</b> with <b>value</b>=0.0.

Finally, choose the <b>boundary</b> to which this condition should be applied (<b>left</b>) and click <b>OK</b>.

<b>Important Note</b> Do not click the <b>Apply</b> button in the builder window.  This button enables users to continue building boundary conditions without having to close and re-open the builder window in a real world practice, but in this tutorial setting, it will keep you from advancing to the next slide. If you DID click <b>Apply</b>, close the builder window and move to the next slide. """,
    ),

    TutoringItem(
        subject="Applying Boundary Conditions -- continued",
        comments=
"""Click <b>New...</b> to add the second boundary condition.

Select <b>y</b> for both <b>Displacement</b> and <b>Force_Balance</b> components.

Select <b>Constant Profile</b> and type in <b>0</b>.

This condition's going to be applied to the <b>bottom</b> of the mesh. Select <b>bottom</b> and click <b>OK</b> to finish.""",
    ),

    TutoringItem(
        subject="Applying Boundary Conditions -- continued again",
        comments=
"""Click <b>New...</b> to add the third boundary condition.

Select <b>x</b> for both <b>Displacement</b> and <b>Force_Balance</b> components.

Its value is <b>10.0</b>, which is constant along the side.  Select <b>Constant Profile</b> and type in <b>10.0</b>.

This condition's going to be applied to the <b>right</b> side of the mesh. Select <b>right</b> and click <b>OK</b> to finish.

We've just finished creating all three boundary conditions. """,
    ),

    TutoringItem(
        subject="Setting a Solver",
        comments=
"""Open the <b>Solver</b> page.  There are three subregions of the page.

The top part determines which of the Mesh's <b>Subproblems</b> will be solved, and what methods will be used to solve them.

The middle section determines the <b>initial values</b> of Fields.

The bottom section sets global solution parameters (applied to all subproblems), reports Mesh status, and contains the <b>Solve</b> button, which does all the hard work.  The <b>Solve</b> button is dimmed because we haven't assigned a Solver to any Subproblems yet.

Select the <b>default</b> subproblem in the top pane, and either double click it or click the <b>Set Solver...</b> button.  A dialog box appears.  We're solving a linear, static problem, and can use the default parameters for <b>Basic</b> mode, so don't change anything in the dialog box.  (In <b>Advanced</b> mode you can control more details of the solution procedure.)  Just click <b>OK</b>. """
    ),

    TutoringItem(
        subject="Solving and Displaying a Mesh",
        comments=
"""Click <b>Solve</b>. Bring up the graphics window to examine the deformed mesh. """,
    ),

    TutoringItem(
        subject="Displaying Contours",
        comments=
"""At the bottom of the graphics window, you'll see that four layers are listed, <b>Mesh</b>, <b>Skeleton</b>, <b>Microstructure</b> and <b>Image</b>.  (You may have to drag the divider between the canvas and the layer list and/or expand the window in order to see all the layers.) The Mesh layer displays the Mesh element edges at their displaced positions.  We'll change it to display a contour map of the x displacements.
    
Double-click on the Mesh layer to edit it.

In the pop-up window, change <b>Element Edges</b> to <b>Filled Contour</b>.

The set of pull-down menus labelled <b>how</b> determines which quantity will be plotted.  Displacement is a <b>Field</b>, so set the top "what" menu to <b>Field</b>, and then set the next menu to <b>Component</b>.

The two menus below <b>Component</b> in the "what" box allow you to choose which field and which component to display.  The only field defined in this problem is Displacement, so leave that menu alone. Make sure that the <b>component</b> menu is set to <b>x</b>.

The <b>where</b> parameter controls whether the contours will be displayed at their original positions (ie, on the Skeleton) or at their actual displaced positions (ie, on the Mesh), or somewhere in between.  Leave it set to <b>original</b>.

Click <b>OK</b> and go back to the Graphics Window to observe the result.  The map on the right edge of the window indicates how colors correspond to actual values.

Notice that the contour graphics layer is hiding the Skeleton element edges, and is above the Skeleton edge layer in the layer list. This is because you edited the Mesh edge layer to turn it into a contour layer, and the Mesh edges were displayed above the Skeleton edges.  If instead you had created a new layer, it would have appeared in its default position, below the Skeleton edge layer in the list.  Using the <b>Layer</b> menu you can lower the contour layer below the edges, or choose <b>Reorder All</b> to put the contour layer in its default position.  """
    ),
        
        TutoringItem(
            subject="Modifying the Problem",
            comments=
"""The solution you obtained wasn't very interesting. Let's change the problem and solve it again.

Go back to the <b>Boundary Conditions</b> page.  Select the third boundary condition and click the <b>Edit</b> button, or double click on the boundary condition.

In the dialog box, change <b>Dirichlet</b> to <b>Neumann</b>.  Neumann boundary conditions allow you to specify the normal components of a flux (eg, stress) instead of a field (eg, displacement) along a boundary.

Set <b>flux</b> to <b>Stress</b>.  Stress is a tensor, and its normal components are the external force density, which is two dimensional vector, specified by the <b>p0</b> and <b>p1</b> parameters. If the <b>normal</b> parameter is <b>false</b>, then the force is given in lab coordinates, where <b>p0</b> is the x component and <b>p1</b> is the y component.  If <b>normal</b> is <b>true</b>, then the force is give in a local coordinate system with <b>p0</b> in the outward normal direction and <b>p1</b> in the counterclockwise tangential direction.
            
Change <b>p1</b> to <b>0.01</b>, and click <b>OK</b>.  Return to the <b>Solver</b> page and click <b>Solve</b> again.  Go to the graphics window to observe the result.

In the graphics window, double click the <b>Mesh</b> layer in the layer list, and experiment with different values. You can set <b>where</b> to <b>actual</b> to see how the mesh is deformed.  Change the <b>what</b> field to display contour plots of different quanties.  Change <b>min</b> and <b>max</b> and <b>levels</b> to control which contours are computed, and change <b>nbins</b> to adjust how smooth the contours are. """
        ),

        TutoringItem(
            subject="Finished",
            comments=
"""Congratulations.  You've completed an OOF2 problem. To learn more about the program, continue to the next tutorial. Please also read the manual, at

            <tt>https://www.ctcms.nist.gov/~langer/oof2man/</tt> """
        )
    ]
)
