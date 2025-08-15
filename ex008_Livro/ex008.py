import  os
with open("texto.txt","r", encoding="utf-8") as arquivo:
    frase = ["voce é o melhor porgramador que agnete ja teve", "gay"
             ,"por isso que  vcoe é um corno "]
    texto = arquivo.read()
    conte = texto.count("melhor")
    print(conte)





