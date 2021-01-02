#include <iostream>
#include "pointerclass.h"

PC::PC()
{
}

PC::~PC()
{
}

int PC::pointfunk(int calcint)
{
  std::cout << "START FUNCTION" << std::endl;
  std::cout << "Getal voor berekening: ";
  std::cout << calcint << std::endl;
  calcint = calcint*2;
  std::cout << "Getal na berekening: ";
  std::cout << calcint << std::endl;
  std::cout << "END FUNCTION" << std::endl;
  return calcint;
}

void PC::setter(int p) {
  privar = p;
}

int PC::getter() {
  return privar;
}
