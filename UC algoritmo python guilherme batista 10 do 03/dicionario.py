#sem dicionario
matricula1 = 2026001
nome1 = "Ana silva"
telefone1 = "9999-8888" #Colocar várias variáveis sem razão.

#com dicionario
aluno ={
    "matricula": 2026001, 
    "nome": "Ana silva",
    "telefone": "9999-8888" #Um dicionáriopara várias variáveis.
}

print(aluno)

contato ={
    "@camilaqueiroz": "Camila Queiroz",
    "@brunamarquezine" : "Bruna Marquezine",
    "@sheronmendes" : "Sheron M.",
    "@paolaoliveira": "Paula O.",
    "@joaoguilherme" : "João G."
}

print(contato)
print(type(contato))

#acesso direto
print(contato["@camilaqueiroz"])

#acesso seguro com get()
print(contato.get("@camilaqueiroz"))
print(contato.get("inexistente"))
print(contato.get("@inexistente", "não encontrado"))

#add novo elemento
contato["@brunamarquezine"] = "Paola oliveira"
print("após add:", contato)

contato.update({ 
    "@brunamarquezine": "Bruna Marquezine",
    "@camilaqueiroz": "Camila Q." 
})

#pop: romove e retorna
removido = contato.pop("@paolaoliveira")
print(f"Removido: {removido}")
print("Após o pop: ", contato)

# del remove sem retornar 
del contato ["@camilaqueiroz"]
print("Após o del: ",contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("Após clear", contato)
print("Cópia: ", copia)

print("Número de contato: ", len(contato)) #tamanho dicio

#verificar existencia
if "@joao" in contato:
    print(f"Encontrado:  {contato['@joao']}")

if "@inexistente" in contato:
    print("Existe.")

else:
    print("Não existe.")