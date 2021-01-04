#include <iostream>
#include "../headers/oscillator.h"

Oscillator::Oscillator(double samplerate, float ophase) {
  osamplerate = samplerate;
  ophase = ophase;
  sinus = Sine();
  //triangles = Tri();
  square = Sqr();
}

Oscillator::~Oscillator() {
}

float Oscillator::calcfreq(float freq, float freqoffset) {
  newfreq = freq + freqoffset;
  return newfreq;
}

float Oscillator::getSamp(int osctype, float freq, float freqoffset) {
  osctype = osctype;
  newfreq = calcfreq(freq, freqoffset);
  if (osctype == 1) {
    sample = sinus.getTick(ophase);
  }
  else if (osctype == 2) {
    sample = square.getTick(ophase);
  } else {
    sample = 0.9 * asin(sin(ophase * 3.14159265358979323846 * 2.0f )) * (2.0 / 3.14159265358979323846);
  }

  delta = newfreq / osamplerate;
  ophase += delta;
  if(ophase > 1.0) ophase -= 1.0;
  return sample;
}
