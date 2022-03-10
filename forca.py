def forca():
    print("* O Jogo necessita de 2 jogadores *")
    palavra = input("DIgite uma palavra: ")
    palavra = list(palavra.upper())

    print("******** Escondendo a resposta ******** \n \n \n \n \n\n \n \n \n \n\n \n \n \n \n\n \n \n \n \n\n \n \n \n \n\n \n \n \n \n\n \n \n \n ******** Resposta escondida ********\n\n \n \n \n \n ")
    base = []
    for letra in palavra:
        base.append("_")

    #acertou = False
    print(base)
    tentativas = 2
    while tentativas > 0:
        print("Voce tem {} tenativas".format(tentativas))
        chute = input("Digite seu chute: ")
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