#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario 
#y llamar a esta función con los valores ingresados.

#Creamos la variable con los argumentos nombre, apellido, edad, residencia
def informacion_personal(nombre, apellido, edad, residencia):
    return nombre, apellido, edad, residencia

#Programa principal.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su país de residencia: ")

print(informacion_personal(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"))
