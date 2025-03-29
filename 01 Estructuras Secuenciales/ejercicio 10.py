#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
num1 = int(input("Ingrese un número entero (mayor o igual a 0): "))
num2 = int(input("Ingrese otro número entero (mayor o igual a 0): "))
num3 = int(input("Ingrese un último número entero (mayor o igual a 0): "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio entre los tres números ingresados es: {promedio}")

