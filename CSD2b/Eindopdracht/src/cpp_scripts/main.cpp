#include <iostream>
#include <thread>
#include "../headers/jack_module.h"
#include "./synth.cpp"
#include <limits>
#include <fstream>
#include <iterator>
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

  // Define all initial values
  float amp = 0.1;
  float freq = 0;
  float phase = 1;
  int syntyp = 0;
  Synth synthesizer(1, 2, 3, freq, amp, phase, samplerate);
  float sdelta = freq / samplerate;
  std::vector<float> mel{ 195.997718, 0, 220, 0, 246.941651, 0, 195.997718};
  std::vector<float> store{};
  int melnum = 0;
  int x = 0;

  jack.onProcess = [samplerate, &phase, sdelta, amp, &freq, &synthesizer, &melnum, &x, &mel, &syntyp, &store](jack_default_audio_sample_t *inBuf,
     jack_default_audio_sample_t *outBuf, jack_nframes_t nframes) {
    int hs = samplerate / 2;

    for(unsigned int i = 0; i < nframes; i++) {
      x += 1;
      if (x % hs == 0) {
        // Sets the current frequency to the one stored in the melody vector and saves it to a store vector
        freq = mel.at(melnum);
        store.push_back (freq);
        melnum ++;
        if(melnum > 6) melnum = 0;
      }
      if (syntyp == 0) {
        outBuf[i] = synthesizer.getSValAdd(freq);
      } else if (syntyp == 1) {
        outBuf[i] = synthesizer.getSValMult(freq);
      } else {
        outBuf[i] = (synthesizer.getSValMult(freq) + synthesizer.getSValAdd(freq)) / 2;
      }
    }
    return 0;
  };


  jack.autoConnect();

  //keep the program running and listen for user input, q = quit
  std::cout << "\n\nWhat would you like to do? (press 'H' enter to see all the possibilities)\n";
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
        mel = synthesizer.MelodyMaker();
        break;
      case 'r':
        syntyp = 1;
        break;
      case 'a':
        syntyp = 0;
        break;
      case 'c':
        syntyp = 2;
        break;
      case 'h':
        std::cout << "Hello, you can type a key to execute it's funtion, the following keys are possible: \n";
        std::cout << "m - See synthesizer values \n";
        std::cout << "m - Generate new melody \n";
        std::cout << "r - Set synthesizer to ring modulation \n";
        std::cout << "a - Set synthesizer to adding the waves \n";
        std::cout << "c - Set synthesizer to a combination of the previous two modes \n";
        std::cout << "s - Save notes synth has played so far \n";
        std::cout << "q - Quit synth \n \n";
        break;
      case 's':
        // Saving code found on https://stackoverflow.com/questions/6406356/how-to-write-vector-values-to-a-file
        std::ofstream outFile("Melody.txt");
        for (const auto &e : store) outFile << e << "\n";
        outFile.close();
        break;
    }

  }

  return 0;
}; // main()
