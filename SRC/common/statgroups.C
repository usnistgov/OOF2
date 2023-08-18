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

#include "common/activearea.h"
#include "common/cmicrostructure.h"
#include "common/coord.h"
#include "common/progress.h"
#include "common/random.h"
#include "common/statgroups.h"
#include "common/tostring.h"
#include "common/ooferror.h"

#include <algorithm>
#include <map>
#include <set>


static const ICoord directions[] = {ICoord(-1,-1), ICoord(-1,0), ICoord(-1, 1),
				    ICoord(0, -1), ICoord(0, 1),
				    ICoord(1, -1), ICoord(1, 0), ICoord(1, 1)};

// TODO: StatBurn -- add neighboring pixels if they're within n
// deviations of the mean of the burned region.  Update the mean and
// deviation as pixels are added.

struct SortDists {
  bool operator()(const PixelDistribution *a, const PixelDistribution *b) {
    return a->npts() > b->npts();
  }
};

// void PixelDistribution::remove_noupdate(const ICoord &pxl) {
//   // TODO: Use a std::set instead of a std::vector?
//   auto iter = std::find(pxls.begin(), pxls.end(), pxl);
//   pxls.erase(iter);
// }

std::vector<std::set<ICoord>> PixelDistribution::contiguousPixels() const {
  // Split the pixels in the PixelDistribution into contiguous sets.
  std::vector<std::set<ICoord>> sets;
  
  std::set<ICoord> sourcePixels(pxls.begin(), pxls.end());
  while(!sourcePixels.empty()) {
    std::vector<ICoord> activeSites; // pixels being considered for inclusion
    std::set<ICoord> targetPixels;   // pixels already included

    // Pick a starting point
    auto iter = sourcePixels.begin();
    activeSites.push_back(*iter);
    sourcePixels.erase(iter);
    
    while(!activeSites.empty()) {
      ICoord active = activeSites.back();
      activeSites.pop_back();
      targetPixels.insert(active);
      for(const ICoord &dir : directions) {
	ICoord nbr = active + dir;
	if(sourcePixels.count(nbr) == 1) {
	  // Neighboring pixel is in the source set
	  activeSites.push_back(nbr); // make neighbor active
	  sourcePixels.erase(nbr); // don't make it active again later
	}
      }
    } // end while there are active sites
    sets.emplace_back(std::move(targetPixels));
    
  } // end loop over source pixels
  return sets;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Given a pixel, count the number of neighboring pixels in each
// PixelDistribution.
std::map<PixelDistribution*, int> countNeighbors(
				 SimpleArray2D<PixelDistribution*> &dists,
				 const ICoord &pt)
{
  std::map<PixelDistribution*, int> counts;
  for(const ICoord &dir : directions) {
    ICoord nbr = pt + dir;
    // If nbr is within the array bounds and the array is non-null there
    if(dists.contains(nbr) && dists[nbr] != nullptr)
	counts[dists[nbr]] += 1;
  }
  return counts;
}

bool isBdyPixel(SimpleArray2D<PixelDistribution*> &dists, const ICoord &pt) {
  for(const ICoord &dir : directions) {
    ICoord nbr = pt + dir;
    if(dists.contains(nbr) && dists[nbr] != dists[pt])
      return true;
  }
  return false;
}

// Given a bunch of PixelDistributions, return an array saying which
// distribution a pixel is in, if the distribution contains more then
// minsize pixels.

SimpleArray2D<PixelDistribution*> getDistArray(
		       const ICoord &mssize,
		       const std::vector<PixelDistribution*> &pixelDists,
		       int minsize)
{
  SimpleArray2D<PixelDistribution*> dists(mssize);
  for(PixelDistribution *pixdist : pixelDists) {
    if(pixdist->npts() >= minsize) {
      for(const ICoord &pt : pixdist->pixels()) {
	dists[pt] = pixdist;
      }
    }
  }
  return dists;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

static void cleanUp_(std::vector<PixelDistribution*> &dists) {
  for(PixelDistribution *dist : dists)
    delete dist;
  dists.clear();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// This is sort of like autogroups, but statistical.  It assumes that
// groups are formed from distributions of pixel values, stored in
// PixelDistribution objects, consisting of a set of pixels (ICoords)
// and information about the mean and variance of the pixel values.
// There are different subclasses of PixelDistribution for different
// types of pixel values (eg, color or orientation).  If a pixel value
// is within delta standard deviations of the mean value of an
// existing distribution, it is added to the distribution.  If it's
// within delta deviations of more than one distribution, it's added
// to the most compatible group (measured in terms of number of
// deviations from the mean).  After adding a pixel, the mean and
// deviation of the distribution are updated.  If after updating, the
// means of two distributions are within gamma deviations of one
// another, the distributions are merged.
// 
// After the initial distributions are formed, each is split into its
// connected components -- sets of contiguous pixels. If any
// contiguous set contains fewer than minsize pixels, it's absorbed
// into the neighboring distributions (those with more than minsize
// pixels).  Pixels in the small sets that neighbor the large
// distribution are put into the most compatible neighboring
// distribution, creating new neighbors of that distribution,
// repeating until all pixels in the small set are absorbed.

// If the caller does not want to force groups to be formed from
// contiguous pixels, the large pixel sets that were split off from
// each PixelDistribution are merged back into one PixelDistribution
// before the small sets are absorbed.  Forcing groups to be made of
// contiguous pixels produces results sort of like a repeated
// application of the Burn method, which selects sets of contiguous
// similar pixels.  Not requiring contiguity is like repeatedly
// selecting all pixels with a given color.

// At the end, a PixelGroup is created for each PixelDistribution and
// stored in the Microstructure.

// The arguments are:
//   microstructure:   the microstructure
//   factory:  creates the right type of PixelDistribution
//   delta: pixels w/in this many deviations are added to a group
//   gamma: groups with means w/in this many deviations are merged
//   minsize: groups smaller than this are merged with neighboring groups
//   contiguous: true==> each resulting group will be contiguous,
//               false==> resulting groups may have disjoint regions
//   name_template: Name for the new groups.  "%n" will be replaced by a number.
//   clear: whether or not to remove pixels from a pre-existing group before
//          adding the new ones.

const std::string *statgroups(CMicrostructure *microstructure,
			      const PixelDistributionFactory *factory,
			      double delta,
			      double gamma,
			      int minsize,
			      bool contiguous,
			      const std::string &name_template, bool clear)
{
  // TODO: This routine is too long.  Break it up.
  
  Progress *progress =
    dynamic_cast<DefiniteProgress*>(findProgress("AutoGroup"));

  std::vector<PixelDistribution*> pixelDists;
  std::string groupname;	// name of last group created
  DummyDistribution bdyPixelMarker; // marks the bdy pixels in dists.

  try {
    ICoord mssize(microstructure->sizeInPixels());
    const ActiveArea *activeArea = microstructure->getActiveArea();
    const std::vector<ICoord> shuffledPix = microstructure->shuffledPix();
    unsigned int npix = shuffledPix.size();
    unsigned int nChecked = 0;

    for(const ICoord &pixel : shuffledPix) { // Loop over all pixels
      if(progress->stopped()) {
	cleanUp_(pixelDists);
	return new std::string("");
      }

      // std::cerr << "statgroups: pixel=" << pixel << " *************" 
      // 		<< std::endl;
      
      // Find the existing pixel group that this pixel fits best.

      // TODO: Use a hash table.  When there are a lot of groups in a
      // large image this is very slow.  Hash table will have to be
      // implemented in the PixelDistribution subclasses.
      double bestSigma2 = std::numeric_limits<double>::max();
      PixelDistribution *bestDist = nullptr;
      for(PixelDistribution *pd : pixelDists) {
	double s2 = pd->deviation2(pixel);
	if(s2 < bestSigma2) {
	  bestSigma2 = s2;
	  bestDist = pd;
	}
      }

      // std::cerr << "statgroups: bestDist=" << bestDist << std::endl;
    
      if(bestDist == nullptr || bestSigma2 > delta*delta) {
	// No suitable group was found.  This may be the first pass
	// through the loop, or the pixel value is too far from existing
	// groups.  Create a new group.
	pixelDists.push_back(factory->newDistribution(pixel));
	// std::cerr << "statgroups: new distribution " << pixelDists.back()
	// 	  << " " << pixelDists.back()->stats() << std::endl;
      }
      else {
	// An appropriate group was found.  Add the pixel to it.
	bestDist->add(pixel);
	// std::cerr << "statgroups: added to dist " << bestDist
	// 	  << " " << bestDist->stats() << std::endl;

	// Adding the pixel changed the group's mean and
	// deviation. Check to see if this distribution should now be
	// merged with another one. If it should, keep checking for more
	// mergers with the newly modified group.
	// TODO: Adding a pixel might have reduced the group's
	// deviation.  Is it possible that other pixels should now be
	// ejected from the group?

	PixelDistribution *modifiedDist = bestDist; // recently modified group
	do {
	  // Look for a group whose mean differs from this group's mean
	  // by fewer than gamma standard deviations (using either
	  // group's deviation).
	  double sigma2Best = gamma*gamma;
	  PixelDistribution *distBest = nullptr;
	  for(PixelDistribution *pd : pixelDists) {
	    if(pd != modifiedDist) { // pointer comparison
	      // PixelDistribution::deviation returns the number of
	      // deviations (squared) between the means of two
	      // distributions, using this's current deviation.
	      double dev1 = pd->deviation2(modifiedDist);
	      double dev2 = modifiedDist->deviation2(pd);
	      double mindev = dev1 < dev2 ? dev1 : dev2;
	      if(mindev <= sigma2Best) {
		sigma2Best = mindev;
		distBest = pd;
	      }
	    
	    } // end if pd != modifiedDist
	  }   // end loop over existing groups pd 

	  if(distBest != nullptr) {
	    // Merge modifiedDist into distBest, which becomes the new
	    // modifiedDist.  Delete the old one and remove it from
	    // pixelDists.
	    distBest->merge(modifiedDist);
	    auto iter = std::find(pixelDists.begin(), pixelDists.end(),
				  modifiedDist);
	    assert(iter != pixelDists.end());
	    pixelDists.erase(iter);
	    delete modifiedDist;
	    modifiedDist = distBest;
	  }
	  else
	    modifiedDist = nullptr;
	
	} while(modifiedDist != nullptr);	// end do
      
      } // end if an appropriate group was found
      progress->setMessage(
		   tostring(nChecked) + "/" + tostring(npix) + " pixels, "
		   + tostring(pixelDists.size()) + " groups");
      progress->setFraction(double(nChecked++)/npix);
    } // end loop over pixels

    // At this point, every pixel is in a PixelDistribution containing
    // similar pixels.  The pixels in each PixelDistribution do not
    // necessarily form a contiguous set.
  
    // -----------

    // If we want only contiguous groups, or if we want to eliminate
    // small groups (or small disconnected regions of large groups) we
    // have to split the PixelDistributions into contiguous pieces.
    
// #ifdef DEBUG
//     std::cerr << "statgroups: before splitting, PixelDistributions are:" 
// 	      << std::endl;
//     for(const PixelDistribution *pd : pixelDists) {
//       std::cerr << "    " << pd << " n=" << pd->npts() << " mean="
// 		<< pd->stats() << std::endl;
//     }
// #endif // DEBUG

    if(contiguous || minsize > 0) {
      // Rebuild the PixelDistributions in pixelDists and store the
      // new ones in pixelDists2.
      std::vector<PixelDistribution*> pixelDists2;
      for(PixelDistribution *pixDist : pixelDists) {
	std::vector<std::set<ICoord>> pixSets = pixDist->contiguousPixels();

	// If we do want discontiguous groups, merge the larger pieces
	// back together, leaving the small ones out so that they can
	// be merged into a nearby group in the minsize step, next.
	if(!contiguous) {
	  std::set<ICoord> bigSet;
	  for(std::set<ICoord> &pixset : pixSets) {
	    if(pixset.size() >= minsize) {
	      bigSet.insert(pixset.begin(), pixset.end());
	      pixset.clear();
	    }
	  }
	  if(!bigSet.empty())
	    pixSets.push_back(bigSet);
	}
	
	for(auto &pixset : pixSets) {
	  if(!pixset.empty()) {
	    PixelDistribution *pixDist2 = pixDist->clone(pixset);
	    pixelDists2.push_back(pixDist2);
	  }
	}
      }	// end loop over PixelDistributions, pixelDists

      // Delete the old PixelDistributions and use the new ones from
      // now on.
      cleanUp_(pixelDists);
      pixelDists = pixelDists2;

    } // end if contiguous or minsize > 0

// #ifdef DEBUG
//     std::cerr << "statgroups: after splitting, PixelDistributions are:" 
// 	      << std::endl;
//     for(const PixelDistribution *pd : pixelDists) {
//       std::cerr << "    " << pd << " n=" << pd->npts() << " mean="
// 		<< pd->stats() << std::endl;
//     }
// #endif // DEBUG

    // -----------
  
    if(minsize > 0) {
      // Get rid of distributions containing fewer than minsize pixels
      // by attaching them to neighboring distributions.
    
      // First check to see if there are any distributions bigger than
      // minsize.  If there aren't, do what?
      int largest = 0;
      for(PixelDistribution *pd : pixelDists) {
	if(pd->npts() > largest)
	  largest = pd->npts();
      }
      if(largest < minsize) {
	throw ErrUserError("minsize is too small: largest group size is " 
			   + tostring(largest));
      }

      Progress *prog2 =
	dynamic_cast<DefiniteProgress*>(getProgress("Merging small groups",
						    DEFINITE));
      try {
	// dists[x] is the PixelDistribution containing ICoord x if it's
	// not in one of the small distributions. 
	SimpleArray2D<PixelDistribution*> dists =
	  getDistArray(mssize, pixelDists, minsize);

	// Get the pixels immediately neighboring the big distributions.
	// Those pixels are in the small distributions.  Also compute
	// the total size of the small distributions, ntodo.
	std::vector<ICoord> bdyPixels;
	int ntodo = 0;
	int nSmallGroups = 0;
	int g = 0;
	for(PixelDistribution *pixDist : pixelDists) {
	  prog2->setMessage("Checking group " + tostring(++g) + "/" +
			    tostring(pixelDists.size()));
	  prog2->setFraction(g/(double) pixelDists.size());
	  if(pixDist->npts() < minsize) {
	    ntodo += pixDist->npts();
	    nSmallGroups++;
	    for(const ICoord &pt : pixDist->pixels()) {
	      for(const ICoord &dir : directions) {
		ICoord nbr = pt + dir;
		if(microstructure->contains(nbr)
		   && activeArea->isActive(nbr)
		   && dists[nbr] != nullptr
		   && dists[nbr] != &bdyPixelMarker)
		  {
		    bdyPixels.push_back(pt);
		    // The boundary pixels are marked with
		    // &bdyPixelMarker in dists.  This distinguishes
		    // them from pixels that haven't yet been added to
		    // bdyPixels, which are still 0 in dists.
		    dists[pt] = &bdyPixelMarker;
		    break;
		  }
	      } // end loop over neighbor directions
	    }   // end loop over pixels in the small distribution

	    // Clear the small distribution so no group will be made from
	    // it.
	    pixDist->clear_noupdate();
	
	  } // end if it's a small distribution
	}	  // end loop over all distributions

	// Randomize the neighboring pixels.
	OOFRandomNumberGenerator r;
	oofshuffle(bdyPixels.begin(), bdyPixels.end(), r);

	// For each pixel in bdyPixels, examine which big distributions it
	// is next to. If it's next to only one, add it to that
	// distribution. If it's next to more than one, add it to the one
	// that its value is closest to, statistically.  Remove the pixel
	// from bdyPixels and add its neighbors, if they're not already in
	// it and aren't already in a big group.
	int ndone = 0;
	while(!bdyPixels.empty()) {
	  if(prog2->stopped())
	    break;
	  prog2->setMessage("Checking pixel " + tostring(ndone) + "/" +
			    tostring(ntodo));
	  prog2->setFraction(ndone/(double) ntodo);
	  ICoord pxl = bdyPixels.back();
	  bdyPixels.pop_back();
	  // Get the PixelDistributions that contain neighbors of pxl.
	  std::map<PixelDistribution*, int> counts = countNeighbors(dists, pxl);
// #ifdef DEBUG
// 	  std::cerr << "statgroups: counts=" << std::endl;
// 	  for(auto iter=counts.begin(); iter!=counts.end(); ++iter) {
// 	    std::cerr << "statgroups:    ";
// 	    if(iter->first == &bdyPixelMarker)
// 	      std::cerr << "bdy";
// 	    else
// 	      std::cerr << iter->first;
// 	    std::cerr << ", " << iter->second << std::endl;
// 	  }
// #endif // DEBUG
	
	  // mostDists contains the PixelDistributions containing the
	  // most pixels neighboring pxl.  There may be more than one
	  // with the same number of neighbors.
	  std::set<PixelDistribution*> mostDists;
	  int nMost = 0;
	  for(auto iter=counts.begin(); iter!=counts.end(); ++iter) {
	    if(iter->first != &bdyPixelMarker) {
	      if(iter->second > nMost) {
		mostDists.clear();
		mostDists.insert(iter->first);
		nMost = iter->second;
	      } 
	      else if(iter->second == nMost) {
		mostDists.insert(iter->first);
	      }
	    } // end if not the bdyPixelMarker distribution
	  }   // end loop over distributions of neighbor pixels
	  assert(!mostDists.empty());
	
	  PixelDistribution *bestDist = nullptr;
	  if(mostDists.size() == 1) {
	    // It there's only one neighboring distribution, use it.
	    bestDist = *mostDists.begin();
	  }
	  else {
	    // More than one distribution has the same number of
	    // neighbors. Choose the one that the pixel fits best.
	    double bestVariance = std::numeric_limits<double>::max();
	    for(PixelDistribution *pixDist : mostDists) {
	      double var = pixDist->deviation2(pxl);
	      if(var < bestVariance) {
		bestVariance = var;
		bestDist = pixDist;
	      }
	    }
	  }
	  assert(bestDist != nullptr && bestDist != &bdyPixelMarker);
	  // Add the pixel to the best neighboring distribution
	  bestDist->add(pxl);
	  dists[pxl] = bestDist;
	  // If the newly added pixel has neighbors that aren't in
	  // distributions, add them to the list of pixels to be examined.
	  for(const ICoord &dir : directions) {
	    ICoord nbr = pxl + dir;
	    if(microstructure->contains(nbr) && 
	       dists[nbr] == nullptr &&
	       activeArea->isActive(nbr))
	      {
		bdyPixels.push_back(nbr);
		dists[nbr] = &bdyPixelMarker;
	      }
	  }
	  prog2->setMessage(tostring(ndone) + "/" + tostring(ntodo));
	  prog2->setFraction(ndone/(double) ntodo);
	  ndone++;
	}	// end while bdyPixels is not empty
      }
      catch (...) {
	prog2->finish();
	throw;
      }
      prog2->finish();
    } // end if minsize > 0
  
    // -----------

    // Sort the groups from largest to smallest before naming them.
    std::sort(pixelDists.begin(), pixelDists.end(), SortDists());
    // How many groups are non-empty?
    int nonEmpty = 0;
    for(PixelDistribution *pixDist : pixelDists) {
      if(pixDist->npts() == 0)
	break;
      nonEmpty++;
    }
    assert(nonEmpty > 0);

    // Create a real PixelGroup for each PixelDistribution, and delete
    // the PixelDistributions.
    int groupNo = 0;
    int maxDigits = tostring(nonEmpty-1).size(); // for padding with 0
    for(PixelDistribution *pd : pixelDists) {
      if(pd->npts() > 0) {
	// Create the name for the group by replacing '%n' in the
	// template with a number.  Pad the number with 0's on the left
	// so that the groups appear in numerical order in the GUI
	// (which sorts them alphabetically).
	groupname = name_template;
	std::string::size_type pos = groupname.find("%n", 0);
	if(pos != std::string::npos) {
	  std::string g = tostring(groupNo++);
	  int nzeros = maxDigits - g.size();
	  groupname = groupname.replace(pos, 2, std::string(nzeros, '0') + g);
	}
	bool newness = false;
	PixelGroup *grp = microstructure->getGroup(groupname, &newness);
	if(clear)
	  grp->clear();
	grp->addWithoutCheck(&pd->pixels());

// #ifdef DEBUG
// 	std::cerr << "statgroups: " << groupname << " n=" << pd->npts()
// 		  << " " << pd->stats() << std::endl;
// #endif // DEBUG
      } // end if PixelDistribution is not empty
    }
  } // end try
  catch (...) {
    cleanUp_(pixelDists);
    throw;
  }
  cleanUp_(pixelDists);
  
  return new std::string(groupname);
}


