def calcular_total():
    while True:
        try:
            p1 = float(input("Preço 1: "))
            p2 = float(input("Preço 2: "))
            print("Total:", round(p1 + p2, 2))
            break
        except:
            print("Digite apenas números.")

calcular_total()