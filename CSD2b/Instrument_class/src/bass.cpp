
#include <iostream>
#include <string>
#include "bass.h"
#include "WTP.h"

Bass::Bass()
{
}

Bass::~Bass()
{
}

void Bass::PoS(std::string aBass)
{
  if (aBass == "show") {
    show();
  } else if (aBass == "play") {
    std::cout << "Swam!" << std::endl;
  } else {
    std::cout << "Hellaas dat kan niet doei" << std::endl;
  }
}

void Bass::show()
{
  std::cout << "                                                      ████    " <<std::endl;
  std::cout << "                                              ██  ██  ████████" <<std::endl;
  std::cout << "                                              ▓▓▓▓██▓▓▓▓██    " <<std::endl;
  std::cout << "                                              ██▓▓▓▓          " <<std::endl;
  std::cout << "                                              ▓▓██            " <<std::endl;
  std::cout << "                                            ░░▓▓              " <<std::endl;
  std::cout << "                                          ██▓▓                " <<std::endl;
  std::cout << "                                        ░░▓▓▒▒                " <<std::endl;
  std::cout << "                                        ░░▓▓                  " <<std::endl;
  std::cout << "                                      ▓▓▓▓                    " <<std::endl;
  std::cout << "                                    ▒▒                        " <<std::endl;
  std::cout << "                                ▒▒██▓▓                        " <<std::endl;
  std::cout << "                              ▓▓▓▓▓▓                          " <<std::endl;
  std::cout << "                            ▒▒▓▓▓▓                            " <<std::endl;
  std::cout << "                  ░░▒▒      ██▒▒░░                            " <<std::endl;
  std::cout << "                ░░░░      ▒▒▓▓                                " <<std::endl;
  std::cout << "              ░░░░      ▓▓░░▒▒                                " <<std::endl;
  std::cout << "              ░░░░    ▒▒▓▓▓▓                                  " <<std::endl;
  std::cout << "            ░░░░░░▒▒▒▒▓▓▓▓                                    " <<std::endl;
  std::cout << "            ░░░░░░▒▒▓▓▓▓                                      " <<std::endl;
  std::cout << "        ░░░░░░░░▒▒▒▒▒▒                                        " <<std::endl;
  std::cout << "    ░░░░░░░░░░░░▒▒▒▒▒▒    ▓▓                                  " <<std::endl;
  std::cout << "  ░░░░░░░░░░▓▓░░░░▒▒░░░░░░░░                                  " <<std::endl;
  std::cout << "  ░░░░░░░░░░▓▓▒▒░░░░░░░░░░░░                                  " <<std::endl;
  std::cout << "░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░                                    " <<std::endl;
  std::cout << "░░░░░░░░▓▓░░▒▒▓▓░░░░░░                                        " <<std::endl;
  std::cout << "░░░░░░░░▒▒▓▓░░▒▒░░░░                                          " <<std::endl;
  std::cout << "  ░░▓▓▓▓░░▒▒░░░░░░░░                                          " <<std::endl;
  std::cout << "  ░░▓▓██▓▓░░░░▒▒░░░░                                          " <<std::endl;
  std::cout << "    ▒▒██▒▒░░░░░░░░                                            " <<std::endl;
  std::cout << "      ▒▒░░▒▒░░░░░░                                            " <<std::endl;
  std::cout << "        ░░░░░░░░                                              " <<std::endl;

}

void Bass::userinput()
{
  std::cout << "Tell me, do you want me to show the bass or play da bass? (type 'show' or 'play')" << std::endl;
  std::cin >> aBass;
  PoS(aBass);
}
