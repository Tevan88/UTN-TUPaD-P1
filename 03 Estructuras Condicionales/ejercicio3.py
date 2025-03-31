#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

#Definimos la variable num pidiendole un numero entero positivo al usuario.
num = int(input("Ingrese un número entero positivo:"))
#Comenzamos el condicional if con dos condiciones, si num es mayor o igual a 0 Y si num dividido 2 el resto es 0.
if (num >= 0) and (num % 2 == 0):
    #Mostramos el mensaje en pantalla.
    print("Ha ingresado un número par")
else:
    #Mostramos el mensaje por pantalla si no se cumple la condicion.
    print("Por favor, ingrese un número par")
