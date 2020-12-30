#pragma once
#include "trumpet.h"
#include "bass.h"
#include <iostream>

class WTP
{
  public:
    WTP();
    ~WTP();
    void userinput();
  private:
    Bass basske;
    Trumpet trompetteke;
    int aWTP;
};
