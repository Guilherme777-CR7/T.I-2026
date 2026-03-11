aluno = {}

aluno["nome"] = input("nome do aluno: ")
aluno["n1"] = float(input("1° nota: "))
aluno["n2"] = float(input("2° nota: "))
soma = aluno["n1"] + aluno["n2"]
media = soma / 2

aluno["media"] = media

print("nome", aluno["nome"])
print("1° nota: ", aluno["n1"])
print("2° nota: ", aluno["n2"])
print("a media do aluno é: " (media))
if media >= 7: 
    print("aluno aprovado")
elif media >= 5:
    print("aluno em recuperação")
else:
    print("aluno reprovado")


