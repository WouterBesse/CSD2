#include <iostream>
#include "../headers/oscillator.h"

Oscillator::Oscillator(double samplerate, float ophase) {
  osamplerate = samplerate;
  ophase = ophase;
  sinus = Sine();
  //zaag = Saw();
  square = Sqr();
}

Oscillator::~Oscillator() {
}

float Oscillator::calcfreq(float freq, float freqoffset) {
  newfreq = freq + freqoffset;
  delta = newfreq / osamplerate;
  return newfreq;
}

float Oscillator::getSamp(int osctype, float freq, float freqoffset) {
  osctype = osctype;
  //std::cout << "freqosc";
  //std::cout << freq;
  //std::cout << "\n";
  newfreq = calcfreq(freq, freqoffset);
  //std::cout << "newfreq: ";
  //std::cout << newfreq;
  //std::cout << "\n";
  if (osctype == 1) {
  sample = sinus.getTick(ophase);
} else if (osctype == 2) {
  sample = square.getTick(ophase);
}
  ophase += delta;
  if(ophase > 1.0) ophase -= 1.0;
  //std::cout << "ophase : ";
  //std::cout << ophase;
  //std::cout << "\n";

  return sample;
}
