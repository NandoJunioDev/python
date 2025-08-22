



class Contato():
    def __init__(self, nome,numero, id=None):

        self.id = id
        self.nome = nome
        self.numero = numero


    def __str__(self):
        return f"Agenda( ID:{self.id},nome={self.nome}, numero={self.numero})"

