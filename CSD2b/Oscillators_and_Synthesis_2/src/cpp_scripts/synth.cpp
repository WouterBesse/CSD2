#include <iostream>
#include "../headers/synth.h"

Synth::Synth(int osc1, int osc2, int osc3, float freq, float amp, float phase, float samplerate) {
  freq = freq;
  amp = amp;
  phase = phase;
  samplerate = samplerate;
  if (osc1 == 1) {
    Sine wav1(float freq, float amp, float phase, float samplerate); // ik ben het er mee eens dat dit niet efficiënt is, maar kom er op het moment niet uit hoe ik losse osc instanties kan maken als het een member of child is
  } else if (osc1 == 2) {
    Sine wav1(float freq, float amp, float phase, float samplerate);
    //Block fosc;
  } else {
    Sine wav1(float freq, float amp, float phase, float samplerate);
    //Triangle fosc;
  }
  if (osc2 == 1) {
    Sine wav2(float freq, float amp, float phase, float samplerate);
  } else if (osc2 == 2) {
    Sine wav2(float freq, float amp, float phase, float samplerate);
    //Block sosc;
  } else {
    Sine wav2(float freq, float amp, float phase, float samplerate);
    //Triangle sosc;
  }
  if (osc3 == 1) {
    Sine wav3(float freq, float amp, float phase, float samplerate);
  } else if (osc3 == 2) {
    Sine wav3(float freq, float amp, float phase, float samplerate);
    //Block fosc;
  } else {
    Sine wav3(float freq, float amp, float phase, float samplerate);
    //Triangle fosc;
  }
}

Synth::~Synth() {
}

float Synth::getSVal() {
  sBuf = wav1.getSamp();
  return sBuf;
}
