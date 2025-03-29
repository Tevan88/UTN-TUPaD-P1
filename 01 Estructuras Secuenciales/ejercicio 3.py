#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = int(input("Ingrese la medida del radio del círculo: "))
pi = 3.1415
area = pi * radio **2 
perimetro = 2 * pi * radio
print (f"El área del círculo es {area}, y su perímetro es {perimetro}")
