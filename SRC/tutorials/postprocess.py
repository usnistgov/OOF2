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
    subject = "Postprocessing",
    ordering = 4,
    lessons = [
      
    TutoringItem(
    subject="Introduction",
    comments=

    """OOF2 provides various post-processing tools for viewing and
    analyzing a solution.  This tutorial provides a brief discussion
    of these tools."""  ),

    TutoringItem(
    subject="Example Mesh",
    comments=

    """Let us load an example Mesh. Locate the file BOLD(cyallow.mesh)
    it within the share/oof2/examples directory in your OOF2
    installation.  From the BOLD(File) menu, choose BOLD(Load/Data),
    and in the file selector, select BOLD(cyallow.mesh).  Click
    BOLD(OK) to load the mesh.""",
    signal = ("new who" ,"Mesh")
    ),

    TutoringItem(
    subject="Graphics window",
    comments=

    """Open a graphics window to display the mesh.  If you've
    completed the BOLD(Simple Example) tutorial, you should be
    familiar with this mesh.

    Display the mesh by selecting BOLD(New) from the BOLD(Layer) menu.
    Set BOLD(category) to BOLD(Mesh), BOLD(what) to
    "cyallow.png/skeleton/mesh" and BOLD(how) to BOLD(Element Edges)
    with BOLD(where)=BOLD(original).

    Next, we'll go over standard features such as displaying contour
    (filled or line) plots and element/node queries in the graphics
    window."""

    ),

    TutoringItem(
    subject="New layer",
    comments=

    """We'll start with a filled contour of the displacement in the
    x-direction, which is one of a few non-trivial results - the mesh
    is subjected to an uniaxial tension in the x-direction.

    Open the new layer dialog box again, using the BOLD(Layer/New)
    dialog box or by right-clicking in the layer list.  BOLD(category)
    and BOLD(what) should still be set to the values you used in the
    previous step.

    Select BOLD(Filled Contour) in the BOLD(how) box.
    
    In the BOLD(what) option block, select BOLD(Field) and
    BOLD(Component).  Then, select BOLD(Displacement) and BOLD(x)
    for the field and the component, respectively.
        
    The option BOLD(where) determines whether to plot the contour at
    the displaced or original position.  Select BOLD(original).
    
    Leave the next five options as they are.  Click BOLD(OK) to display
    the contour plot."""
    ),
        
    TutoringItem(
    subject="More levels for contour",
    comments=
    """Admire the contour plot in the graphics window.  To add more levels
    to the plot, double-click on the BOLD(FilledContourDisplay) line
    in the the BOLD(Layers) list (or right-click on it and select
    BOLD(Edit), or select it and choose BOLD(Edit) in the window's
    BOLD(Layer) menu.)
    
    Look for the parameter BOLD(levels) and type in BOLD(21).  Click
    BOLD(OK).  The contour plot in the graphics window should reflect
    the change accordingly."""
    ),
        
    TutoringItem(
    subject="Values for the level",
    comments=

    """A map of all the contour levels is displayed on the right-hand
    pane of the graphics window, called the BOLD(Contour Map).  The
    actual value range for a given color on the BOLD(Contour Map) can
    be queried here, by clicking on the contour map itself.  This will
    cause the value range for the clicked color-block to be displayed
    at the bottom of the contour map pane.""" ),
        
    TutoringItem(
    subject="Mesh info toolbox",
    comments=

    """While contour plots are effective in presenting an overall trend,
    if you are interested in data at specific locations, you need to
    use other tools.  OOF2 provides the BOLD(Mesh Info) toolbox for
    this situation.
    
    Open the BOLD(Mesh Info) toolbox in the graphics window.  The
    toolbox lets you query complete information on elements and
    nodes""" ),
        
    TutoringItem(
    subject="Querying node data",
    comments=

    """The first order of business in using the toolbox is to set the
    mode.  Enter node mode by clicking on the BOLD(Node) button at the
    top of the toolbox.
    
    Click the mouse inside the mesh in the graphics window.  The
    closest node is highlighted with a blue dot and its basic data,
    such as index and position, and the values of all of its fields
    are displayed in the toolbox. """,
    
    signal = "redraw" ),
        
    TutoringItem(
    subject="Querying element data",
    comments=
        
    """Now, switch the toolbox to the element mode.  Notice an element is
    automatically selected.  It's the element containing the last
    mouse point from the previous mode.
    
    Basic data about the element, including index, nodes, and
    material, are displayed in the toolbox.  To query BOLD(Displacement) or
    BOLD(Stress) data, use the BOLD(Mesh Data) window.  It is a good
    idea to expand the graphics window to have a better access to the
    displayed values. """,
    signal = "redraw" ),

    TutoringItem(
    subject="Querying data at interior points",
    comments=

    """To display data at any point inside an element, click the BOLD(New
    Data Viewer...) button in the lower part of the toolbox.  You can
    open more than one data viewer at a time if necessary.

    Each data viewer window displays the value of one output quantity.
    The upper part of the window, marked BOLD(Source), determines what
    is computed and where.  (If the window is too large, you can
    collapse the BOLD(Source) region with by clicking the triangle in
    the upper left, and then resize the window.) The BOLD(Data) box at
    the bottom of the window shows the result.
    
    Any output that can be computed in the OOF2 BOLD(Analysis) page
    can be examined in a data viewer window.  The output is evaluated
    at the position given in the Source region.  You can change the
    position by typing in the BOLD(x) or BOLD(y) boxes, or by clicking
    the mouse in the graphics window.  If you don't want the position
    and data to change when you click the mouse, check BOLD(Space) in
    the BOLD(Freeze) box at the bottom.

    Normally, the data in the viewer window updates when the Mesh
    changes or when you select a new point.  The BOLD(Space) and
    BOLD(Time) checkboxes in the BOLD(Freeze) pane prevent the data
    from changing, if you need to compare values at different places
    or times.
    """),

    TutoringItem(
    subject="Clearing up",
    comments=

    """There are three utility buttons at the bottom of the toolbox.
    They are self-explanatory.  Click on the BOLD(Clear) button, which
    will effectively remove all the data from the toolbox, and clear
    the element or node selection from the canvas.  It does not clear
    the data in the data viewer.""",

    signal = "redraw" ),
    
    TutoringItem(
    subject="Mesh cross section",
    comments=

    """Imagine a situation where you want to extract field or flux
    data along a specified path.  The BOLD(Mesh Cross Section)
    toolbox lets you export data calculated along a user-created
    path.
    
    Open this toolbox.  The BOLD(Source) frame shows what data is to
    be processed.  For this to work properly, a graphics window should
    contain at least one contour layer.
    
    A path is created by clicking and dragging the mouse.  (At this
    time, only straight line paths can be created.) The paths are
    automatically added to a list of cross sections and can be managed
    through the buttons in the BOLD(Cross Section) frame of the
    toolbox.
    
    Click BOLD(Next) for more instruction.""",
    ),
        
    TutoringItem(
    subject="Mesh cross section - Continued",
    comments=

    """Create a path - it will be displayed as a gray line on on the
    canvas.  Rename it to BOLD(MyCrossSection).  Leave the
    BOLD(points) parameter set to Line Points, which will space the
    output points evenly along the entire cross section.
    
    The destination of the extracted data can be either the message
    window or a file.  To create a file for the data, select
    BOLD(New...) from the BOLD(Destination) menu. (You may need to
    rescroll or resize the toolbox to see all the options.) For now,
    select BOLD(Message Window) for the destination and give it a
    BOLD(Go!)"""),

    TutoringItem(
    subject="Mesh cross section - Final",
    comments=

    """Bring up the message window.  You will see that some data has
    been dumped here.  It's organized in columns, with a header at the
    top indicating what the columns mean.  For each data point, the
    distance along the cross-section, the fractional distance (between
    0.0 and 1.0), and the location on the mesh are all given, along
    with the data itself."""),
        
    TutoringItem(
    subject="Analysis page",
    comments=

    """Move to the BOLD(Analysis) page in the main BOLD(OOF) window.
    Here there are more general tools than in the BOLD(Mesh Cross
    Section) toolbox.  These tools do not require that the data be
    present in the graphics window, and they allow many other ways of
    selecting the analysis domain.  In addition, this BOLD(Analysis)
    page includes statistical operations, as well as direct
    output."""),

    TutoringItem(
    subject="Analysis page - organization",

    comments=

    """There are four panes in this window.  Each pane has
    automatic scroll-bars -- it may be necessary to enlarge the main
    OOF window, or scroll the panes, to see all the controls.  The
    BOLD(Output) pane determines what data will be used for the
    analysis operation.  The BOLD(Domain) pane determines where the
    data will come from.  In the previous example, a BOLD(Cross
    Section Domain) was automatically selected by the toolbox.  The
    BOLD(Operation) pane determines how the data will be processed,
    and the BOLD(Sampling) pane determines how data will be taken from
    the domain.

    The selections available in the BOLD(Sampling) pane are sensitive
    to what selections have been made in the BOLD(Domain) and
    BOLD(Operation) panes.

    Go to the next tutorial page for an example."""  ),

    TutoringItem(
    subject="Analysis page - Grid example",
    comments=

    """We will evaluate some data on an evenly-spaced BOLD(Grid) of points.

    Begin with the BOLD(Output) pane.  Select BOLD(Field) and
    BOLD(Derivative).  As soon as you select BOLD(Derivative), another
    menu bar should appear.  Select BOLD(Component).  So far, we've
    decided that we're going to output a derivative of a field
    component.  The next three option menus are for specific choices.
    Select BOLD(Displacement), BOLD(x), and BOLD(x) in order - it's a
    normal strain in the BOLD(x)-direction.

    Select BOLD(Entire Mesh) for the BOLD(Domain), and BOLD(Direct
    Output) for the BOLD(Operation).  You can also select the comment
    character to use in the output, and the separator character to use
    between data items on a line.

    Then select BOLD(Grid Points), and set BOLD(x_points) and
    BOLD(y_points) both to BOLD(5), so we get a manageable amount of
    data.  You may also elect to suppress certain columns from the
    data output using the toggle buttons.  For now, retain all of the
    data.
    
    Set the controls for the heart of the message window and
    give it a BOLD(Go).  Check the output in the message window."""),
    
    TutoringItem(
    subject="Analysis page - Final",
    comments=

    """You can try other BOLD(Operations) here, also.  Select
    BOLD(Average) or BOLD(Standard Deviation), and hit BOLD(Go) again.

    Other available BOLD(Domains) include pixel groups or
    selections, element groups or selections, or, as we have already
    seen from the toolbox, mesh cross-sections.

    BOLD(Grid) samples on element or pixel groups or selections are
    computed on a rectangular bounding box of the selection.
    Statistical outputs are integrated over the elements, or summed
    over the data from the centers of the pixels."""
    ),

    TutoringItem(
    subject="Boundary analysis",
    comments=

    """Move to the BOLD(Boundary Analysis) page, which is the final
    subject for this tutorial.  This page does the simple thing -
    outputting the integrated sum of the flux along the specified
    boundary.

    Select BOLD(right) from the BOLD(Boundaries) pane, and select
    BOLD(Stress) for BOLD(flux) in the BOLD(Boundary Operation) pane.
    Set the destination to BOLD(Message
    Window) and click BOLD(Go!) button.  A list of two values are
    reported.  In this example, they are the sum of reaction forces in
    the x and y-direction along the right side of the mesh.

    Thanks for following the tutorial.
    """  )
    
    ])
