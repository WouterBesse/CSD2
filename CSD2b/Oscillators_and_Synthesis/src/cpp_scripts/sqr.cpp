#include <iostream>
#include "../headers/sqr.h"

Sqr::Sqr(){
}

Sqr::~Sqr() {

}

float Sqr::getTick(float phase) {
  qtickvalue = 0.9 * sin(phase * M_PI * 2.0f );
  if (qtickvalue > 0)
    return 1;
  else
    return -1;

  return 0;
}
