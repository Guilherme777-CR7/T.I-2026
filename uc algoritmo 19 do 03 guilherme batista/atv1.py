pt = float(input("quantos pontos você tem?"))
drt = float(input("quantas derrotas você tem?"))

def rj(pt, drt):
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
    