nomes = ["ana", "bruno", "carlos", "diana"]
print("nomes:", nomes)

nomes.remove("bruno")
print("Lista atualizada:", nomes)

removido = nomes.pop()
print(f"removido:{removido}")
print("Apos pop():", nomes)

del nomes[0]
print("Apos del nome[0]", nomes)

nomes.clear()
print("Lista atualizada:", nomes)