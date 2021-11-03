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

## TODO: Add instructions to close graphics windows and delete
## microstructures if running this tutorial after running another one,
## so that new images will appear automatically.

TutorialClass(
    subject="A Simple Example",
    ordering=0.1,
    lessons = [
        TutoringItem(
            subject="Introduction",
            comments=

    """This tutorial is designed to familiarize users with OOF2 by
    guiding them through a simple but complete project.

    We assume that you run this tutorial from a fresh start of OOF2.
    Whether you run it this way or not doesn't make any significant
    difference but it simplifies things in a few places.

    BOLD(Objective): A simple finite element analysis of a fictitious
    microstructure under uniaxial tension.  The microstructure is
    composed of two fictitious materials named BOLD(yellow) and
    BOLD(cyan) with linear elastic properties given by:

    BOLD(yellow) : E=1.0, nu=0.3

    BOLD(cyan) : E=0.5. nu=0.3
    """
        ),

    TutoringItem(
        subject="Graphics Window",
        comments=

    """Open a graphics window, if none has been opened yet, with the
    BOLD(Graphics/New) command in the BOLD(Windows) menu in any OOF2
    window.  Graphical representations of entities such as
    Microstructure, Skeleton, and Mesh, are displayed in the graphics
    window.

    (New!) The graphics window doesn't automatically display objects
    unless you add a new graphics layer.  It can be told to
    automatically add layers, though.  In the Settings menu, select
    BOLD(New Layer Policy), and in the dialog box set BOlD(policy) to
    BOLD(Single).  Click BOLD(OK).  This makes the window
    automatically display new Images, Meshes, and Skeletons if only one
    such object exists."""
    ),

    TutoringItem(
        subject="Get the Image",
        comments="""Locate the file BOLD(cyallow.png) within the
    share/oof2/examples directory in your OOF2 installation.

    """),

    TutoringItem(
        subject="Loading a Microstructure and an Image",
        comments=

        ## TODO GTK3: figure out how to use real markup in tutorial
        ## entries.  The angle braces in BOLD(<automatic>) aren't
        ## appearing.
    """Open the BOLD(Microstructure) page from the BOLD(Task) menu in
    the main OOF2 window.

    Create a new Microstructure from an existing image file by
    clicking the BOLD(New from Image File) button.

    In the file selector, navigate to BOLD(cyallow.png).  For now,
    leave the BOLD(microstructure_name), BOLD(width) and BOLD(height)
    values set to BOLD(<automatic>).  Click BOLD(OK).

    You should see an image -- cyan on top of yellow -- displayed on
    the graphics window.  Also, the BOLD(Microstructure) pull down
    menu at the top of the Microstructure page now contains a single
    entry, "cyallow.png", which is the automatically generated name
    for the Microstructure that was created by the BOLD(New from Image
    File) command.
    """,
        
    signal=("new who", "Microstructure")
    ),

    TutoringItem(
        subject="Categorizing Pixels",
        comments=

    """At this point, a microstructure has been created but it
    contains no useful information other than its size.

    We need to let the microstructure know that it has two different
    materials and they are represented by the two different colors in
    the Image.

    Generally, this is a fairly complicated process, but the sample
    microstructure in this tutorial can be automatically categorized
    with a single click of a button, since the base image features
    only two distinct colors.

    Open the BOLD(Image) page in the main OOF2 window.

    Click the BOLD(Group) button, and click BOLD(OK) in the dialog box.

    Go back to the BOLD(Microstructure) page, and notice that two
    pixel groups have been created.""",
        signal="new pixel group"
    ),

    TutoringItem(
        subject="Renaming Pixel Groups",
        comments=

    """The automatically generated names of the pixel groups are the
    hexadecimal values of the colors and are not terribly
    convenient. The groups can be renamed.

    Select the first pixel group, BOLD(#00ffff (2160 pixels meshable))

    Once it's been highlighted, click BOLD(Rename), in the buttons to
    the left of the group list. (The buttons above the group list act
    on the Microstructure, not the groups).

    Delete the old name and type in BOLD(cyan), which is the actual
    color of the group. 

    Click BOLD(OK) to finalize the change.
    """,
        signal="renamed pixel group"
    ),

    TutoringItem(
        subject="Renaming Pixel Groups -- continued",
        comments=

    """Select the second pixel group and BOLD(Rename) it to
    BOLD(yellow).

    Now you're ready to create materials for each pixel group.
    """,
        signal="renamed pixel group"
    ),        

    TutoringItem(
        subject="Adding Materials",
        comments=
        """Open the BOLD(Materials) page in the main OOF2 window.

    The page contains two panes.  The left hand BOLD(Property) pane
    allows you to define material properties.  The right hand
    BOLD(Material) pane allows you to combine properties into a
    Material.

    Create a new material by clicking on the BOLD(New) button in the
    BOLD(Material) pane.

    The BOLD(name) field contains the text "<automatic>" in italics.
    If you don't change it, OOF2 will generate an automatic name for
    the material.  If you type anything in the field, it will replace
    "<automatic>", and what you've typed will be used for the name of
    the material.  If you delete everything that you've typed,
    "<automatic>" will reappear.  Whenever OOF2 is able to
    automatically generate an input value, it uses a widget like this,
    where typing anything turns off the automatic behavior and
    deleting everything turns it back on. 

    Type BOLD(yellow-material) in the text entry field.  (You can use
    any name you like for the material, including names that you've
    used for other objects.  To avoid confusion in this tutorial,
    though, don't use the name "yellow" since it's already been used
    for the pixel group.)

    Leave "material_type" set to "bulk".
    
    Click BOLD(OK).
    """,
        signal="new_material"
    ),

    TutoringItem(
        subject="Adding Materials -- continued",
        comments=
        """Create a second BOLD(New) material with the name
    BOLD(cyan-material).""",
        signal="new_material"
    ),

    TutoringItem(
        subject="Creating a Property",
        comments=

    """We now need to make materials meaningful by adding properties
    to them.

    The BOLD(Property) pane on the left side of the Materials page
    hierarchically lists all of the Property types that are installed
    in OOF2.  Clicking on a triangle pointing RIGHT will expand a level,
    and clicking on a triangle pointing DOWN will collapse a
    level of the hierarchy.

    Start creating a property for BOLD(yellow-material) by selecting
    BOLD(Isotropic) from BOLD(Elasticity) in the BOLD(Mechanical)
    property hierarchy.

    Click BOLD(Copy) and give the Property a user-defined name. (This
    is another automatic widget.  Use the Copy button in the Property
    pane, not the one in the Material pane!)

    Type in BOLD(yellow_elasticity) and click BOLD(OK).  Note that
    Property names must begin with a letter and can only contain
    letters, numerals, and underscores (they must be legal Python
    variable names). """,
        signal = "new property"
    ),
        
    TutoringItem(
        subject="Parametrizing a Property",
        comments=
        
    """Select BOLD(yellow_elasticity) from the Property hierarchy and
    either double click it or click the BOLD(Parametrize...) button to
    input actual values.

    The elasticity parameters can be entered in a variety of formats.
    The default format is BOLD(Cij).  Change it to BOLD(E and nu) with
    the pull down menu at the top of the Parametrize dialog box.

    Set the Young's modulus (BOLD(young)) to 1.0 and Poisson's ratio
    (BOLD(poisson)) to 0.3.

    Click BOLD(OK) to finish up.
    """,
        signal = "redraw"
    ),

    TutoringItem(
        subject="Adding a Property to a Material",
        comments=

    """ Below the BOLD(New) button in the BOLD(Material) pane is a
    pull-down menu that lists all of the Materials that have been
    defined.  Select the BOLD(yellow-material) that you defined
    earlier.

    Make sure that the BOLD(yellow_elasticity) Property is still
    selected.

    Click BOLD(Add Property to Material) in the BOLD(Property) pane to
    add the Property to the Material.

    The addition should immediately appear in the BOLD(Material) pane,
    in the list of Properties below the Material selector.
    """,
        signal= "prop_added_to_material"
    ),

    TutoringItem(
        subject="Creating Another Property",
        comments=
        """Make another BOLD(Copy) of BOLD(Isotropic) and name it
    BOLD(cyan_elasticity).""",
        signal = "new property"
    ),

    TutoringItem(
        subject="Parametrizing Another Property",
        comments=
        """BOLD(Parametrize) the property BOLD(cyan_elasticity) with these
    values: BOLD(young)=0.5, BOLD(poisson)=0.3.""",
        signal = "redraw"
    ),

    TutoringItem(
        subject="Adding Another Property to a Material",
        comments=

    """Select BOLD(cyan-material) in the Material selector in the
    BOLD(Material) pane, and add the Property BOLD(cyan_elasticity) by
    clicking on the BOLD(Add Property to Material) button.

    Make sure that the Materials contain the correct Properties before
    you move on.  Select a Property in the BOLD(Material) pane and use
    the BOLD(Remove Property from Material) button if you've made a
    mistake.  """,
        
    signal= "prop_added_to_material"
    ),

    TutoringItem(
        subject="Adding Colors to Materials",
        comments=
        """Although it's not necessary mathematically, it's convenient to
    assign colors to Materials so that the Microstructure can be
    displayed.

    BOLD(Copy) the BOLD(Color) property in the BOLD(Property) pane,
    giving the copy the name BOLD(yellow).

    BOLD(Parametrize) the BOLD(yellow) Property.  The color of the
    Material doesn't have to be the same as the color in the Image,
    but might be confusing if it's different.  In the Parametrize
    dialog box, switch from BOLD(TranslucentGray) to BOLD(RGBAColor),
    and set the BOLD(red), BOLD(green), BOLD(blue), and BOLD(alpha)
    sliders to something yellowish, say BOLD(red)=1, BOLD(green=0.8),
    and BOLD(blue)=0.  BOLD(Alpha) is the opacity.  Leave it at 1.0.
    (You can change the values either by sliding the sliders or typing
    in the text boxes on the right.)  Click BOLD(OK).

    Add the BOLD(yellow) Property to the BOLD(yellow-material).

    Similarly create a BOLD(Color) property for BOLD(cyan) and add it to the
    BOLD(cyan-material).  Parametrize it with BOLD(Red)=0,
    BOLD(Green)=0.8, and BOLD(Blue)=1.
    """,
        signal="prop_added_to_material"
    ),

    TutoringItem(
        subject="Assigning a Material to Pixels",
        
    comments=

    """Now that we have defined Materials and created pixel groups in
    the Microstructure, we can assign Materials to the microstructure.

    Select the material BOLD(yellow-material) and click on the button labelled
    BOLD(Assign to Pixels...) in the BOLD(Material) pane.

    The pop-up window lets you choose the Microstructure to which the
    Material will be assigned (currently we only have one,
    "cyallow.png"), and the pixels within the Microstructure.  Choose
    the pixel group BOLD(yellow) in the BOLD(pixels) pull-down menu.

    Click BOLD(OK) to finish.
    """,
        signal = "materials changed in microstructure"
    ),

    TutoringItem(
        subject="Displaying a Microstructure",
        comments=

    """The graphics window can display some things automatically, but if
    you want to view a Microstructure you must do it explicitly by
    adding a new BOLD(Display Layer).

    Dig up the Graphics window that you opened earlier by choosing
    BOLD(Graphics/Graphics 1) in the BOLD(Windows) menu on any OOF2
    window.

    Select BOLD(New) from the BOLD(Layer) menu in the Graphics window.
    Earlier versions of OOF2 used a really awkward graphics layer
    editor window here.  Fortunately, it's been eliminated.

    The dialog box for creating a new graphics layer asks you to
    specify three things: BOLD(category), BOLD(what), and BOLD(how).

    BOLD(category) is what kind of thing is to be displayed by the
    layer: BOLD(Microstructure), BOLD(Image), BOLD(Skeleton), etc.
    Click on the pulldown menu and select BOLD(Microstructure).

    BOLD(what) is the name of the particular object that is to be
    displayed.  Select BOLD(cyallow.png), the name of the
    Microstructure, in the pulldown menu.  (The other two items in the
    menu refer to the Microstructures displayed in other layers, but
    there are no relevant layers at the moment, so ignore them.)

    BOLD(how) is the way in which the object will be displayed.
    Different kinds of objects have different kinds of display
    methods.  Leave the pull-down menu at the top of the BOLD(how)
    field set to BOLD(Material), which draws the Microstructure by
    coloring each pixel with the color of the Material assigned to the
    pixel.  This display method has two parameters:
    BOLD(no_material), the color to use for pixels that have no
    associated Material; and BOLD(no_color), the color to use for
    pixels that have a Material which has no ColorProperty.  Ignore
    both parameters for now and click the BOLD(OK) button.
    """),

    TutoringItem(
        subject="Layer List",
        comments=
        
    """The Microstructure Material Display appears in the Graphics window.
    Pixels to which you assigned the yellow-material are drawn in
    yellow.  The remaining pixels are black because they have no
    Material, and the default value for BOLD(no_material) is black.

    The Layer List at the bottom of the Graphics Window now shows two
    layers: a Microstructure layer on top of an Image layer.  You may
    have to scroll the list to see both layers.  Because the
    Microstructure and the Image are the same size, you can only see
    one of them at a time.  The buttons in the column labelled
    BOLD(Show) in the Layer List allow you to choose which layers will
    actually be displayed.  If you un-check the BOLD(Show) button for
    the Microstructure layer you will see the Image layer below
    it. 

    The order of the layers can be changed by selecting a layer
    and using the commands in the BOLD(Layer) menu, or right-clicking
    on a layer and using the pop-up menu. (Clicking and dragging
    layers might also work.)
    """),

    TutoringItem(
        subject="Assigning a Material to Pixels -- continued",
        comments=
        
    """Select the BOLD(cyan-material) in the BOLD(Material) pane in
    the main OOF2 window and assign it to the pixel group named
    BOLD(cyan).

    Make the Microstructure display layer visible in the graphics
    window, and note that the black pixels have turned cyan, since
    they now have a Material assigned to them.""",

    signal = "materials changed in microstructure"
    ),


    TutoringItem(
        subject="Creating a Skeleton",
        comments=

    """OOF2 doesn't create a finite element mesh directly from a
    Microstructure.  Instead, it creates a BOLD(Skeleton), which
    specifies the mesh geometry and nothing else.  One Skeleton can be
    used to create many different meshes, with different element types
    and different physical fields.  One Microstructure can contain
    many Skeletons.

    Open the BOLD(Skeleton) page in the main OOF2 window.

    Since we have such a simple microstructure, creating a reasonable
    skeleton is going to be easy.

    Click the BOLD(New) button to open up a skeleton initializer.

    To keep things simple, just click BOLD(OK) to create a 4x4 grid of
    quadrilateral skeleton elements.""",
        
    signal = ("new who", "Skeleton")
    ),

    TutoringItem(
        subject="Snapping Nodes to Material Boundaries",
        comments=

    """The Skeleton is now displayed on top of the Microstructure in
    the graphics window.

    The second row of elements (from the bottom) contains both
    BOLD(cyan) and BOLD(yellow), while other elements contain only one
    Material.

    The Skeleton will be a better representation of the Microstructure
    if each element contains only one Material.  In this case, moving
    the nodes of the third row to the material boundary will fix the
    Skeleton.
    
    Click on the chooser widget for the BOLD(method) parameter in the
    BOLD(Skeleton Modification) pane and select BOLD(Snap Nodes).

    Set BOLD(alpha) to 1.0.  Place the mouse over the labels and menu
    items to see an explanation of what the parameters mean.
    
    Click BOLD(OK) to modify the skeleton.

    All the elements in the skeleton are now completely homogeneous.
    """,

    signal = "Skeleton modified"
    ),

    TutoringItem(
        subject="Creating a Finite Element Mesh",
        comments=
        """It's time to create an FE mesh based on this skeleton.

    Open the BOLD(FE Mesh) page.

    Click the BOLD(New) button to get a dialog box for creating a new
    Mesh.  Here you must specify which types of mesh elements to use
    for triangular and quadrilateral skeleton elements.  The
    BOLD(mapping order) and BOLD(interpolation order) pull-down menus
    specify what order polynomials will be used for positioning the
    elements (mapping) and for interpolating within them.  Leave these
    set to BOLD(1) to use linear elements.

    The pull-down menus labelled BOLD(2-cornered element),
    BOLD(3-cornered element) and BOLD(4-cornered element) list the
    available element types that are consistent with the polynomial
    orders chosen.  There's only one choice for each: BOLD(D2_2),
    BOLD(T3_3) and BOLD(Q4_4).  Positioning the mouse over the menus
    will bring up a tooltip describing the element type.

    Click BOLD(OK) to create an FE Mesh.  The new mesh is displayed in
    the graphics window, but at the moment it looks just like the
    Skeleton, so it's hard to see.
    """,
        ## TODO GTK3: there are supposed to be tooltips for the
        ## element types
    signal = ("new who", "Mesh")
    ),

    TutoringItem(
        subject="Defining Fields",
        comments=

    """Proceed to the BOLD(Fields & Equations) page.
        
    Here, we need to tell OOF2 about the (known) unknowns of the
    problem that we're trying to solve.

    Fields are BOLD(defined) if they have been given values on the Mesh.

    Fields are BOLD(active) if the solver will find their values.
    Only defined fields can be active.

    Fields are BOLD(in-plane) if they have no out-of-plane
    derivatives. (This is a generalization of plane-strain.)

    We're solving a uniaxial tension problem, so BOLD(displacement) is
    the only (known) unknown.

    Check all BOLD(three) boxes for the BOLD(Displacement) field.
    """
    ),

    TutoringItem(
        subject="Activating Equations",
        comments=

    """We're solving the BOLD(Force_Balance) equation, so check the
    corresponding box on the right hand side of the BOLD(Fields &
    Equations) page.
    """
    ),

    TutoringItem(
        subject="Applying Boundary Conditions",
        comments="""Now, move to the BOLD(Boundary Conditions) page.

    The boundary conditions we're going to apply are:

    BOLD(1.) u_x = 0 on the BOLD(left) side
    
    BOLD(2.) u_y = 0 on the BOLD(bottom) side

    BOLD(3.) u_x = 10.0 on the BOLD(right) side

    To set fixed boundary conditions in OOF2, you must specify not
    only the Field that is to be fixed, but the Equation that is
    constrained by fixing the Field.  This is because OOF2 handles
    general couplings between Fields, so it's not always obvious which
    Equation should be constrained.  For the problem we're solving
    now, we'll make the simplest choice.

    Since only one Field is defined and only one Equation is active
    for this example,
    the BOLD(field) and BOLD(equation) will have only one choice
    each, BOLD(Displacement) for field and BOLD(Force_Balance) for equation.

    Go to the next slide to really set the boundary conditions.
    """),

    TutoringItem(
        subject="Applying Boundary Conditions -- continued",
        comments=
        """Click the BOLD(New...) button in the BOLD(Condition) pane to bring
    up a boundary condition builder. 
    
    Give the boundary condition a name, or leave the name field set to
    "<automatic>".

    The pull-down menu below the name allows you to choose the type of
    boundary condition.  Leave it set to BOLD(Dirichlet) boundary
    conditions, which gives Fields fixed values at the boundaries.

    The first B.C. deals with displacement in the BOLD(x)-direction,
    so select BOLD(x) for both BOLD(Displacement) and
    BOLD(Force_Balance) components.

    The BOLD(profile) is the functional form of the Field along the
    boundary.  The predefined boundaries in OOF2 (top, left, bottom,
    right) go counterclockwise around the microstructure.  Set the
    BOLD(profile) to BOLD(Constant Profile) with BOLD(value)=0.0.

    Finally, choose the BOLD(boundary) to which this condition should
    be applied (BOLD(left)) and click BOLD(OK).

    BOLD(Important Note) Do not click the BOLD(Apply) button in the
    builder window.  This button enables users to continue building
    boundary conditions without having to close and re-open the
    builder window in a real world practice, but in this tutorial
    setting, it will keep you from advancing to the next slide. If you
    DID click BOLD(Apply), close the builder window and move to the
    next slide.

    """,
        
    signal = "boundary conditions changed"
    ),

    TutoringItem(
        subject="Applying Boundary Conditions -- continued",
        comments=

    """Click BOLD(New...) to add the second boundary condition.

    Select BOLD(y) for both BOLD(Displacement) and
    BOLD(Force_Balance) components.

    Select BOLD(Constant Profile) and type in BOLD(0).

    This condition's going to be applied to the BOLD(bottom) of the
    mesh. Select BOLD(bottom) and click BOLD(OK) to finish.""",

    signal = "boundary conditions changed"
    ),

    TutoringItem(
        subject="Applying Boundary Conditions -- continued again",
        comments=

    """Click BOLD(New...) to add the third boundary condition.

    Select BOLD(x) for both BOLD(Displacement) and
    BOLD(Force_Balance) components.

    Its value is BOLD(10.0), which is constant along the side.  Select
    BOLD(Constant Profile) and type in BOLD(10.0).

    This condition's going to be applied to the BOLD(right) side of
    the mesh. Select BOLD(right) and click BOLD(OK) to finish.

    We've just finished creating all three boundary conditions.
    """,
        signal = "boundary conditions changed"
    ),

    TutoringItem(
        subject="Setting a Solver",
        comments=
        
    """ Open the BOLD(Solver) page.  There are three subregions of the
    page.

    The top part determines which of the Mesh's BOLD(Subproblems) will
    be solved, and what methods will be used to solve them.

    The middle section determines the BOLD(initial values) of Fields.

    The bottom section sets global solution parameters (applied to all
    subproblems), reports Mesh status, and contains the BOLD(Solve)
    button, which does all the hard work.  The BOLD(Solve) button is
    dimmed because we haven't assigned a Solver to any Subproblems
    yet.

    Select the BOLD(default) subproblem in the top pane, and either
    double click it or click the BOLD(Set Solver...) button.  A dialog
    box appears.  We're solving a linear, static problem, and can use
    the default parameters for BOLD(Basic) mode, so don't change
    anything in the dialog box.  (In BOLD(Advanced) mode you can
    control more details of the solution procedure.)  Just click
    BOLD(OK).

    """
    ),


    # TutoringItem(
    #     subject="Solving a Mesh",
    #     comments="""
    # We're almost at the end of this tutorial.

    # """,
    #     signal="mesh solved"
    # ),
        
    TutoringItem(
        subject="Solving and Displaying a Mesh",
        comments=

        """ Click BOLD(Solve).
        Bring up the graphics window to examine the deformed mesh.
        """,
        signal="mesh solved"
    ),

    TutoringItem(
        subject="Displaying Contours",
        comments=

    """ At the bottom of the graphics window, you'll see that four layers
    are listed, BOLD(Mesh), BOLD(Skeleton), BOLD(Microstructure) and
    BOLD(Image).  (You may have to drag the divider between the canvas
    and the layer list and/or expand the window in order to see all
    the layers.) The Mesh layer displays the Mesh element edges at
    their displaced positions.  We'll change it to display a contour
    map of the x displacements.
    
    Double-click on the Mesh layer to edit it.

    In the pop-up window, change BOLD(Element Edges) to BOLD(Filled
    Contour).

    The set of pull-down menus labelled BOLD(how) determines which
    quantity will be plotted.  Displacement is a BOLD(Field), so set
    the top "what" menu to BOLD(Field), and then set the next menu to
    BOLD(Component).

    The two menus below BOLD(Component) in the "what" box allow you to
    choose which field and which component to display.  The only field
    defined in this problem is Displacement, so leave that menu alone.
    Make sure that the BOLD(component) menu is set to BOLD(x).

    The BOLD(where) parameter controls whether the contours will be
    displayed at their original positions (ie, on the Skeleton) or at
    their actual displaced positions (ie, on the Mesh), or somewhere
    in between.  Leave it set to BOLD(original).

    Click BOLD(OK) and go back to the Graphics Window to observe the
    result.  The map on the right edge of the window indicates how
    colors correspond to actual values.

    Notice that the contour graphics layer is hiding the Skeleton
    element edges, and is above the Skeleton edge layer in the layer
    list. This is because you edited the Mesh edge layer to turn it
    into a contour layer, and the Mesh edges were displayed above the
    Skeleton edges.  If instead you had created a new layer, it would
    have appeared in its default position, below the Skeleton edge
    layer in the list.  Using the BOLD(Layer) menu you can lower the
    contour layer below the edges, or choose BOLD(Reorder All) to put
    the contour layer in its default position.  """
    ),
        
        TutoringItem(
            subject="Modifying the Problem",
            comments=
            
            """The solution you obtained wasn't very interesting.  
            Let's change the problem and solve it again.

            Go back to the BOLD(Boundary Conditions) page.  Select the
            third boundary condition and click the BOLD(Edit) button,
            or double click on the boundary condition.

            In the dialog box, change BOLD(Dirichlet) to
            BOLD(Neumann).  Neumann boundary conditions allow you to
            specify the normal components of a flux (eg, stress)
            instead of a field (eg, displacement) along a boundary.

            Set BOLD(flux) to BOLD(Stress).  Stress is a tensor, and
            its normal components are the external force density,
            which is two dimensional vector, specified by the BOLD(p0)
            and BOLD(p1) parameters. If the BOLD(normal) parameter is
            BOLD(false), then the force is given in lab coordinates,
            where BOLD(p0) is the x component and BOLD(p1) is the y
            component.  If BOLD(normal) is BOLD(true), then the force
            is give in a local coordinate system with BOLD(p0) in the
            outward normal direction and BOLD(p1) in the
            counterclockwise tangential direction.
            
            Change BOLD(p1) to BOLD(0.01), and click BOLD(OK).  Return
            to the BOLD(Solver) page and click BOLD(Solve) again.  Go
            to the graphics window to observe the result.

            In the graphics window, double click the BOLD(Mesh) layer
            in the layer list, and experiment with different values.
            You can set BOLD(where) to BOLD(actual) to see how the
            mesh is deformed.  Change the BOLD(what) field to display
            contour plots of different quanties.  Change BOLD(min) and
            BOLD(max) and BOLD(levels) to control which contours are
            computed, and change BOLD(nbins) to adjust how smooth the
            contours are.

            """),

        TutoringItem(
            subject="Finished",
            comments=

            """Congratulations.  You've completed an OOF2 problem. 
            To learn more about the program, continue to the next tutorial. 
            Please also read the manual, at

            https://www.ctcms.nist.gov/~langer/oof2man/
            """)
    ]
)
