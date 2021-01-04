#pragma once
#include <iostream>
#include <thread>
#include "../headers/sine.h"
#include "../headers/sqr.h"
#include "../headers/tri.h"
#include <limits>
#include <math.h>
#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif

class Oscillator {
public:
  Oscillator(double osamplerate, float ophase);
  ~Oscillator();
  float calcfreq(float freq, float freqoffset);
  float getSamp(int osctype, float freq, float ophase);
protected:
  float freq;
  float ophase;
  double osamplerate;
  float sample;
  float freqoffset;
  float newfreq;
  float delta;
  Sine sinus;
  Sqr square;
  //Tri triangles;
};
