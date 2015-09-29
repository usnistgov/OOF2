# -*- python -*-
# $RCSfile: simpleexample.py,v $
# $Revision: 1.31 $
# $Author: langer $
# $Date: 2012/06/05 18:40:12 $

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

TutorialClass(subject="A Simple Example",
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
    """
    ),

    TutoringItem(
    subject="Get the Image",
    comments="""Locate the file BOLD(cyallow.png) within the
    share/oof2/examples directory in your OOF2 installation.

    """),

    TutoringItem(
    subject="Loading a Microstructure and an Image",
    comments=

    """Open the BOLD(Microstructure) page from the BOLD(Task) menu in
    the main OOF2 window.

    Create a new Microstructure from an existing image file by
    clicking the BOLD(New from Image File) button.

    In the file selector, navigate to BOLD(cyallow.png).  For now,
    leave the BOLD(microstructure_name), BOLD(width) and BOLD(height)
    values set to BOLD(automatic).  Click BOLD(OK).

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

    """The automatically generated names of the pixel groups are not
    terribly convenient. The groups can be renamed.

    Select the first pixel group, BOLD(RGBColor(red=1.00, green=1.00,
    blue= ....)).

    Once it's been highlighted, click BOLD(Rename).

    Delete the old name and type in BOLD(yellow), which is the actual
    color of the group.  (Triple-clicking on the old name in the
    dialog box will select the whole name, making it easier to
    replace.)

    Click BOLD(OK) to finalize the change.
    """,
    signal="renamed pixel group"
    ),

    TutoringItem(
    subject="Renaming Pixel Groups -- continued",
    comments=

    """Select the second pixel group and BOLD(Rename) it to
    BOLD(cyan).

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

    The check box in the BOLD(name) field controls whether OOF2 will
    automatically generate a name for the Material or let you choose
    it.  Click the check box and type BOLD(yellow-material) in the
    text entry field.  (You can use any name you like for the
    material, including names that you've used for other objects.  To
    avoid confusion in this tutorial, though, don't use the name
    "yellow" since it's already been used for the pixel group.)

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

    Click BOLD(Copy) and check the box to give it a user-defined name.
    (Use the Copy button in the Property pane, not the one in the
    Material pane!)

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
    dialog box, switch from BOLD(GrayColor) to BOLD(RGBColor), and set
    the BOLD(Red), BOLD(Green), and BOLD(Blue) sliders to something
    yellowish, say BOLD(Red)=1, BOLD(Green=0.8), and BOLD(Blue)=0.
    Click BOLD(OK).

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
    BOLD(Assign Material to Pixels...) in the BOLD(Material) pane.

    The pop-up window lets you choose the Microstructure to which the
    Material will be assigned (currently we only have one,
    "cyallow.png"), and the pixels within the Microstructure.  Choose
    the pixel group BOLD(yellow) in the BOLD(pixels) pull-down menu.

    Click BOLD(OK) to finish.
    """,
    signal = "materials changed in microstructure"
    ),

    TutoringItem(
    subject="Displaying a Microstructure (Layer Editor)",
    comments=

    """The graphics window displays many things automatically, but if
    you want to view a Microstructure you must tell it to do so
    explicitly by adding a new BOLD(Display Layer).

    Dig up the Graphics window that you opened earlier by choosing
    BOLD(Graphics/Graphics 1) in the BOLD(Windows) menu on any OOF2
    window.

    Select BOLD(New) from the BOLD(Layer) menu in the Graphics window.
    The BOLD(Graphics Layer Editor) window will appear.

    Graphics layers each display a single object, which is specified
    in the left hand pane of the Layer Editor.  Objects come in a
    variety of categories: Microstructure, Image, Skeleton, etc.
    Choose BOLD(Microstructure) in the BOLD(category) pull-down menu.
    Since you have defined only one Microstructure, "cyallow.png",
    it's shown in the BOLD(object) menu.

    An object being displayed may appear in more than one Layer.  The
    layers for the object selected in the BOLD(Displayed Object) pane
    on the left side of the Layer Editor are listed in the
    BOLD(Display Methods) list on the right side.
    
    """),

    TutoringItem(
    subject="Adding a Graphics Layer",
    comments=

    """ Click the BOLD(New) button below the BOLD(Display Methods)
    list.  A dialog box for defining a Microstructure display layer
    appears.

    The pull-down menu at the top of the display method definition
    dialog lists all of the Display Methods applicable to a
    Microstructure.  Leave it set to BOLD(Material), which draws the
    Microstructure by coloring each pixel with the color of the
    Material assigned to it.  This display method has two parameters:
    BOLD(no_material), the color to use for pixels that have no
    associated Material; and BOLD(no_color), the color to use for
    pixels that have a Material which has no ColorProperty.  Ignore
    both parameters for now and click the BOLD(OK) button.

    """),

    TutoringItem(
    subject="Layer List",
    comments=
    
    """The Microstructure Material Display appears in the Graphics
    window.  Pixels to which you assigned the yellow-material are
    drawn in yellow, or whatever color you gave to that Material.  The
    remaining pixels are black because they have no Material, and the
    default value for BOLD(no_material) is black.

    The Layer List in the Graphics Window now shows two layers: a
    Microstructure layer on top of an Image layer.  You may have to
    scroll the list to see both layers.  Because the Microstructure
    and the Image are the same size, you can only see one of them at a
    time.  The buttons in the column labelled BOLD(Show) in the Layer
    List allow you to choose which layers will actually be displayed.
    The order of the layers can be changed by clicking and dragging
    the layers in the list, or by selecting a layer and using the
    commands in the BOLD(Layer) menu.

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
    and different physical fields.

    Open the BOLD(Skeleton) page in the main OOF2 window.

    Since we have such a simple microstructure, creating a reasonable
    skeleton is going to be short and sweet.

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

    Click BOLD(OK) to create an FE Mesh.""",
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

    BOLD(3.) u_x = 10.0 on the BOLD(right) side"""
    ),

    TutoringItem(
    subject="Applying Boundary Conditions -- continued",
    comments=
    """
    The BOLD(Boundary Condition) page has two panes, BOLD(Profile) and
    BOLD(Condition).  The BOLD(Profile) pane allows you to predefine
    the functional form of a boundary condition.

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
    """

    First, expand this tutorial window so that you can see the full
    text.  Once you open the boundary condition building dialog, you
    won't be able to scroll the tutorial (sorry!).
    
    Click the BOLD(New...) button in the BOLD(Condition) pane to bring
    up a boundary condition builder.  The pull-down menu at the top of
    the dialog box allows you to choose the type of boundary
    condition.  Leave it set to BOLD(Dirichlet) boundary conditions, which
    gives Fields fixed values at the boundaries.

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


    TutoringItem(
    subject="Solving a Mesh",
    comments="""
    We're almost at the end of this tutorial.

    Click BOLD(Solve).
    """,
    signal="mesh solved"
    ),
    
    TutoringItem(
    subject="Displaying a Mesh",
    comments=

    """Bring up the graphics window to examine the deformed mesh.
    """),

    TutoringItem(
    subject="Displaying Contour",
    comments=

    """ At the bottom of the graphics window, you'll see that four
    layers are listed, BOLD(Mesh), BOLD(Skeleton),
    BOLD(Microstructure) and BOLD(Image).  (You may have to drag the
    divider between the canvas and the layer list in order to see all
    the layers.) The Mesh layer displays the Mesh element edges at
    their displaced positions.
    
    Double-click on the Mesh layer to bring up the layer editor.
    Make it bigger, if necessary, so that you can view the whole
    editor.

    Double-click on the BOLD(Element Edges) display method in the
    layer editor.  This brings up a window in which you can edit the
    display layer.  We'll display the BOLD(x) component of the
    displacement.

    In the pop-up window, change BOLD(Element Edges) to BOLD(Filled
    Contour).

    The set of pull-down menus labelled BOLD(what) determines which
    quantity will be plotted.  Displacement is a BOLD(Field), so set the top
    "what" menu to BOLD(Field), and then set the next menu to
    BOLD(Component).

    Two new menus appear inside the "what" box, allowing you to choose
    which BOLD(field) and which BOLD(component) to display.  The only
    field defined in this problem is Displacement, so leave that menu alone.
    Make sure that the BOLD(component) menu is set to BOLD(x).

    Click BOLD(OK) and go back to the Graphics Window to observe the
    result.  The map on the right edge of the window indicates how
    colors correspond to actual values.

    Congratulations!!! You've finished your first OOF2 project.
    """
    )

      
    ])
