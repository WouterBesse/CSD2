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
  virtual ~Oscillator();
  float BufOutput(float sample);
  float updatephase(float phase, float newfreq);
  float calcfreq(float freq, double samplerate);
  virtual float getSamp(float freq) {
    return 0;
  }
protected:
  float freq;
  float amp;
  float phase;
  double samplerate;
  float sample;
  float freqoffset;
  float newfreq;
  float delta;
};
