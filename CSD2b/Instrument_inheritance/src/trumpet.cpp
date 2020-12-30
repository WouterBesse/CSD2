#include <iostream>
#include <string>
#include "trumpet.h"
#include "instruments.h"

Trumpet::Trumpet()
{
}

Trumpet::~Trumpet()
{
}

void Trumpet::NoT(std::string aNoT)
{
  if (aNoT == "noot") {
    snd = "N00T";
    sound(snd);
  } else if (aNoT == "toot") {
    snd = "T00T";
    sound(snd);
  } else {
    std::cout << "Helaas dat kan niet doei" << std::endl;
  }
}

void Trumpet::userinput()
{
  std::cout << "Tell me, do you want to play a noot or a toot? (type 'noot' or 'toot')" << std::endl;
  std::cin >> aNoT;
  NoT(aNoT);
}
