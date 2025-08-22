from psycopg2 import Error


from config_db.Config_Postgree import conectar
from entity.agenda import Contato


class Crud:
    def __init__(self):
        pass
    
    def inserir_contato( self,obj_contato ):

        conn = conectar()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO agenda (nome,telefone) VALUES ( %s,%s)"
                    cursor.execute(sql,  (obj_contato.nome,obj_contato.telefone))
                    conn.commit()
                    print(f"Contato {obj_contato.nome} criado com sucesso!")

            except Error as e:
                print(f"Erro ao inserir contato: {e}")
            finally:
                conn.close()

    def listar_contato():

        lista_de_contatos = []
        conn = conectar()
        try:
            if conn:
                with conn.cursor() as cursor:
                    sql = " SELECT id,nome,telefone FROM agenda ORDER BY nome"
                    cursor.execute(sql)
                    consulta = cursor.fetchall()
                    for contato in consulta:
                        contatos = Contato(id=contato[0],nome=contato[1],telefone=contato[2])
                        lista_de_contatos.append(contatos)

        except Error as erro:
            print(f"nao foi possivel criar por causa  {erro}")
        finally:
            conn.close()
        return lista_de_contatos        

    


            






