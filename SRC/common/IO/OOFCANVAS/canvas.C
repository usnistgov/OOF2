// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "common/threadstate.h"
#include "canvas.h"
#include "canvasitem.h"
#include "canvaslayer.h"
#include <iostream>
#include <cassert>
#include <algorithm>

// TODO: If the layout size as computed from the bounding box is
// smaller than the window size in one or both directions, the image
// is drawn in the upper left corner of the window.  Can we center it?
	
// TODO: Save visible area or entire canvas to a file (pdf or png).

// TODO? Canvas::setMargin(double) to add some space when zooming to
// fill.  Not the same as the old OOFCanvas::set_margin.

// TODO: Layers shouldn't be replaced, but they can be "edited".  An
// edited layer is cleared of all of its contents and then passed to
// DisplayMethod::draw().

namespace OOFCanvas {

  OffScreenCanvas::OffScreenCanvas(double ppu)
    : backingLayer(nullptr),
      transform(Cairo::identity_matrix()),
      ppu(ppu),			// pixels per unit
      bgColor(1.0, 1.0, 1.0),
      antialiasing(Cairo::ANTIALIAS_DEFAULT)
  {}

  OffScreenCanvas::~OffScreenCanvas() {
    if(backingLayer)
      delete backingLayer;
    for(CanvasLayer *layer : layers)
      delete layer;
    layers.clear();
  }

  CanvasLayer *OffScreenCanvas::newLayer(const std::string &name) {
    // The OffScreenCanvas owns the CanvasLayers and is responsible
    // for deleting them.  Even if the layers are returned to Python,
    // Python does not take ownership.
    CanvasLayer *layer = new CanvasLayer(this, name);
    layers.push_back(layer);
    return layer;
  }

  void OffScreenCanvas::deleteLayer(CanvasLayer *layer) {
    auto iter = std::find(layers.begin(), layers.end(), layer);
    if(iter != layers.end())
      layers.erase(iter);
    delete layer;
  }

  void OffScreenCanvas::clear() {
    for(CanvasLayer *layer : layers)
      delete layer;
    layers.clear();
    draw();
  }

  bool OffScreenCanvas::empty() const {
    for(const CanvasLayer* layer : layers)
      if(!layer->empty())
	return false;
    return true;
  }

  int OffScreenCanvas::layerNumber(const CanvasLayer *layer) const {
    for(int i=0; i<layers.size(); i++)
      if(layers[i] == layer)
	return i;
    throw "Layer number out of range."; 
  }

  CanvasLayer *OffScreenCanvas::getLayer(const std::string &nm) const {
    for(CanvasLayer *layer : layers)
      if(layer->name == nm)
	return layer;
    throw "Layer not found.";
  }

  void OffScreenCanvas::raiseLayer(int which, int howfar) {
    assert(howfar >= 0);
    assert(which >= 0 && which < layers.size());
    CanvasLayer *moved = layers[which];
    int maxlayer = which + howfar; // highest layer that will be moved
    if(maxlayer >= layers.size())
      maxlayer = layers.size() - 1;
    for(int i=which; i < maxlayer; i++)
      layers[i] = layers[i+1];
    layers[maxlayer] = moved;
    draw();
  }
  
  void OffScreenCanvas::lowerLayer(int which, int howfar) {
    assert(howfar >= 0);
    assert(which >= 0 && which < layers.size());
    CanvasLayer *moved = layers[which];
    int minlayer = which - howfar; // lowest layer that will be moved
    if(minlayer < 0)
      minlayer = 0;
    for(int i=which; i > minlayer; i--)
      layers[i] = layers[i-1];
    layers[minlayer] = moved;
    draw();
  }

  void OffScreenCanvas::raiseLayerToTop(int which) {
    CanvasLayer *moved = layers[which];
    for(int i=which; i<layers.size()-1; i++)
      layers[i] = layers[i+1];
    layers[layers.size()-1] = moved;
    draw();
  }

  void OffScreenCanvas::lowerLayerToBottom(int which) {
    CanvasLayer *moved = layers[which];
    for(int i=which; i>0; i--) 
      layers[i] = layers[i-1];
    layers[0] = moved;
    draw();
  }

  void OffScreenCanvas::reorderLayers(const std::vector<CanvasLayer*> *neworder)
  {
    // reorderLayers should be called with a list of layers that is
    // the same as the existing list, but in a different order.
    layers = *neworder;		// vector copy
  }
  
  void OffScreenCanvas::setBackgroundColor(double r, double g, double b) {
    bgColor = Color(r, g, b);
  }

