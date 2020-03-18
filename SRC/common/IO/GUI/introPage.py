# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.common import oofversion
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import oofGUI
from gi.repository import Gtk
from gi.repository import Pango

from ooflib.common.IO.words import words
# words['Credits'], words['Disclaimer'], and words['Copyright']
# are defined in common.IO.

if config.dimension() == 2:
    name = "OOF2"
    pixels = "pixels"
elif config.dimension() == 3:
    name = "OOF3D"
    pixels = "voxels"

words['Welcome'] = """

                          Welcome to %(name)s!
                           Version %(version)s

%(name)s performs physical computations on microstructures, starting from a micrograph or other image of the microstructure.  The "Task" menu above brings up pages that lead you through the required steps.

Here is an extremely simplified description of the process, just to get you started.  For more details and examples, see the Tutorials in the Help menu and the manual, which may be found on-line at http://www.ctcms.nist.gov/~langer/oof2man.

First, create a Microstructure, which is %(name)s's basic data type. A Microstructure is a map which assigns Materials to %(pixels)s.  A Microstructure can contain Images.  You can select %(pixels)s in an Image and assign Materials to those %(pixels)s in the Microstructure.

After creating a Microstructure and assigning Materials to it, you need to create a Skeleton.  A Skeleton defines the geometry of a finite element mesh, specifying node positions and element edges only. It does not specify element type, equations, or boundary conditions. The Skeleton Modification tools allow you to adapt the Skeleton to the geometry of your Microstructure.  A Microstructure can contain more than one Skeleton.

The FE Mesh page creates a real finite element mesh from a Skeleton by specifying the types of elements to use.  A Skeleton can have more than one Mesh.

The Fields and Equations page determines what physical quantities are defined on the mesh (eg, Temperature) and what equations will be solved.  Fields must be defined before they are given values.  Fields must be activated before they can be solved for.

The Boundary Conditions page sets the boundary conditions (surprise!), and the Solver page finds the solution.  Finally, the Analysis and Boundary Analysis pages evaluate the results.

Graphics windows may be opened from the Windows menu.  They can be used to view Images, Microstructures, Skeletons, and Meshes, and to interactively operate on them.  The behavior of a graphics window is determined by the currently selected toolbox, which can be changed with the pull-down menu in the window's left pane. 

""" % {'name':name, 'version':oofversion.version, 'pixels':pixels}

## TODO MERGE: The second to last paragraph above isn't correct for OOF3D.

####################
   
class IntroPage(oofGUI.MainPage):
    def __init__(self):
        oofGUI.MainPage.__init__(self, name="Introduction", ordering=0,
                                 tip="Welcome to %s!"%name)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(vbox)
        scroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(scroll, "Scroll")
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
        vbox.pack_start(scroll, expand=True, fill=True, padding=0)
        self.textarea = Gtk.TextView(name="fixedfont")
        scroll.set_shadow_type(Gtk.ShadowType.IN)
        scroll.add(self.textarea)
        self.textarea.set_editable(False)
        self.textarea.set_cursor_visible(False)
        self.textarea.set_wrap_mode(Gtk.WrapMode.WORD)

        buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            homogeneous=True, spacing=2, border_width=2)
        vbox.pack_start(buttonbox, expand=False, fill=False, padding=0)

        self.labels = ['Welcome', 'Credits', 'Copyright', 'Disclaimer']
        self.buttons = [Gtk.ToggleButton(x) for x in self.labels]
        for button, label in zip(self.buttons, self.labels):
            buttonbox.pack_start(button, expand=True, fill=True, padding=0)
            gtklogger.setWidgetName(button, label)
            gtklogger.connect(button, 'clicked', self.buttonCB, label)

        self.buttons[0].set_active(1)

    def buttonCB(self, button, which):
        if button.get_active():
            for button, label in zip(self.buttons, self.labels):
                if label == which:
                    button.set_sensitive(False)
                else:
                    button.set_sensitive(True)
                    button.set_active(False)
            self.textarea.get_buffer().set_text(words[which])
            
IntroPage()

    
