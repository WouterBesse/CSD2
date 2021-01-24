#include <iostream>
#include "../headers/sine.h"

Sine::Sine(float freq, float amp, float phase, double samplerate){
  this->freq = freq;
  this->amp = amp;
  this->phase = phase;
  this->samplerate = samplerate;
}

Sine::~Sine() {

}

float Sine::getSamp(float freq) {
  delta = calcfreq(freq, samplerate);
  tickvalue = amp * sin(phase * M_PI * 2.0f );
  phase += delta;
  if(phase > 1.0) phase -= 1.0;
  return tickvalue;
}
