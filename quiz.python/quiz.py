import random

# 
# Banco de perguntas

perguntas = [

{
    "pergunta": "Quem é considerado um dos criadores do Arduino?",
    "alternativas": ["Linus Torvalds", "Massimo Banzi", "Bill Gates", "Alan Turing", "Ken Thompson"],
    "correta": 1
},

{
    "pergunta": "O Arduino foi criado para atender inicialmente qual público?",
    "alternativas": ["Engenheiros militares", "Estudantes e designers", "Redes corporativas", "Automação industrial", "Jogos eletrônicos"],
    "correta": 1
},

{
    "pergunta": "O Arduino começou como um projeto desenvolvido em:",
    "alternativas": ["MIT", "Harvard", "Stanford", "Instituto Ivrea", "Google Labs"],
    "correta": 3
},

{
    "pergunta": "O nome 'Arduino' veio de:",
    "alternativas": ["Um microcontrolador antigo", "Um bar na Itália", "Uma cidade", "Um programador famoso", "Um acrônimo técnico"],
    "correta": 1
},

{
    "pergunta": "O principal objetivo inicial do Arduino era:",
    "alternativas": ["Concorrer com o Raspberry Pi", "Substituir PCs", "Facilitar a prototipagem eletrônica", "Criar novos jogos", "Gerar imagens 3D"],
    "correta": 2
},

{
    "pergunta": "Qual o microcontrolador padrão do Arduino Uno?",
    "alternativas": ["ATmega32U4", "ATmega2560", "ATmega328P", "ESP8266", "RP2040"],
    "correta": 2
},

{
    "pergunta": "Qual placa possui 54 portas digitais e 16 analógicas?",
    "alternativas": ["Nano", "Due", "Mega 2560", "Pro Mini", "Leonardo"],
    "correta": 2
}, 

{
    "pergunta": "Qual placa é famosa por seu tamanho reduzido?",
    "alternativas": ["Mega", "Nano", "Due", "Zero", "Portenta"],
    "correta": 1
},

{
    "pergunta": "A placa Arduino com maior poder de processamento é:",
    "alternativas": ["Uno", "Micro", "Portenta H7", "Nano Every", "Mega"],
    "correta": 2
},

{
    "pergunta": "Qual placa usa o microcontrolador SAM3X8E ARM Cortex-M3?",
    "alternativas": ["Nano", "Due", "Uno", "Micro", "Mini"],
    "correta": 1
},

{
    "pergunta": "Qual Arduino possui comunicação nativa USB?",
    "alternativas": ["Uno R3", "Mega 2560", "Nano", "Leonardo", "Mini"],
    "correta": 3
},

{
    "pergunta": "Qual placa é mais indicada para projetos vestíveis?",
    "alternativas": ["Mega", "Nano", "LilyPad", "Uno", "Pro Mini"],
    "correta": 2
},

{
    "pergunta": "A porta VIN do Arduino serve para:",
    "alternativas": ["Comunicação USB", "Saída 5V", "Entrada de alimentação", "Controle PWM", "Reset"],
    "correta": 2
},

{
    "pergunta": "A função do regulador de tensão no Arduino é:",
    "alternativas": ["Gerar sinais PWM", "Estabilizar a tensão recebida", "Controlar corrente", "Armazenar energia", "Transformar AC em DC"],
    "correta": 1
},

{
    "pergunta": "O cristal oscilador do Arduino define:",
    "alternativas": ["O clock do microcontrolador", "A tensão máxima", "A potência dos pinos", "O modo de comunicação", "A temperatura"],
    "correta": 0
},

{
    "pergunta": "O microcontrolador é responsável por:",
    "alternativas": ["Converter áudio", "Executar o código gravado", "Regular tensão", "Gerar potência", "Enviar vídeo"],
    "correta": 1
},

{
    "pergunta": "A porta 3.3V do Arduino fornece:",
    "alternativas": ["Sinal PWM", "Tensão regulada baixa", "Clock", "Comunicação serial", "Reset automático"],
    "correta": 1
}, 

{
    "pergunta": "A porta AREF é usada para:",
    "alternativas": ["Referência analógica", "Sinal digital", "PWM", "Reset", "Clock externo"],
    "correta": 0
},

{
    "pergunta": "O que define o número de portas em uma placa Arduino?",
    "alternativas": ["Tipo de caixa", "Tamanho da placa", "Microcontrolador utilizado", "Material da placa", "Número de LEDs"],
    "correta": 2
},

{
    "pergunta": "As portas analógicas do Arduino Uno são:",
    "alternativas": ["A0–A5", "D0–D13", "PWM0–PWM6", "RX–TX", "P0–P7"],
    "correta": 0
},

{
    "pergunta": "As portas digitais com PWM possuem:",
    "alternativas": ["Cor azul", "Símbolo ~", "Letra P", "Número em vermelho", "Letra M"],
    "correta": 1
},

{
    "pergunta": "O conversor ADC do Arduino Uno tem resolução de:",
    "alternativas": ["6 bits", "8 bits", "10 bits", "12 bits", "14 bits"],
    "correta": 2
},

{
    "pergunta": "A porta RX é usada para:",
    "alternativas": ["Enviar dados", "Receber dados", "Gerar clock", "PWM", "Reset"],
    "correta": 1
},

{
    "pergunta": "Qual frequência do PWM no Arduino Uno?",
    "alternativas": ["30 Hz", "100 Hz", "490 Hz", "10 kHz", "1 MHz"],
    "correta": 2
},

{
    "pergunta": "O pino 13 do Arduino Uno inclui:",
    "alternativas": ["GND", "LED integrado", "Porta analógica", "I2C", "Vin"],
    "correta": 1
},

{
    "pergunta": "O que caracteriza um pino digital?",
    "alternativas": ["Apenas saída", "Somente entrada", "Leitura e escrita binária", "Somente analógico", "Alta corrente"],
    "correta": 2
},

{
    "pergunta": "Qual função executa uma única vez no início do programa?",
    "alternativas": ["start()", "main()", "setup()", "loop()", "init()"],
    "correta": 2
},

{
    "pergunta": "Qual extensão de arquivo é usada na IDE Arduino?",
    "alternativas": [".ard", ".ino", ".cpp", ".py", ".hex"],
    "correta": 1
},

{
    "pergunta": "Qual comando define o modo de uma porta digital?",
    "alternativas": ["pinMode()", "digitalMode()", "setPin()", "gpioMode()", "pinSet()"],
    "correta": 0
},

{
    "pergunta": "Qual comando liga uma saída digital?",
    "alternativas": ["write()", "digitalWrite()", "setOutput()", "pinOn()", "turnHigh()"],
    "correta": 1
},

{
    "pergunta": "Qual biblioteca é usada para comunicação serial?",
    "alternativas": ["Wire", "SPI", "Serial", "EEPROM", "SoftwareServo"],
    "correta": 2
},

{
    "pergunta": "A função delay() recebe valores em:",
    "alternativas": ["Microsegundos", "Milissegundos", "Segundos", "Minutos", "Ciclos de clock"],
    "correta": 1
},

{
    "pergunta": "O comando analogRead() retorna valores entre:",
    "alternativas": ["0–255", "0–100", "0–1023", "0–500", "0–4095"],
    "correta": 2
},

{
    "pergunta": "Qual componente é usado para medir luminosidade?",
    "alternativas": ["LDR", "DHT11", "HC-SR04", "BMP180", "Reed Switch"],
    "correta": 0
},

{
    "pergunta": "Qual sensor mede temperatura e umidade?",
    "alternativas": ["Gyro", "DHT11", "LDR", "RFID", "Ultrassônico"],
    "correta": 1
},

{
    "pergunta": "O servo motor é controlado por:",
    "alternativas": ["PWM", "I2C", "SPI", "Serial", "TCP/IP"],
    "correta": 0
},

{
    "pergunta": "Qual shield adiciona comunicação Wi-Fi?",
    "alternativas": ["Data Logger", "Ethernet Shield", "WiFi Shield", "Motor Shield", "LCD Shield"],
    "correta": 2
},

{
    "pergunta": "Qual módulo é usado para RFID?",
    "alternativas": ["ESP32", "MPU6050", "RC522", "HC-05", "L298N"],
    "correta": 2
},

{
    "pergunta": "O módulo HC-05 é usado para:",
    "alternativas": ["Wi-Fi", "Bluetooth", "RFID", "I2C", "Ethernet"],
    "correta": 1
},

{
    "pergunta": "Qual sensor mede aceleração e giroscópio?",
    "alternativas": ["MQ-2", "BMP280", "MPU6050", "TSOP", "RTC DS1307"],
    "correta": 2
},

{
    "pergunta": "Qual protocolo usa SDA e SCL?",
    "alternativas": ["SPI", "UART", "I2C", "CAN", "Ethernet"],
    "correta": 2
},

{
    "pergunta": "O SPI utiliza quantas linhas principais?",
    "alternativas": ["2", "3", "4", "5", "6"],
    "correta": 2
},

{
    "pergunta": "A taxa de transmissão usual para comunicação serial é:",
    "alternativas": ["4800", "7200", "9600", "12800", "56000"],
    "correta": 2
},

{
    "pergunta": "Qual módulo integra Wi-Fi e Bluetooth?",
    "alternativas": ["HC-05", "ESP01", "ESP32", "RC522", "NRF24L01"],
    "correta": 2
},

{
    "pergunta": "A comunicação UART utiliza:",
    "alternativas": ["CLK e DATA", "SDA e SCL", "MOSI e MISO", "RX e TX", "TX e CLK"],
    "correta": 3
},

{
    "pergunta": "A tensão máxima recomendada nos pinos digitais do Uno é:",
    "alternativas": ["3.3V", "5V", "7V", "9V", "12V"],
    "correta": 1
},

{
    "pergunta": "A função do resistor em série com LED é:",
    "alternativas": ["Aumentar brilho", "Evitar sobrecorrente", "Gerar clock", "Armazenar carga", "Converter AC"],
    "correta": 1
},

{
    "pergunta": "Qual cuidado é essencial ao alimentar o Arduino por fonte externa?",
    "alternativas": ["Trocar o bootloader", "Evitar ligar GND", "Checar polaridade e tensão", "Desativar PWM", "Trocar cristal"],
    "correta": 2
},

{
    "pergunta": "O Arduino é muito utilizado para:",
    "alternativas": ["Renderização 3D", "Prototipagem eletrônica", "Edição de vídeo", "Compilação de software", "Jogos AAA"],
    "correta": 1
},

{
    "pergunta": "Um exemplo comum de aplicação com Arduino é:",
    "alternativas": ["Gerador de energia elétrica", "Controle de motores e sensores", "Renderização gráfica", "Placa-mãe de PC", "Servidor de nuvem"],
    "correta": 1
},

]  

