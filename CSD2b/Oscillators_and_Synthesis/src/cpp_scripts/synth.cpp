#include <iostream>
#include "../headers/synth.h"

Synth::Synth(int osc1, int osc2, int osc3, float phase, double samplerate) : osc1(osc1), osc2(osc2), osc3(osc3), fosc(samplerate, phase), sosc(samplerate, phase), tosc(samplerate, phase) {
  //std::cout << osc1 << osc2 << osc3;
  phase = phase;
  samplerate = samplerate;
}

Synth::~Synth() {
}

float Synth::getSVal(float ampl, float freqy) {
  amp = ampl;
  //std::cout << amp;
  //std::cout << "\n";
  freq = freqy;
  //std::cout << freq;
  //std::cout << "\n";
  sBuf = fosc.getSamp(osc1, freq, 0) + sosc.getSamp(osc2, freq, 5) + tosc.getSamp(osc3, freq, 2);
  return (sBuf / 3) * amp;
}
