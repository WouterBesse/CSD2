#include <iostream>
#include <thread>
#include "../headers/jack_module.h"
//#include "../headers/synth.h"
#include "./synth.cpp"
#include <limits>
#include <math.h>
#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif


int main()
{
  float amp = 0.1;
  float freq = 400;
  float phase = 1;
  float samplerate = 48000;
  Synth synthesizer(1, 2, 3, freq, amp, phase, samplerate);
  return 0;
}; // main()
