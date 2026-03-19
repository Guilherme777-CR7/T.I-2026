def tipo_magia(f, a):
    if f and a:
        return "Vapor"
    elif f:
        return "Fogo"
    elif a:
        return "Água"
    else:
        return "Sem magia"