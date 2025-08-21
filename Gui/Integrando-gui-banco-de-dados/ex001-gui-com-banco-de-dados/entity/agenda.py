class Agenda:
    def __init__(self, nome,telefone):
        self.nome = nome
        self.telefone = telefone


    def criarContato(self, nome, telefone):

        self.nome = input('Digite seu nome: ')

        self.telefone = int(input('Digite sua telefone: '))



