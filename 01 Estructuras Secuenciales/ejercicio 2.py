#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ahora su apellido: ")
edad = input("¿Cuántos años tiene?: ")
lugar_residencia = input("¿Cuál es su país de residencia?: ")

print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {lugar_residencia}")