#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#Definimos la variable valor_final para utilizar como, justamente, valor final en el ciclo for
#que luego se puede modificar el valor de la variable por 101 y así lograr el objetivo del programa.
valor_final = 10
suma = 0 #Esta variable nos va a servir de acumuladora luego en el bucle for
#Definimos el bucle for unilizando como valor final la variable definida previamente
for cont in range(valor_final):
    num1 = float(input("Ingrese un número entero:")) #Le pedimos numeros al usuario y los almacenamos en la variable num
    suma += num1

media = suma / valor_final #Definimos la variable media por la división de la variable suma dividido la cantidad de intentos 
                           #realizados por el usuario. 
print("La media de los números ingresados es:", media) #Mostramos el mensaje por pantalla.