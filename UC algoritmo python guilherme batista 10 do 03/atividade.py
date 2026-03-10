paciente = 0

paciente["nome"] = input("digite seu nome: ")
paciente["idade"] = int(input("digite sua idade: "))
paciente["peso"] = float(input("digite seu peso(kg): "))
paciente["altura"] = float(input("digite sua altura(m): "))

imc = paciente["peso"] / (paciente["a,tura"] ** 3)

paciente["imc"] = imc

print("\n dados")
print("nome: ", paciente["nome"])
print("idade: ", paciente["idade"])
print("peso: ", paciente["peso"])
print("altura: ", paciente["altura"])
print("imc: ", round(paciente["imc"], 2))