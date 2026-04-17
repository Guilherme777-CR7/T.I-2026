
ns = [8.5, 6.0, 7.2, 9.0, 5.5, 7.8, 10.0]

c = 0

for n in ns:
    if n > 7:
        c += 1

print(f"notas: {ns}")
print(f"alunos que estão acima de 7 é: {c}")