  void OffScreenCanvas::antialias(bool aa) {
    if(aa && antialiasing != Cairo::ANTIALIAS_DEFAULT) {
      antialiasing = Cairo::ANTIALIAS_DEFAULT;
    }
    else if(!aa && antialiasing != Cairo::ANTIALIAS_NONE) {
      antialiasing = Cairo::ANTIALIAS_NONE;
    }
    else
      return;
    for(CanvasLayer *layer : layers)
      layer->dirty = true;
    draw();
  }

  //=\\=//

  // OffScreenCanvas::transform is a Cairo::Matrix that converts from user
  // coordinates to device coordinates in the CanvasLayers'
  // Cairo::Contexts. It is *not* the transform that maps the
  // CanvasLayers to the gtk Layout, nor does it have anything to do
  // with scrolling.

  void OffScreenCanvas::setTransform(double scale) {
    // If no layers are dirty and ppu hasn't changed, don't do anything.
    bool newppu = (scale != ppu);
    bool layersChanged = false;
    if(!newppu) {
      for(CanvasLayer *layer : layers) {
	if(!layer->empty() && layer->dirty) {
	  layersChanged = true;
	  break;
	}
      }
    }
    if(!newppu && !layersChanged)
      return;
    
    // Find the bounding box of all drawn objects at the new scale
    Rectangle bbox;
    for(CanvasLayer *layer : layers) {
      if(!layer->empty()) {
	Rectangle rect = layer->findBoundingBox(scale, newppu);
	if(rect.initialized())
	  bbox.swallow(rect);
      }
    }
    
    if(!bbox.initialized()) {
      // Nothing is drawn.
      transform = Cairo::identity_matrix();
    }
    else {
      if(newppu  || !boundingBox.initialized() || bbox != boundingBox) {
	boundingBox = bbox;
	ppu = scale;
	guint w = ppu*boundingBox.width();
	guint h = ppu*boundingBox.height();
	setWidgetSize(w, h);
	Coord offset = ppu*boundingBox.lowerLeft();
	transform = Cairo::Matrix(ppu, 0., 0., -ppu, -offset.x, h+offset.y);

	// Force layers to be redrawn
	for(CanvasLayer *layer : layers) {
	  layer->dirty = true; 
	}
	//rubberBandLayer.dirty = true; // probably not necessary, but harmless
      }
    }
    backingLayer->clear();
  } // OffScreenCanvas::setTransform

  ICoord OffScreenCanvas::user2pixel(const Coord &pt) const {
    assert(backingLayer != nullptr);
    return backingLayer->user2pixel(pt);
  }

  Coord OffScreenCanvas::pixel2user(const ICoord &pt) const {
    assert(backingLayer != nullptr);
    return backingLayer->pixel2user(pt);
  }

  double OffScreenCanvas::user2pixel(double d) const {
    assert(backingLayer != nullptr);
    return backingLayer->user2pixel(d);
  }

  double OffScreenCanvas::pixel2user(double d) const {
    assert(backingLayer != nullptr);
    return backingLayer->pixel2user(d);
  }

  ICoord OffScreenCanvas::boundingBoxSizeInPixels() const {
    return ICoord(ppu*boundingBox.width(), ppu*boundingBox.height());
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Routines that can be called from a mouse callback to retrieve the
  // CanvasItem(s) at a given user coordinate.
  
  std::vector<CanvasItem*> OffScreenCanvas::clickedItems(double x, double y)
    const
  {
    Coord where(x,y);
    std::vector<CanvasItem*> items;
    for(const CanvasLayer *layer : layers) {
      if(layer->clickable) 
	layer->clickedItems(where, items);
    }
    return items;
  }

  std::vector<CanvasItem*> OffScreenCanvas::allItems() const {
    std::vector<CanvasItem*> items;
    for(const CanvasLayer *layer : layers)
      layer->allItems(items);
    return items;
  }

  // The *_new versions of clickedItems and allItems return their
  // results in a new vector, because swig works better that way.  If
  // we instead swig the above versions, without using new, swig will
  // make an extra copy of the vectors.
  std::vector<CanvasItem*> *OffScreenCanvas::clickedItems_new(double x,
							      double y)
    const
  {
    Coord where(x,y);
    std::vector<CanvasItem*> *items = new std::vector<CanvasItem*>;
    for(const CanvasLayer *layer : layers) 
      if(layer->clickable)
	layer->clickedItems(where, *items);
    return items;
  }

  std::vector<CanvasItem*> *OffScreenCanvas::allItems_new() const {
    std::vector<CanvasItem*> *items = new std::vector<CanvasItem*>;
    for(const CanvasLayer *layer : layers)
      layer->allItems(*items);
    return items;
  }

};				// namespace OOFCanvas


