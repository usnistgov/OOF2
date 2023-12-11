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
    tip="Tools for viewing and analyzing a solution.",
    discussion="""<para>
    This tutorial discusses post-processing tools for viewing and
    analyzing a soltion.
    </para>""",
    lessons = [
      
    TutoringItem(
    subject="Introduction",
    comments=
"""OOF2 provides various post-processing tools for viewing and analyzing a solution.  This tutorial provides a brief discussion of these tools. """
    ),

    TutoringItem(
    subject="Example Mesh",
    comments=
"""First, load an example Mesh. Locate the file <tt>cyallow.mesh</tt> within the share/oof2/examples directory in your OOF2 installation.  From the <b>File</b> menu, choose <b>Load/Data</b>, and in the file selector, select <b>cyallow.mesh</b>.  Click <b>OK</b> to load the mesh.

This is the same simple mesh that you generated if you worked through the <b>Simple Example</b> tutorial.""",
    ),

    TutoringItem(
    subject="The Analysis Page",
    comments=
"""Open the the <b>Analysis Page</b> in the main OOF2 window.  This page lets you compute various quantities in a number of ways at your choice of locations.  We will compute the average and standard deviation of the stress over the entire mesh.
    
There are four main panes in this window.  The panes can be resized by dragging the dividers between them, and they can also be scrolled.  You may need to resize the window at times to make the panes fully visible.

You must specify five things for each analysis operation:

<b>Output</b>: What data will be extracted from the mesh.  Outputs can be <b>Scalar</b> or <b>Aggregate</b> (anything that's not a simple scalar).  Scalar examples include the components and invariants of fields and fluxes.  Aggregate examples include entire field and flux objects.  

Select <b>Aggregate</b>, and set the top pull-down menu to <b>Flux</b>, and the one below that to <b>Value</b>.  The menu below that lets you choose which Flux you'll be computing the value of. This Mesh only defines one, <b>Stress</b>.

<b>Domain</b>: Where on the Mesh the data will be computed.  Set it to <b>Entire Mesh</b>.

<b>Operation</b>: What to do with the data.  Set it to <b>Average and Deviation</b>.

<b>Sampling</b>: How the data will be be extracted fro the domain. The choices available in the <b>Sampling</b> pane depend on what selections have been made in the <b>Domain</b> and <b>Operation</b> panes.  Leave it set to <b>Element Set</b>, so that the average will be computed by integrating over elements.

<b>Destination</b>: Where to send the result.  Leave it set to <b>&lt;Message Window&gt;</b>.

Click <b>Go</b>.

Expand the Message Window to see the results.  There will be many comments (lines beginning with #), and one line of data.  The comments identify the contents of the data line.  """
    ),

    TutoringItem(
    subject="Output to a File",
    comments=
"""In this step we'll evaluate the x derivative of the x displacement on a grid of points and write the results to a file.  (Because the example mesh contains a uniform strain, the results won't be very interesting, but that's not the point.)

In the <b>Output</b> pane on the <b>Analysis Page</b>, select <b>Scalar</b> mode.  Then set the top pull-down menu in the pane to <b>Field</b>, and the one below it to <b>Derivative</b>, and the one below that to <b>Component</b>.  Notice that the pull-down menus listed in the lower part of the <b>Output</b> pane change as you set the upper ones.  The upper ones set the kind of output, and the lower ones set the parameters that determine exactly which output you'll get.  Set <b>field</b> to <b>Displacement</b> and set both <b>derivative</b> and <b>component</b> to <b>x</b>.

In the <b>Domain</b> pane, choose <b>Entire Mesh</b>.  This choice requires no parameters, so there are no pull-down menus below it.

In the <b>Operation</b> pane, select <b>Direct Output</b>.  The data will be extracted from the domain but will not be processed further.

In the <b>Sampling</b> pane, select <b>Grid Points</b>.  To get a manageable amount of data for this tutorial, set both <b>x_points</b> and <b>y_points</b> to <b>5</b>.  If <b>show_x</b> and <b>show_y</b> are checked, the x and y coordinates of the points will be included in the output.

In the <b>Destination</b> pane at the bottom of the window, notice that the pull down menu contains only <b>&lt;Message Window&gt;</b>.  To add a file to the list, click the <b>New...</b> button and select a file.  The new file will appear as an option for the Destination.

Click <b>Go</b>. """
    ),

    TutoringItem(
    subject="More about Output to a File",
    comments=
"""In a text editor or other utility, outside of OOF2, open the file that you just created.  There are comment lines at the top, each beginning with '#'.  (This default can be changed with the <b>Settings/Output Formatting/Comment Character</b> menu in the main OOF2 window.)  The comments describe the settings of the settings in the <b>Output</b>, <b>Operation</b>, <b>Domain</b>, and <b>Sampling</b> panes.  Below that is a description of the contents of each column in the data and the time that the data was computed (in case you were solving a time dependent problem).  Below that is the data itself.

If you want to compute more output, you can send it to the same file or select a different one.  If you use the same file, you can tell where the new data starts because new header lines will be printed.  If instead you want to overwrite the old data, use the <b>Rewind</b> button in the <b>Destination</b> pane before pressing <b>Go</b>. """
    ),

    TutoringItem(
    subject="Boundary analysis",
    comments=
"""Move to the <b>Boundary Analysis</b> page.  This page is like the <b>Analysis</b> page, but it only computes two things: averages of fields and integrals of fluxes along boundaries.

Select <b>right</b> from the <b>Boundaries</b> pane, and select <b>Integrate Flux</b> in the <b>Boundary Operation</b> pane.  The only available flux in this mesh is Stress.

At the bottom of the page, set the destination to <b>Message Window</b> and click <b>Go</b> button.
    
The message window contains the usual header information and the data: the sum of the reaction forces in the x and y directions along the right side of the mesh. """
    ),
        
    TutoringItem(
    subject="Contour Plots in the Graphics window",
    comments=
"""OOF2 can also display contour plots of any scalar quantity that can be computed in the <b>Analysis Page</b>.

Open a graphics window to display the mesh.

Display the mesh by selecting <b>New</b> from the <b>Layer</b> menu. Set <b>category</b> to <b>Mesh</b>, <b>what</b> to "cyallow.png/skeleton/mesh" and <b>how</b> to <b>Element Edges</b> with <b>where</b>=<b>original</b>.  Click <b>OK</b>. """
    ),

    TutoringItem(
    subject="New layer",
    comments=
"""We'll start with a filled contour of the displacement in the x-direction.  The mesh is subjected to an uniaxial tension in the x-direction and the strain is uniform, so the displacement contours should be vertical lines.

Open the new layer dialog box again, using the <b>Layer/New</b> dialog box or by right-clicking in the layer list.  <b>category</b> and <b>what</b> should still be set to the values you used in the previous step.

Select <b>Filled Contour</b> in the pull-down menu at the top of the <b>how</b> box. 

Any scalar quantity that you can compute on the <b>Analysis</b> page can be made into a contour plot.  In the <b>what</b> option block, select <b>Field</b> and <b>Component</b>.  Then, select <b>Displacement</b> and <b>x</b> for the field and the component, respectively.
        
The option <b>where</b> determines whether to plot the contour at the displaced or original position.  Select <b>original</b>.
    
Leave the next five options as they are.  Click <b>OK</b> to display the contour plot."""
    ),
        
    TutoringItem(
    subject="More levels for contour",
    comments=
"""Admire the contour plot in the graphics window.  To add more contour levels, double-click on the <b>FilledContourDisplay</b> line in the the <b>Layers</b> list (or right-click on it and select <b>Edit</b>, or select it and choose <b>Edit</b> in the window's <b>Layer</b> menu.)
    
Look for the parameter <b>levels</b> and type in <b>21</b>.  Click <b>OK</b>.  The contour plot in the graphics window now has finer gradations of color.

(The <b>nbins</b> parameter in the dialog for filled contour displays controls how the output values are computed within each element.  If the contours were curved, higher values of <b>nbins</b> would produce smoother contours, at the cost of more computation time.  Since this plot only contains straight lines, there's no point in increasing nbins.) """
    ),
        
    TutoringItem(
    subject="Values for the level",
    comments=
"""A color bar is displayed on the right-hand pane of the graphics window, called the <b>Contour Map</b>.  It indicates the range of colors in the contour plot.  The actual value range for a given color on the <b>Contour Map</b> can be queried here.  Click on a color in the map and its value range will be displayed at the bottom of the contour map pane."""
    ),
        
    TutoringItem(
    subject="Mesh info toolbox",
    comments=
"""While contour plots are effective in presenting an overall trend, if you are need precise values at specific locations, you can use the <b>Mesh Info</b> toolbox and the <b>Mesh Data Viewer</b>.
    
Open the <b>Mesh Info</b> toolbox in the graphics window.  The toolbox lets you extract information from elements and nodes."""
    ),
        
    TutoringItem(
    subject="Querying node data",
    comments=
"""The first order of business in using the toolbox is to set the mode.  Enter node mode by clicking on the <b>Node</b> button at the top of the toolbox.
    
Click the mouse inside the mesh in the graphics window.  The closest node is highlighted with a blue dot and all of its data, including its position and the values of its fields are displayed in the toolbox.  You may need to scroll the toolbox and/or expand the graphics window to see it all. """,
    ),
        
    TutoringItem(
    subject="Querying element data",
    comments=
"""Now, switch the toolbox to the element mode.  Notice an element is automatically selected.  It's the element containing the last mouse point from the previous mode.  Click on any other element to select it instead.

Clicking on one of the nodes listed in the toolbox will highlight it in the graphics window.  Double-clicking on a node in the list will switch the toolbox back to node mode, with the given node selected.""",
    ),

    TutoringItem(
    subject="Querying data at interior points",
    comments=
"""The <b>Mesh Info</b> toolbox can tell you field values at nodes, but if you want the values at other locations you need to use a <b>Mesh Data Viewer</b>.  It displays not only fields, but also any other quantity that can be computed on the <b>Analysis Page</b>.

At the bottom of the toolbox (you may need to scroll it) there's a button labelled <b>New Data Viewer</b>.  Click it.

You can open more than one data viewer at a time if necessary. Each data viewer window displays the value of one output quantity. The upper part of the window, marked <b>Source</b>, determines what is computed and where.  (If the window is too large, you can collapse the <b>Source</b> region with by clicking the triangle in the upper left, and then resize the window.) The <b>Data</b> box at the bottom of the window shows the result.
    
Any output that can be computed in the OOF2 <b>Analysis</b> page can be examined in a data viewer window.  The output is evaluated at the position given in the Source region.  You can change the position by typing in the <b>x</b> or <b>y</b> boxes, or by clicking the mouse in the graphics window.  If you don't want the position and data to change when you click the mouse, check <b>Space</b> in the <b>Freeze</b> box at the bottom.

Normally, the data in the viewer window updates when the Mesh changes or when you select a new point.  The <b>Space</b> and <b>Time</b> checkboxes in the <b>Freeze</b> pane prevent the data from changing, if you need to compare values at different places or times.

Select an <b>Output</b> in the data viewer and click on the Mesh in the graphics window.  Observe the changes in the data viewer. """
    ),

    TutoringItem(
    subject="Mesh cross section",
    comments=
"""The <b>Mesh Cross Section</b> toolbox lets you save data from a contour plot along a path that you define on the mesh.
    
Open this toolbox.  The <b>Source</b> frame shows what data is to be processed.  It will always be the topmost contour plot in the graphics window.
    
A path is created by clicking and dragging the mouse.  (At this time, only straight line paths can be created.) The paths are automatically added to a list of cross sections and can be managed through the buttons in the <b>Cross Section</b> frame of the toolbox.
    
Click <b>Next</b> for more instruction.""",
    ),
        
    TutoringItem(
    subject="Mesh cross section - Continued",
    comments=
"""Click and drag the mouse on the graphics window canvas to create a path.  It will be displayed as a gray line on on the canvas. Using the <b>Rename</b> button in the <b>Cross Section</b> box in the toolbox, rename the new cross section to <b>MyCrossSection</b>. Leave the <b>points</b> parameter set to <b>Line Points</b>, which will space the output points evenly along the entire cross section.
    
The destination of the extracted data can be either the message window or a file.  The pull-down menu at the top of the <b>Destination</b> box, currently displaying <b>&lt;Message Window&gt;</b> lists all recent destinations.  Add a file to the list by using the <b>New</b> button, just below it.

Click the <b>Go!</b> button at the bottom of the toolbox. """
    ),

    TutoringItem(
    subject="Mesh cross section - Final",
    comments=
"""Open the file you created and examine the results.  Or, if you didn't select a file, bring up the <b>Message Window</b>.  The data is organized in columns, with a header at the top indicating what the columns mean (just like the headers produced by the <b>Analysis Page</b>).  For each data point, the distance along the cross-section, the fractional distance (between 0.0 and 1.0), and the location on the mesh are all given, along with the data itself.
    
This is the end of the post-processing tutorial. """
    )


        ## TODO: Something about Named Analyses

        
    # TutoringItem(
    # subject="Analysis page",
    # comments=

    # """Move to the <b>Analysis</b> page in the main <b>OOF</b> window.
    # Here there are more general tools than in the <b>Mesh Cross
    # Section</b> toolbox.  These tools do not require that the data be
    # present in the graphics window, and they allow many other ways of
    # selecting the analysis domain.  In addition, this <b>Analysis</b>
    # page includes statistical operations, as well as direct
    # output."""),

    # TutoringItem(
    # subject="Analysis page - organization",

    # comments=

    # """

    # The <b>Output</b> pane determines what data will be used for the
    # analysis operation. 

    # The <b>Domain</b> pane determines where the data will come from.
    # In the previous example, a <b>Cross Section Domain</b> was
    # automatically selected by the toolbox.

    # The <b>Operation</b> pane determines how the data will be
    # processed.

    # The <b>Sampling</b> pane determines how data will be taken from the
    # domain.  The choices available in the <b>Sampling</b> pane depend
    # on what selections have been made in the <b>Domain</b> and
    # <b>Operation</b> panes.

    # Go to the next tutorial page for an example."""  ),

    # TutoringItem(
    # subject="Analysis page - Grid example",
    # comments=

    # """We will evaluate some data on an evenly-spaced <b>Grid</b> of points.

    # Begin with the <b>Output</b> pane.  Select <b>Field</b> and
    # <b>Derivative</b>.  As soon as you select <b>Derivative</b>, another
    # menu bar should appear.  Select <b>Component</b>.  So far, we've
    # decided that we're going to output a derivative of a field
    # component.  The next three option menus are for specific choices.
    # Select <b>Displacement</b>, <b>x</b>, and <b>x</b> in order - it's a
    # normal strain in the <b>x</b>-direction.

    # Select <b>Entire Mesh</b> for the <b>Domain</b>, and <b>Direct
    # Output</b> for the <b>Operation</b>.  You can also select the comment
    # character to use in the output, and the separator character to use
    # between data items on a line.

    # Then select <b>Grid Points</b>, and set <b>x_points</b> and
    # <b>y_points</b> both to <b>5</b>, so we get a manageable amount of
    # data.  You may also elect to suppress certain columns from the
    # data output using the toggle buttons.  For now, retain all of the
    # data.
    
    # Set the controls for the heart of the message window and
    # give it a <b>Go</b>.  Check the output in the message window."""),
    
    # TutoringItem(
    # subject="Analysis page - Final",
    # comments=

    # """You can try other <b>Operations</b> here, also.  Select
    # <b>Average</b> or <b>Standard Deviation</b>, and hit <b>Go</b> again.

    # Other available <b>Domains</b> include pixel groups or
    # selections, element groups or selections, or, as we have already
    # seen from the toolbox, mesh cross-sections.

    # <b>Grid</b> samples on element or pixel groups or selections are
    # computed on a rectangular bounding box of the selection.
    # Statistical outputs are integrated over the elements, or summed
    # over the data from the centers of the pixels."""
    # ),

    ])
