#include <iostream>
#include "../headers/oscillator.h"

class Triangle : public Oscillator
{
public:
  Triangle(float freq, float amp, float phase, double samplerate);
  ~Triangle();
  float getSamp(float freq);
private:
  float tickvalue;
};
