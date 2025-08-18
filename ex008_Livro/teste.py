import datetime
frutas = ["dadada", "banana", "abacaxi "]
for fruta in frutas:
    frute = f"nome:{fruta:12}  - numero de letras {len(fruta): 3} "
    print(frute)


print()

pi = 3.1444444444
numero_pi = f"O numero  PI  é: {pi:.2f}"
numero_pi_deslocado = f" o numero  PI  deslocado: {pi:5.2f}"
numero_pi_preciso = f"O numero  PI  preciso: {pi:.3f}"
print(numero_pi_deslocado)
print(numero_pi)
print(numero_pi_preciso)

print()

data = datetime.datetime.now()
minha_data = f"A data  de hooje {data.year} - {data.month} - {data.day}"
minha_data_formatada = f" A data de hoje {data:%d/%m/%Y - %H:%M}"
print(minha_data_formatada)
print(minha_data)
print(data)
print(minha_data_formatada)