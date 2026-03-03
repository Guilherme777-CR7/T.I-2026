sc = "123456"
nu = "fulano"
tr = 3

while tr > 0:
    sd = input("digite sua senha: ")

    if sd == sc:
        print(f"ola, {nu}. Seja bem vindo ao nosso banco!")
        break
    else:
        tr -= 1
        
        if tr == 2:
            print("Senha incorreta! Você ainda tem 2 tentativas.")
        elif tr == 1:
            print("senha incorreta! Você ainda tem 1 tentativa.")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")