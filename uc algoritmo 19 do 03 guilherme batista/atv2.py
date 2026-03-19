s = float(input("quanto é o seu saldo?"))
sq = float(input("quanto é o seu saque?"))
def saldo_final(s, sq):
    if sq > s:
        return "Saldo insuficiente"
    
    if sq > 1000:
        taxa = sq * 0.02
        return s - (sq + taxa)
    
    return s - sq

