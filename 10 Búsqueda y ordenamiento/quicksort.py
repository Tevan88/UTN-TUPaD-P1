import random 

lista = random.sample(range(1, 101), 100)# Generamos una lista de 100 números aleatorios entre 1 y 100

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
print(lista)   
print(f"lista ordenada {quicksort(lista)}")