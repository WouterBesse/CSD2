#include <iostream>
#include "../headers/oscillator.h"

Oscillator::Oscillator() {
}

Oscillator::~Oscillator() {
}

float RandomFloat(float a, float b) {
    float random = ((float) rand()) / (float) RAND_MAX;
    float diff = b - a;
    float r = random * diff;
    return a + r;
}

void Oscillator::calcfreq(float freq) {
  this->freqoffset = RandomFloat(-16.0, 16.0);
  this->newfreq = freq + freqoffset;
  this->delta = newfreq / samplerate;
}
