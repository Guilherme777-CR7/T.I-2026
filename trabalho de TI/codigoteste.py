doadores = {}

def cadastrar_doador():
    nome = input("Nome do doador: ").strip()
    contato = input("Contato (telefone/email): ").strip()
    if not nome:
        print("Entrada inválida: nome não pode ser vazio.")
        return
    if nome not in doadores:
        doadores[nome] = {"contato": contato, "doacoes": []}
        print(f"Doador {nome} cadastrado com sucesso!")
    else:
        print("Este doador já está cadastrado.")

def cadastrar_item():
    nome = input("Nome do doador: ").strip()
    if nome not in doadores:
        print("Doador não encontrado. Cadastre primeiro o doador.")
        return
    tipo = input("Tipo de item (roupa/alimento/outro): ").lower().strip()
    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Quantidade inválida: deve ser maior que zero.")
            return
    except ValueError:
        print("Entrada inválida: quantidade deve ser um número.")
        return
    if tipo not in ["roupa", "alimento", "outro"]:
        print("Informações inválidas: tipo não reconhecido.")
        return
    doadores[nome]["doacoes"].append({"tipo": tipo, "quantidade": quantidade})
    print(f"Doação registrada para {nome} com sucesso!")

def buscar_doacoes():
    tipo = input("Digite o tipo de item para buscar: ").lower().strip()
    encontrados = []
    for nome, dados in doadores.items():
        for d in dados["doacoes"]:
            if d["tipo"] == tipo:
                encontrados.append((nome, d))
    if encontrados:
        print("\nDoações encontradas:")
        for nome, d in encontrados:
            print(f"{nome}: {d['quantidade']} {d['tipo']}(s)")
    else:
        print("Nenhuma doação encontrada.")

def buscar_por_doador():
    nome = input("Digite o nome do doador: ").strip()
    if nome in doadores:
        print(f"\nDoações de {nome}:")
        for d in doadores[nome]["doacoes"]:
            print(f"{d['quantidade']} {d['tipo']}(s)")
    else:
        print("Doador não encontrado.")

def buscar_por_quantidade_minima():
    try:
        minimo = int(input("Digite a quantidade mínima: "))
    except ValueError:
        print("Entrada inválida.")
        return
    print(f"\nDoadores com doações acima de {minimo}:")
    for nome, dados in doadores.items():
        total = sum(d["quantidade"] for d in dados["doacoes"])
        if total >= minimo:
            print(f"{nome} - {total} itens")

def excluir_doacao():
    nome = input("Nome do doador: ").strip()
    if nome not in doadores or not doadores[nome]["doacoes"]:
        print("Nenhuma doação encontrada para este doador.")
        return
    print(f"\nDoações de {nome}:")
    for i, d in enumerate(doadores[nome]["doacoes"], start=1):
        print(f"{i}. {d['quantidade']} {d['tipo']}(s)")
    try:
        escolha = int(input("Digite o número da doação que deseja excluir: "))
        if 1 <= escolha <= len(doadores[nome]["doacoes"]):
            confirmacao = input("Confirmar exclusão? (s/n): ").lower().strip()
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
    print("Doadores cadastrados:", len(doadores))
    if doadores:
        media = total / len(doadores)
        print(f"Média de doações por doador: {media:.2f}")
        maior = max(doadores.items(), key=lambda x: sum(d["quantidade"] for d in x[1]["doacoes"]))
        menor = min(doadores.items(), key=lambda x: sum(d["quantidade"] for d in x[1]["doacoes"]))
        print(f"Maior doador: {maior[0]} ({sum(d['quantidade'] for d in maior[1]['doacoes'])} itens)")
        print(f"Menor doador: {menor[0]} ({sum(d['quantidade'] for d in menor[1]['doacoes'])} itens)")
    print("=====================\n")

def ranking_doadores():
    ranking = [(nome, sum(d["quantidade"] for d in dados["doacoes"])) for nome, dados in doadores.items()]
    ranking.sort(key=lambda x: x[1], reverse=True)
    print("\n===== RANKING DE DOADORES =====")
    if ranking:
        for i, (nome, total) in enumerate(ranking, start=1):
            print(f"{i}. {nome} - {total} itens doados")
    else:
        print("Nenhum doador registrado ainda.")
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

def listar_doadores():
    print("\n===== LISTA DE DOADORES =====")
    if doadores:
        for nome, dados in doadores.items():
            print(f"Doador: {nome} | Contato: {dados['contato']} | Total de doações: {len(dados['doacoes'])}")
    else:
        print("Nenhum doador cadastrado.")
    print("=============================\n")

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Cadastrar Doador")
        print("2 - Cadastrar Item Doado")
        print("3 - Buscar Doações por Tipo")
        print("4 - Buscar Doações por Doador")
        print("5 - Buscar por Quantidade Mínima")
        print("6 - Excluir Doação")
        print("7 - Gerar Relatório Geral")
        print("8 - Ranking de Doadores")
        print("9 - Ranking por Tipo de Item")
        print("10 - Listar Doadores")
        print("11 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_doador()
        elif opcao == "2":
            cadastrar_item()
        elif opcao == "3":
            buscar_doacoes()
        elif opcao == "4":
            buscar_por_doador()
        elif opcao == "5":
            buscar_por_quantidade_minima()
        elif opcao == "6":
            excluir_doacao()
        elif opcao == "7":
            gerar_relatorio()
        elif opcao == "8":
            ranking_doadores()
        elif opcao == "9":
            ranking_por_tipo()
        elif opcao == "10":
            listar_doadores()
        elif opcao == "11":
            print("Obrigado por contribuir! Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
