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
    sumatoria = sumatoria + num #Otra forma de escribirlo sería sumatoria += num.
    print()

print("La sumatoria de los numeros ingresados es: ", sumatoria)
print("El promedio entre los numeros ingresados es: ",(sumatoria/cant_numeros))

print("/////Ciclo por contador y por bandera/////")

sueldo_anual = 0
cont_meses = 1

print("Ingrese su sueldo del mes n°", cont_meses)
sueldo_mensual = float(input())

while cont_meses < 12 and sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual
    cont_meses += 1
    print("Ingrese su sueldo del mes n°", cont_meses)
    sueldo_mensual = float(input())

if sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual

print("Tu sueldo anual es: ", sueldo_anual)

print("////minimo y maximo////")

cantidad = 4
max_numero = float('-inf')
min_numero = float('inf')

for contador in range(cantidad):
    print("Ingrese num",contador+1)
    num = float(input())
    if num > max_numero:
        max_numero = num
    elif num < min_numero:
        min_numero = num

print("El mayor número ingresado es:",max_numero)
print("El menor número ingresado es:",min_numero)

#Cambiando la variable max_numero por min_numero y poner 'inf' y cambiando IF NUM<MIN_NUMERO: podemos sacar el numero minimo ingresado.