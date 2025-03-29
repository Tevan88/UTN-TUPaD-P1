#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

altura = float(input("Ingrese su altura en metros (por ejemplo: 1.72 metros): "))
peso = float(input("Ingrese cuantos kgs pesa: "))

indice_masa = peso / (altura * altura)

print(f"Su Indice de Masa Corporal es: {indice_masa}")