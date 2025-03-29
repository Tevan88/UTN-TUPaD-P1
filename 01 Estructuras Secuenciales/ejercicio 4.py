#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundo = int(input("Ingrese una cantidad de segundos: "))
hora = 3600
hora_calculada = segundo / hora

print(f"{segundo} segundos equivalen a {hora_calculada} horas")
