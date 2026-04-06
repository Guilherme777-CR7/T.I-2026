import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("advinhe o numero")

while True:
    try:
        palpite = int(input("Adivinhe o número (1 a 100): "))
        tentativas += 1

        if palpite < numero_secreto:
            print("maior")
        elif palpite > numero_secreto:
            print("menor")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
    except ValueError:
        print("Digite um número válido!")