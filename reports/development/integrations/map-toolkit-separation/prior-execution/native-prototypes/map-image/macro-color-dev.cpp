#include "../../tools/cpp/map-image/macro-mask.h"
#include <cstdlib>
#include <cstring>
#include <iostream>
int main(int argc,char** argv){
  if(argc!=5)return 2;
  const bool visible=std::string(argv[1])=="visible";const int width=std::atoi(argv[2]),height=std::atoi(argv[3]),count=std::atoi(argv[4]);
  std::vector<std::array<double,3>> colors(count);for(auto& color:colors)for(auto& component:color)std::cin>>component;
  std::vector<std::uint8_t> rgb(std::size_t(width)*height*3);for(auto& value:rgb){int v;std::cin>>v;value=static_cast<std::uint8_t>(v);}
  const auto output=pando::map_image::macroClassify(rgb,width,height,colors,visible);
  for(const auto value:output)std::cout<<int(value)<<' ';
}
