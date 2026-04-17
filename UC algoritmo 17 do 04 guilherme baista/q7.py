ven = [120, 75, 200, 33, 88, 145, 60]

sp = 0

for val in ven:
    if val % 2 == 0: 
        sp += val

print(f"vendas: {ven}")
print(f"soma de numeros pares: {sp}")