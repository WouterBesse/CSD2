#include <iostream>
#include "../headers/oscillator.h"

Oscillator::Oscillator() {
}

Oscillator::~Oscillator() {
}

float Oscillator::calcfreq(float freq, double samplerate) {
  delta = freq / samplerate;
  return delta;
}
