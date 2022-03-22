

def palavra_aleatoria():
    import random
    palavras = open("palavras.txt", "r")
    aleatorio = random.randrange(1,quantidade_de_palavras())
    contador = 1
    for linha in palavras:
        if aleatorio == contador:
            palavra_escolida = linha
            return palavra_escolida
        else:
            contador += 1
    palavras.close()

def quantidade_de_palavras():
    palavras = open("palavras.txt")
    lista = list(palavras)
    tamanho = len(lista)
    return tamanho



if (__name__ == "__main__"):
   print(palavra_aleatoria())
   print(quantidade_de_palavras())
