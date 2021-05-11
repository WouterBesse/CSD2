cmake_minimum_required(VERSION 3.17)
project(MijnSimdFeestje)

add_executable(simdInst SIMD_Oefeningen.cpp)

target_compile_features(simdInst PRIVATE cxx_std_17)