// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// A std::vector-like object which allocates its memory in discrete
// non-contiguous chunks, to (ironically) try to reduce memory
// fragmentation.  Its advantage is that it doesn't have to reallocate
// itself as it grows (unlike a vector) and it still can be accessed
// in constant time (unlike a linked list).  

// Memory is allocated in blocks of 2**logChunkSize, for integer
// logChunkSize, so that it's easy to convert from vector indices to
// chunk indices.

#ifndef CHUNKYVECTOR_H
#define CHUNKYVECTOR_H

#define DEFAULT_LOGCHUNKSIZE 8

#include <oofconfig.h>
#include <vector>

template <class CHUNKYVECTOR> class CVIterator;
template <class CHUNKYVECTOR> class CVConstIterator;

template <class TYPE>
class ChunkyVector {

public:
  typedef TYPE value_type;
  typedef CVIterator<ChunkyVector<TYPE>> iterator;
  typedef CVConstIterator<ChunkyVector<TYPE>> const_iterator;
  typedef std::size_t size_type;
  typedef std::ptrdiff_t difference_type;

protected:
  std::vector<std::vector<TYPE>*> chunkList;
  const int logChunkSize;
  const size_type chunkSize;

  void addChunk() {
    std::vector<TYPE> *chunk = new std::vector<TYPE>();
    chunk->reserve(chunkSize);
    chunkList.push_back(chunk);
  }
  
public:
  
  ChunkyVector(int logChunkSize=DEFAULT_LOGCHUNKSIZE)
    : logChunkSize(logChunkSize),
      chunkSize(1 << logChunkSize)
  {
    // The empty vector contains one empty chunk so that the size()
    // method doesn't need to do anything special for it.
    addChunk();
  }

  ChunkyVector(size_type size, const TYPE &val,
	       int logChunkSize=DEFAULT_LOGCHUNKSIZE)
    : logChunkSize(logChunkSize),
      chunkSize(1 << logChunkSize)
  {
    size_type n = size/chunkSize;
    size_type extra = size - n*chunkSize;
    chunkList.reserve(n);
    for(size_type i=0; i<n; i++)
      chunkList.push_back(new std::vector<TYPE>(chunkSize, val));
    if(extra > 0) {
      std::vector<TYPE> *chunk = new std::vector<TYPE>();
      chunk->reserve(chunkSize);
      chunkList.push_back(chunk);
      for(size_type i=0; i<extra; i++)
	chunk->push_back(val);
    }
  }

  ChunkyVector(const ChunkyVector<TYPE> &other)
    : logChunkSize(other.logChunkSize),
      chunkSize(other.chunkSize)
  {
    chunkSize = other.chunkSize;
    chunkList.reserve(other.nChunks());
    for(auto chunk : other.chunkList)
      chunkList.push_back(new std::vector<TYPE>(*chunk));
  }

  ChunkyVector(ChunkyVector<TYPE> &&other)
    : chunkList(std::move(other.chunkList)),
      logChunkSize(other.logChunkSize),
      chunkSize(other.chunkSize)
  {
    other.chunkList = std::vector<std::vector<TYPE>*>();
  }

  ~ChunkyVector() {
    for(auto v : chunkList)
      delete v;
  }

  size_type size() const {
    return (chunkList.size()-1)*chunkSize + chunkList.back()->size();
  }
  
  size_type nChunks() const {
    return chunkList.size();
  }

  void clear() {
    for(auto v: chunkList)
      delete v;
    chunkList.clear();
    addChunk();
  }

  void shrink_to_fit() {
    // Since we don't have any way of removing entries at the moment,
    // there's no point in implementing shrink_to_fit().  OOF2 calls
    // it after calling clear() in LinearizedSystem::consolidate().
  }

  void reserve(size_type n) {
    // The whole point of this class is to make reserving unnecessary,
    // but since it's supposed to be a drop-in replacement for
    // std::vector, this method must be implemented.
  }

  void push_back(TYPE &val) {
    if(chunkList.back()->size() == chunkSize)
      addChunk();
    chunkList.back()->push_back(val);
  }

  template <class... Args>
  void emplace_back(Args&&... args) {
    if(chunkList.back()->size() == chunkSize)
      addChunk();
    chunkList.back()->emplace_back(std::forward<Args>(args)...);
  }
  
  TYPE &operator[](size_type i) {
    assert(i < size());
    size_type n = i >> logChunkSize; // which chunk
    return (*chunkList[n])[i-n*chunkSize];
  }

  const TYPE &operator[](size_type i) const {
    assert(i < size());
    size_type n = i >> logChunkSize; // which chunk
    return (*chunkList[n])[i-n*chunkSize];
  }

  iterator begin() {
    return CVIterator<ChunkyVector<TYPE>>(this, 0);
  }

  iterator end() {
    return CVIterator<ChunkyVector<TYPE>>(this, size());
  }

  const_iterator begin() const {
    return CVConstIterator<ChunkyVector<TYPE>>(this, 0);
  }

