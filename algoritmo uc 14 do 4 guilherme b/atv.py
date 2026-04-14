def soma_segura(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Entrada inválida")
        return 0

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
except ValueError:
    print("Entrada inválida")
    a, b = 0, 0

print("Resultado:", soma_segura(a, b))