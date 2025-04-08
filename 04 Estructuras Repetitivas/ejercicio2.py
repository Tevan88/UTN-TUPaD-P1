#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#Primero le pedimos al usuario que ingrese un número y lo guardamos como string en una variable.
print("Ingrese un número entero:")
num = str(input())
#definimos la variable cantidad como la longitud de la variable num.
cantidad = len(num)
#mostramos por pantalla la cantidad de digitos que contiene el numero ingresado.
print("La cantidad de digitos del numero ingresado es:",cantidad)