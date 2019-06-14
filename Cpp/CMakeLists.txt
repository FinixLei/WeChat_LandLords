cmake_minimum_required (VERSION 2.6)
project (SolvePuzzle)

add_compile_options(-std=c++11)

include_directories("./")

add_executable(solve_puzzle 
    solve_puzzle.cpp 
    utils.hpp 
    MoveGener.hpp 
    MoveClassifier.hpp 
    MoveFilter.hpp 
    MovePlayer.hpp 
    MinMax.hpp
)

find_package(Threads REQUIRED)

target_link_libraries(solve_puzzle ${CMAKE_THREAD_LIBS_INIT})
