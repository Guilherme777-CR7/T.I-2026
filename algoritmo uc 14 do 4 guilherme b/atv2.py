def divisao(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Não divida por zero!"

try:
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
except ValueError:
    print("Entrada inválida")
    x, y = 0, 1  
print("Resultado:", divisao(x, y))