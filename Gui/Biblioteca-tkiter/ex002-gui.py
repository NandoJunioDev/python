import tkinter as gui


contador = 0 
def contador_geral(routulo):
    def funcao_contar():
        global contador
        contador = contador + 1
        routulo.config(text=str(contador))
        routulo.after(1000, funcao_contar)
    funcao_contar()

janela = gui.Tk()
janela.title("Contagem  dos segundos")
routulo = gui.Label (janela, fg="green" ,text=f"{contador}")
routulo.pack()
contador_geral(routulo)
btnAcao = gui.Button (janela,  text="clique  aqui para interroper", width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()