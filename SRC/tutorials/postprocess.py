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
    of these tools.
    """  ),

    TutoringItem(
    subject="Example Mesh",
    comments=

    """First, load an example Mesh. Locate the file BOLD(cyallow.mesh)
    within the share/oof2/examples directory in your OOF2
    installation.  From the BOLD(File) menu, choose BOLD(Load/Data),
    and in the file selector, select BOLD(cyallow.mesh).  Click
    BOLD(OK) to load the mesh.

    This is the same simple mesh that you generated if you worked
    through the BOLD(Simple Example) tutorial.""",
    ),

    TutoringItem(
    subject="The Analysis Page",
    comments=

    """Open the the BOLD(Analysis Page) in the main OOF2 window.  This
    page lets you compute various quantities in a number of ways at
    your choice of locations.  We will compute the average and
    standard deviation of the stress over the entire mesh.
    
    There are four main panes in this window.  The panes can be
    resized by dragging the dividers between them, and they can also
    be scrolled.  You may need to resize the window at times to make
    the panes fully visible.

    You must specify five things for each analysis operation:

    BOLD(Output): What data will be extracted from the mesh.  Outputs
    can be BOLD(Scalar) or BOLD(Aggregate) (anything that's not a
    simple scalar).  Scalar examples include the components and
    invariants of fields and fluxes.  Aggregate examples include entire
    field and flux objects.  

    Select BOLD(Aggregate), and set the top pull-down menu to
    BOLD(Flux), and the one below that to BOLD(Value).  The menu below
    that lets you choose which Flux you'll be computing the value of.
    This Mesh only defines one, BOLD(Stress).

    BOLD(Domain): Where on the Mesh the data will be computed.  Set it
    to BOLD(Entire Mesh).

    BOLD(Operation): What to do with the data.  Set it to BOLD(Average
    and Deviation).

    BOLD(Sampling): How the data will be be extracted fro the domain.
    The choices available in the BOLD(Sampling) pane depend on what
    selections have been made in the BOLD(Domain) and BOLD(Operation)
    panes.  Leave it set to BOLD(Element Set), so that the average
    will be computed by integrating over elements.

    BOLD(Destination): Where to send the result.  Leave it set to
    BOLD(<Message Window>).

    Click BOLD(Go).

    Expand the Message Window to see the results.  There will be many
    comments (lines beginning with #), and one line of data.  The
    comments identify the contents of the data line.  """),

    TutoringItem(
    subject="Output to a File",
    comments=

    """In this step we'll evaluate the x derivative of the x displacement
    on a grid of points and write the results to a file.  (Because the
    example mesh contains a uniform strain, the results won't be very
    interesting, but that's not the point.)

    In the BOLD(Output) pane on the BOLD(Analysis Page), select
    BOLD(Scalar) mode.  Then set the top pull-down menu in the pane to
    BOLD(Field), and the one below it to BOLD(Derivative), and the one
    below that to BOLD(Component).  Notice that the pull-down menus
    listed in the lower part of the BOLD(Output) pane change as you
    set the upper ones.  The upper ones set the kind of output, and
    the lower ones set the parameters that determine exactly which
    output you'll get.  Set BOLD(field) to BOLD(Displacement) and set
    both BOLD(derivative) and BOLD(component) to BOLD(x).

    In the BOLD(Domain) pane, choose BOLD(Entire Mesh).  This choice
    requires no parameters, so there are no pull-down menus below it.

    In the BOLD(Operation) pane, select BOLD(Direct Output).  The data
    will be extracted from the domain but will not be processed
    further.

    In the BOLD(Sampling) pane, select BOLD(Grid Points).  To get a
    manageable amount of data for this tutorial, set both
    BOLD(x_points) and BOLD(y_points) to BOLD(5).  If BOLD(show_x) and
    BOLD(show_y) are checked, the x and y coordinates of the points
    will be included in the output.

    In the BOLD(Destination) pane at the bottom of the window, notice
    that the pull down menu contains only BOLD(<Message Window>).  To
    add a file to the list, click the BOLD(New...) button and select a
    file.  The new file will appear as an option for the Destination.

    Click BOLD(Go).  
    """),

    TutoringItem(
    subject="More about Output to a File",
    comments=

    """In a text editor or other utility, outside of OOF2, open the file
    that you just created.  There are comment lines at the top, each
    beginning with '#'.  (This default can be changed with the
    BOLD(Settings/Output Formatting/Comment Character) menu in the
    main OOF2 window.)  The comments describe the settings of the
    settings in the BOLD(Output), BOLD(Operation), BOLD(Domain), and
    BOLD(Sampling) panes.  Below that is a description of the contents
    of each column in the data and the time that the data was computed
    (in case you were solving a time dependent problem).  Below that
    is the data itself.

    If you want to compute more output, you can send it to the same
    file or select a different one.  If you use the same file, you can
    tell where the new data starts because new header lines will be
    printed.  If instead you want to overwrite the old data, use the
    BOLD(Rewind) button in the BOLD(Destination) pane before pressing
    BOLD(Go).
    """),

    TutoringItem(
    subject="Boundary analysis",
    comments=

    """Move to the BOLD(Boundary Analysis) page.  This page is like the
    BOLD(Analysis) page, but it only computes two things: averages of
    fields and integrals of fluxes along boundaries.

    Select BOLD(right) from the BOLD(Boundaries) pane, and select
    BOLD(Integrate Flux) in the BOLD(Boundary Operation) pane.  The
    only available flux in this mesh is Stress.

    At the bottom of the page, set the destination to BOLD(Message
    Window) and click BOLD(Go) button.
    
    The message window contains the usual header information and the
    data: the sum of the reaction forces in the x and y directions
    along the right side of the mesh.
    """  ),
        
    TutoringItem(
    subject="Contour Plots in the Graphics window",
    comments=

    """ OOF2 can also display contour plots of any scalar quantity that
    can be computed in the BOLD(Analysis Page).

    Open a graphics window to display the mesh.

    Display the mesh by selecting BOLD(New) from the BOLD(Layer) menu.
    Set BOLD(category) to BOLD(Mesh), BOLD(what) to
    "cyallow.png/skeleton/mesh" and BOLD(how) to BOLD(Element Edges)
    with BOLD(where)=BOLD(original).  Click BOLD(OK).
    """

    ),

    TutoringItem(
    subject="New layer",
    comments=

    """We'll start with a filled contour of the displacement in the
    x-direction.  The mesh is subjected to an uniaxial tension in the
    x-direction and the strain is uniform, so the displacement
    contours should be vertical lines.

    Open the new layer dialog box again, using the BOLD(Layer/New)
    dialog box or by right-clicking in the layer list.  BOLD(category)
    and BOLD(what) should still be set to the values you used in the
    previous step.

    Select BOLD(Filled Contour) in the pull-down menu at the top of
    the BOLD(how) box. 

    Any scalar quantity that you can compute on the BOLD(Analysis)
    page can be made into a contour plot.  In the BOLD(what) option
    block, select BOLD(Field) and BOLD(Component).  Then, select
    BOLD(Displacement) and BOLD(x) for the field and the component,
    respectively.
        
    The option BOLD(where) determines whether to plot the contour at
    the displaced or original position.  Select BOLD(original).
    
    Leave the next five options as they are.  Click BOLD(OK) to display
    the contour plot."""
    ),
        
    TutoringItem(
    subject="More levels for contour",
    comments=
    """Admire the contour plot in the graphics window.  To add more
    contour levels, double-click on the BOLD(FilledContourDisplay)
    line in the the BOLD(Layers) list (or right-click on it and select
    BOLD(Edit), or select it and choose BOLD(Edit) in the window's
    BOLD(Layer) menu.)
    
    Look for the parameter BOLD(levels) and type in BOLD(21).  Click
    BOLD(OK).  The contour plot in the graphics window now has finer
    gradations of color.

    (The BOLD(nbins) parameter in the dialog for filled contour
    displays controls how the output values are computed within each
    element.  If the contours were curved, higher values of
    BOLD(nbins) would produce smoother contours, at the cost of more
    computation time.  Since this plot only contains straight lines,
    there's no point in increasing nbins.) """
    ),
        
    TutoringItem(
    subject="Values for the level",
    comments=

    """A color bar is displayed on the right-hand pane of the graphics
    window, called the BOLD(Contour Map).  It indicates the range of
    colors in the contour plot.  The actual value range for a given color on
    the BOLD(Contour Map) can be queried here.  Click on a color in
    the map and its value range will be displayed at the bottom of the
    contour map pane.""" ),
        
    TutoringItem(
    subject="Mesh info toolbox",
    comments=

    """While contour plots are effective in presenting an overall trend,
    if you are need precise values at specific locations, you can use
    the BOLD(Mesh Info) toolbox and the BOLD(Mesh Data Viewer).
    
    Open the BOLD(Mesh Info) toolbox in the graphics window.  The
    toolbox lets you extract information from elements and nodes.""" ),
        
    TutoringItem(
    subject="Querying node data",
    comments=

    """The first order of business in using the toolbox is to set the
    mode.  Enter node mode by clicking on the BOLD(Node) button at the
    top of the toolbox.
    
    Click the mouse inside the mesh in the graphics window.  The
    closest node is highlighted with a blue dot and all of its data,
    including its position and the values of its fields
    are displayed in the toolbox.  You may need to scroll the toolbox
    and/or expand the graphics window to see it all.
    """,
    ),
        
    TutoringItem(
    subject="Querying element data",
    comments=
        
    """Now, switch the toolbox to the element mode.  Notice an element is
    automatically selected.  It's the element containing the last
    mouse point from the previous mode.  Click on any other element to
    select it instead.

    Clicking on one of the nodes listed in the toolbox will highlight
    it in the graphics window.  Double-clicking on a node in the list
    will switch the toolbox back to node mode, with the given node
    selected.""",
    ),

    TutoringItem(
    subject="Querying data at interior points",
    comments=

    """The BOLD(Mesh Info) toolbox can tell you field values at nodes, but
    if you want the values at other locations you need to use a
    BOLD(Mesh Data Viewer).  It displays not only fields, but also any
    other quantity that can be computed on the BOLD(Analysis Page).

    At the bottom of the toolbox (you may need to scroll it) there's a
    button labelled BOLD(New Data Viewer).  Click it.

    You can open more than one data viewer at a time if necessary.
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

    Select an BOLD(Output) in the data viewer and click on the Mesh in
    the graphics window.  Observe the changes in the data viewer.
    
    """),

    TutoringItem(
    subject="Mesh cross section",
    comments=

    """ The BOLD(Mesh Cross Section) toolbox lets you save data from a
    contour plot along a path that you define on the mesh.
    
    Open this toolbox.  The BOLD(Source) frame shows what data is to
    be processed.  It will always be the topmost contour plot in the
    graphics window.
    
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

    """Click and drag the mouse on the graphics window canvas to create a
    path.  It will be displayed as a gray line on on the canvas.
    Using the BOLD(Rename) button in the BOLD(Cross Section) box in
    the toolbox, rename the new cross section to BOLD(MyCrossSection).
    Leave the BOLD(points) parameter set to BOLD(Line Points), which
    will space the output points evenly along the entire cross
    section.
    
    The destination of the extracted data can be either the message
    window or a file.  The pull-down menu at the top of the
    BOLD(Destination) box, currently displaying BOLD(<Message Window>)
    lists all recent destinations.  Add a file to the list by using
    the BOLD(New) button, just below it.

    Click the BOLD(Go!) button at the bottom of the toolbox.
    """),

    TutoringItem(
    subject="Mesh cross section - Final",
    comments=

    """Open the file you created and examine the results.  Or, if you
    didn't select a file, bring up the BOLD(Message Window).  The data
    is organized in columns, with a header at the top indicating what
    the columns mean (just like the headers produced by the
    BOLD(Analysis Page)).  For each data point, the distance along the
    cross-section, the fractional distance (between 0.0 and 1.0), and
    the location on the mesh are all given, along with the data
    itself.
    
    This is the end of the post-processing tutorial.
    """)


        ## TODO: Something about Named Analyses

        
    # TutoringItem(
    # subject="Analysis page",
    # comments=

    # """Move to the BOLD(Analysis) page in the main BOLD(OOF) window.
    # Here there are more general tools than in the BOLD(Mesh Cross
    # Section) toolbox.  These tools do not require that the data be
    # present in the graphics window, and they allow many other ways of
    # selecting the analysis domain.  In addition, this BOLD(Analysis)
    # page includes statistical operations, as well as direct
    # output."""),

    # TutoringItem(
    # subject="Analysis page - organization",

    # comments=

    # """

    # The BOLD(Output) pane determines what data will be used for the
    # analysis operation. 

    # The BOLD(Domain) pane determines where the data will come from.
    # In the previous example, a BOLD(Cross Section Domain) was
    # automatically selected by the toolbox.

    # The BOLD(Operation) pane determines how the data will be
    # processed.

    # The BOLD(Sampling) pane determines how data will be taken from the
    # domain.  The choices available in the BOLD(Sampling) pane depend
    # on what selections have been made in the BOLD(Domain) and
    # BOLD(Operation) panes.

    # Go to the next tutorial page for an example."""  ),

    # TutoringItem(
    # subject="Analysis page - Grid example",
    # comments=

    # """We will evaluate some data on an evenly-spaced BOLD(Grid) of points.

    # Begin with the BOLD(Output) pane.  Select BOLD(Field) and
    # BOLD(Derivative).  As soon as you select BOLD(Derivative), another
    # menu bar should appear.  Select BOLD(Component).  So far, we've
    # decided that we're going to output a derivative of a field
    # component.  The next three option menus are for specific choices.
    # Select BOLD(Displacement), BOLD(x), and BOLD(x) in order - it's a
    # normal strain in the BOLD(x)-direction.

    # Select BOLD(Entire Mesh) for the BOLD(Domain), and BOLD(Direct
    # Output) for the BOLD(Operation).  You can also select the comment
    # character to use in the output, and the separator character to use
    # between data items on a line.

    # Then select BOLD(Grid Points), and set BOLD(x_points) and
    # BOLD(y_points) both to BOLD(5), so we get a manageable amount of
    # data.  You may also elect to suppress certain columns from the
    # data output using the toggle buttons.  For now, retain all of the
    # data.
    
    # Set the controls for the heart of the message window and
    # give it a BOLD(Go).  Check the output in the message window."""),
    
    # TutoringItem(
    # subject="Analysis page - Final",
    # comments=

    # """You can try other BOLD(Operations) here, also.  Select
    # BOLD(Average) or BOLD(Standard Deviation), and hit BOLD(Go) again.

    # Other available BOLD(Domains) include pixel groups or
    # selections, element groups or selections, or, as we have already
    # seen from the toolbox, mesh cross-sections.

    # BOLD(Grid) samples on element or pixel groups or selections are
    # computed on a rectangular bounding box of the selection.
    # Statistical outputs are integrated over the elements, or summed
    # over the data from the centers of the pixels."""
    # ),

    ])
