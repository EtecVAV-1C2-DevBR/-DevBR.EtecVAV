#include <iostream>
#include <vector>

enum Ordenacao {
    CRESCENTE,
    DECRESCENTE,
    NAO_ORDENADA
};

Ordenacao verificaOrdem(const std::vector<int>& numeros) {
    bool crescente = true;
    bool decrescente = true;

    for (size_t i = 1; i < numeros.size(); ++i) {
        if (numeros[i] < numeros[i-1]) {
            crescente = false;
        }
        if (numeros[i] > numeros[i-1]) {
            decrescente = false;
        }
    }

    if (crescente) return CRESCENTE;
    if (decrescente) return DECRESCENTE;
    return NAO_ORDENADA;
}

int main() {
    std::vector<int> numeros(5);

    std::cout << "Digite 5 numeros:\n";
    for (int i = 0; i < 5; ++i) {
        std::cin >> numeros[i];
    }

    std::cout << "Numeros digitados: ";
    for (size_t i = 0; i < numeros.size(); i++) {
        std::cout << numeros[i] << " ";
    }
    std::cout << std::endl;

    Ordenacao ordem = verificaOrdem(numeros);

    switch (ordem) {
        case CRESCENTE:
            std::cout << "Os numeros estao em ordem crescente.\n";
            break;
        case DECRESCENTE:
            std::cout << "Os numeros estao em ordem decrescente.\n";
            break;
        default:
            std::cout << "Os numeros nao estao ordenados.\n";
            break;
    }

    return 0;
}
