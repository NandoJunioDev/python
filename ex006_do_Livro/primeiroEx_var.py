def ver_sucesso_e_antecessor():
    print("digite um numero para verificar o su antecessor e sucesso")
    numero_selecionado = int(input())
    
    while True:
        if numero_selecionado > 0:
            break

    antecessor = numero_selecionado - 1
    sucessor = numero_selecionado + 1 
    print(" numero selecionado", numero_selecionado,"\n antecessor: ",antecessor, "sucessor:",sucessor)  
    print("fechando a funçao")  

ver_sucesso_e_antecessor    