#define main pando_review_program_main
#include "../../tools/cpp/map-review/review-masks.cpp"
#undef main
#include <cstdlib>
int main(int argc,char** argv){
    if(argc!=8)return 2;
    const int w=std::atoi(argv[1]),h=std::atoi(argv[2]),x0=std::atoi(argv[3]),y0=std::atoi(argv[4]);
    const int x1=std::atoi(argv[5]),y1=std::atoi(argv[6]),lineWidth=std::atoi(argv[7]);
    std::vector<Byte> output(std::size_t(w)*h);Canvas canvas{w,h,output,1,false};
    pando::map_image::draw::wideLine(canvas,x0,y0,x1,y1,lineWidth,1);
    for(const auto value:output)std::cout<<int(value);
}
