#include<iostream>
using namespace std;

int im(int n) {
    return n % 2 != 0;  // retorna 1 se for ímpar, 0 se for par
}

int main() {
    int nu, s = 0;

    std::cout<<"Digite um numero inteiro: ";
    std::cin>>nu;

    for (int i = 1; i <= nu; i++) {
        if (im(i)) {
            s += i;
        }
    }

    std::cout<<"A soma dos numeros impares ate "<< nu <<" e: "<< s << endl;
    return 0;
}
