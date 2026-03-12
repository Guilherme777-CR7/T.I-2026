n1 = float(input("1° valor:"))
n2 = float(input("2° valor:"))

def calcularmedia(n1, n2):
    soma = n1 + n2
    produto = n1 * n2
    return soma, produto

resultado = calcularmedia(n1, n2)
print(f"resultado: {resultado}")