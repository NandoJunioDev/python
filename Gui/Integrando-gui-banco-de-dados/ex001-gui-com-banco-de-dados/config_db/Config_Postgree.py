import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os


load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


def conectar():
        conn = None
        try:
            conn =  psycopg2.connect(user=DB_USER,password=DB_PASSWORD,host=DB_HOST,port=DB_PORT,database=DB_NAME)

            print("conexao feita com sucesso!")

            return conn
        except Error  as e:
            print(f"erro  ao conectar  ao banco de dados: {e}" )
            return None
        

if __name__ == "__main__":

     conn = conectar()

     if conn:
        try:
              with conn as conexao:
                  with conexao.cursor() as cursor:
                      cursor.execute("SELECT version()")
                      versao = cursor.fetchone()
                      print(versao)

        except Error as e:
            print(f"erro  {e} ")

        finally:
            if conn:
                conn.close()
                print("conexao fechada")
