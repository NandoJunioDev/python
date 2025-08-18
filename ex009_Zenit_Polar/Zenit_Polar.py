def zenit_polar_convert (text):
    # PADRAO QUE SERA TROCADO 
    zenit_polar = [("z","p"),("e","o"),("n","l"),("i","a"),("t","r"),
                   ("Z","P"),("E","O"),("N","L"),("I","A"),("T",'R')] 
    for old,new in zenit_polar: # LOOP QUE PERCORERRA A LISTA DE TUPLAS
        text = zenit_polar.replace(old, new) # NOVO TEXTO SEPARADO
    return text



def main():

    