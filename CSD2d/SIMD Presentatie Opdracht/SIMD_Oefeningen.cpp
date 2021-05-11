//
// Maak de leuke oefeningen!
//

#include <iostream>
#include <vector>
#include <immintrin.h>

int main() {

    // Tel de vectors firstOne( 1.2f, 6.3f, 2.1f, 8.8f, 7.2f, 2.1f, 4.9f, 6.1f ) en secondOne( 2.6f, 6.1f, 7.7f, 1.8f, 4.2f, 2.5f, 1.3f, 6.2f ) bij elkaar op in de vector firstResult

    std::cout << "firstResult = ";
    for(int i = 0; i < 8; i++){
        std::cout << ((float *)&firstResult)[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "Wat valt je op aan de volgorde van de waardes? \n";
    std::cout << std::endl;

    // leuk feit om direct te melden, als je snel één van de waardes wil accessen
    // dan kun je dat doen met ((dataType *)&naamVector)[index]

    // Vermenigvuldig nu firstResult met firstOne naar secondResult
    // doe dit met _mm_mul_ps



    // Trek nu secondOne van secondResult af en zet dit in thirdResult
    // Probeer hiervoor de syntax te vinden door bijvoorbeeld te Googlen of één van deze bronnen te gebruiken:
    // https://software.intel.com/sites/landingpage/IntrinsicsGuide/



    // Deze vraag is voor de doorzetters:
    // Tel alle waardes van thirdResult bij elkaar op naar één float
    // Er zijn meerdere manieren om dit te doen, sommige sneller dan anderen
    // Sommige manieren gebruiken niet eens SIMD instructies hiervoor

    // Bronnen die je hiervoor kunnen helpen, maar daarbij ook heel verwarrend zijn:
    // https://stackoverflow.com/questions/13219146/how-to-sum-m256-horizontally
    // https://stackoverflow.com/questions/13879609/horizontal-sum-of-8-packed-32bit-floats
    // Het is mij niet gelukt om deze voorbeelden direct aan de praat te krijgen,
    // maar heb er wel goede delen van kunnen gebruiken voor potentiele oplossingen




    return(0);
}