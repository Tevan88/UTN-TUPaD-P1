#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

#Le pedimos la edad al usuario.
edad = int(input("Ingrese su edad:"))
#Armamos la estructura condicional if con la condicion si la edad es mayor o igual a 18.
if edad >= 18:
    #Mostramos el mensaje por pantalla.
    print("Es mayor de edad")
#Sino, termina el codigo.
else:
    pass