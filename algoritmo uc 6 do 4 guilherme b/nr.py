print("numeros repetidos")

numeros = []

for i in range(8):
    while True:
        try:
            n = int(input(f"digite o {i+1}º número: "))
            numeros.append(n)
            break
        except ValueError:
            print("digite um número válido!")

contagem = {}

for n in numeros:
    contagem[n] = contagem.get(n, 0) + 1

print("\nnúmeros repetidos:")
tem_repetido = False

for numero, qtd in contagem.items():
    if qtd > 1:
        print(f"{numero} apareceu {qtd} vezes")
        tem_repetido = True

if not tem_repetido:
    print("nenhum número repetido.")