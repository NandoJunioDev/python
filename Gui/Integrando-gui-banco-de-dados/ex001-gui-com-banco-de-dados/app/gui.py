import customtkinter  as ctk 



from entity.agenda import Contato
from app.CRUD_CONTATO import Crud

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AGenda ")

        self.geometry("1000x1000")
        self.crud=Crud() 
        
        self.grid_columnconfigure(index=10,weight=0)
        self.grid_rowconfigure(index=10,weight=0  )

        self.minha_aba = ctk.CTkTabview(self)
        self.minha_aba.grid(row=0,column=0,columnspan=2,sticky='nsew')
        
        self.interface_inserir()
        self.interface_consulta()
        self.interface_deletar()
        self.interface_atualizar()
        



    def interface_inserir(self):
        aba_inserir = self.minha_aba.add("Inserirar o contato")
        #label para nome
        label_nome = ctk.CTkLabel(aba_inserir,text="Digite o nome")
        label_nome.grid(row=0, column=0, padx=10, pady=10)
        # entrada
        self.entry_nome = ctk.CTkEntry(aba_inserir,placeholder_text="entre com o nome")
        self.entry_nome.grid(row=1, column=0, sticky="w")

        label_telefone = ctk.CTkLabel(aba_inserir,text="Digite o seu telefone")
        label_telefone.grid(row=2, column=0, padx=10, pady=10)

        self.entry_telefone = ctk.CTkEntry(aba_inserir,placeholder_text="Telefone")
        self.entry_telefone.grid(row=3, column=0, sticky="w")
        buton = ctk.CTkButton(aba_inserir,text="Confirmar", command=self.adicionar_contato)
        buton.grid(row=4, column=0, padx=10, pady=10)
    def interface_consulta(self):
        aba_consulta = self.minha_aba.add("Ver Contatos ")
        self.lista_frame = ctk.CTkScrollableFrame(aba_consulta)
        self.lista_frame.grid(row=0, column=1,)
        self.botao_atualizar=ctk.CTkButton(aba_consulta,text="Atualizar contato", command=self.atualizar_contato)
        self.botao_atualizar.grid(row=2,column=1)
    def interface_deletar(self):
        aba_deletar = self.minha_aba.add("Deletar contato")
        self.lista_frame_interface_deletar = ctk.CTkScrollableFrame(aba_deletar)
        self.lista_frame_interface_deletar.grid(row=1, column=0)
        id_label = ctk.CTkLabel(aba_deletar,text="Digite o id ")
        id_label.grid(row=1 ,column=0, )

        self.id_entry = ctk.CTkEntry(aba_deletar,placeholder_text="ID do contato")
        self.id_entry.grid(row=2, column=0)
        butao_apagar = ctk.CTkButton(aba_deletar,text="DELETAR",command=self.deletar_contato)
        butao_apagar.grid()
    def interface_atualizar(self):
        aba_atualizar = self.minha_aba.add("atualizar contato")
        self.lista_frame_interface_atualizar = ctk.CTkScrollableFrame(aba_atualizar)
        self.lista_frame_interface_atualizar.grid(row=0, column=0,)
        label_id = ctk.CTkLabel(aba_atualizar,text="Digite id do contato que deseja atualizar")
        label_id.grid(row=1, column=0, padx=10, pady=10)

        self.label_nome_novo= ctk.CTkLabel(aba_atualizar,text="digite o novo nome")
        self.label_nome_novo.grid(row=1,column=1)
        self.entry_nome_novo = ctk.CTkEntry(aba_atualizar,placeholder_text="digite o novo nome")
        self.entry_nome_novo.grid(row=2, column=1)


        self.label_numero_novo = ctk.CTkLabel(aba_atualizar,text="Digite O novo numero")
        self.label_numero_novo.grid(row=3,column=1)
       
        



        entry_id = ctk.CTkEntry(aba_atualizar,placeholder_text="ID")
        entry_id.grid(row=2, column=0, padx=10, pady=10)

    def adicionar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()

        print(f" dados pegados {nome} {telefone}")
        if nome and  telefone:
            contato = Contato(nome, telefone)
            self.crud.inserir_contato(contato)
        else:
            print("telefone e nome, vazios")
    def atualizar_contato(self):
      
      lista_de_componetes = self.lista_frame.winfo_children()
      for listacomponetes in lista_de_componetes:
          listacomponetes.destroy()
      lista_de_contatos_novo =self.crud.listar_contato()


      for   contato in lista_de_contatos_novo:

           novo_label = ctk.CTkLabel(self.lista_frame,text=str(contato))
           novo_label.pack(padx=10, pady=10 , fill="x")
    def deletar_contato(self):
        
        self.id_passado = self.id_entry.get()
        
        try:
            self.id_para_deletar= int(self.id_passado)
            
            self.crud.deletar_contato(self.id_para_deletar)
            self.atualizar_contato()
            self.id_entry.delete(0,'end')
            
            
        except ValueError:
            print("id  precisa ser um numero")    
        
           
             
           


        
        

       

























        



       
    

      

    

