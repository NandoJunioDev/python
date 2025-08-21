import tkinter as tkinter # apelidamos o tkinter

def mostrar_nome():
    print("Nome %s\nSobrenome: %s  " % (e1.get(),e2.get()))

janela = tkinter.Tk() # falamos que a variavel  recebe o apelido.Tk() => a onde fica os componetes
janela.title("Testando o label") # renomea o nome  da janela
tkinter.Label(janela, text="nome").grid( row=0) # no label, passamos a variavel que recebido com tk  ou seja com componete

tkinter.Label(janela, text="sobrenome").grid( row=1)
e1 = tkinter.Entry(janela) # aqui magica acontece, e1 = recene a entrada de texto, ( entry, entra com o texto)
e2 = tkinter.Entry(janela)

e1.grid(row=0, column=1) # grid,  tipo de posicionamento em linha e coluna
e2.grid(row=1, column=1)

#chamomos o button(passando a variavel janela,
tkinter.Button(janela, text="sair", command=janela.quit() ).grid( row=2, column=0 , sticky=tkinter.W, pady=5)

tkinter.Button(janela, text= " mostrar o s  nome", command=mostrar_nome).grid( row=3, column=1, sticky=tkinter.W, pady=4)

janela.mainloop() # inicia