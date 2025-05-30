#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberamostrar un mensaje en pantalla que diga “Es mayor de edad”. 
edad = int(input("Por favor, ingresá tu edad: "))
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#  mensaje “Desaprobado”. 
nota = float(input("Por favor, ingresá tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#   número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#   contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#   operador de módulo (%) en Python para evaluar si un número es par o impar. 
num = int(input("Por favor, ingresá un número: "))
if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
   #siguientes categorías pertenece: 
    # Niño/a: menor de 12 años. 
    # Adolescente: mayor o igual que 12 años y menor que 18 años. 
    # Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
    # Adulto/a: mayor o igual que 30 años. 
edad = int(input("Por favor, ingresá tu edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
   #5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
   #(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
   #pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
   #pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
   #de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
   #como una lista o un string.
contraseña = input("Por favor, ingresá una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
#6)escribir un programa que tome la lista  numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
import random
import statistics
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)
print("Lista de números:", numeros_aleatorios)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
if moda < mediana < media:
    print("Sesgo positivo (asimetría a la derecha).")
elif media < mediana < moda:
    print("Sesgo negativo (asimetría a la izquierda).")
else:
    print("No hay sesgo o es despreciable.")
   #7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
    #termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
   #pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
   #pantalla. 
texto = input("Ingresá una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print("Resultado:", texto)
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
   #dependiendo de la opción que desee: 
   #1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
   #2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
   #3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
   #El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
   #usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
   #lower() y title() de Python para convertir entre mayúsculas y minúsculas. 
nombre = input("Ingresá tu nombre: ")
print("Elegí una opción:")
print("1 - Nombre en MAYÚSCULAS")
print("2 - Nombre en minúsculas")
print("3 - Nombre con la primera letra en mayúscula")
opcion = input("Ingresá el número de la opción (1, 2 o 3): ")
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, elegí 1, 2 o 3.")
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
   #magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
   #por pantalla: 
   #● Menor que 3: "Muy leve" (imperceptible). 
   #● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
   #● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
   #generalmente no causa daños). 
   #● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
   #débiles). 
   #● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
   #● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
magnitud = float(input("Ingresá la magnitud del terremoto (escala de Richter): "))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")
#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
   #del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
   #si el usuario se encuentra en otoño, invierno, primavera o verano. 
   # Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingresá el número del mes (1 a 12): "))
dia = int(input("Ingresá el día del mes: "))

# Convertir mes y día en un número de fácil comparación, por ejemplo 21/03 -> 321
fecha = mes * 100 + dia

# Determinar estación según hemisferio
if hemisferio == "N":
    if (321 <= fecha <= 620):
        estacion = "Primavera"
    elif (621 <= fecha <= 920):
        estacion = "Verano"
    elif (921 <= fecha <= 1220):
        estacion = "Otoño"
    else:  # del 21 de diciembre al 20 de marzo
        estacion = "Invierno"

elif hemisferio == "S":
    if (321 <= fecha <= 620):
        estacion = "Otoño"
    elif (621 <= fecha <= 920):
        estacion = "Invierno"
    elif (921 <= fecha <= 1220):
        estacion = "Primavera"
    else:  # del 21 de diciembre al 20 de marzo
        estacion = "Verano"

else:
    estacion = "Hemisferio no válido"

# Imprimir el resultado
print("Estás en:", estacion)