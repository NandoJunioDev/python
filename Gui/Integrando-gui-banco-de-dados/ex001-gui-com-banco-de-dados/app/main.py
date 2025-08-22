import sys
import os
script_dir = os.path.dirname(__file__)
project_root = os.path.dirname(script_dir)
sys.path.append(project_root)

from config_db.Config_Postgree import conexao



