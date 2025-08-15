import this
from hmac import new


class Vericacao:
    numero_selecionado = 0

    def verificador_antecessor_sucessor(numero_selecionado):
        numero_selecionado = int(input("Digite o numero que deseja verificar: "))
        this.numero_selecionado = numero_selecionado
        sucessor = numero_selecionado + 1
        antecessor = numero_selecionado -1
        print("o numero selecionado foi:", numero_selecionado, " \n sucessor:", sucessor, " \n antecessor:", antecessor)




vericador = Vericacao()
numero_selecionado = 0
Vericacao.verificador_antecessor_sucessor(numero_selecionado)
