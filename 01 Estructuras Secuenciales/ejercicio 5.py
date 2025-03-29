#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un número (no puede ser 0): "))
num2 = int(input("Ingrese otro número (nuevamente no puede ser 0): "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2

print(f"La suma entre {num1} y {num2} es {suma}")
print(f"La resta entre {num1} y {num2} es {resta}")
print(f"La multiplicación entre {num1} y {num2} es {multi}")
print(f"La división entre {num1} y {num2} es {divi}")

