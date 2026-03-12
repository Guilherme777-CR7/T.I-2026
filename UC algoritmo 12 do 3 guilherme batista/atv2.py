n1 = float(input("valor por hora trabalhada: "))
n2 = float(input("horas trabalhadas: "))

def calcularsalario(n1, n2):
    sb = n1 * n2
    return sb

resultado = calcularsalario(n1, n2)
print(f"salario bruto: R${resultado}")