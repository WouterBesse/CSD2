// Je zult je vast afvragen waarom ik niet deze class heb gebruikt, eerlijk gezegd weet ik het ook niet. De enige reden is dat niks meer normaal afspeelt als ik deze class aanroep :(


#include <iostream>
#include "../headers/Tri.h"

Tri::Tri(){
}

Tri::~Tri() {

}

float Tri::getsTick(float tphase) {
  tickvalue = 0.9 * asin(sin(tphase * 3.14159265358979323846 * 2.0f )) * (2.0 / 3.14159265358979323846);
  return tickvalue;
}
