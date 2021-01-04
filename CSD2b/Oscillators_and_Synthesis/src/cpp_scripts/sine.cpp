#include <iostream>
#include "../headers/sine.h"

Sine::Sine(){
}

Sine::~Sine() {

}

float Sine::getTick(float phase) {
  tickvalue = 0.9 * sin(phase * M_PI * 2.0f );
  return tickvalue;
}
