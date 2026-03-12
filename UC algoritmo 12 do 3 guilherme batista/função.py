#sem funçao
print("python é facil")
print("python é facil")
print("python é facil")

#com funçao
def exibirMensagem():
    print("ola, mundo!")

exibirMensagem()

#com funçao pariametro
def saudar(nome):
    print(f"ola, {nome}!")

saudar("ana")
saudar("bruno")


def exibirMensagem(nome, mensagem):
    print(f"{mensagem}, {nome}!")

exibirMensagem("ana", "bom dia")

exibirMensagem(nome = "bruno", mensagem = "bom dia")

#funcao que  retorna media
def calcularmedia(n1, n2):
    media = (n1 + n2) / 2
    return media 


resultado = calcularmedia(8.0, 9.0)
print(f"Média: {resultado}")