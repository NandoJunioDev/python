import sqlite3

def main():
    try:
     #aqui o with gerencia tudo, como fecha o arquivo e comittaaaar é boa pratica
        with sqlite3.connect('banco-de-dados.db') as conexao:
            cursor = conexao.cursor()

            #1 Criar tabela usando cursor.execute
            cursor.execute(''' CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email  TEXT NOT NULL UNIQUE ) 
                            ''')

            #2 vamos inserir os dados agora na tabela criada
            lista_usuarios = [
                ("mamador","arrombado@gmail.com"),("sentarindo","peteratinha@gmail.com"),("mamadornata, " , "gritandoas0000@hoymail.com")
            ]
            for nome, email in lista_usuarios:
                cursor.execute(" INSERT OR IGNORE  INTO usuarios (nome, email) VALUES (?,?)" , ( nome, email) )
            print("dados inseridos com sucesso ")
            #3 CONSULTAR OS DADOS
            cursor.execute("""SELECT id,nome,email FROM usuarios""")
            print("\n esses sao os usuarios: ")
            for usuario in cursor.fetchall():
                print(f"Id:{usuario[0]} nome:{usuario[1]} email:{usuario[2]}")
    except sqlite3.Error as erro:
            print(erro)




if __name__ == '__main__': # 4 chamada para funçao main
        main()

