def gerar_senha():
    import random
    import string


    numero_de_caracteres = random.randrange(8,13)
    alfabeto = list(string.ascii_lowercase)
    senha = []

    #### Gerar senhas apenas com letras
    while len(senha) < numero_de_caracteres:
        aleatorio = random.randrange(0, 26)
        maiusculo = random.randrange(0,2)
        if maiusculo == 1:
            letra_maiuscula = alfabeto[aleatorio].upper()
            senha.append(letra_maiuscula)
        else:
            senha.append(alfabeto[aleatorio])


    #Gerar senhas com letras e números

    quantidade_de_numeros = random.randrange(1,8)
    contador = 0

    while quantidade_de_numeros > contador:
        numeros = random.randrange(0, 10)
        letra = random.randrange(0,len(senha))
        senha[letra] = str(numeros)
        contador += 1

    # Gerar caracteres especiais.
    quantidade_de_especiais = random.randrange(1,4)
    especiais = ["! ", "#" ,"$","'" ,"%", "&","(", ")", "*", "+" , "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]" ,"^", "_","`", "{", "|", "}", "~"]
    contador = 0

    while quantidade_de_especiais > contador:
        especial = especiais[random.randrange(0,len(especiais))]
        lugar_especial = random.randrange(0,len(senha))
        senha[lugar_especial] = especial
        contador += 1

    senha_final = ''.join(senha)
    return senha_final


if __name__ == "__main__":
    sim = True

    while sim:
        desejo = input("Deseja gerar uma senha? S/N ")
        if desejo.upper() == "S":
            print(gerar_senha())
            print("\n")
        elif desejo.upper() == "N":
            exit()
        else:
            print("Digite S (Sim) ou N (Não)")
            print("\n")