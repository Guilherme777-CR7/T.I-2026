def lancar_foguete(com, cli, sc):
    if com < 100:
        return "Combustível insuficiente"
    if cli != "bom":
        return "Clima desfavorável"
    if not sc:
        return "Falha no sistema"
    
    return "Lançamento autorizado"