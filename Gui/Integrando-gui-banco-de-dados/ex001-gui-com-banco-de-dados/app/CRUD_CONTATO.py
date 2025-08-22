from psycopg2 import Error

from config_db.Config_Postgree import conexao
from entity.agenda import Contato

def inserir_contato(obj_contato ):




    conn = conexao()
    if conn:
        try:
            with: conn.cursor() as cursor:
                sql = "INSERT INTO contatos (id,nome,numero) VALUES (%s, %s,%s)"
                conn.execute(sql, obj_contato.id, obj_contato.nome, obj_contato.numero)
                conexao.commit()
                print(f"Contato {obj_contato.nome} criado com sucesso!")

        except Error as e:
            print(f"Erro ao inserir contato: {e}")
        finally:
            conn.close()







