import  sqlite3 as sql
def banco_de_dados():
    try:
        with sql.connect('banco-de-dados2.db') as conexao:
            cursor = conexao.cursor()
            tabela_pessoas = ''' CREATE TABLE  IF NOT  EXISTS   Pessoas (
             cpf INTEGER NOT NULL,
             nome TEXT NOT NULL,
             nascimento DATE NOT NULL,
             oculos BOOLEAN NOT NULL,
             PRIMARY KEY (cpf)
             );
             '''
            tabela_marca = ''' CREATE  TABLE IF NOT EXISTS Marca(
            Id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            sigla CHARACTER(5) NOT NULL,
            PRIMARY KEY (id)
            );
            '''
            tabela_veiculo = '''
            CREATE TABLE IF NOT EXISTS Veiculo(
            placa  CHARACTER(7) NOT NULL,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            proprietario INTEGER NOT NULL,
            marca INTEGER NOT NULL,
            PRIMARY KEY (placa)
            FOREIGN KEY (proprietario) references Pessoas(cpf)
            FOREIGN KEY (marca) REFERENCES Marca(id)
            )'''
            cursor.execute(tabela_pessoas)
            cursor.execute(tabela_marca)
            cursor.execute(tabela_veiculo)
    except sql.DatabaseError as erro:
        print(erro)

    finally:
        print("tudo certo")


if __name__ == '__main__':
    banco_de_dados()
