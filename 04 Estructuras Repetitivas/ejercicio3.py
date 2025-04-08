#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#Le pedimos por consola dos numeros enteros al usuario.
num_min = int(input("Ingrese un número entero: "))
num_max = int(input("Ingrese un número entero mayor al anterior: "))
x = num_min

if num_min < num_max:
    for cont in range(num_min, num_max):
        x += 1  #ACA PUEDE ESTAR EL PROBLEMA, NO CAIGO EN COMO HACER EL CONTADOR.
else:
    print("El segundo número debe ser mayor al primero ingresado")

print(f"La suma de todos los numeros enteros comprendidos entre {num_min} y {num_max} es: {x}")
