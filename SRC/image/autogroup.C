// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/cmicrostructure.h"
#include "common/coord.h"
#include "common/oofomp.h"
#include "common/pixelgroup.h"
#include "common/progress.h"
#include "common/switchboard.h"
#include "common/tostring.h"
#include "image/oofimage.h"
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <unordered_map>


// TODO: OpenMP pragmas have been enclosed in #ifdef HAVE_OPENMP
// blocks so that we control when they're used.  On Ubuntu,
// ImageMagick is built with -fopenmp, and OOF2 gets it c++ flags from
// ImageMagick, so it's being built with OpenMP whether we want it or
// not.  Also, there are some bugs in autogroup that are making it
// crash when running with OpenMP.

// CColor packet2color(const Magick::PixelPacket &packet) {
//   using namespace Magick;
//   double scale = 1./MaxRGB;
//   return CColor(packet.red*scale, packet.green*scale, packet.blue*scale);
// }

// Replace all instances of a by b within source and return the
// result.  Used when constructing group names.
std::string substitute(const std::string &source, const std::string &a,
		       const std::string &b)
{
  std::string result = source;
  std::string::size_type pos = result.find(a, 0);
  while(pos != std::string::npos) {
    result = result.replace(pos, a.size(), b);
    pos = result.find(a, pos+a.size());
  }
  return result;
}

// Calculate the hash value of a CColor object
struct CColorHash {
  size_t operator()(const CColor& cc) const {
    return std::hash<double>()(cc.getRed())
      ^ (std::hash<double>()(cc.getGreen()) << 1)
      ^ (std::hash<double>()(cc.getBlue()) << 2);
  }
};

// This function is called when two CColor objects have
// the same value.
struct CColorEq {
  bool operator() (const CColor& lcc, const CColor& rcc) const {
    return lcc.compare(rcc, 0.000001);
  }
};

typedef std::vector<ICoord> PixelList;
typedef std::unordered_map<const CColor, PixelList,
                           CColorHash, CColorEq> ColorListMap;

std::vector<std::string> *autogroup(CMicrostructure *ms, OOFImage *image,
				    const std::string &name_template)
{
  ICoord size(ms->sizeInPixels());
  const size_t width = size(0);
  const size_t height = size(1);
  const double npixels = height*width; // double, used as denominator
  size_t ndone = 0;	    // number of pixels that have been checked
  size_t nlists = 0;	    // number of pixel lists created by all threads

  std::vector<ColorListMap> colorlists;

  Progress *progress=dynamic_cast<DefiniteProgress*>(findProgress("AutoGroup"));

  // // OOFImage::operator[] doesn't appear to be threadsafe, due to some
  // // ImageMagick problem.  But getting data from the PixelPacket is
  // // faster anyway.
  // const Magick::PixelPacket *packet = image->pixelPacket();

  size_t i, j;
#ifdef HAVE_OPENMP
#pragma omp parallel shared(colorlists, /*packet,*/ progress, ndone) private(i, j)
#endif // HAVE_OPENMP
  {
    // Each thread has its own ColorListMap called 'colorlist', but
    // they're all stored in a global 'colorlists' array so that they
    // can be accessed from other threads later.
#ifdef HAVE_OPENMP
    #pragma omp single
#endif // HAVE_OPENMP
    {
      progress->setMessage("Categorizing pixels");
      colorlists.resize(omp_get_num_threads());
    }
    ColorListMap &colorlist = colorlists[omp_get_thread_num()];

    // Put pixels with the same color into lists.
#ifdef HAVE_OPENMP
    #pragma omp for
#endif // HAVE_OPENMP
    for(j=0; j<height; ++j) {
      for(i=0; i<width && !progress->stopped(); ++i) {
        ICoord pxl(i, j);
        // Direct lookup in the ImageMagick image is not thread safe somehow.
	const CColor color((*image)[pxl]);
        // This is uglier but faster and also apparently thread safe.
        //const CColor color(packet2color(packet[i + j*width]));
        colorlist[color].push_back(pxl); // add this pixel to corresponding list
      }
#ifdef HAVE_OPENMP
      #pragma omp atomic
#endif // HAVE_OPENMP
	  ndone += width;
      progress->setFraction(ndone/npixels);
    } 
  } // end omp parallel

  typedef std::unordered_map<const CColor, PixelGroup*,
                             CColorHash, CColorEq> ColorGroupMap;

  // Create pixel groups in the Microstructure for each Color.  This
  // has to be done serially.

  ColorGroupMap colorgroupmap;
  vector<CColor> colors;
  std::vector<std::string> *groupnames = new std::vector<std::string>;

  progress->setMessage("Creating groups");
  progress->setFraction(0.0);
  ndone = 0;
  // How many sets of pixels have been created in all threads?  We
  // need to know this so that we can update the progress bar.
  for(unsigned int i=0; i<colorlists.size(); i++)
    nlists += colorlists[i].size();

  // Loop over all the pixel lists created by all the threads to find
  // the unique colors in the image.  Each thread may have created a
  // separate list of pixels for every color.
  int grpcount = 0;

  for(size_t ic=0; ic<colorlists.size() && !progress->stopped(); ++ic) {
    ColorListMap &colorlist = colorlists[ic];
    for(ColorListMap::iterator i=colorlist.begin(); i!=colorlist.end(); ++i) {
      const CColor &color = (*i).first;
      // Have we already found the group for this color?
      ColorGroupMap::iterator findgrp = colorgroupmap.find(color);
      if(findgrp == colorgroupmap.end()) { // Didn't find it.
        std::string grpname = name_template;
        grpname = substitute(grpname, "%c", color.name());
        grpname = substitute(grpname, "%n", to_string(grpcount++));
        bool newness = false;
        PixelGroup *grp = ms->getGroup(grpname, &newness); // create group
	groupnames->push_back(grpname);
        colorgroupmap[color] = grp;
        colors.push_back(color);
      }
      progress->setFraction(++ndone/(double)nlists);
    }
  }

  // Add pixels to groups.  Each group is handled by only one thread,
  // but different groups can be done simultaneously by different
  // threads.

  ndone = 0;
  progress->setFraction(0.0);
  progress->setMessage("Adding pixels to groups");

#ifdef HAVE_OPENMP
  #pragma omp parallel for shared(colors, colorlists, colorgroupmap) \
                           private(i)
#endif // HAVE_OPENMP
  for (i = 0; i < colors.size(); ++i) {
    if (!progress->stopped()) {
      const CColor color = colors[i];
      PixelGroup *grp = colorgroupmap[color];
      for (auto& list : colorlists) {
        if (list.find(color) != list.end())
          grp->add(&list[color]);
      }
      #pragma omp atomic 
      ++ndone;
      progress->setFraction(ndone / (double)colorgroupmap.size());
    }
  }

  return groupnames;
} 
