#include <iostream>
#include <thread>
#include "math.h"
#include <limits>
#define _USE_MATH_DEFINES
#include <cmath>
#ifndef M_PIs
    #define M_PI 3.14159265358979323846
#endif

class Sqr
{
public:
  Sqr();
  ~Sqr();
  float getTick(float phase);
private:
  float tickvalue;
  float qtickvalue;
  float phase;
};
