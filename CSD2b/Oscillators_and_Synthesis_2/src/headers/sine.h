#include <iostream>
#include "../headers/oscillator.h"

class Sine : public Oscillator
{
public:
  Sine(float freq, float amp, float phase, double samplerate);
  ~Sine();
  float getSamp(float freq);
private:
  float tickvalue;
};
