resposta = input("Você possui carteira de motorista? (S/N): ").upper()

tem_carteira = (resposta == "S")

print(f"Valor: {tem_carteira}")
print(f"Tipo: {type(tem_carteira)}")