  const_iterator end() const {
    return CVConstIterator<ChunkyVector<TYPE>>(this, size());
  }

};				

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

template <class CHUNKYVECTOR>
class CVIterator {
protected:
  CHUNKYVECTOR *vec;
  typedef typename CHUNKYVECTOR::size_type size_type;
  typedef typename CHUNKYVECTOR::difference_type difference_type;
  typedef typename CHUNKYVECTOR::value_type value_type;
  size_type index;
  
public:

  CVIterator(CHUNKYVECTOR *v, size_type i)
    : vec(v),
      index(i)
  {}

  value_type &operator*() const {
    return (*vec)[index];
  }

  value_type *operator->() const {
    return &(*vec)[index];
  }

  CVIterator<CHUNKYVECTOR> &operator++() {
    index++;
    return *this;
  }

  CVIterator<CHUNKYVECTOR> &operator--() {
    assert(index != 0);
    index--;
    return *this;
  }

  CVIterator<CHUNKYVECTOR> operator++(int) {
    CVIterator<CHUNKYVECTOR> copy(*this);
    index++;
    return copy;
  }
    
  CVIterator<CHUNKYVECTOR> operator--(int) {
    CVIterator<CHUNKYVECTOR> copy(*this);
    index--;
    return copy;
  }

  CVIterator &operator+=(difference_type n) {
    index += n;
    return *this;
  }

  CVIterator &operator-=(difference_type n) {
    index -= n;
    return *this;
  }

  difference_type operator-(const CVIterator &other) const {
    assert(vec == other.vec);
    return index - other.index;
  }

  CVIterator operator+(difference_type n) {
    return CVIterator(vec, 0, index+n);
  }
  
  CVIterator operator-(difference_type n) {
    return CVIterator(vec, 0, index-n);
  }

  bool operator==(const CVIterator &other) const {
    assert(vec == other.vec);
    return index == other.index;
  }

  bool operator!=(const CVIterator &other) const {
    assert(vec == other.vec);
    return index != other.index;
  }
  
  bool operator>(const CVIterator &other) const {
    assert(vec == other.vec);
    return index > other.index;
  }

  bool operator<(const CVIterator &other) const {
    assert(vec == other.vec);
    return index < other.index;
  }

  bool operator>=(const CVIterator &other) const {
    assert(vec == other.vec);
    return index >= other.index;
  }

  bool operator<=(const CVIterator &other) const {
    assert(vec == other.vec);
    return index <= other.index;
  }
};

// TODO: Use a common base class to remove duplicated code in
// CVIterator and CVConstIterator.

template <class CHUNKYVECTOR>
class CVConstIterator {
protected:
  const CHUNKYVECTOR *vec;
  typedef typename CHUNKYVECTOR::size_type size_type;
  typedef typename CHUNKYVECTOR::difference_type difference_type;
  typedef typename CHUNKYVECTOR::value_type value_type;
  size_type index;
  
public:

  CVConstIterator(const CHUNKYVECTOR *v, size_type i)
    : vec(v),
      index(i)
  {}

  const value_type &operator*() const {
    return (*vec)[index];
  }

  const value_type *operator->() const {
    return &(*vec)[index];
  }

  CVConstIterator<CHUNKYVECTOR> &operator++() {
    index++;
    return *this;
  }

  CVConstIterator<CHUNKYVECTOR> &operator--() {
    assert(index != 0);
    index--;
    return *this;
  }

  CVConstIterator<CHUNKYVECTOR> operator++(int) {
    CVConstIterator<CHUNKYVECTOR> copy(*this);
    index++;
    return copy;
  }
    
  CVConstIterator<CHUNKYVECTOR> operator--(int) {
    CVConstIterator<CHUNKYVECTOR> copy(*this);
    index--;
    return copy;
  }

  CVConstIterator &operator+=(difference_type n) {
    index += n;
    return *this;
  }

  CVConstIterator &operator-=(difference_type n) {
    index -= n;
    return *this;
  }

  difference_type operator-(const CVConstIterator &other) const {
    assert(vec == other.vec);
    return index - other.index;
  }

  CVConstIterator operator+(difference_type n) {
    return CVConstIterator(vec, 0, index+n);
  }
  
  CVConstIterator operator-(difference_type n) {
    return CVConstIterator(vec, 0, index-n);
  }

  bool operator==(const CVConstIterator &other) const {
    assert(vec == other.vec);
    return index == other.index;
  }

  bool operator!=(const CVConstIterator &other) const {
    assert(vec == other.vec);
    return index != other.index;
  }
  
  bool operator>(const CVConstIterator &other) const {
    assert(vec == other.vec);
    return index > other.index;
  }

  bool operator<(const CVConstIterator &other) const {
    assert(vec == other.vec);
    return index < other.index;
  }

  bool operator>=(const CVConstIterator &other) const {
    assert(vec == other.vec);
    return index >= other.index;
  }

  bool operator<=(const CVConstIterator &other) const {
    assert(vec == other.vec);
    return index <= other.index;
  }
};


#endif // CHUNKYVECTOR_H
