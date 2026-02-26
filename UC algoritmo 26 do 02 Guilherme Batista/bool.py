resp = input("VocÊ vai passar de ano? S/N ").strip().lower()
#resposta = bool(resp)
#resposta = (resp == "s")
resposta = resp in("Sim", "s")

print("resposta do aluno", resp)
print("resultado", resposta)