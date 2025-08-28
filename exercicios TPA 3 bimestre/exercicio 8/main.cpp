#include <iostream>
#include <cmath>

using namespace std;

const double PI = 3.141592653589793;

double areaCirculo(double raio) {
    return PI * raio * raio;
}

int main() {
    double raio, somaAreas = 0.0;

    for (int i = 1; i <= 5; ++i) {
        std::cout << "digite o raio do circulo " << i << ": ";
        std::cin >> raio;
        somaAreas += areaCirculo(raio);
    }

    std::cout << "A soma das areas dos 5 circulos e: " << somaAreas << endl;

    return 0;
}
