#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

#Importamos desde statistics sólo mode, median y mean.
from statistics import mode, median, mean
#Importamos para utilizar la función random.
import random
#Definimos la variable numeros_aleatorios para que de los numeros contenidos entre 1 y 100 (incluidos los extremos) nos de una 
#lista de 50 numeros aleatorios.
numeros_aleatorios = [random.randint(1,100) for i in range (50)]
#Asignamos estos 50 numeros aleatorios a la variable mi_lista.
mi_lista = numeros_aleatorios
#Definimos las variables moda, mediana y media con sus respectivas funciones.
moda = (mode(mi_lista))
mediana = (median(mi_lista))
media = (mean(mi_lista))
#Mostramos por pantalla la media, mediana y moda.
print(media)
print(mediana)
print(moda)
#Comenzamos el condicional if.
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
if (media > mediana) and (mediana > moda):
    print("Sesgo positivo")
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo")
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
elif (media == mediana == moda):
    print("Sin sesgo")
else:
    print("No se puede determinar si esta distribución tiene sesgo o no.")





