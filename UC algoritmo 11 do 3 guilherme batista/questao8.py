Compra = float(input("insira o valor da compra:"))

if Compra < 100:
    desconto = 0 
elif Compra >= 100 and Compra < 500:
   desconto = Compra * 0.05
elif Compra >= 500 and Compra < 1000:
   desconto = Compra * 0.10
else:
   desconto = Compra * 0.15

print("seu desconto vai ser: R$", desconto)
dt = Compra - desconto
print("seu desconto total é: R$", dt)