#include <iostream>
#include <thread>
#include "../headers/jack_module.h"
#include "../headers/generator.h"
//#include "../headers/synth.h"
#include "./synth.cpp"
#include <limits>
#include <math.h>
#include <cstdlib>
#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif


int main(int argc,char **argv)
{
  // create a JackModule instance
  JackModule jack;
  Generator gen;
  //init the jack, use program name as JACK client name
  jack.init("example.exe");
  double samplerate = jack.getSamplerate();

  float amp = 0.99;
  float freq = 400;
  float phase = 1;
  //double samplerate = 48000;
  float sdelta = freq / samplerate;
  int io = rand() % 3 + 1;
  int iio = rand() % 3 + 1;
  int iiio = rand() % 3 + 1;


  // init first synth object, first 3 ints are waveform selectors. 1 = sine, 2 = square, 3 = triangle
  Synth synthesizer(io, iio, iiio, phase, samplerate);
  //
  //
  jack.onProcess = [samplerate, &phase, sdelta, amp, &freq, &synthesizer](jack_default_audio_sample_t *inBuf,
     jack_default_audio_sample_t *outBuf, jack_nframes_t nframes) {


    for(unsigned int i = 0; i < nframes; i++) {
      outBuf[i] = synthesizer.getSVal(amp, freq);
    }
    return 0;
  };


  jack.autoConnect();

  //keep the program running and listen for user input, q = quit
  std::cout << "\n\nPress 'q' ENTER when you want to quit the program.\n";
  bool running = true;

  while (running)
  {
    switch (std::cin.get())
    {
      case 'q':
        running = false;
        jack.end();
        break;
      case 'p':
        std::cout << "frequency: " << freq << "\n";
        std::cout << "samplerate: " << samplerate << "\n";
        std::cout << "amplitude: " << amp << "\n";
        std::cout << "phase: " << phase << "\n";
        std::cout << "delta: " << sdelta << "\n";
        break;
      case 'm':
        freq = gen.generate();
    }

  }


  return 0;
}; // main()
