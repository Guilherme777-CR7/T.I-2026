doadores = {} 

def cadastrar_doador():
    nome = input("Nome do doador: ")
    contato = input("Contato: ")
    if nome.strip() == "":
        print("Entrada inválida: nome não pode ser vazio.")
        return
    if nome not in doadores:
        doadores[nome] = {"contato": contato, "doacoes": []}
    print("Doador cadastrado com sucesso!")

def cadastrar_item():
    nome = input("Item a ser doado: ")
    if nome not in doadores:
        print("item não encontrado. Cadastre primeiro o doador.")
        return
    tipo = input("Tipo de item (roupa/alimento/outro): ").lower()
    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Entrada inválida: quantidade deve ser um número.")
        return
    if tipo not in ["roupa", "alimento", "outro"]:
        print("Informações inválidas: tipo não reconhecido.")
        return
    doadores[nome]["doacoes"].append({"tipo": tipo, "quantidade": quantidade})
    print(f"Doação registrada para {nome} com sucesso!")

def buscar_doacoes():
    tipo = input("Digite o tipo de item para buscar: ").lower()
    encontrados = []
    for nome, dados in doadores.items():
        for d in dados["doacoes"]:
            if d["tipo"] == tipo:
                encontrados.append((nome, d))
    if encontrados:
        print("Doações encontradas:")
        for nome, d in encontrados:
            print(f"{nome}: {d['quantidade']} {d['tipo']}(s)")
    else:
        print("Nenhuma doação encontrada.")

def excluir_doacao():
    nome = input("Nome do doador: ")
    if nome not in doadores or not doadores[nome]["doacoes"]:
        print("Nenhuma doação encontrada para este doador.")
        return
    print(f"Doações de {nome}:")
    for i, d in enumerate(doadores[nome]["doacoes"], start=1):
        print(f"{i}. {d['quantidade']} {d['tipo']}(s)")
    try:
        escolha = int(input("Digite o número da doação que deseja excluir: "))
        if 1 <= escolha <= len(doadores[nome]["doacoes"]):
            confirmacao = input("Confirmar exclusão? (s/n): ").lower()
            if confirmacao == "s":
                removida = doadores[nome]["doacoes"].pop(escolha - 1)
                print(f"Doação de {removida['quantidade']} {removida['tipo']}(s) removida com sucesso!")
            else:
                print("Ação cancelada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def gerar_relatorio():
    total = sum(d["quantidade"] for dados in doadores.values() for d in dados["doacoes"])
    print("\n===== RELATÓRIO =====")
    print(f"Total de itens doados: {total}")
    print("ODS 1 – Erradicação da Pobreza: cada doação ajuda a reduzir a desigualdade!")
    print("=====================\n")

def ranking_doadores():
    ranking = []
    for nome, dados in doadores.items():
        total_doador = sum(d["quantidade"] for d in dados["doacoes"])
        ranking.append((nome, total_doador))
    ranking.sort(key=lambda x: x[1], reverse=True)
    print("\n===== RANKING DE DOADORES =====")
    for i, (nome, total) in enumerate(ranking, start=1):
        print(f"{i}. {nome} - {total} itens doados")
    print("===============================\n")

def ranking_por_tipo():
    tipos = ["roupa", "alimento", "outro"]
    print("\n===== RANKING POR TIPO DE ITEM =====")
    for tipo in tipos:
        ranking = []
        for nome, dados in doadores.items():
            total_tipo = sum(d["quantidade"] for d in dados["doacoes"] if d["tipo"] == tipo)
            if total_tipo > 0:
                ranking.append((nome, total_tipo))
        ranking.sort(key=lambda x: x[1], reverse=True)
        print(f"\nTipo: {tipo.capitalize()}")
        if ranking:
            for i, (nome, total) in enumerate(ranking, start=1):
                print(f"{i}. {nome} - {total} {tipo}(s)")
        else:
            print("Nenhuma doação deste tipo.")
    print("====================================\n")

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Cadastrar Doador")
        print("2 - Cadastrar Item Doado")
        print("3 - Buscar Doações")
        print("4 - Excluir Doação")
        print("5 - Gerar Relatório")
        print("6 - Ranking de Doadores")
        print("7 - Ranking por Tipo de Item")
        print("8 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_doador()
        elif opcao == "2":
            cadastrar_item()
        elif opcao == "3":
            buscar_doacoes()
        elif opcao == "4":
            excluir_doacao()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            ranking_doadores()
        elif opcao == "7":
            ranking_por_tipo()
        elif opcao == "8":
            print("Obrigado por contribuir! Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
