import random

n1 = [91, 34, 67, 15, 82]
print(f"Lista original: {n1}")

n1.sort()
print(f"Ordem crescente: {n1}")

n1.sort(reverse=True)
print(f"Ordem decrescente: {n1}")

n2 = [6, 7, 8, 9, 10]
random.shuffle(n2)
print(f"Lista n2 embaralhada: {n2}")

print("\nDesafio")
ml = [42, 7, 19, 88, 3, 55]
print(f"lista original: {ml}")

ml.sort()
print(f"Desafio - Crescente: {ml}")

ml.sort(reverse=True)
print(f"Desafio - Decrescente: {ml}")

random.shuffle(ml)
print(f"Desafio - Embaralhada: {ml}")