for x in range(11,1,-2):
    print(x, "Debo practicar ciclos FOR")

print("////////")

x = 1
while x <= 5:
    print(x,"Debo aprender ciclos")
    x = x + 1
print("////////")
x = 5
while x >= 1:
    print(x,"Debo aprender ciclos")
    x = x - 1

print("//// Por bandera ////")

umbral = 10
sumatoria = 0

while sumatoria < umbral:
    print("Ingrese un número: ")
    num = int(input())
    sumatoria += num # Esto es igual a sumatoria = sumatoria + num
