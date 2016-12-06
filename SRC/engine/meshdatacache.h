// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef MESHDATACACHE_H
#define MESHDATACACHE_H

#include <oofconfig.h>
#include <map>
#include <set>
#include <vector>

typedef std::vector<double> DVec;

class FEMesh;

class MeshDataCache {
private:
  DVec times_;
  DVec interpolant;
protected:
  FEMesh *mesh;
  void clear_times();
  void add_time(double);
  // latest stores original mesh dofs when cached data is installed
  DVec *latest;
  double latesttime;
  void saveLatest();
  virtual DVec &fetchOne(double) = 0;
  virtual bool checkTime(double) const = 0;
  virtual DVec *allTimes() const = 0;
public:
  MeshDataCache(FEMesh *mesh) : mesh(mesh), latest(0) {}
  virtual ~MeshDataCache();
  void setMesh(FEMesh *mesh);
  virtual const DVec *times() const { return &times_; }
  void restore(double);		// restore data to mesh, if needed
  bool interpolate(double);
  virtual void restoreLatest();
  virtual void restore_(double) = 0; // actually restore
  virtual void record() = 0;	     // save data from mesh
  virtual void clear() = 0;
  double latestTime() const;
  double earliestTime() const;
  double latestCachedTime() const;
  void transfer(MeshDataCache*);
  int size() const { return times_.size(); }
  bool atLatest() const { return latest == 0; }
  bool atEarliest() const;
};

class MemoryDataCache : public MeshDataCache {
private:
  typedef std::map<double, DVec> DataCache;
  DataCache cache;
  void storedofs(DVec&); // get data from mesh
  virtual DVec &fetchOne(double);
  virtual bool checkTime(double) const;
  virtual DVec *allTimes() const;
public:
  MemoryDataCache(FEMesh *mesh) : MeshDataCache(mesh) {}
  virtual void restore_(double);
  virtual void record();
  virtual void clear();
};

class DiskDataCache : public MeshDataCache {
private:
  static int nCaches;
  struct lt {
    bool operator()(const DiskDataCache*, const DiskDataCache*) const;
  };
  static std::set<DiskDataCache*, lt> allCaches;

  static bool initialized;
  int cacheID;
  typedef std::map<double, std::string> FileDict;
  DVec localdata;
  FileDict fileDict; // maps ints to file names
  void clear_(bool force);
  virtual DVec &fetchOne(double);
  virtual bool checkTime(double) const;
  virtual DVec *allTimes() const;
public:
  DiskDataCache(FEMesh *mesh);
  ~DiskDataCache();
  virtual void restore_(double);
  virtual void record();
  virtual void clear();
  friend void cleanUpDDcaches();
};

void cleanUpDDcaches();

#endif // MESHDATACACHE_H
