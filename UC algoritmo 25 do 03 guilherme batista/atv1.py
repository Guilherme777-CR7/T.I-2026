def s(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b
def div(a, b):
    if b == 0:
        return "Não pode haver uma divisão com zero."
    return a / b

def cal():
    while True:
        print("\n calculadora")
        print("1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão, 0: Sair")
        
        op = input("Escolha uma opção: ")

        if op == '0':
            print("Saindo")
            break
        
        if op not in ['1', '2', '3', '4']:
            print("Oção invalida tente novamente")
            continue

        try:
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))

            if op == '1':
                print(f"Resultado: {s(n1, n2)}")
            elif op == '2':
                print(f"Resultado: {sub(n1, n2)}")
            elif op == '3':
                print(f"Resultado: {mult(n1, n2)}")
            elif op == '4':
                print(f"Resultado: {div(n1, n2)}")
                
        except ValueError:
            print("apenas numeros por favor")

if __name__ == "__main__":
    cal()