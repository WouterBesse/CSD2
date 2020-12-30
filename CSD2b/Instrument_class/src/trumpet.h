#pragma once
#include <string>


class Trumpet
{
public:
  Trumpet(); // constructor
  ~Trumpet(); // destructor
  void NoT(std::string aNoT);
  void userinput();
private:
  std::string aNoT;
};
