from unittest import case

print("escolha sua pizza")
print("\n 1: pizza mussarela R$: 50,00", "\n 2: pizza calabressa R$:100,00", "\n 3: pizza portuesa R$:150,00")
escolha = int(input())

match escolha:
     case 1:
         print ("voce selecionou a pizza de mussarela")
         valor = 50


     case 2:
         print ("voce selecionou a pizza de calabressa")
         valor = 100

     case 3:
         print ("voce selecionou a pizza de portuesa")
         valor = 150





print("\n o valor da pizza foi", valor)

print("\n voce vai querer dividir a conta? S/N")
opcao = input()
if opcao == "s":
    print("com quantas pessoas")
    pessoas = int(input())
    divisao = valor / pessoas
    print("sua conta foi dividida em ", divisao,"por", pessoas, "pessoas")  
else:
    print("o valor vai ficar cheio:",valor)