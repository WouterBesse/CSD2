#pragma once
#include <string>
#include <iostream>
#include "instruments.h"

class Trumpet : public Instruments
{
public:
  Trumpet(); // constructor
  ~Trumpet(); // destructor
  void NoT(std::string aNoT);
  void userinput();
private:
  std::string aNoT;
};
