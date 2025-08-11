import os

arquivoo = open("dados.txt", "w", encoding='utf-8')
arquivoo.write("vai chorar, ola python")
print(os.path.relpath(arquivoo.name))
print(arquivoo)