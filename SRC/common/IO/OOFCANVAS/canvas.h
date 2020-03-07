// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFCANVAS_H
#define OOFCANVAS_H

#include <cairomm/cairomm.h>
#include <gtk/gtk.h>
#include <string>
#include <vector>
#ifdef PYTHON_OOFCANVAS
#include <Python.h>
#endif

namespace OOFCanvas {
  class CanvasBase;
  class Canvas;
#ifdef PYTHON_OOFCANVAS
  class CanvasPython;
#endif
};


#include "utility.h"


namespace OOFCanvas {

  class CanvasLayer;
  class CanvasItem;

  class CanvasBase {
  protected:
    GtkWidget *layout;
    CanvasLayer *backingLayer;
    std::vector<CanvasLayer*> layers;
    // boundingBox is the bounding box, in user coordinates, of all of
    // the visible objects.
    Rectangle boundingBox;

    // transform is used by the CanvasLayers when drawing their
    // CanvasItems to their ImageSurfaces.
    Cairo::Matrix transform;
    double ppu;	// pixels per unit. Converts user coords to device coords
    
    Color bgColor;

    void initSignals();
    
    void setTransform(double);
    void zoomAbout(double, const Coord&);

    int layerNumber(const CanvasLayer*) const;
    
    bool allowMotion;
    int lastButton;		// last mouse button pressed
    bool mouseInside;
    bool buttonDown;
    virtual void doCallback(const std::string&, int, int, int, bool, bool)
      const = 0;

    Cairo::Antialias antialiasing;

  public:
    CanvasBase(double ppu);
    virtual ~CanvasBase();
    virtual void destroy();

    // widthInPixels and heightInPixels return the size of the widget,
    // in pixels.
    int widthInPixels() const;
    int heightInPixels() const;
    ICoord layoutSize() const;
    ICoord boundingBoxSizeInPixels() const;
    
    double getPixelsPerUnit() const { return ppu; }
    void zoom(double);
    void zoomAbout(double x, double y, double factor);
    void zoomToFill();
    void center();

    // Coordinate system transformations
    const Cairo::Matrix &getTransform() const { return transform; }
    ICoord user2pixel(const Coord&) const;
    Coord pixel2user(const ICoord&) const;
    double user2pixel(double) const;
    double pixel2user(double) const;

    void antialias(bool);

    void removeMouseCallback();
    void allowMotionEvents(bool allow) { allowMotion = allow; }
    

    bool empty() const;		// Is anything drawn?

    void setBackgroundColor(double, double, double);
    void show();		// make gtk widgets visible

    CanvasLayer *newLayer(const std::string&);
    void deleteLayer(CanvasLayer*);
    CanvasLayer *getLayer(int i) const { return layers[i]; }
    CanvasLayer *getLayer(const std::string&) const;
    int nLayers() const { return layers.size(); }
    void draw();		// draws all modified layers
    void redraw();		// forces all layers to be redrawn

    void raiseLayer(int layer, int howfar); 
    void lowerLayer(int layer, int howfar);
    void raiseLayerToTop(int layer);
    void lowerLayerToBottom(int layer);

    void clear();

    // TODO: These callbacks should be private
    static void realizeCB(GtkWidget*, gpointer);
    void realizeHandler();
    static void allocateCB(GtkWidget*, GdkRectangle*, gpointer);
    virtual void allocateHandler();

    static void drawCB(GtkWidget*, Cairo::Context::cobject*, gpointer);
    void drawHandler(Cairo::RefPtr<Cairo::Context>);
    static void buttonCB(GtkWidget*, GdkEventButton*, gpointer);
    void mouseButtonHandler(GdkEventButton*);
    static void motionCB(GtkWidget*, GdkEventMotion*, gpointer);
    void mouseMotionHandler(GdkEventMotion*);

    // static void crossingCB(GtkWidget*, GdkEventCrossing*, gpointer);
    // void crossingEventHandler(GdkEventCrossing*);
    // static void focusCB(GtkWidget*, GdkEventFocus*, gpointer);

    GtkAdjustment *getHAdjustment() const;
    GtkAdjustment *getVAdjustment() const;

    std::vector<CanvasItem*> clickedItems(double, double) const;
    std::vector<CanvasItem*> allItems() const;

    // Versions for swig.
    std::vector<CanvasItem*> *clickedItems_new(double, double) const;
    std::vector<CanvasItem*> *allItems_new() const;

    friend class CanvasLayer;
    friend class CanvasItem;
  };

  //=\\=//

  // In C++, the OOFCanvas constructor creates the gtk Layout.

  typedef void (*MouseCallback)(const std::string&, double, double,
				int, bool, bool);

  class Canvas : public CanvasBase {
  protected:
    // mouse callback args are event type, position (in user coords),
    // button, state (GdkModifierType)
    MouseCallback mouseCallback;
    void *mouseCallbackData;
    virtual void doCallback(const std::string&, int, int, int, bool, bool)
      const;
  public:
    Canvas(double);
    virtual void destroy();
    
    // Second argument to setMouseCallback is extra data to be passed
    // through to the callback function.    
    void setMouseCallback(MouseCallback, void*);

    // gtk() is not exported to Python, since the GtkWidget* is not a
    // properly wrapped PyGTK object.
    GtkWidget *gtk() const { return layout; }
  };
  
  //=\\=//
#ifdef PYTHON_OOFCANVAS
  
  // In Python, the Gtk.Layout is created in Python and passed in to
  // the OOFCanvasPython constructor, and the callback functions are
  // Python functions.

  class CanvasPython : public CanvasBase {
  protected:
    PyObject *pyCanvas;
    PyObject *mouseCallback;
    PyObject *mouseCallbackData;
    PyObject *resizeCallback;
    PyObject *resizeCallbackData;
    virtual void doCallback(const std::string&, int, int, int, bool, bool)
      const;
    virtual void allocateHandler();
  public:
    CanvasPython(PyObject*, double);
    virtual void destroy();
    // Second argument to setMouseCallback is extra data to be passed
    // through to the callback function.
    void setMouseCallback(PyObject*, PyObject*);
    void setResizeCallback(PyObject*, PyObject*);
  };
#endif // PYTHON_OOFCANVAS

  void initializePyGTK();

};				// namespace OOFCanvas


#endif // OOFCANVAS_H

