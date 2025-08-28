#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
    char sexo, resposta;
    double altura, pesoideal;
    
    resposta = 's';

    while (resposta == 's') {
        std::cout << "\nQual o sexo (f/m)? ";
        std::cin >> sexo;

        std::cout << "Qual a sua altura (em metros)? ";
        std::cin >> altura;

        if (sexo == 'f' || sexo == 'F') {
            pesoideal = 62.1 * altura - 44.7;
        } else if (sexo == 'm' || sexo == 'M') {
            pesoideal = 72.7 * altura - 58;
        } else {
            std::cout << "Sexo invalido.\n";
            continue; 
        }

        std::cout << "\nSeu peso ideal e: " << pesoideal;

		std::cout << "\nDeseja continuar (s/n)? ";
    	std::cin >> resposta;
    }
    return 0;
}
