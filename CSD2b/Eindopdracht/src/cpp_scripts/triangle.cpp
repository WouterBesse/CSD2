#include <iostream>
#include "../headers/Triangle.h"

Triangle::Triangle(float freq, float amp, float phase, double samplerate){
  this->freq = freq;
  this->amp = amp;
  this->phase = phase;
  this->samplerate = samplerate;
}

Triangle::~Triangle() {

}

float Triangle::getSamp(float freq) {
  delta = calcfreq(freq, samplerate);
  tickvalue = amp * asin(sin(phase * 3.14159265358979323846 * 2.0f )) * (2.0 / 3.14159265358979323846);
  phase += delta;
  if(phase > 1.0) phase -= 1.0;
  return tickvalue;
}
