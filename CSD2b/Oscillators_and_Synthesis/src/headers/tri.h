#include <iostream>
#include "math.h"


class Tri
{
public:
  Tri();
  ~Tri();
  float getsTick(float tphase);
private:
  float tickvalue;
  float tphase;
};
