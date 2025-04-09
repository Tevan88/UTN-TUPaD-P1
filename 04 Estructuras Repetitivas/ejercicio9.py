#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#Importamos la funcion mean (para calcular la media) de statistics
from statistics import mean
#Definimos la variable valor_final para utilizar como, justamente, valor final en el ciclo for
#que luego se puede modificar el valor de la variable por 101 y así lograr el objetivo del programa.
valor_final = 4
num1 = 0

for cont in range(1,valor_final):
    num2 = float(input("Ingrese un número entero:"))
    num1 += num2

media = mean(num1)
print("La media de los números ingresados es:", media)