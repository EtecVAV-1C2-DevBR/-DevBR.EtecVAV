#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

using namespace std;

int soma(int x, int y){
    return x + y;
}

int subtracao(int x, int y){
    return x - y;
}

int mult(int x, int y){
    return x * y;
}

float divisao(int x, int y){
    if (y == 0) {
        std::cout << " Erro: divisao por zero!" << endl;
        return 0;
    }
    return (float)x / y;
}

int main() {
    int x, y;
    float resultado; 
    char resposta = 's';

    while(resposta == 's'){
        std::cout << "Qual o primeiro numero? ";
        std::cin >> x;

        std::cout << "Qual o segundo numero? ";
        std::cin >> y;

        resultado = soma(x, y);
        std::cout << x << " + " << y << " = " << resultado;

        resultado = subtracao(x, y);
        std::cout << "\n" << x << " - " << y << " = " << resultado;

        resultado = mult(x, y);
        std::cout << "\n" << x << " * " << y << " = " << resultado;

        resultado = divisao(x, y);
        std::cout << "\n" << x << " / " << y << " = " << resultado;

        std::cout << "\nDeseja continuar? (s/n): ";
        std::cin >> resposta; 
    }
    return 0;
}
