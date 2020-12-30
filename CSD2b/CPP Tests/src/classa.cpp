#include <iostream>
#include "classa.h"

World::World(int year) : year(year)
{
  std::cout << "This world begins" << std::endl;
}

World::~World()
{
  std::cout << "This world ends" << std::endl;
}

void World::hello(int year)
{
  std::cout << "Ehlo ni eth reay " << year << std::endl;
}

void World::userinput()
{
  std::cout << "Wha year es et?" << std::endl;
  std::cin >> year;
  hello(year);
}
