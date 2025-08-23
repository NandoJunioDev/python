import sys
import os
script_dir = os.path.dirname(__file__)
project_root = os.path.dirname(script_dir)
sys.path.append(project_root)

from config_db.Config_Postgree import conectar
from entity.agenda import Contato
from app.CRUD_CONTATO import Crud




print("\n LISTA DE CONTATOS")
todos_os_contatos = Crud.listar_contato(self="")
if todos_os_contatos:
    for contatos in todos_os_contatos:
        print(contatos)
else:
    print("Nenhum contato encotrado")

    crud = Crud()
    