perguntas = perguntas[:50]


#Funções


def mostrar_menu():
    print("\n QUIZ ARDUINO ")
    print("1 - Responder Quiz")
    print("2 - Exibir as Regras")
    print("3 - Encerrar Quiz")
    return input("Escolha uma das opções acima: ")


def mostrar_regras():
    print("\n REGRAS DO QUIZ ")
    print("1. O quiz possui 20 perguntas sorteadas aleatoriamente.")
    print("2. Cada pergunta vale 0,5 ponto.")
    print("3. Alternativas são embaralhadas.")
    print("4. Nota máxima: 10 pontos.")
    print("5. Digite apenas A, B, C, D ou E como resposta.\n")


def sortear_questoes():
    return random.sample(perguntas, 20)


def exibir_questao(num, questao):
    print(f"\nPergunta {num}:")
    print(questao["pergunta"])

    alternativas = questao["alternativas"][:]
    random.shuffle(alternativas)

    indice_correto = alternativas.index(questao["alternativas"][questao["correta"]])

    letras = ["A", "B", "C", "D", "E"]

    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}) {alt}")

    return indice_correto


def verificar_resposta(indice_correto):
    letras = ["A", "B", "C", "D", "E"]
    while True:
        resposta = input("Resposta: ").upper()

        if resposta in letras:
            return letras.index(resposta) == indice_correto

        print("Resposta incorreta! Digite A, B, C, D ou E.")


def exibir_resultado(acertos):
    nota = acertos * 0.5
    print("\n RESULTADO ")
    print(f"Acertos: {acertos}/20")
    print(f"Nota final: {nota:.1f}")


# Programa Principal

def main():
    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            questoes = sortear_questoes()
            acertos = 0

            for i, q in enumerate(questoes, start=1):
                indice_correto = exibir_questao(i, q)
                if verificar_resposta(indice_correto):
                    acertos += 1

            exibir_resultado(acertos)

        elif opcao == "2":
            mostrar_regras()

        elif opcao == "3":
            print("Quiz encerrado!")
            break

        else:
            print("Opção inválida! Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()
