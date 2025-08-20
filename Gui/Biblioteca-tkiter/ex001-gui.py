import tkinter as tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

janela = tkinter.Tk() # a variavel receber o objeto da bibliote tkinter
janela.title("TESTANDO ESSA PORCARIA DE INTERFACE GRAFICA") # TITULO DA JANELA
# colocamos um label, esse componetes sao classes, text "textod dalabel".grid(posiamento como no css collun e row do modo grid ) 
tkinter.Label(janela, text="olha isso que lindo <3" ).grid(column=0, row=0) 

janela.mainloop() # roda o que ja fez
