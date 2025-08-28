#include <iostream>
#include <string>
#include <cctype> 
using namespace std;

int contarVogais(string nome) {
    int cont = 0;
    for (char c : nome) {
        c = tolower(c);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            cont++;
        }
    }
    return cont;
}

int contarConsoantes(string nome) {
    int cont = 0;
    for (char c : nome) {
        c = tolower(c);
        if (isalpha(c) && !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')) {
            cont++;
        }
    }
    return cont;
}

int main() {
    string nome;

    cout << "Digite seu nome completo: ";
    getline(cin, nome); 

    int qtdVogais = contarVogais(nome);
    int qtdConsoantes = contarConsoantes(nome);

    cout << "Quantidade de vogais: " << qtdVogais << endl;
    cout << "Quantidade de consoantes: " << qtdConsoantes << endl;

    return 0;
}
