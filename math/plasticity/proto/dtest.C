#include <iostream>
#include <map>
#include <string>

// Compile with -std=c++11 or the "auto" thing won't work.

class Data_b {
public:
  int x,y;
  Data_b(int x, int y) : x(x), y(y) {};
  virtual ~Data_b() {};
};

class Data_d : public Data_b {
public:
  int z;
  Data_d(int x, int y, int z) : Data_b(x,y), z(z) {};
};


std::ostream & operator<<(std::ostream &o, const Data_b &d) {
  o << "Data_b(" << d.x << "," << d.y << ")";
  return o;
};


std::ostream & operator<<(std::ostream &o, const Data_d &d) {
  o << "Data_d(" << d.x << "," << d.y << "," << d.z << ")";
  return o;
};



int main(int argc, char*argv[]) {
  Data_b d1 = Data_b(3,4);
  Data_b d2 = Data_b(4,5);
  Data_d d3 = Data_d(1,2,3);
  
  std::cout << d1 << std::endl;
  std::cout << d2 << std::endl;
  std::cout << d3 << std::endl;
  
  std::map<std::string,Data_b *> mp;

  mp["one"] = &d1;
  mp["three"] = &d3;

  auto mpi = mp.find("two");
  if (mpi==mp.end()) {
    std::cout << "Item 'two' not found." << std::endl;
  }

  mpi = mp.find("three");
  if (mpi==mp.end()) {
    std::cout << "Item 'three' not found, very strange." << std::endl;
  }
  else {
    std::cout << "Item 'three' found, it's this:" << std::endl;
    std::cerr << *(dynamic_cast<Data_d*>(mpi->second)) << std::endl;
    // Wrong: std::cerr << *(mpi->second) << std::endl;
  }
}
				


