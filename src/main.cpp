#include <iostream>
#include <string>

int pown(int x, int y) {
    int temp = 1;
    for (int i = 0; i < y; i++) {
        temp *= x;
    }
    return temp;
}

int main(int argc, char** argv) {
    for (int i = 1; i < argc; i++) std::cout << std::string(argv[i]) + ": " + std::to_string(i) << "\n";

    std::cout << "2 to the power of 30: " << pown(2, 30) << "\n";
    return 0;
}