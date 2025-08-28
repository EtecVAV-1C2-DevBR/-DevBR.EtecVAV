#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int potencia(int base, int expoente){
	int resultado = 1;
	int i = 1;
	while(i <= expoente){
		resultado = base * resultado;
		i = i + 1;
	}
	return resultado;
}
	int main(int argc, char** argv){
		 int base, expoente;
		 char resposta;
		 resposta = 's';

		 while(resposta == 's'){
		 std::cout << "digite uma base: ";
		 std::cin >> base;

		 std::cout << "digite um expoente: ";
	     std::cin >> expoente;

	     int resultado = potencia(base, expoente);
	     std::cout << "\n" << base << " elevado a " << expoente << " e igual a : " << resultado;

	     std::cout << "\ndeseja continuar? (s/n): ";
	     std::cin >> resposta;
	 	}
		return 0;
	}
