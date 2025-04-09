#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Definimos cada una de las variables que nos servirán de contador, les damos el valor 0 a todas 
# para que luego le sumemos cada numero ingresado segun corresponda 
positivo = 0
negativo = 0
par = 0
impar = 0

#Utilizamos el bucle for porque sabemos la cantidad de iteraciones que vamos a realizar
for cont in range (10): #Luego cambiando el 10 por el 100 logramos las iteraciones necesarias para el programa.
    #Le pedimos por consola los números al usuario y los guardamos en la variable num_ingresado.
    num_ingresado = int(input("Ingrese un número, el que usted quiera: "))
   #Luego de ingresar el número comenzamos con los condicionales if para cada caso, si es positivo, negativo, par o impar 
   #y sumamos a la variable correspondiente.
    if num_ingresado > 0:
        positivo += 1
    if num_ingresado % 2 == 0:
        par += 1
    if num_ingresado < 0:
        negativo += 1
    if num_ingresado % 2 == 1:
        impar += 1
#Mostramos por pantalla el mensaje con el resultado de cada variable.
print("Los números ingresados se componen de la siguiente manera:")
print("números positivos:", positivo)
print("números negativos:", negativo)
print("números pares:", par)
print("números impar:", impar)