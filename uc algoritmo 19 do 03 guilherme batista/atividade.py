# 1. Sistema de Rank com Penalidade
def rank_jogador(pt, drt):
    pf = pt - (drt * 10)
    
    if pf < 0:
        return "Banido"
    elif pf < 100:
        return "Bronze"
    elif pf < 300:
        return "Prata"
    elif pf < 600:
        return "Ouro"
    else:
        return "Diamante"

def saldo_final(s, sq):
    if sq > s:
        return "Saldo insuficiente"
    
    if sq > 1000:
        taxa = sq * 0.02
        return s - (sq + taxa)
    
    return s - sq

def tipo_magia(f, a):
    if f and a:
        return "Vapor"
    elif f:
        return "Fogo"
    elif a:
        return "Água"
    else:
        return "Sem magia"

def pontuacao_total(pontos, tempo):
    if tempo < 30:
        pontos += 50
    elif tempo > 100:
        pontos -= 20
        
    if pontos > 200:
        return "Recorde"
    return pontos

# 5. Sistema de Segurança com Múltiplas Condições
def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"
    
    if usuario == "admin":
        if senha == "1234":
            return "Acesso total"
        else:
            return "Senha incorreta"
    else:
        return "Usuário inválido"

# 6. Missão Espacial – Lógica Composta
def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível insuficiente"
    if clima != "bom":
        return "Clima desfavorável"
    if not sistema_ok:
        return "Falha no sistema"
    
    return "Lançamento autorizado"