CXX:= g++
CXXFLAGS:= -Ic:/Program\ Files/JACK2/include -Wall -std=c++1z
LDFLAGS:= -Lc:/Program\ Files/JACK2/lib32 -llibjack
SOURCE:=$(wildcard cpp_scripts/*.cpp)
HEADERS:=$(wildcard headers/*.h)
OBJECTS:=$(patsubst cpp_scripts/%.cpp,%.o,$(SOURCE))

example: $(OBJECTS)
	$(CXX) -o $@ $(CXXFLAGS) $(OBJECTS) $(LDFLAGS)

%.o:
	$(CXX) -c $(CXXFLAGS) $(SOURCE) $(HEADERS) $<

clean:
	rm -f example %.o
