#Forma Iterativa
def factorial_iterativo(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado    

#Forma Recursiva simple
def factorial_recursivo(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num - 1)
    
#Suma recursiva
def suma_lista(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + suma_lista(lst[1:])
    
lista = [1,2,3,4,5]

print(f"el valor de la suma de todos los elementos de la lista es: {suma_lista(lista)}")

#Repetir frase recursivo
def repetir_frase(num, frase):
    if num == 0:
        return "No hay más frases para repetir"
    elif num < 0:
        return "El número de repeticiones no puede ser negativo"
    else:
        print(frase)
        repetir_frase(num - 1, frase)

num = int(input("Ingrese el número de veces que desea repetir la frase: "))
frase = input("Ingrese la frase que desea repetir: ")
repetir_frase(num, frase)

#Sumar n valores recursivo
def sumar_n_valores(num):
    if num == 0:
        return 0
    else:
        return num + sumar_n_valores(num - 1)
    
num = int(input("Ingrese un número: "))
print(f"La suma de los primeros {num} números es: {sumar_n_valores(num)}")

#Fibonacci recursivo
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

n = int(input("Ingrese la posición en la serie de Fibonacci que quiere saber: "))
print(f"El número en la posición {n} de la serie de Fibonacci es: {fibonacci_recursivo(n)}")

#Sumar n primos recursivos
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sumar_n_primos(num):
    if num == 1:
        return 0
    elif es_primo(num):
        return num + sumar_n_primos(num - 1)
    else:   
        return sumar_n_primos(num - 1)  
    
num = int(input("Ingrese un número: "))
print(f"La suma de los primeros primos hasta {num} es: {sumar_n_primos(num)}")