#include <iostream>
#include "../headers/synth.h"

Synth::Synth(int osc1, int osc2, int osc3, float freq, float amp, float phase, float samplerate) {
  freq = freq;
  amp = amp;
  phase = phase;
  samplerate = samplerate;
  if (osc1 == 1) {
    wav1 = new Sine(freq, amp, phase, samplerate); // ik ben het er mee eens dat dit niet efficiënt is, maar kom er op het moment niet uit hoe ik losse osc instanties kan maken als het een member of child is
  } else if (osc1 == 2) {
    wav1 = new Sine(freq, amp, phase, samplerate);
    //Block fosc;
  } else {
    wav1 = new Sine(freq, amp, phase, samplerate);
    //Triangle fosc;
  }
  if (osc2 == 1) {
    wav2 = new Sine(freq, amp, phase, samplerate);
  } else if (osc2 == 2) {
    wav2 = new Sine(freq, amp, phase, samplerate);
    //Block sosc;
  } else {
    wav2 = new Sine(freq, amp, phase, samplerate);
    //Triangle sosc;
  }
  if (osc3 == 1) {
    wav3 = new Sine(freq, amp, phase, samplerate);
  } else if (osc3 == 2) {
    wav3 = new Sine(freq, amp, phase, samplerate);
    //Block fosc;
  } else {
    wav3 = new Sine(freq, amp, phase, samplerate);
    //Triangle fosc;
  }
}

Synth::~Synth() {
}

float Synth::getSVal() {
  sBuf = wav1->getSamp();
  return sBuf;
}
