catalogo = {}

emprestimoAtivo = {}

historico = []

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro livro com codigo {codigo} já existe")
        return False
   
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True

def empresta_livro(codigo, nome_aluno):

    # VALIDAÇÃO 1: Livro existe no catálogo?
    if codigo not in catalogo:
        print(f"Erro: Livro com código (codigo) não encontrado!")
        return False

    # VALIDAÇÃO 2: Há quantidade disponível?
    if catalogo[codigo]["quantidade"] <= 0:
        print(f"Erro: '{catalogo[codigo]['titulo']}' não está disponível!")
        return False

    # VALIDAÇÃO 3: Aluno já pegou 2 livros?
    livros_do_aluno = conta_livros_aluno(nome_aluno)
    if livros_do_aluno >= 2:
        print(f"Erro: {nome_aluno} já pegou 2 livros (limite máximo)!")
        return False

    # VALIDAÇÃO 4: Aluno já pegou este livro?
    if codigo in emprestimos_ativos and nome_aluno in emprestimos_ativos[codigo]:
        print(f"Erro: {nome_aluno} já pegou este livro!")
        return False

    if codigo not in emprestimos_ativos:
        emprestimos_ativos[codigo] = []

        # Adiciona o aluno à lista de quem pegou este livro
emprestimos_ativos[codigo].append(nome_aluno)

# Diminui a quantidade disponível
catalogo[codigo]["quantidade"] -= 1

# Registra no histórico
historico.append({
    "tipo": "emprestimo",
    "codigo": codigo,
    "titulo": catalogo[codigo]["titulo"],
    "aluno": nome_aluno
})

print(f"{nome_aluno} pegou '{catalogo[codigo]['titulo']}' com sucesso")
return True