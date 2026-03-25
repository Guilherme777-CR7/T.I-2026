def rn(n1, n2, n3, n4):
    notas = [n1, n2, n3, n4]
    print("Soma:", sum(notas))
    print("Média:", sum(notas)/4)
    print("Maior:", max(notas))
    print("Menor:", min(notas))


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

rn(n1, n2, n3, n4)