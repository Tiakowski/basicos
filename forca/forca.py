import PalavrasAleatorias


def forca():
    escolha = int(input("Escolha o numero de jogadores, 1 ou 2: "))
    tentativas = int(input("Escolha a quantidade de tentativas: "))

    while True:
        if escolha == 1:
            palavra = PalavrasAleatorias.palavra_aleatoria().strip()
            break
        elif escolha == 2:
            palavra = input("Digite uma palavra: ")
            print(
                "******** Escondendo a resposta ******** \n \n \n \n \n\n \n \n \n \n\n \n \n \n \n\n \n \n \n \n\n \n \n \n \n\n \n \n \n \n\n \n \n \n ******** Resposta escondida ********\n\n \n \n \n \n ")
            break
        else:
            print("Escolha a quantidade de jogadores para continuar (1 ou 2)")

    palavra = list(palavra.upper())

    base = []
    for letra in palavra:
        base.append("_")

    print("\n", base)
    while tentativas > 0:
        print(" Voce tem {} tenativas".format(tentativas))
        chute = input(" Digite seu chute: ")
        index = 0
        acertou = False

        for i in palavra:
            if chute.upper() == i.upper():
                base[index] = palavra[index]
                acertou = True
            index += 1

        if not acertou:
            tentativas = tentativas - 1

        if "_" not in base:
            print("\n Você acertou!")
            print(base)
            break

        print(base)

    print("\n Voce foi enforcado :(")
    print((" A resposta era {}").format(''.join(palavra)))


if (__name__ == "__main__"):
    forca()
