#include <iostream>
#include <string>
#include "bass.h"

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
    snd = "Badoem PA!";
    sound(snd);
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
