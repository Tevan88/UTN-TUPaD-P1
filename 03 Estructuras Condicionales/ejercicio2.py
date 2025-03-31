#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

#Le pedimos la nota al usuario definiendo la variable nota.
nota = float(input("Ingrese su calificacion (del 1 al 10):"))
#Comenzamos el condicional if la nota ingresada es mayor o igual a 6.
if nota >= 6:
    #Imprimimos el mensaje aprobado por pantalla.
    print("Aprobado")
else:
    #Sino mostramos el mensaje desaprobado por pantalla.
    print("Desaprobado")
