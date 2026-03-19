def verificar_acesso(u, s, t):
    if t >= 3:
        return "Bloqueado"
    
    if u == "admin":
        if s == "1234":
            return "Acesso total"
        else:
            return "Senha incorreta"
    else:
        return "Usuário inválido"