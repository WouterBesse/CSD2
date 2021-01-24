#include <iostream>
#include "../headers/sine.h"

Sine::Sine(float freq, float amp, float phase, float samplerate){
  freq = freq;
  std::cout << freq;
  std::cout << "\n";
  amp = amp;
  std::cout << amp;
  std::cout << "\n";
  phase = phase;
  std::cout << phase;
  std::cout << "\n";
  samplerate = samplerate;
  std::cout << samplerate;
  std::cout << "\n";
  Oscillator::calcfreq(freq);
  std::cout << newfreq;
  std::cout << "\n";
}

Sine::~Sine() {

}

float Sine::getSamp() {
  tickvalue = amp * sin(phase * M_PI * 2.0f );
  phase += delta;
  return tickvalue;
}
