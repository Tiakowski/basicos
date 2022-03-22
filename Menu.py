import ProgramaCPF
import forca
import AdivinharNumero
import GeradorSenha

continuar = "S"
while continuar == "S":
    print("************* Escolha um programa *****************\n \n")
    print("Programa de validação de CPF: (1) \nJogo de adivinhar numero: (2) \nJogo da Forca: (3) \nGerador de Senha (4)")

    escolha = int(input("Digite o numero do programa correspondente: "))
    print("\n")

    if escolha == 1:
        ProgramaCPF.cpf_programa()
    elif escolha == 2:
        AdivinharNumero.adivinhar()
    elif escolha == 3:
        forca.forca()
    elif escolha == 4:
        print(f"Senha: {GeradorSenha.gerar_senha()}")

    print("\n")
    continuar = input("Deseja continuar? S/N ").upper()
    print("\n")