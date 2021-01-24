#include <iostream>
#include <thread>
#include "../headers/jack_module.h"
//#include "../headers/synth.h"
#include "./synth.cpp"
#include <limits>
#include <math.h>
#include <list>
#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif


int main()
{
  // create a JackModule instance
  JackModule jack;
  //init the jack, use program name as JACK client name
  jack.init("example.exe");
  double samplerate = jack.getSamplerate();
  float amp = 0.1;
  float freq = 0;
  float phase = 1;
  Synth synthesizer(1, 2, 3, freq, amp, phase, samplerate);
  float sdelta = freq / samplerate;
  //float mel [7] = {195.997718, 0, 220, 0, 246.941651, 0, 195.997718};
  std::list<float> mel = {195.997718, 0, 220, 0, 246.941651, 0, 195.997718};
  int melnum = 0;
  int x = 0;

  jack.onProcess = [samplerate, &phase, sdelta, amp, &freq, &synthesizer, &melnum, &x, &mel](jack_default_audio_sample_t *inBuf,
     jack_default_audio_sample_t *outBuf, jack_nframes_t nframes) {
    int hs = samplerate / 2;

    for(unsigned int i = 0; i < nframes; i++) {
      x += 1;
      if (x % hs == 0) {
        freq = std::next(mel.begin(), 1);;
        //melnum ++;
        //if(melnum > 6) melnum = 0;
      }
      outBuf[i] = synthesizer.getSVal(freq);
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
        freq = 900;
    }

  }

  return 0;
}; // main()
