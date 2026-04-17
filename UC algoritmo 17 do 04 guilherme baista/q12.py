while True:
    print("\n calculadora")
    print("1 Soma")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")
    print("5 Sair")

    try:
        op = int(input("escolha uma das opções: "))
        if op == 5:
            break

        n1 = float(input("primeiro número: "))
        n2 = float(input("segundo número: "))

        if op == 1:
            print("resultado:", n1 + n2)
        elif op == 2:
            print("resultado:", n1 - n2)
        elif op == 3:
            print("resultado:", n1 * n2)
        elif op == 4:
            print("resultado:", n1 / n2 if n2 != 0 else "não há divisão por zero")
        else:
            print("não tem essa opção")

    except ValueError:
        print("erro na entrada")