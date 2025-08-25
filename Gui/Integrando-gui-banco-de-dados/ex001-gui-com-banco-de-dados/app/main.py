import sys
import os
script_dir = os.path.dirname(__file__)
project_root = os.path.dirname(script_dir)
sys.path.append(project_root)

from config_db.Config_Postgree import conectar
from entity.agenda import Contato
from app.CRUD_CONTATO import Crud
from app.gui import App

app = App()

app.mainloop()



    
  








