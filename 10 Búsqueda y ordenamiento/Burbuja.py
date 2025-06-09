#importamos las librerías necesarias 
import random #importamos la librería random para generar números aleatorios

lista = random.sample(range(1, 51), 50)

#Método de ordenamiento burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]: 
                lista[j], lista[j+1] = lista[j+1], lista[j] 
    return lista    #retornamos la lista ordenada    

# Ejemplo de uso bubble sort
print(lista)
print(f"Lista ordenada: {burbuja(lista)}")

