#include <iostream>
#include <string>
#include "trumpet.h"
#include "WTP.h"

Trumpet::Trumpet()
{
}

Trumpet::~Trumpet()
{
}

void Trumpet::NoT(std::string aNoT)
{
  if (aNoT == "noot") {
    std::cout << "N00T" << std::endl;
  } else if (aNoT == "toot") {
    std::cout << "T00T" << std::endl;
  } else {
    std::cout << "Hellaas dat kan niet doei" << std::endl;
  }
}

void Trumpet::userinput()
{
  std::cout << "Tell me, do you want to play a noot or a toot? (type 'noot' or 'toot')" << std::endl;
  std::cin >> aNoT;
  NoT(aNoT);
}
