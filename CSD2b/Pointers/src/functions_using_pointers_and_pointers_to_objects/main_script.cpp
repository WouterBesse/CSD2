#include <iostream>
#include "pointerclass.h"


main() {
  PC PointerClass;

    // Opdracht Pointer B
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

    // Opdracht Pointer C
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


}
