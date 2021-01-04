#include <iostream>
#include "../headers/oscillator.h"

class Synth {
public:
  Synth(int osc1, int osc2, int osc3, float phase, double samplerate);
  ~Synth();
  float getSVal(float ampl, float freqy);
  float freq;
  float amp;
  float phase;
  double samplerate;
private:
  int osc1, osc2, osc3;
  float sBuf;
  Oscillator fosc;
  Oscillator sosc;
  Oscillator tosc;
};
