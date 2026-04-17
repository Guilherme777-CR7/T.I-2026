t = [30.5, 28.0, 29.3, 31.2, 27.8, 26.5, 30.0]

s = 0.0

for temp in t:
    s += temp

m = s / len(t)

print(f"temperaturas: {t}")
print(f"média: {m:.2f} °C")