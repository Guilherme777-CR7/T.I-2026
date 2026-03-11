idade = input("digite sua idade: ")

if idade < 12:
    print("você está na categoria infatil!")
elif idade >= 12 and idade < 18:
    print("você está na categoria juvenil!")
elif idade >= 18 and idade <60:
    print("você está na categoria adulto!")
else:
    print("você está na categoria senior!")
