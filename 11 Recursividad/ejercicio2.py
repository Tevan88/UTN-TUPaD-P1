#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

#Definimos la función fibonacci_recursivo que recibe un número como parámetro
#y devuelve el valor de la serie de Fibonacci en esa posición
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    
#Programa principal

#Le pedimos al usuario que ingrese un número y lo guardamos en la variable num
num = int(input("Ingrese la posición en la serie de Fibonacci que quiere saber: "))

for i in range(num + 1):
    #Mostramos el valor de la serie de Fibonacci en cada posición
    print(f"El número en la posición {i} de la serie de Fibonacci es: {fibonacci_recursivo(i)}")    

