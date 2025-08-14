def main():
    print("Começe a digitar para, criar o arquivo e digite sair para encerrar o programa ")
    frases = []
    while True:
        entrada = input("Digite algo: ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)

    try:
        with open("problematica.txt", "w", encoding='utf-8') as file:
            for frase in frases:
                file.write(frase + "\n")

    except IOError as e:
        print(f"Erro ao criar o arquivo: {e}")

        return
    print("Programa encerrado, arquivo criado com sucesso!")
    print("agora vamos manipular o arquivo")
    dados_modificados = []
    try:
        with open("problematica.txt", "a", encoding='utf-8') as file:
            for frase in frases:
