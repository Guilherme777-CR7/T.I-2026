v = float(input("digite o valor da compra: R$ "))

if v > 500:
    d = v * 0.20
elif v >= 200:
    d = v * 0.10
else:
    d = 0

pf = v - d

print(f"valor do produto: R$ {v:.2f}")
print(f"desconto: R$ {d:.2f}")
print(f"preço total: R$ {pf:.2f}")