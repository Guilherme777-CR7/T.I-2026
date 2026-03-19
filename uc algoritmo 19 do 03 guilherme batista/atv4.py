
def pontuacao_total(p, t):
    if t < 30:
        p += 50
    elif t > 100:
        p -= 20
        
    if p > 200:
        return "Recorde"
    return p
