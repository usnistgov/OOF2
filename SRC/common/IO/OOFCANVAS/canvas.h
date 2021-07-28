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
#include <string>
#include <vector>

namespace OOFCanvas {
  class OffScreenCanvas;
};

#include "canvaslayer.h"
#include "utility.h"


namespace OOFCanvas {

  class CanvasLayer;
  class CanvasItem;
  class SurfaceCreator;

  // OffScreenCanvas is the base class for GUICanvasBase, which is the
  // base class for PythonCanvas and Canvas.  OffScreenCanvas can be
  // used by itself, but can only display its contents by exporting to
  // an image format.

  class OffScreenCanvas {
  protected:
    CanvasLayer backingLayer;
    std::vector<CanvasLayer*> layers;
    // boundingBox is the bounding box, in user coordinates, of all of
    // the visible objects.
    Rectangle boundingBox;

    // centerOffset is the translation applied to the coordinates that
    // centers the image in the window if it's zoomed out so far that
    // it's smaller than the window.
    Coord centerOffset;

    // transform is used by the CanvasLayers when drawing their
    // CanvasItems to their ImageSurfaces.
    Cairo::Matrix transform;
    double ppu;	// pixels per unit. Converts user coords to device coords
    Cairo::Matrix findTransform(double, const Rectangle&, const ICoord) const;
    
    Color bgColor;
    double margin;
    Cairo::Antialias antialiasing;

    void setTransform(double);
    Cairo::Matrix getTransform(double);
    
    virtual void setWidgetSize(int, int) {}
    std::size_t layerNumber(const CanvasLayer*) const;
    void drawBackground(Cairo::RefPtr<Cairo::Context>) const;
    bool initialized;

    bool saveRegion(SurfaceCreator&, int, bool, const Coord&, const Coord&);

  public:
    OffScreenCanvas(double ppu);
    virtual ~OffScreenCanvas();

    ICoord desiredBitmapSize() const;
    
    double getPixelsPerUnit() const { return ppu; }
    double getFilledPPU(int, double, double) const;
    Rectangle findBoundingBox(double) const;

    // Coordinate system transformations
    const Cairo::Matrix &getTransform() const { return transform; }
    ICoord user2pixel(const Coord&) const;
    Coord pixel2user(const ICoord&) const;
    double user2pixel(double) const;
    double pixel2user(double) const;

    // This version just exists for calling from Python. Used when
    // converting GdkEvent coordinates to user coordinates.  Event
    // coords are floats.
    Coord *pixel2user(double, double) const;

    void setAntialias(bool);
    void setMargin(double);

    bool empty() const;		// Is anything drawn?

    void setBackgroundColor(double, double, double);

    CanvasLayer *newLayer(const std::string&);
    void deleteLayer(CanvasLayer*);
    CanvasLayer *getLayer(int i) const { return layers[i]; }
    CanvasLayer *getLayer(const std::string&) const;
    std::size_t nLayers() const { return layers.size(); }
    std::size_t nVisibleItems() const;

    void raiseLayer(int layer, int howfar); 
    void lowerLayer(int layer, int howfar);
    void raiseLayerToTop(int layer);
    void lowerLayerToBottom(int layer);
    void reorderLayers(const std::vector<CanvasLayer*>*);

    void clear();
    // Since the base class doesn't have anyplace to draw to, it's
    // draw method doesn't.
    virtual void draw() {}

    bool saveAsPDF(const std::string &filename, int, bool);
    bool saveRegionAsPDF(const std::string &filename, int, bool,
			 const Coord&, const Coord&);
    bool saveRegionAsPDF(const std::string &filename, int, bool,
			 const Coord*, const Coord*);
    bool saveAsPNG(const std::string &filename, int, bool);
    bool saveRegionAsPNG(const std::string &filename, int, bool,
			 const Coord&, const Coord&);
    bool saveRegionAsPNG(const std::string &filename, int, bool,
			 const Coord*, const Coord*);

    std::vector<CanvasItem*> clickedItems(double, double) const;
    std::vector<CanvasItem*> allItems() const;

    // Versions for swig return a new instance.
    std::vector<CanvasItem*> *clickedItems_new(double, double) const;
    std::vector<CanvasItem*> *allItems_new() const;

    friend class CanvasLayer;
    friend class CanvasItem;
  };				// OffScreenCanvas

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Utility classes used by OffScreenCanvas::saveRegion()
  
  class SurfaceCreator {
  protected:
    Cairo::RefPtr<Cairo::Surface> surface;
  public:
    virtual ~SurfaceCreator();
    virtual Cairo::RefPtr<Cairo::Surface> create(int, int) = 0;
  };

  class PDFSurfaceCreator : public SurfaceCreator {
  private:
    const std::string filename;
  public:
    PDFSurfaceCreator(const std::string &fname) : filename(fname) {}
    virtual Cairo::RefPtr<Cairo::Surface> create(int, int);
  };

  class ImageSurfaceCreator : public SurfaceCreator{
  public:
    ImageSurfaceCreator() {}
    virtual Cairo::RefPtr<Cairo::Surface> create(int, int);
    void saveAsPNG(const std::string&);
  };
  
};				// namespace OOFCanvas


#endif // OOFCANVAS_H

