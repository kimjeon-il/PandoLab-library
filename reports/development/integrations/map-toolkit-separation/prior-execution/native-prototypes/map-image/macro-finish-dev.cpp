#include "../../tools/cpp/map-image/macro-mask.h"
#include <cstdlib>
#include <iostream>
int main(int argc,char** argv){
  if(argc!=6)return 2;
  const int w=std::atoi(argv[1]),h=std::atoi(argv[2]),rotation=std::atoi(argv[3]),ng=std::atoi(argv[4]),ne=std::atoi(argv[5]);
  std::vector<std::array<std::int32_t,4>> glyphs(ng),exclusions(ne);
  for(auto& r:glyphs)for(auto& v:r)std::cin>>v;for(auto& r:exclusions)for(auto& v:r)std::cin>>v;
  const auto pixels=std::size_t(w)*h;std::vector<std::uint8_t> image(pixels*3),target(pixels),known(pixels);
  for(auto* plane:{&image,&target,&known})for(auto& value:*plane){int v;std::cin>>v;value=static_cast<std::uint8_t>(v);}
  const auto out=pando::map_image::macroFinish(image,target,known,w,h,rotation,glyphs,exclusions);
  for(const auto* plane:{&out.image,&out.target,&out.known})for(auto value:*plane)std::cout<<int(value)<<' ';
}
