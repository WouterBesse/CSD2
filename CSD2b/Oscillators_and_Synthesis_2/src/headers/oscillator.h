#pragma once
#include <iostream>
#include <limits>
#include <math.h>
#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif

class Oscillator {
public:
  Oscillator();
  ~Oscillator();
  float BufOutput(float sample);
  float updatephase(float phase, float newfreq);
  void calcfreq(float freq);
protected:
  float freq;
  float amp;
  float phase;
  float samplerate;
  float sample;
  float freqoffset;
  float newfreq;
  float delta;
};
