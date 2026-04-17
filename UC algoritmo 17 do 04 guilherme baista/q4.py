def ci(p, a):
    try:
        p = float(p)
        a = float(a)

        if a <= 0 or p <= 0:
            return "digite um valor maior que 0"

        imc = p / (a ** 2)

        if imc < 18.5:
            c = "magro"
        elif imc <= 24.9:
            c = "normal"
        elif imc <= 29.9:
            c = "sobrepeso"
        else:
            c = "obesidade"

        return f"o imc é: {imc:.2f} e a categoria é: {c}"

    except ValueError:
        return "digite seu peso e altura"


p = input("digite seu peso: ")
a = input("digite sua altura: ")

print(ci(p, a))