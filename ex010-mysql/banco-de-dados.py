import sqlite3 as banco_de_dados

conexao = banco_de_dados.connect("empresa.db")
cursor = conexao.cursor()
cursor.execute( '''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
'''
)
print("tabela criada com sucesso")
conexao.commit()
cursor.close()
conexao.close()