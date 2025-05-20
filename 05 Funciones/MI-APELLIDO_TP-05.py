def siguiente_numero(numero):
    return numero + 1

def anterior_numero(numero):
    return numero - 1

def agregar_lista(lista, elemento):
    lista.append(elemento)

mi_lista = [1, 2, 3]
agregar_lista(mi_lista, 4)
print(mi_lista)  

def eliminar_lista(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
        print(f"Se ha eliminado el elemento {elemento} de la lista.")
        print(f"Lista después de eliminar: {lista}")
    else:
        print(f"El elemento {elemento} no está en la lista.")

mi_lista = [1, 2, 3, 4]
eliminar_lista(mi_lista, 2)

valor = int(input("Ingrese un número: "))

print(f"El siguiente número es: {siguiente_numero(valor)}")
print(f"El número anterior es: {anterior_numero(valor)}")



