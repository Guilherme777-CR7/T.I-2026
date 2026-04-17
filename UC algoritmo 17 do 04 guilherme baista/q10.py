f = input("digite uma frase: ")

v = "aeiouAEIOU"
c = 0

for l in f:
    if l in v:
        c += 1

print(f"tem {c} vogais")