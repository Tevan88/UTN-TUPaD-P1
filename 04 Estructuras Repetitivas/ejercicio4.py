#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

#Le pedimos por consola un número entero al usuario y lo guardamos en la variable num.
num1 = int(input("Ingrese un número entero: "))
num2 = 1 #Definimos ocasionalmente la variable num2 para ingresar en el bucle while ya que tenemos un AND como condiciones logicas para realizarse.

while num1 >= 0 and num2 > 0:
    #le pedimos al usuario otro numero para sumar, si ingresa 0 termina el bucle.
    print("Ingrese otro número entero para sumarlo ó ingrese 0 para terminar") 
    num2 = int(input())
    num1 = num1 + num2 #Redefinimos en cada bucle la variable num1 por la suma de num1 + num2.

#Cuando el usuario ingresa 0 sale del bucle y muestra el mensaje con la suma final por pantalla.
print("La suma entre los números ingresados es",num1)


