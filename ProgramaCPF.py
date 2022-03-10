def numero_repetido(cpf):
   contador = 0
   for numero in cpf:
      if cpf[numero] == cpf[1]:
         contador += 1

   if contador == 11:
      print("CPF Inválido")
      return True

####################################################
def digitar_cpf(cpf):
   while True:
      try:
         cpf = list(map(int, (input("Digite seu CPF: "))))
         return cpf
      except ValueError:
         print("Digite números!")
         continue
####################################################
def cpf_programa():

   cpf = "0"
   while len(cpf) != 11:
      cpf = digitar_cpf(1)
      if len(cpf) > 11:
         print("Quantidade de números acima do esperado.")
      elif len(cpf) < 11:
         print("Quantidade de números abaixo do esperado.")
      elif numero_repetido(cpf):
         return

   cpf2 = list(cpf)

   indice = 10
   contador = 0
   soma = 0
   for numero in cpf:
      algarismo_multiplicado = numero * indice
      indice -= 1
      cpf[contador] = algarismo_multiplicado

      soma += cpf[contador]
      contador += 1
      if contador <= 8:
          continue
      else:
          break


   resto = soma % 11


   if resto <= 1:
      J = 0  #J = Primeiro digito verificador
   else:
      J = 11 - resto

   if J != cpf[9]:
      print("CPF Inválido")
      return



   algarismo_multiplicado = 0
   soma = 0
   indice = 11
   contador = 0

   for numero2 in cpf2:
      algarismo_multiplicado = numero2 * indice
      indice -= 1
      cpf2[contador] = algarismo_multiplicado

      soma += cpf2[contador]
      contador += 1
      if (contador <= 9):
         continue
      else:
         break

   resto = soma % 11

   if (resto <= 1):
      K = 0 #K = Segundo digito verificador
   else:
      K = 11 - resto

   if (K == cpf2[10]):
      print("CPF Válido")
   else:
      print("CPF Inválido")

if (__name__ == "__main__"):
   continuar = True
   while continuar:
      cpf_programa()
      continuacao = False

      while continuacao == False:
         continuacao = input("\nDeseja testar outro CPF? S/N: ")
         if continuacao.upper() == "S":
            continuacao = True
         elif continuacao.upper() == "N":
            continuar = False
            continuacao = True
         else:
            continuacao = False
            print("Digite S ou N para responder.")


