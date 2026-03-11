s = input("digite sua senha: ")
tm = len(s) >= 8
tnumero = any(char.isdigit() for char in s)

if tm and tnumero:
    print("Senha válida!")
else:
    print("Senha inválida!")
    
    if not tm:
        print("- A senha deve ter no mínimo 8 caracteres.")
    if not tnumero:
        print("- A senha deve conter pelo menos um número.")
