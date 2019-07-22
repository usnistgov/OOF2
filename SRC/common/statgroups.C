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
#include "common/statgroups.h"

#include <algorithm>


// TODO: Auto-despeckling of groups at end of statgroups.

// TODO: StatBurn -- add neighboring pixels if they're within n
// deviations of the mean of the burned region.  Update the mean and
// deviation as pixels are added.

struct SortDists {
  bool operator()(const PixelDistribution *a, const PixelDistribution *b) {
    return a->npts() > b->npts();
  }
};

const std::string *statgroups(CMicrostructure *microstructure,
			      const PixelDistributionFactory *factory,
			      double delta,
			      double gamma,
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

  ICoord mssize(microstructure->sizeInPixels());
  Progress *progress =
    dynamic_cast<DefiniteProgress*>(findProgress("AutoGroup"));
  unsigned int nChecked = 0;

  const std::vector<ICoord> shuffledPix = microstructure->shuffledPix();
  unsigned int npix = shuffledPix.size();
  // std::cerr << "statgroups: npix=" << npix << std::endl;

  std::vector<PixelDistribution*> pixelDists;
  
  for(const ICoord p : shuffledPix) { // Loop over all pixels
    
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
      // std::cerr << "statgroups: new group at " << p
      // 		<< " val=" << pixelDists.back()->value(p)
      // 		<< " dist=" << pixelDists.back() << " "
      // 		<< pixelDists.back()->stats()
      // 		<< std::endl;
    }
    else {
      // An appropriate group was found.  Add the pixel to it.
      bestDist->add(p);
      // std::cerr << "statgroups: added " << p << " " << bestDist->value(p)
      // 		<< " to " << bestDist << " "
      // 		<< "sigma=" << sqrt(bestSigma2) << " new dist="
      // 		<< bestDist->stats() << std::endl;
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
	  // std::cerr << "statgroups: merged " << modifiedDist << " into "
	  // 	    << distBest
	  // 	    << " " << distBest->stats() << std::endl;
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

  std::sort(pixelDists.begin(), pixelDists.end(), SortDists());

  // Create a real PixelGroup for each PixelDistribution, and delete
  // the PixelDistributions.
  std::string groupname;	// name of last group created
  int groupNo = 0;
  int maxDigits = to_string(pixelDists.size()-1).size(); // for padding with 0
  for(PixelDistribution *pd : pixelDists) {
    // Create the name for the group by replacing '%n' in the template
    // with a number.  Pad the number with 0's on the left so that the
    // groups appear in numerical order in the GUI (which sorts them
    // alphabetically).
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
    delete pd;
  }

  return new std::string(groupname);
}
