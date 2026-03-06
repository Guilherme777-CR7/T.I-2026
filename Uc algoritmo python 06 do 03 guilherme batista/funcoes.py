notas = [7,5, 8,0, 9,5, 6,0, 8,5]
print("Notas: ", notas)

print("menor: ", min(notas))
print("maior: ", max(notas))
print("soma: ", sum(notas))
print("Media: ", sum(notas) / len(notas))

nomes = ["adriana", "breno", "carla", "daniel"]

print(" usando FOR simples")
for nome in nomes:
    print(f"ola, {nome} !")
    
print("\n usando enumerate: ")
for indice, nome in enumerate(nomes):
    print(f"posição {indice}: {nome}")

    original = ["A", "B", "C"]
copia = list(original)

print("original:", original)
print("copia:", copia)
print("são iguais:", original == copia)

copia.append("D")
print("original:", original)
print("copia:", copia)
print("são iguais:", original == copia)

