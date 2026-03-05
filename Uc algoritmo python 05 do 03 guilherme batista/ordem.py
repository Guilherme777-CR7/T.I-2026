import random
numeros = [45, 12, 78, 23, 56]
print("Lista original:", numeros)

numeros.sort()
print("Apos sort():", numeros)

numeros.sort(reverse=True)
print("Apos sort():", numeros)

random.shuffle(numeros)
print("lista embaralhada:", numeros)