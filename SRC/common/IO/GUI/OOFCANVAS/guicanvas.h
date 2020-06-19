// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFGUICANVAS_H
#define OOFGUICANVAS_H

#include "canvas.h"
#include "guicanvaslayer.h"
#include <gtk/gtk.h>

namespace OOFCanvas {
  class Canvas;
  class GUICanvasBase;
  class RubberBand;
  class WindowSizeCanvasLayer;
#ifdef OOFCANVAS_USE_PYTHON
#include <Python.h>
  class CanvasPython;
#endif
  
  // GUICanvasBase includes code that actually draws in a GtkWidget
  // and can interact with the user.  Other than this and its derived
  // classes, no OOFCanvas classes use Gtk.
  
  class GUICanvasBase : public OffScreenCanvas {
  protected:
    GtkWidget *layout;
    bool allowMotion;
    int lastButton;		// last mousebutton pressed
    bool buttonDown;

    void initSignals();
    // Mouse handling 
    static void buttonCB(GtkWidget*, GdkEventButton*, gpointer);
    void mouseButtonHandler(GdkEventButton*);
    static void motionCB(GtkWidget*, GdkEventMotion*, gpointer);
    void mouseMotionHandler(GdkEventMotion*);
    virtual void doCallback(const std::string&, const Coord&,
			    int, bool, bool) = 0;

    // Window creation
    static void realizeCB(GtkWidget*, gpointer);
    virtual void realizeHandler();

    // Window resizing
    static void allocateCB(GtkWidget*, GdkRectangle*, gpointer);
    void allocateHandler(GdkRectangle*);
    virtual void resizeHandler() = 0;

    static void drawCB(GtkWidget*, Cairo::Context::cobject*, gpointer);
    void drawHandler(Cairo::RefPtr<Cairo::Context>);

    virtual void setWidgetSize(int, int);
    
    // Machinery used to draw rubberbands quickly.
    WindowSizeCanvasLayer rubberBandLayer; // rubberband representation
    Cairo::RefPtr<Cairo::ImageSurface> nonRubberBandBuffer;
    RubberBand *rubberBand;	   // the rubberband, or nullptr
    Rectangle rubberBandBBox;	   // bounding box of the previous rubberband
    Coord mouseDownPt;		   // where the rubberband drawing started
    bool nonRubberBandBufferFilled;

    bool destroyed;

  public:
    GUICanvasBase(double ppu);
    virtual ~GUICanvasBase() {}

    // widgetWidth and widgetHeight return the size of the widget,
    // in pixels.
    int widgetWidth() const;
    int widgetHeight() const;

    void zoom(double);
    void zoomAbout(double x, double y, double factor);
    void zoomAbout(const Coord&, double factor);
    void zoomToFill();
    void center();

    Rectangle visibleRegion() const;

    void removeMouseCallback();
    void allowMotionEvents(bool allow) { allowMotion = allow; }

    void show();		// make gtk widgets visible
    void draw();		// draws all modified layers
    
    GtkAdjustment *getHAdjustment() const;
    GtkAdjustment *getVAdjustment() const;
    void getEffectiveAdjustments(double&, double&);

    void setRubberBand(RubberBand*);
    void removeRubberBand();
  };				// GUICanvasBase

  //=\\=//

  // In C++, the OOFCanvas constructor creates the gtk Layout.

  typedef void (*MouseCallback)(const std::string&, double, double,
				int, bool, bool);
  typedef void (*ResizeCallback)(void*);

  class Canvas : public GUICanvasBase {
  protected:
    // mouse callback args are event type, position (in user coords),
    // button, state (GdkModifierType)
    MouseCallback mouseCallback;
    void *mouseCallbackData;
    virtual void doCallback(const std::string&, const Coord&, int, bool, bool);
    ResizeCallback resizeCallback;
    void *resizeCallbackData;
    virtual void resizeHandler();
  public:
    Canvas(double);
    virtual ~Canvas();
    virtual void destroy();
    // Second argument to setMouseCallback is extra data to be passed
    // through to the callback function.    
    void setMouseCallback(MouseCallback, void*);
    void setResizeCallback();

    // gtk() is not exported to Python, since the GtkWidget* is not a
    // properly wrapped PyGTK object.
    GtkWidget *gtk() const { return layout; }
  };
  
  //=\\=//
#ifdef OOFCANVAS_USE_PYTHON
  
  // In Python, the Gtk.Layout is created in Python and passed in to
  // the OOFCanvasPython constructor, and the callback functions are
  // Python functions.

  class PythonCanvas : public GUICanvasBase {
  private:
    bool destroyed;
  protected:
    PyObject *pyCanvas;
    PyObject *mouseCallback;
    PyObject *mouseCallbackData;
    PyObject *resizeCallback;
    PyObject *resizeCallbackData;
    virtual void doCallback(const std::string&, const Coord&, int, bool, bool);
    virtual void resizeHandler();
  public:
    PythonCanvas(PyObject*, double);
    virtual ~PythonCanvas();
    virtual void destroy();
    // Second argument to setMouseCallback is extra data to be passed
    // through to the callback function.
    void setMouseCallback(PyObject*, PyObject*);
    void setResizeCallback(PyObject*, PyObject*);
  };
#endif	// OOFCANVAS_USE_PYTHON

  void initializePyGTK();

};				// namespace OOFCanvas

#endif	// OOFGUICANVAS_H

