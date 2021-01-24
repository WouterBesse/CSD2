#include <iostream>
#include "../headers/oscillator.h"

class Square : public Oscillator
{
public:
  Square(float freq, float amp, float phase, double samplerate);
  ~Square();
  float getSamp(float freq);
private:
  float tickvalue;
  float qtickvalue;
};
