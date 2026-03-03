numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = numero ** 2
    print(f"O número {numero} é par. Seu quadrado é: {resultado}")
else:
    resultado = numero ** 3
    print(f"O número {numero} é ímpar. Seu cubo é: {resultado}")