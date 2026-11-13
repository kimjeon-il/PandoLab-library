#include "../../tools/cpp/map-image/macro-mask.h"
#include <cstdlib>
#include <iostream>
int main(int argc,char** argv){
  if(argc!=5)return 2;
  int w=std::atoi(argv[2]),h=std::atoi(argv[3]),r=std::atoi(argv[4]);
  std::vector<std::uint8_t> in(std::size_t(w)*h);std::cin.read(reinterpret_cast<char*>(in.data()),in.size());
  if(std::string(argv[1])=="dilate"){const auto out=pando::map_image::macroDilate(in,w,h,r);for(auto v:out)std::cout<<int(v);}
  else{const auto [a,b]=pando::map_image::macroAdjacency(in,w,h,r);for(auto v:a)std::cout<<int(v);std::cout<<' ';for(auto v:b)std::cout<<int(v);}
  std::cout<<std::endl;
}
