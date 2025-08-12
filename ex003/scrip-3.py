import os









#abaixo vc vera outra forma de escrever no arquivo
# passando um variavel ou objeto 

linhas = ["vc agora esta verendo que essas linha foi adicionando a trasves do arrays", "\n essa é a segunda linha "]

arquivo_escrita = open("dados.txt", "w", encoding="utf-8")
arquivo_escrita.writelines (linhas)
arquivo_escrita.close
