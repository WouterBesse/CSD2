#pragma once
#include <iostream>
#include <string>

class Bass
{
  public:
    Bass();
    ~Bass();
    void userinput();
    void note();
    void show();
    void PoS(std::string aBass);
  private:
    std::string aBass;
};
