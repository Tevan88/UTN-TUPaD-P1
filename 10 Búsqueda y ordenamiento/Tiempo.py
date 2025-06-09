#importamos las librerías necesarias 
import random #importamos la librería random para generar números aleatorios
import time #importamos la librería time para medir el tiempo de ejecución


lista = random.sample(range(1, 10001), 10000)# Generamos una lista de números aleatorios 


#Método de ordenamiento quicksort

def quicksort(lista): 
    if len(lista) <= 1: 
        return lista 
    else: 
        pivot = lista[len(lista) // 2]
        izquierda = [x for x in lista if x < pivot]
        medio = [x for x in lista if x == pivot]
        derecha = [x for x in lista if x > pivot]
        return quicksort(izquierda) + medio + quicksort(derecha)

#Método de ordenamiento burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
          
            if lista[j] > lista[j+1]:# 
                lista[j], lista[j+1] = lista[j+1], lista[j] #
    return lista   



#Se mide el tiempo de ejecución del método quicksort
inicio_tiempo = time.process_time()
lista_ordenada = quicksort(lista)
fin_tiempo = time.process_time()
 
print("Tiempo de ordenamiento quicksort:", fin_tiempo - inicio_tiempo, "segundos")

 
inicio_tiempo_burbuja = time.process_time()
lista_ordenada_burbuja = burbuja(lista)
fin_tiempo_burbuja = time.process_time()

print(f"Tiempo de ordenamiento burbuja: {fin_tiempo_burbuja - inicio_tiempo_burbuja} segundos")

