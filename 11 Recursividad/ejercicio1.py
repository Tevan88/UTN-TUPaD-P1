#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

#Definimos la función factorial_recursivo que recibe un número como parámetro
#y devuelve el factorial de ese número
def factorial_recursivo(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num - 1)

#Programa principal

num = int(input("Ingrese un número: ")) #Le pedimos al usuario que ingrese un número
#y lo guardamos en la variable num

#Iteramos desde 1 hasta el número ingresado por el usuario
#y mostramos el factorial de cada número
for i in range(1, num + 1):
    print(f"El factorial de {i} es: {factorial_recursivo(i)}")

