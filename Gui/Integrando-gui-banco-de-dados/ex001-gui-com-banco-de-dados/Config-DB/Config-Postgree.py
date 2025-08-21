import psycopg2
from psycopg2 import Error
import os



DB_USER = os.getenv("")
DB_PASSWORD = os.getenv("")
DB_HOST = os.getenv("")
DB_PORT = os.getenv("")
DB = os.getenv("")


def conectar():

        try:
            with psycopg2.connect(user = DB_USER,password = DB_PASSWORD,host=DB_HOST,port=DB_PORT,database=DB) as conn:
                 return conn
                 
            return connection

        except Error  as e:
            print(f"erro  ao conectar  ao banco de dados: {e}" )
            return None
        

if __name__ == "__main__":
     
     conn = conectar()

     if conn:
          print("conexao sucessida")
          try:
               with conn.cursor() as cursor:
                    cursor.execute("SELECT version();")
                    versao = cursor.fetchone()
                    print(f"versao do postgree {versao}")
          except Error  as e:
               print(f"dadadd {e}")        
          finally:
               if conn:
                    conn.close()
                    print("conexao fechada")     
    
