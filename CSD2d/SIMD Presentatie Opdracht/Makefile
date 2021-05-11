CXX = g++
CXXFLAGS = -mavx
SOURCE= SIMD_Oefeningen_Antwoorden.o

Mijn_SIMD_Feestje: $(SOURCE)
	$(CXX) -o $@ $(CXXFLAGS)  $(SOURCE)

.o:
	$(CXX) -c $(CXXFLAGS) $<

clean:
	rm -f example *.o