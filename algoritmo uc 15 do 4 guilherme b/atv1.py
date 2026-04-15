def calcular_media():
    notas = []

    for i in range(3):
        while True:
            try:
                nota = float(input("Digite uma nota: "))
                notas.append(nota)
                break
            except:
                print("Digite um número válido.")

    media = sum(notas) / 3
    print("Média:", round(media, 2))

calcular_media()