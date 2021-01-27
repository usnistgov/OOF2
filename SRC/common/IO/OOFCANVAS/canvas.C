// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "common/tostring.h"
#include "common/threadstate.h"
#include "canvas.h"
#include "canvasitem.h"
#include "canvaslayer.h"
#include <iostream>
#include <cassert>
#include <algorithm>
#include <math.h>

// TODO? Layers shouldn't be replaced, but they can be "edited".  An
// edited layer is cleared of all of its contents and then passed to
// DisplayMethod::draw().

namespace OOFCanvas {

  OffScreenCanvas::OffScreenCanvas(double ppu)
    : backingLayer(this, "<backinglayer>"),
      transform(Cairo::identity_matrix()),
      ppu(ppu),
      bgColor(1.0, 1.0, 1.0),
      margin(0.0),
      antialiasing(Cairo::ANTIALIAS_DEFAULT),
      initialized(false)
  {
    assert(ppu > 0.0);
    backingLayer.setClickable(false);
    setTransform(ppu);
  }

  OffScreenCanvas::~OffScreenCanvas() {
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
  
  int OffScreenCanvas::nVisibleItems() const {
    int n = 0;
    for(CanvasLayer *layer : layers)
      if(layer->visible) {
	n += layer->size();
      }
    return n;
  }
  
  void OffScreenCanvas::setBackgroundColor(double r, double g, double b) {
    bgColor = Color(r, g, b);
  }

  void OffScreenCanvas::drawBackground(Cairo::RefPtr<Cairo::Context> ctxt) const
  {
    ctxt->save();
    // One might think that one should call ctxt->reset_clip() here,
    // to ensure that the background is painted over the entire
    // canvas.  But doing that will paint the background over the
    // entire window.  Just be sure to call drawBackground before any
    // other drawing operations reset the clip region.
    ctxt->set_source_rgb(bgColor.red, bgColor.green, bgColor.blue);
    ctxt->paint();
    ctxt->restore();
  }

  void OffScreenCanvas::setAntialias(bool aa) {
    if(aa && antialiasing != Cairo::ANTIALIAS_DEFAULT) {
      antialiasing = Cairo::ANTIALIAS_DEFAULT;
    }
    else if(!aa && antialiasing != Cairo::ANTIALIAS_NONE) {
      antialiasing = Cairo::ANTIALIAS_NONE;
    }
    else
      return;
    for(CanvasLayer *layer : layers) {
      layer->rebuild();
    }
    draw();
  }

  void OffScreenCanvas::setMargin(double m) {
    margin = m;
  }

  //=\\=//

  Rectangle OffScreenCanvas::findBoundingBox(double ppu) const {
    Rectangle bb;
    for(const CanvasLayer *layer : layers)
      if(!layer->empty())
	bb.swallow(layer->findBoundingBox(ppu));
    return bb;
  }

  //=\\=//

  // OffScreenCanvas::transform is a Cairo::Matrix that converts from user
  // coordinates to device coordinates in the CanvasLayers'
  // Cairo::Contexts. It is *not* the transform that maps the
  // CanvasLayers to the gtk Layout, nor does it have anything to do
  // with scrolling.        

  // findTransform() computes the transform without setting or using
  // any state data from the Canvas.  setTransform() uses
  // findTransform() and state data to set OffScreenCanvas::transform.

  Cairo::Matrix OffScreenCanvas::findTransform(
					double peepeeyou, const Rectangle &bbox,
					const ICoord pxlsize)
    const
  {
    // The bounding box for the objects that are actually drawn is
    // smaller than the bitmap and centered in it.
    double bbw = peepeeyou*bbox.width();
    double bbh = peepeeyou*bbox.height();
    double deltax = 0.5*(pxlsize.x - bbw);
    double deltay = 0.5*(pxlsize.y - bbh);
    Coord offset = peepeeyou*bbox.lowerLeft() + Coord(-deltax, deltay);
    return Cairo::Matrix(peepeeyou, 0., 0., -peepeeyou,
			 -offset.x, bbh+offset.y);
  }
			     

  void OffScreenCanvas::setTransform(double scale) {
    assert(scale > 0.0);
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
    if(initialized && !newppu && !layersChanged &&
       backingLayer.bitmapSize() == desiredBitmapSize())
      {
	return;
      }

    // Find the bounding box of all drawn objects at the new scale
    Rectangle bbox;
    for(CanvasLayer *layer : layers) {
      if(!layer->empty()) {
	bbox.swallow(layer->findBoundingBox(scale, newppu));
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
	ICoord bitmapsz = desiredBitmapSize();
	setWidgetSize(bitmapsz.x, bitmapsz.y); // is a no-op for OffScreenCanvas

	transform = findTransform(ppu, boundingBox, bitmapsz);

	// Force layers to be redrawn
	for(CanvasLayer *layer : layers) {
	  layer->dirty = true; 
	}
      }
    }

    backingLayer.rebuild();
    initialized = true;
  } // OffScreenCanvas::setTransform

  ICoord OffScreenCanvas::user2pixel(const Coord &pt) const {
    return backingLayer.user2pixel(pt);
  }

  Coord OffScreenCanvas::pixel2user(const ICoord &pt) const {
    return backingLayer.pixel2user(pt);
  }

  Coord *OffScreenCanvas::pixel2user(double px, double py) const {
    return backingLayer.pixel2user(px, py);
  }

  double OffScreenCanvas::user2pixel(double d) const {
    return backingLayer.user2pixel(d);
  }

  double OffScreenCanvas::pixel2user(double d) const {
    return backingLayer.pixel2user(d);
  }

  ICoord OffScreenCanvas::desiredBitmapSize() const {
    return ICoord(ppu*boundingBox.width()*(1+margin),
		  ppu*boundingBox.height()*(1+margin));
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // getFilledPPU() and helper routines used to calculate the optimal
  // ppu for a given size canvas.  Used by GUICanvas::zoomToFill().
  // At one point this was also used when saving the canvas to a file,
  // and might be used that way again, which is why it's here and not
  // in guicanvas.C.

  // pixSize() computes the size in pixels that the window would have
  // to be at the given ppu in order to contain a bounding box from
  // bbmin to bbmax and a bunch of objects spanning user coords from
  // refLo to refHi with pixel extensions pLo and pHi.  X and Y are
  // handled separately. pixSize() just does one of them at a time.

  static double pixSize(double ppu,
			const std::vector<double> &pLo,
			const std::vector<double> &refLo,
			const std::vector<double> &pHi,
			const std::vector<double> &refHi)
  {
    // CanvasItem i extends from refLo[i] to refHi[i] in physical
    // units, but extends past that by pLo[i] and pHi[i] in pixel
    // units.
    // The total size is
    //    max(ppu*refHi_i + pHi_i) - min(ppu*refLo_i - pLo_i)
    double maxHi = -std::numeric_limits<double>::max();
    double minLo = std::numeric_limits<double>::max();
    int iHi = -1;
    int iLo = -1;
    for(unsigned int i=0; i<pLo.size(); i++) {
      double xHi = ppu*refHi[i] + pHi[i];
      if(xHi > maxHi) {
	maxHi = xHi;
	iHi = i;
      }
      double xLo = ppu*refLo[i] - pLo[i];
      if(xLo < minLo) {
	minLo = xLo;
	iLo = i;
      }
    }
    return maxHi - minLo;
  }

  //=\\=//

  // getFilledPPU() uses optimalPPU() to compute the ppu in one
  // direction.

  static double optimalPPU(double w0, 
			   const std::vector<double> &pLo,
			   const std::vector<double> &refLo, 
			   const std::vector<double> &pHi,
			   const std::vector<double> &refHi)
  {
    // Item i extends from
    //     xLo[i] = ppu*(refLo[i]-C) - pLo[i]
    // to
    //     xHi[i] = ppu*(refHi[i]-C) + pHi[i]
    // where the origin C is arbitrary and ignored.
    // The total width is 
    //     w(ppu) = max(xHi[i]) - min(xLo[i])
    // We need to solve w(ppu) = w0.
    // w is a piecewise linear function of ppu, so we find the
    // critical ppu values at which it changes slope, and look for a
    // solution in each interval.

    assert(pLo.size() == refLo.size() &&
	   pHi.size() == refHi.size() &&
	   pLo.size() == pHi.size());
    unsigned int n = pLo.size();

    double maxRefHi = -std::numeric_limits<double>::max();
    double minRefLo = std::numeric_limits<double>::max();
    int iMax, iMin;
    
    // ppus at which the slope of max(ppu*xmax+pmax) or
    // min(ppu*xmin-pmin) changes.
    std::vector<double> criticalPPUs;
    criticalPPUs.reserve(2*n*(n-1));
    criticalPPUs.push_back(0.0);

    // TODO: Is there a way to do this that isn't o(N^2)?
    
    for(unsigned int i=0; i<n; i++) {
      if(refHi[i] > maxRefHi) {
	maxRefHi = refHi[i];
	iMax = i;
      }
      if(refLo[i] < minRefLo) {
	minRefLo = refLo[i];
	iMin = i; 
      }
      for(unsigned int j=i+1; j<n; j++) {
	// Find the ppu at which items i and j extend equally far down.
	// ppu*refLo[i] - pLo[i] = ppu*refLo[j] - pLo[j]
	if(refLo[i] != refLo[j]) {
	  double ppu = (pLo[i] - pLo[j])/(refLo[i] - refLo[j]);
	  if(ppu > 0)
	    criticalPPUs.push_back(ppu);
	}
	// Find the ppu at which items i and j extend equally far up.
	// ppu*refHi[i] + pHi[i] = ppu*refHi[j] + pHi[j]
	if(refHi[i] != refHi[j]) {
	  double ppu = (pHi[j] - pHi[i])/(refHi[i] - refHi[j]);
	  if(ppu > 0)
	    criticalPPUs.push_back(ppu);
	}
      }
    }

    std::sort(criticalPPUs.begin(), criticalPPUs.end());

    double ppuMax = 0.0;	// maximum ppu that gives a solution
    for(unsigned int i=0; i<criticalPPUs.size()-1; i++) {
      // Interval in which W is a linear function of ppu
      double ppuA = criticalPPUs[i];
      double ppuB = criticalPPUs[i+1];
      if(ppuA != ppuB) {
	// Find value of ppu that gives width W = totalPixels
	double wA = pixSize(ppuA, pLo, refLo, pHi, refHi);
	double wB = pixSize(ppuB, pLo, refLo, pHi, refHi);
	if((wA - w0) * (wB - w0) <= 0.0) {
	  double ppu = ppuA + (w0 - wA)*(ppuB - ppuA)/(wB - wA);
	  if(ppuA <= ppu && ppu <= ppuB && ppu > ppuMax) {
	    ppuMax = ppu;
	  }
	}
      }
    }

    // The interval from the largest criticalPPU to infinity has to be
    // examined too.  As ppu goes to infinity, only the largest refHi
    // and smallest refLo contribute.
    // w0 = (ppu*refHi[iMax] + pHi[iMax]) - (ppu*refLo[iMin] - pLo[iMin])
    double ppu = (w0 - pHi[iMax] - pLo[iMin])/(refHi[iMax] - refLo[iMin]);
    if(ppu > criticalPPUs.back() && ppu > ppuMax)
      ppuMax = ppu;
    
    return ppuMax;
  } // optimalPPU

  //=\\=//

  // If the target surface is xsize by ysize pixels, compute the ppu
  // that fills the surface.  This is tricky, because some objects
  // have fixed sizes in device units and therefore change their size
  // when the ppu is changed.  n is the number of visible items being
  // drawn.
  
  double OffScreenCanvas::getFilledPPU(int n, double xsize, double ysize)
    const
  {
    if(n == 0)
      return 1.0;
    
    // Pixel extents of each item from its reference point.
    std::vector<double> pxLo, pxHi, pyLo, pyHi;
    // User coordinates of the upper and lower reference points of
    // each object in each direction.
    std::vector<double> xLo, yLo, xHi, yHi;
    pxLo.reserve(n);
    pxHi.reserve(n);
    pyLo.reserve(n);
    pyHi.reserve(n);
    xLo.reserve(n);
    xHi.reserve(n);
    yLo.reserve(n);
    yHi.reserve(n);

    for(CanvasLayer *layer : layers) {
      if(layer->visible) {
	for(CanvasItem *item : layer->items) {
	  const Rectangle &bbox0 = item->findBareBoundingBox();
	  xHi.push_back(bbox0.xmax());
	  xLo.push_back(bbox0.xmin());
	  yHi.push_back(bbox0.ymax());
	  yLo.push_back(bbox0.ymin());
	  double pxlo, pxhi, pylo, pyhi;
	  item->pixelExtents(pxlo, pxhi, pyhi, pylo);
	  pxLo.push_back(pxlo);
	  pxHi.push_back(pxhi);
	  pyHi.push_back(pyhi);
	  pyLo.push_back(pylo);
	}
      }
    }
    double ppu_x = optimalPPU(xsize, pxLo, xLo, pxHi, xHi);
    double ppu_y = optimalPPU(ysize, pyLo, yLo, pyHi, yHi);
    // Pick the smaller of ppu_x and ppu_y, so that the entire image
    // is visible in both directions.
    double newppu = ppu_x < ppu_y ? ppu_x : ppu_y;
    return newppu;
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

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Save the whole canvas or a region of it as a pdf.  The saveAs
  // methods return true if they were successful.
  
  // TODO: Add saveAsPNG, saveRegionAsPNG.  If ImageMagick is being
  // used, we could save in other formats as well, presumably.

  bool OffScreenCanvas::saveAsPDF(const std::string &filename,
				  int maxpix, bool drawBG)
  {
    // Saving the whole image requires that we compute the ppu as if
    // we're zooming to fill.
    double newppu = getFilledPPU(nVisibleItems(), maxpix, maxpix); // margin?
    Rectangle bb = findBoundingBox(newppu);
    return saveRegionAsPDF(filename, maxpix, drawBG,
			   bb.lowerLeft(), bb.upperRight());
  }

  bool OffScreenCanvas::saveRegionAsPDF(
				const std::string &filename,
				int maxpix, // no. of pixels in max(w, h)
				bool drawBG,
				const Coord &pt0, const Coord &pt1)
  {
    if(nVisibleItems() == 0) {
      return false;
    }

    Rectangle region(pt0, pt1); // ensures that upperRight[i] >= lowerLeft[i]

    // Compute pixel size of region and make a PdfSurface to fit.
    Coord imgsize = region.upperRight() - region.lowerLeft();
    double peepeeyou = maxpix/(imgsize.x > imgsize.y ? imgsize.x : imgsize.y);
    Coord psize = peepeeyou*imgsize;
    ICoord pxlsize(ceil(psize.x), ceil(psize.y));
    
    auto surface = Cairo::PdfSurface::create(filename, pxlsize.x, pxlsize.y);
    cairo_t *ct = cairo_create(surface->cobj());
    auto pdfctxt = Cairo::RefPtr<Cairo::Context>(new Cairo::Context(ct, true));
    pdfctxt->set_antialias(antialiasing);

    if(drawBG)
      drawBackground(pdfctxt);

    auto layersurf = Cairo::Surface::create(surface,
					    Cairo::CONTENT_COLOR_ALPHA,
					    pxlsize.x, pxlsize.y);
    cairo_t *lt = cairo_create(layersurf->cobj());
    auto lctxt = Cairo::RefPtr<Cairo::Context>(new Cairo::Context(lt, true));

    Cairo::Matrix transf = findTransform(peepeeyou, region, pxlsize); 
    lctxt->set_matrix(transf);
    Coord deviceOrigin(0,0);
    lctxt->device_to_user(deviceOrigin.x, deviceOrigin.y);
    Coord offset = deviceOrigin - region.upperLeft();
    lctxt->translate(offset.x, offset.y);

    for(CanvasLayer *layer : layers) {
      if(!layer->empty() && layer->visible) {
	lctxt->save();
	lctxt->set_operator(Cairo::OPERATOR_CLEAR);
	lctxt->paint();
	lctxt->restore();

	layer->redrawToContext(lctxt);

	pdfctxt->set_source(layersurf, 0, 0);
	pdfctxt->paint_with_alpha(layer->alpha);
      }
    }
    // Not sure if these are needed.
    // pdfctxt->show_page();
    // surface->finish();
    return true;
  }

  bool OffScreenCanvas::saveRegionAsPDF(
				const std::string &filename,
				int maxpix, bool drawBG,
				const Coord *pt0, const Coord *pt1)
  {
    return saveRegionAsPDF(filename, maxpix, drawBG, *pt0, *pt1);
  }
    
};				// namespace OOFCanvas


