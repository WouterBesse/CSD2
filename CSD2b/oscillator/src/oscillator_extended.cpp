#include <iostream>

class Oscillator {
public:
  Oscillator();
  ~Oscillator();
  void setFreq(float freq);
  float getFreq();
protected:
  float freq;
};

Oscillator::Oscillator() : freq(220) {
  std::cout << "Oscillator - constructor\n";
  std::cout << "Freq field contains the value: " << freq << "\n";
}

Oscillator::~Oscillator() {
  std::cout << "Oscillator - destructor\n";
}

void Oscillator::setFreq(float freq) {
  if(freq > 0 && freq < 22050) {
    this->freq = freq;
  }
  else {
    std::cout << "Yo man, foute frequentie \n";
  }
}

float Oscillator::getFreq() {
  return freq;
}

int main () {
  Oscillator osc;
  osc.setFreq(220);
  std::cout << "Freq field contains the value: " << osc.getFreq() << "\n";

  return 0;
}
