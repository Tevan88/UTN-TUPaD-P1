#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
# y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
# como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario 
# y llamar ambas funciones para mostrar los resultados.
PI = 3.1416
def calcular_area_circulo(radio):
    return PI * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * PI * radio

#Programa principal

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")