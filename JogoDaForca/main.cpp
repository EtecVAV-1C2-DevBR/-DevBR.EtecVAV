#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cctype>

int main() {
    srand(time(NULL));

    std::cout << "Bem-vindo ao Jogo da Forca! Tema: Esportes.\n";
    std::cout << "Tente adivinhar o nome de um esporte!\n\n";

    char banco[17][20] = {
        "futebol", "voleibol", "basquete", "jiujitsu", "handebol",
        "natacao", "tenis", "boxe", "motocross", "ciclismo",
        "xadrez", "dama", "beisebol", "skate", "surfe",
        "judo", "karate"
    };

    char opcao;
    do {
        int indice = rand() % 17;  
        char palavra[20];
        strcpy(palavra, banco[indice]);
        int totalLetras = strlen(palavra);

        char mascara[20];
        for (int i = 0; i < totalLetras; i++) {
            mascara[i] = '_';
        }
        mascara[totalLetras] = '\0';

        int acertos = 0;
        int erros = 0;
        const int maxErros = 10;

        char letrasUsadas[26] = {0};
        int qtdLetrasUsadas = 0;

        std::cout << " JOGO DA FORCA \n";

        bool jogoAtivo = true;
        while (jogoAtivo) {
            std::cout << "Palavra: " << mascara << std::endl;
            std::cout << "Erros: " << erros << "/" << maxErros << std::endl;
            std::cout << "Acertos: " << acertos << "/" << totalLetras << std::endl;
            std::cout << "Digite uma letra: ";
            std::cin >> opcao;
            std::cin.ignore(); 
            char palpite = toupper(opcao);

            if (letrasUsadas[palpite - 'A'] != 0) {
                std::cout << "Letra ja usada! Tente outra.\n\n";
                continue;
            }

            letrasUsadas[palpite - 'A'] = palpite;
            qtdLetrasUsadas++;

            bool achou = false;
            for (int i = 0; i < totalLetras; i++) {
                if (toupper(palavra[i]) == palpite) {
                    mascara[i] = palavra[i];
                    acertos++;
                    achou = true;
                }
            }

            if (!achou) {
                erros++;
                std::cout << "Letra nao encontrada! Erro " << erros << ".\n\n";
            } else {
                std::cout << "Letra encontrada! Atualizando...\n\n";
            }

            if (acertos == totalLetras) {
                std::cout << "Parabens! Voce acertou a palavra: " << palavra << std::endl;
                jogoAtivo = false;
            } else if (erros == maxErros) {
                std::cout << "Que pena! Voce perdeu. A palavra era: " << palavra << std::endl;
                jogoAtivo = false;
            }
        }

        std::cout << "\nDeseja jogar novamente? (s/n): ";
        std::cin >> opcao;
        opcao = toupper(opcao);
        std::cout << std::endl;
    } while (opcao == 'S');

    std::cout << "Obrigado por jogar! Ate a proxima.\n";
    return 0;
}

