#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#Definimos la variable edad pidiendo al usuario su edad.
edad = int(input("Ingrese su edad:"))
#Comenzamos el condicional if la edad ingresada es mayor o igual a 0 Y edad es menor a 12.
if edad >= 0 and edad < 12:
    #Mostramos por pantalla el mensaje de niño/a.
    print("Usted es un niño/a")
#Sino si edad es mayor o igual a 12 Y edad es menor a 18.
elif edad >= 12 and edad < 18:
    #Mostramos por pantalla el mensaje de adolescente.
    print("Usted es adolescente")
#Sino si edad es mayor o igual a 18 Y edad es menor a 30.
elif edad >= 18 and edad < 30:
    #Mostramos por pantalla el mensaje de adulto/a joven.
    print("Usted es adulto/a joven")
#Sino se cumplen las condiciones anteriores, es decir, si la edad es 30 o mayor.
else:
    #Mostramos por pantalla el mensaje de adulto/a mayor.
    print("Usted es adulto/a mayor")
