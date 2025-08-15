import this

class Pizzaria:
    escolha = 0


    def cardapio(self,escolha, ):


         self.escolha = escolha



         match escolha:
             case 1:
                 print("voce escolheu a pizza de mussarela ")
                 valor = 50
             case 2:
                 print("voce escolheu a pizza portuguesa ")
                 valor = 200
             case _:
                 print("escolha errada, escolha enre 1 ou 2")
                 return

         print("\n o valor da pizza foi  ","R$", valor , "reais")

         print(" \nvai querer dividir o valor da pizza? S/N")
         opcao = input()
         if opcao == "S":
             print("vai querer dividir o por quantas pessoas o valor da pizza?")
             qtdPessoas = int(input())
             divisao = valor / qtdPessoas
             print("o valor deu: ", f"{divisao:.2f}", "por", qtdPessoas, "pessoas")
         else:
             print("o valor da pizza ficara cheio")




pizzaria = Pizzaria()
print("BEM VINDO A PIZZARIA FAZ O L")
print("AS PIZZA DISPONIVEL SÃO:", "\n 1:Pizza de mussarela: R$:50,00", "\n 2:pizza portuguesa: R$: 200,00")
escolha = int(input("digite o numero:"))
pizzaria.cardapio(escolha)