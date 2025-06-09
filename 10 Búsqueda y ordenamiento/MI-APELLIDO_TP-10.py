#importamos las librerías necesarias 
import random #importamos la librería random para generar números aleatorios
import time #importamos la librería time para medir el tiempo de ejecución


lista = random.sample(range(1, 10000), 9990)# Generamos una lista de 9900 números aleatorios entre 1 y 10000


#Método de ordenamiento quicksort

def quicksort(lista): #definición de la función quicksort
    if len(lista) <= 1: #caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
        return lista 
    else: # caso recursivo: se elige un pivote y se divide la lista en tres partes
        # elementos menores que el pivote, elementos iguales al pivote y elementos mayores que el pivote
        # luego se ordenan recursivamente las dos partes y se combinan
        pivot = lista[len(lista) // 2]
        izquierda = [x for x in lista if x < pivot]
        medio = [x for x in lista if x == pivot]
        derecha = [x for x in lista if x > pivot]
        return quicksort(izquierda) + medio + quicksort(derecha)# se combinan las partes ordenadas y se devuelve la lista ordenada

#Método de ordenamiento burbuja
def burbuja(lista):# definición de la función burbuja
    n = len(lista)# obtenemos la longitud de la lista
    for i in range(n):# iteramos sobre la lista n veces
        for j in range(0, n-i-1):# iteramos sobre la lista desde el inicio hasta el final menos i
            # comparamos los elementos adyacentes y los intercambiamos si están en el orden incorrecto.
            if lista[j] > lista[j+1]:# 
                lista[j], lista[j+1] = lista[j+1], lista[j] #
    return lista    #retornamos la lista ordenada    


# Ejemplo de uso quicksort
#Se mide el tiempo de ejecución del método quicksort
inicio_tiempo = time.process_time()# inicia el conteo del tiempo de ejecución
lista_ordenada = quicksort(lista)# ordena la lista usando el método quicksort
fin_tiempo = time.process_time()# finaliza el conteo del tiempo de ejecución
#mostramos por pantalla el tiempo de ejecución del método quicksort    
print("Tiempo de ordenamiento quicksort:", fin_tiempo - inicio_tiempo, "segundos")



# Ejemplo de uso buble sort
# Se mide el tiempo de ejecución del método burbuja   
inicio_tiempo_burbuja = time.process_time()# inicia el conteo del tiempo de ejecución
lista_ordenada_burbuja = burbuja(lista)# ordena la lista usando el método burbuja
fin_tiempo_burbuja = time.process_time()# finaliza el conteo del tiempo de ejecución
# mostramos por pantalla el tiempo de ejecución del método burbuja
print(f"tiempo de ordenamiento burbuja: {fin_tiempo_burbuja - inicio_tiempo_burbuja} segundos")

