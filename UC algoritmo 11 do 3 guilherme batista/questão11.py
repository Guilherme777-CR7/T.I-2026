
soma_pares = 0

for numero in range(1, 101):
    
    if numero % 2 == 0:
        # Se for par, somamos o valor atual ao total acumulado
        soma_pares = soma_pares + numero

# Imprime o resultado final após sair do laço
print(f"A soma de todos os números pares de 1 a 100 é: {soma_pares}")