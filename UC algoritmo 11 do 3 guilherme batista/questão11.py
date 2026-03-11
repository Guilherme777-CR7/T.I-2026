st = 0

for n in range(1, 101):
    
    if n % 2 == 0:

        st += n

print(f"A soma de todos os números pares entre 1 e 100 é: {st}")

#O codigo da 12:

ta = 0
qt = 0

print("Sistema de Depósitos Bancários")
print("Digite o valor do depósito ou '0' para encerrar.")

while True:
    v = float(input("Valor do depósito: "))
    
    if v == 0:
        break
    
    ta += v
    qt += 1

print("-" * 35)
print(f"Total de depósitos: R$ {ta:.2f}")
print(f"Quantidade de transações: {qt}")
