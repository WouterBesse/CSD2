#include <iostream>
#include "../headers/oscillator.h"

class Sine : public Oscillator
{
public:
  Sine(float freq, float amp, float phase, float samplerate);
  ~Sine();
  void update();
  float getSamp();
private:
  float tickvalue;
};
