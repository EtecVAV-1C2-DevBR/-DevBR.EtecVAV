#include <iostream>
#include <string>
using namespace std;


string substituirVogais(string palavra) {
    string resultado = palavra;
    for (int i = 0; i < resultado.length(); i++) {
        char c = tolower(resultado[i]); 
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            resultado[i] = '*';
        }
    }
    return resultado;
}

int main() {
    string palavra;

    cout << "Digite uma palavra: ";
    cin >> palavra;

    cout << "Resultado: " << substituirVogais(palavra) << endl;

    return 0;
}
