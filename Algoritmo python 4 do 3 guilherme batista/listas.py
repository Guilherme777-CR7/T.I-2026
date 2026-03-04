no1 = "ana"
no2 = "bruno"
no3 = "caio"

nomes = ["ana", "bruno", "caio"]
print(nomes)

dados = ["carol", 0, 1.70, True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

lista = ["cachorro", "gato"]
print("original: ", lista)
lista.append("coelho")
print("atualizado:", lista)

lista.insert(1, "grilo")
print("atualizado:", lista)

lista.extend(1, "Macaco", "ovelha")
print("lista final:", lista)