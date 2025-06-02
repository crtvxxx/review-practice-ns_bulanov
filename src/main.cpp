#include <iostream>
#include <string>

int main(int argc, char** argv) {
    for (int i = 1; i < argc; i++) std::cout << std::string(argv[i]) + ": " + std::to_string(i) << "\n";
    return 0;
}