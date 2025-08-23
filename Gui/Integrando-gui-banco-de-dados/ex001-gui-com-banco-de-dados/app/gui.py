import customtkinter  as ctk 



from entity.agenda import Contato
from app.CRUD_CONTATO import Crud

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AGenda ")
        self.geometry("1000x1000")
        self.crud=Crud() 
    

