#include <iostream>
#include <list>
#include "../headers/synth.h"

Synth::Synth(int osc1, int osc2, int osc3, float freq, float amp, float phase, double samplerate) {
  freq = freq;
  amp = amp;
  phase = phase;
  samplerate = samplerate;
  if (osc1 == 1) {
    wav1 = new Sine(freq, amp, phase, samplerate); // ik ben het er mee eens dat dit niet efficiënt is, maar kom er op het moment niet uit hoe ik losse osc instanties kan maken als het een member of child is
  } else if (osc1 == 2) {
    wav1 = new Square(freq, amp, phase, samplerate);
  } else {
    wav1 = new Triangle(freq, amp, phase, samplerate);
  }
  if (osc2 == 1) {
    wav2 = new Sine(freq, amp, phase, samplerate);
  } else if (osc2 == 2) {
    wav2 = new Square(freq, amp, phase, samplerate);
  } else {
    wav2 = new Triangle(freq, amp, phase, samplerate);
  }
  if (osc3 == 1) {
    wav3 = new Sine(freq, amp, phase, samplerate);
  } else if (osc3 == 2) {
    wav3 = new Square(freq, amp, phase, samplerate);
  } else {
    wav3 = new Triangle(freq, amp, phase, samplerate);
  }
}

Synth::~Synth() {
  delete wav1;
  delete wav2;
  delete wav3;
}

float Synth::getSVal(float freq) {
  sBuf = wav1->getSamp(freq) + wav2->getSamp(freq) + wav3->getSamp(freq);
  sBufdiv = sBuf / 3;
  return sBufdiv;
}

std::vector<float> Synth::MelodyMaker() {
  std::vector<float> NewMel = {};
  for(unsigned int i = 0; i < 7; i++) {
    NewMel.push_back (500 + static_cast <float> (rand()) / (static_cast <float> (RAND_MAX/(5000 - 500))));
  };
  return NewMel;
}
