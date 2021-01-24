#include <iostream>
#include "../headers/Square.h"

Square::Square(float freq, float amp, float phase, double samplerate){
  this->freq = freq;
  this->amp = amp;
  this->phase = phase;
  this->samplerate = samplerate;
}

Square::~Square() {

}

float Square::getSamp(float freq) {
  delta = calcfreq(freq, samplerate);
  qtickvalue = amp * sin(phase * M_PI * 2.0f );
  phase += delta;
  if(phase > 1.0) phase -= 1.0;
  if (qtickvalue > 0)
    return 1 * amp;
  else
    return -1 * amp;
}
