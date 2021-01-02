#pragma once
#include <iostream>

class PC
{
  public:
    PC();
    ~PC();
    int pointfunk(int calcint);
    void setter(int privar);
    int getter();
  private:
    int calcint;
    int privar;
};
