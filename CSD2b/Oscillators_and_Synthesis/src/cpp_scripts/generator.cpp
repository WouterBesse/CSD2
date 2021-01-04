#include <iostream>
#include "../headers/generator.h"
#include <cstdlib>

Generator::Generator(){
}

Generator::~Generator() {

}

int Generator::generate() {
  return rand() % 6000 + 200;
}
