import os 
arquivo = open("teste.txt", encoding="utf-8")
conteudo = arquivo.read()

print(" tipo  de conteudo " , type(conteudo))
print("consteudo read")
print(repr(conteudo))
arquivo.close()