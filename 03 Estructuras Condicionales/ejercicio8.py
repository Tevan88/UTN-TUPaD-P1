#Definimos las variables nombre y maymain (esta última para definir si es mayuscula, minúscula o mayúscula/minúscula)
nombre = input("Introduzca su nombre: ")
maymin = input("Indique cómo quiere que se escriba su nombre: (1) Todo mayuscula, (2) Todo minúscula, (3) Mayúscula minúscula: ")

#Definimos la variable if con sus Sino si para cada opción que le preguntamos al usuario e imprimimos por pantalla los resultados.
if maymin == "1":
    print(nombre.upper())
elif maymin == "2":
    print(nombre.lower())
elif maymin == "3":
    print(nombre.title())
else:
    pass