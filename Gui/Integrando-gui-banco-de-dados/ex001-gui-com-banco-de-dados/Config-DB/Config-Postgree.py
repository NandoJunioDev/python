import psycopg2
from psycopg2 import Error

DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"
DB = "Agenda"


    def conectar(self):

        try:
            connection = None
            connection = psycopg2.connect(user=DB_USER, host=DB_HOST, port=DB_PORT, password=DB_PASSWORD, database=DB)

            return connection

        except Error  as e:
            print(f"erro  ao conectar  ao banco de dados: {e}" )
        finally:
            if connection is not None:
                connection.close()
                print("conexao feita com sucesso")


