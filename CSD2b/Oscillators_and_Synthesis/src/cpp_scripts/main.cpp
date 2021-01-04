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


int main(int argc,char **argv)
{
  // create a JackModule instance
  JackModule jack;

  // init the jack, use program name as JACK client name
  jack.init("example.exe");
  double samplerate = jack.getSamplerate();
  std::cout << "\n" << std::numeric_limits<float>::min() << "\n";
  std::cout << "\n" << std::numeric_limits<float>::max() << "\n";

  float amp = 0.99;
  float freq = 400;
  float phase = 1;
  float sdelta = freq / samplerate;

  // iit first synth object
  Synth synthesizer(1, 2, 2, phase, samplerate);


  jack.onProcess = [samplerate, &phase, sdelta, amp, &freq, &synthesizer](jack_default_audio_sample_t *inBuf,
     jack_default_audio_sample_t *outBuf, jack_nframes_t nframes) {


    for(unsigned int i = 0; i < nframes; i++) {
      outBuf[i] = synthesizer.getSVal( amp, freq);
    }
    return 0;
  };

  //for (int i = 0; i < 50; i++) {
    //std::cout << "sample";
    //std::cout << synthesizer.getSVal( amp, freq);
    //std::cout << "\n";

  //}
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
      case 'f':
        freq = 1000;
    }
  }

  return 0;
}; // main()
