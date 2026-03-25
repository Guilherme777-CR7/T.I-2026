def somar_todos(*numeros):
    total = 0
    for num in numeros: 
      total += num 
    return total

print(somar_todos(1, 2, 3))   
print(somar_todos(10, 20, 30, 40, 50))   
print(somar_todos())   