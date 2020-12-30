#pragma once
#include <iostream>
#include <string>
#include "instruments.h"

class Bass : public Instruments
{
  public:
    Bass();
    ~Bass();
    void userinput();
    void show();
    void PoS(std::string aBass);
  private:
    std::string aBass;
};
