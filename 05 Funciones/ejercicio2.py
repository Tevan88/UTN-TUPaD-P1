#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.


def saludar_usuario(nombre):
    return nombre

#Programa principal.

#Definimos la variable nombre con lo que ingrese el usuario como su nombre
nombre = input("Escriba su nombre: ")
#Mostramos por pantalla 
print(saludar_usuario(f"Hola {nombre}!"))