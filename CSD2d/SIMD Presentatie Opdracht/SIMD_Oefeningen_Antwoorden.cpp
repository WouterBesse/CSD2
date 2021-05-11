//
// Maak de leuke oefeningen!
//

#include <iostream>
#include <vector>
#include <immintrin.h>

int main() {

    // Tel de vectors firstOne( 1.2f, 6.3f, 2.1f, 8.8f, 7.2f, 2.1f, 4.9f, 6.1f ) en secondOne( 2.6f, 6.1f, 7.7f, 1.8f, 4.2f, 2.5f, 1.3f, 6.2f ) bij elkaar op in de vector firstResult

    __m256 firstOne = _mm256_set_ps( 1.2f, 6.3f, 2.1f, 8.8f, 7.2f, 2.1f, 4.9f, 6.1f );
    __m256 secondOne = _mm256_set_ps( 2.6f, 6.1f, 7.7f, 1.8f, 4.2f, 2.5f, 1.3f, 6.2f );

    __m256 firstResult = _mm256_add_ps( firstOne, secondOne );

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

    __m256 secondResult = _mm256_mul_ps( firstOne, firstResult );

    // Trek nu secondOne van secondResult af en zet dit in thirdResult
    // Probeer hiervoor de syntax te vinden door bijvoorbeeld te Googlen of één van deze bronnen te gebruiken:
    // https://software.intel.com/sites/landingpage/IntrinsicsGuide/

    __m256 thirdResult = _mm256_sub_ps( secondResult, secondOne );

    // Deze vraag is voor de doorzetters:
    // Tel alle waardes van thirdResult bij elkaar op naar één float
    // Er zijn meerdere manieren om dit te doen, sommige sneller dan anderen
    // Sommige manieren gebruiken niet eens SIMD instructies hiervoor

    // Manier 1
    float Antwoord1 = 0;

    for(int i = 0; i < 8; i++){
        Antwoord1 += ((float *)&thirdResult)[i];
    }
    std::cout << "Antwoord1 =" << Antwoord1 << std::endl;

    // Manier 2
    float Antwoord2;

    __m256 tmp = _mm256_hadd_ps( thirdResult, thirdResult );
    tmp = _mm256_hadd_ps( tmp, tmp );
    Antwoord2 = ((float*)&tmp)[3] + ((float*)&tmp)[4];

    std::cout << "Antwoord2 =" << Antwoord2 << std::endl;

    // Manier 3, beetje omslachtig maar kan ook
    // Kan zelf geen moment bedenken waarop dit optimaal is in vergelijking met manier 2

    float Antwoord3;

    tmp = _mm256_hadd_ps( thirdResult, thirdResult );
    __m256d casted = _mm256_castps_pd(tmp);
    __m128 hi = _mm_castpd_ps(_mm256_extractf128_pd(casted, 1));
    __m128 lo = _mm_castpd_ps(_mm256_castpd256_pd128(casted));
    __m128 odd  = _mm_shuffle_ps(hi, lo, _MM_SHUFFLE(3,1,3,1));
    __m128 even = _mm_shuffle_ps(lo, hi, _MM_SHUFFLE(2,0,2,0));
    __m128 together = _mm_add_ps(even, odd);

    Antwoord3 = ((float*)&together)[1] + ((float*)&together)[2];

    std::cout << "Antwoord3 =" << Antwoord3 << std::endl;

    return(0);
}