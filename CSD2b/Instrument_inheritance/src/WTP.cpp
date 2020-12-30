#include <iostream>
#include <string>
#include "trumpet.h"
#include "bass.h"
#include "WTP.h"

WTP::WTP()
{
  trompetteke = Trumpet();
  basske = Bass();
  instrumentke = Instruments();
}

WTP::~WTP()
{
}

void WTP::userinput()
{
  std::cout << "Good day, what sound would you like to play? Choose 1 for trumpet" << std::endl;
  std::cout << "Choose 1 for trumpet" << std::endl;
  std::cout << "Choose 2 for bass" << std::endl;
  std::cin >> aWTP;
  if (aWTP == 1){
    trompetteke.userinput();
  } else if (aWTP == 2){
      basske.userinput();
  } else {
      std::cout << "Helaas ken dat niet :(" << std::endl;
    }
}
