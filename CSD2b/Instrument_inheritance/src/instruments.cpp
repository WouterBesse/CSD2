#include <iostream>
#include <string>
#include "instruments.h"

Instruments::Instruments()
{
}

Instruments::~Instruments()
{
}

void Instruments::sound(std::string snd)
{
  std::cout << snd << std::endl; // Show the string 'snd'
}
