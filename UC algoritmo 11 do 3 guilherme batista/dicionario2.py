contato = {
    "@camila": "camila",
    "@paola": "paola",
    "@sheron": "sheron",
    "@bruna": "bruna",
}

#obter chaves
print("chaves")
for insta in contato.keys():
    print(insta)

#obter valores
print("\n valores: ")
for nome in contato.values():
    print(nome)

#obter pares
print("\n pares: ")
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")   

contato = {
   "@camila": 1.70,
   "@paola": 1.80,
   "@sheron": 1.55,
   "@bruna": 1.60
}

print("ordenando por chaves: ")    
for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]:.2f}m") 

from operator import itemgetter
print("\n ordenando por valor (altura): ")
for insta, estatura in sorted(contato.items (), key = itemgetter(1)):
    print(f"{insta} --> {estatura:.2f}m")                                                                                                                                                                                                                      