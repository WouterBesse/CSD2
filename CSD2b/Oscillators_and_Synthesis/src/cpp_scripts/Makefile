CXX = g++
CXXFLAGS = -Ic:/Program\ Files/JACK2/include -Wall -std=c++1z
LDFLAGS= -Lc:/Program\ Files/JACK2/lib32 -llibjack
SOURCE= sine.o oscillator.o main.o jack_module.o sqr.o
HEADERS:= $(wildcard ./*.h)

example: $(SOURCE) $(HEADERS)
	$(CXX) -o $@ $(CXXFLAGS) $(SOURCE) $(LDFLAGS)

.cpp.o: $(HEADERS)
	$(CXX) -c $(CXXFLAGS) $<

clean:
	rm -f example *.o
