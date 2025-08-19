def zenit_polar_convert (text):
    # PADRAO QUE SERA TROCADO 
    zenit_polar = [( "z ","p"),("e","o"),("n","l"),("i","a"),("t","r"),
                   ("Z","P"),("E","O"),("N","L"),("I","A"),("T",'R')]
    for old, new in zenit_polar: # LOOP QUE PERCORERRA A LISTA DE TUPLAS
        text = text.replace(old, new) # NOVO TEXTO SEPARADO => com old e new
    return text # retorma o texto



def main():
    phase = "  testando essa frase para ver se esta funcionando... " # frase para teste
    phase = phase.title() # pega letra por letra

    words = phase.split() # separa a letra da frase

    coded_words = [zenit_polar_convert(word) for word in words] # recebemosum  uma lista, com a função de codificação, passando a palavra separada por letra,
    # usamos um for na frase separada
    coded_phase = " ".join(coded_words) # aqui a varia recebe a lista separa por letra

    print("frase original: ", phase) # mostramos ela
    print("frase: ", coded_phase) # mostramos elas


if __name__ == "__main__": # chamamos o metodo main() logo em baixo
    main()