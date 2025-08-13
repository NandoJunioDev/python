# boas praricas para manipular dados
import os

with open ("dados.txt", "r", encoding="utf-8") as arquivo:
        for  linha in arquivo:
                print(linha)
        print("fim do arquivo" , arquivo.name)        


        # vamos analisar o codigo acima
        #with () => funçao que ja fecha o arquivo automatico
            #open("arquirvo que vc queira abrir", "o modo", encoding) as
            # as => apelido/ nome dessa funçao