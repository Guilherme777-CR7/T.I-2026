t = 0.0

while True:
    v = float(input("Digite os valores dos produtos, e quando quiser parar digite 0: "))
    if v == 0:
        break
    t += v

print(f"total: R$ {t:.2f}")