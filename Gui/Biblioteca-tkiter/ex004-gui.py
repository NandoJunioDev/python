import tkinter as tkinter
from ex001 import 
janela = tkinter.Tk()
v = tkinter.IntVar() # aqui trabalhamos com variavel usando um metodo intvar da classe tkinter
tkinter.Label(janela, text=" Escolha um  uma linguagem ", justify=tkinter.LEFT, padx=5,).pack() # label
tkinter.Radiobutton(janela, text="Python", variable=v, value=1, padx=25).pack(anchor=tkinter.W)
tkinter.Radiobutton(janela,text="c++", variable=v, value=2, padx=25).pack(anchor=tkinter.W)

janela.mainloop()

