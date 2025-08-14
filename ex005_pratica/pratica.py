def main():
    """
    Função principal que coleta frases do usuário, salva em um arquivo,
    lê o arquivo, converte as frases para maiúsculas e salva novamente.
    """
    print("Digite suas frases. Digite 'sair' para terminar.")
    frases = []

    # Loop infinito para coletar a entrada do usuário.
    while True:
        entrada = input("Digite sua frase: ")
        if entrada.lower() == "sair":
            break  # Interrompe o loop se o usuário digitar "sair".
        frases.append(entrada)

    # Abre o arquivo "problematica.txt" no modo de escrita ('w').
    # O 'with' garante que o arquivo será fechado automaticamente.
    try:
        with open("problematica.txt", "w", encoding='utf-8') as file:
            # Itera sobre a lista 'frases' (e não sobre o 'file').
            for frase in frases:
                file.write(frase + "\n")
    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}")
        return # Sai da função se não conseguir escrever o arquivo

    print("\nArquivo 'problematica.txt' foi criado com o conteúdo original.")
    print("Agora vamos manipular os dados...")

    dados_modificados = []
    # Abre o arquivo no modo de leitura ('r').
    try:
        with open("problematica.txt", "r", encoding='utf-8') as file:
            for linha in file:
                # Remove espaços em branco/quebras de linha do início e fim
                # e converte a linha para maiúsculas.
                dados_modificados.append(linha.strip().upper())
    except IOError as e:
        print(f"Erro ao ler o arquivo: {e}")
        return # Sai da função se não conseguir ler

    # Reabre o arquivo no modo de escrita ('w') para salvar as modificações.
    # ATENÇÃO: Isso apagará o conteúdo anterior do arquivo.
    try:
        with open("problematica.txt", "w", encoding='utf-8') as file:
            for frase in dados_modificados:
                file.write(frase + "\n")
    except IOError as e:
        print(f"Erro ao modificar o arquivo: {e}")
        return

    # Esta linha agora está fora do loop, sendo impressa apenas uma vez.
    print("O arquivo foi modificado com sucesso. Todas as frases estão em maiúsculas.")

# Esta verificação deve estar fora da definição da função main.
# Ela garante que main() só será chamada quando o script for executado diretamente.
if __name__ == "__main__":
    main()