#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(numero):
    if numero == 0:
        return ""
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)
    
# Programa principal
numero = int(input("Ingresa un número entero positivo: "))
if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    resultado = decimal_a_binario(numero)
    if resultado == "":
        resultado = "0"

print(f"La representación en binario de {numero} es: {resultado}")