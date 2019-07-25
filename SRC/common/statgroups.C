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
#include "common/progress.h"
#include "common/random.h"
#include "common/statgroups.h"

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
    if(dists.contains(nbr))	// if nbr is in bounds
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
}

const std::string *statgroups(CMicrostructure *microstructure,
			      const PixelDistributionFactory *factory,
			      double delta,
			      double gamma,
			      // int despeckle,
			      int minsize,
			      const std::string &name_template, bool clear)
{
  // This is sort of like autogroups, but statistical.  It assumes
  // that groups are formed from gaussian distributions of pixel
  // values.  If a pixel value is within delta standard deviations of
  // the mean value of an existing group, it is added to the group.
  // If it's within delta deviations of more than one group, it's
  // added to the closest group.  After adding a pixel, the mean and
  // deviation of the group are updated.  If after updating, the means
  // of two groups are within gamma deviations of one another, the
  // groups are merged.

  std::cerr << "statgroups:" << std::endl;

  ICoord mssize(microstructure->sizeInPixels());
  Progress *progress =
    dynamic_cast<DefiniteProgress*>(findProgress("AutoGroup"));
  unsigned int nChecked = 0;

  const std::vector<ICoord> shuffledPix = microstructure->shuffledPix();
  unsigned int npix = shuffledPix.size();

  std::vector<PixelDistribution*> pixelDists;
  
  for(const ICoord p : shuffledPix) { // Loop over all pixels
    if(progress->stopped()) {
      cleanUp_(pixelDists);
      return new std::string("");
    }
    
    // Find the existing pixel group that this pixel fits best.
    double bestSigma2 = std::numeric_limits<double>::max();
    PixelDistribution *bestDist = nullptr;
    for(PixelDistribution *pd : pixelDists) {
      double s2 = pd->deviation2(p);
      if(s2 < bestSigma2) {
	bestSigma2 = s2;
	bestDist = pd;
      }
    }
    
    if(bestDist == nullptr || bestSigma2 > delta*delta) {
      // No suitable group was found.  This may be the first pass
      // through the loop, or the pixel value is too far from existing
      // groups.  Create a new group.
      pixelDists.push_back(factory->newDistribution(p));
    }
    else {
      // An appropriate group was found.  Add the pixel to it.
      bestDist->add(p);
      // TODO: Adding a pixel might have reduced the group's
      // deviation.  Is it possible that other pixels should now be
      // ejected from the group?
      
      // Adding the pixel changed the group's mean and
      // deviation. Check to see if this distribution should now be
      // merged with another one. If it should, keep checking for more
      // mergers with the newly modified group.

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
	    if(mindev < sigma2Best) {
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
	 to_string(nChecked) + "/" + to_string(npix) + " pixels, "
	 + to_string(pixelDists.size()) + " groups");
    progress->setFraction(double(nChecked++)/npix);
  } // end loop over pixels

  // -----------

  // Split PixelDistributions into contiguous regions, and make each
  // of them into a PixelDistribution.

  std::vector<PixelDistribution*> pixelDists2;
  for(PixelDistribution *pixDist : pixelDists) {
    std::vector<std::set<ICoord>> pixSets = pixDist->contiguousPixels();
    for(auto &pixset : pixSets) {
      PixelDistribution *pixDist2 = pixDist->clone(pixset);
      pixelDists2.push_back(pixDist2);
    }
    delete pixDist;
  }
  pixelDists = pixelDists2;

  // -----------

  if(minsize > 0) {
    std::cerr << "statgroups: merging small groups" << std::endl;
    
    // Get rid of distributions containing fewer than minsize pixels
    // by attaching them to neighboring distributions.

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
      DummyDistribution bdyPixelMarker; // marks the bdy pixels in dists.
      std::cerr << "statgroups: &bdyPixelMarker=" << &bdyPixelMarker
		<< std::endl;
      for(PixelDistribution *pixDist : pixelDists) {
	if(pixDist->npts() < minsize) {
	  ntodo += pixDist->npts();
	  nSmallGroups++;
	  for(const ICoord &pt : pixDist->pixels()) {
	    for(const ICoord &dir : directions) {
	      ICoord nbr = pt + dir;
	      if(microstructure->contains(nbr)
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

      std::cerr << "statgroups: removing " << nSmallGroups
		<< " small groups, containing " << ntodo << " pixels."
		<< std::endl;

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
	ICoord pxl = bdyPixels.back();
	bdyPixels.pop_back();
	// Get the PixelDistributions that contain neighbors of pxl.
	std::map<PixelDistribution*, int> counts = countNeighbors(dists, pxl);
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
#ifdef DEBUG
	if(mostDists.empty()) {
	  std::cerr << "statgroups: mostDists is empty!" << std::endl;
	  std::cerr << " counts:";
	  for(auto iter=counts.begin(); iter!=counts.end(); ++iter)
	    std::cerr << " (" << iter->first << ", " << iter->second
		      << ")";
	  std::cerr << std::endl;
	}
#endif // DEBUG
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
	// Add the pixel to the best neighboring distribution
	bestDist->add(pxl);
	dists[pxl] = bestDist;
	// If the newly added pixel has neighbors that aren't in
	// distributions, add them to the list of pixels to be examined.
	for(const ICoord &dir : directions) {
	  ICoord nbr = pxl + dir;
	  if(microstructure->contains(nbr) && dists[nbr] == nullptr) {
	    bdyPixels.push_back(nbr);
	    dists[nbr] = &bdyPixelMarker;
	  }
	}
	prog2->setMessage(to_string(ndone) + "/" + to_string(ntodo));
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

  std::cerr << "statgroups: sorting groups" << std::endl;
  
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
  std::string groupname;	// name of last group created
  int groupNo = 0;
  int maxDigits = to_string(nonEmpty-1).size(); // for padding with 0
  for(PixelDistribution *pd : pixelDists) {
    if(pd->npts() > 0) {
      // Create the name for the group by replacing '%n' in the
      // template with a number.  Pad the number with 0's on the left
      // so that the groups appear in numerical order in the GUI
      // (which sorts them alphabetically).
      groupname = name_template;
      std::string::size_type pos = groupname.find("%n", 0);
      if(pos != std::string::npos) {
	std::string g = to_string(groupNo++);
	int nzeros = maxDigits - g.size();
	groupname = groupname.replace(pos, 2, std::string(nzeros, '0') + g);
      }
      bool newness = false;
      PixelGroup *grp = microstructure->getGroup(groupname, &newness);
      if(clear)
	grp->clear();
      grp->addWithoutCheck(&pd->pixels());
    } // end if PixelDistribution is not empty
    delete pd;
  }
  std::cerr << "statgroups: done" << std::endl;
  return new std::string(groupname);
}


