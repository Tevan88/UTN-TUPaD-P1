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

print("/////Sumatorias y promedios/////")

cant_numeros = 5
sumatoria = 0

for cont in range(1,cant_numeros+1): #Le ponemos a cant_numeros+1 así incluye el 5 como valor final
    print("Ingrese un número",cont)
    num = int(input())
    sumatoria = sumatoria + num
    print()

print("La sumatoria de los numeros ingresados es: ", sumatoria)
print("El promedio entre los numeros ingresados es: ",(sumatoria/cant_numeros))



