#pragma once
#include <iostream>
#include <string>

class Instruments
{
  public:
    Instruments();
    ~Instruments();
    void sound(std::string snd);
  protected:
    std::string snd;
};
