#include <iostream>
#include <cstdlib>
#include "pointerclass.h"


main() {
  PC PointerClass;
    // Opdracht Pointer B
    std::cout << "~~~~~~~~~~~~~~~~ Assignment B ~~~~~~~~~~~~~~~~" << std::endl;
    std::cout << " " << std::endl;
    int nummer = 21;
    int* nummerpointer;
    nummerpointer = &nummer;
    int& nummerref = nummer;
    std::cout << "~~~~~~~~~~~~~~~~ Variable ~~~~~~~~~~~~~~~~" << std::endl;
    std::cout << "Getal voor functie: ";
    std::cout << nummer << std::endl;
    nummer = PointerClass.pointfunk(nummer);
    std::cout << "~~~~~~~~~~~~~~~~ Pointer ~~~~~~~~~~~~~~~~" << std::endl;
    std::cout << "Getal voor functie: ";
    std::cout << *nummerpointer << std::endl;
    *nummerpointer = PointerClass.pointfunk(*nummerpointer);
    std::cout << "~~~~~~~~~~~~~~~~ Reference ~~~~~~~~~~~~~~~~" << std::endl;
    std::cout << "Getal voor functie: ";
    std::cout << nummerref << std::endl;
    nummerref = PointerClass.pointfunk(nummerref);
    std::cout << "~~~~~~~~~~~~~~~~ Ending Values ~~~~~~~~~~~~~~~~" << std::endl;
    std::cout << "Variable na functie: ";
    std::cout << nummer << std::endl;
    std::cout << "Variable location: '";
    std::cout << &nummer ;
    std::cout << "', variable seems to operate on the same location" << std::endl;
    std::cout << "Pointer na functie: ";
    std::cout << *nummerpointer << std::endl;
    std::cout << "Pointer location: '";
    std::cout << &nummerpointer ;
    std::cout << "', pointer seems to be a copy on a different location" << std::endl;
    std::cout << "Reference na functie: ";
    std::cout << nummerref << std::endl;
    std::cout << "Reference location: '";
    std::cout << &nummerref ;
    std::cout << "', reference seems to operate on the same location" << std::endl;

    // Opdracht Pointer C en D
  std::cout << " " << std::endl;
  std::cout << " " << std::endl;
  std::cout << " " << std::endl;
  std::cout << "~~~~~~~~~~~~~~~~ Assignment C and D ~~~~~~~~~~~~~~~~" << std::endl;
  std::cout << " " << std::endl;
  std::cout << "Starting to set values and create objects" << std::endl;
  PC PointerClass1;
  PC PointerClass2;
  PC PointerClass3;
  PC PointerClass4;
  PC PointerClass5;
  PC PointerClass6;
  PC* PointerClassPointer;
  PointerClassPointer = &PointerClass3;
  PointerClassPointer->setter(5);
  PointerClassPointer->getter();
  PC *ptray=new PC[50];

  for (int i =0; i < 50; i++) {
    int rndm;
    rndm = rand() % 100;
    ptray[i].setter(rndm);
    std::cout << "Set value of object ";
    std::cout << i;
    std::cout << " to: ";
    std::cout << rndm << std::endl;
  }
  std::cout << "Finished setting values and creating objects" << std::endl;
  std::cout << "Getting all values from objects" << std::endl;
  for (int i =0; i < 50; i++) {
    std::cout << "The value of object ";
    std::cout << i;
    std::cout << " is: ";
    std::cout << ptray[i].getter() << std::endl;
  }
  delete[] ptray;


}
