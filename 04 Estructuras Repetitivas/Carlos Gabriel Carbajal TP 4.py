#1) Imprimir números del 0 al 100 en orden creciente (uno por línea):
for i in range(101):
    print(i)
#2) Determinar la cantidad de dígitos de un número entero ingresado por el usuario:

numero = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print(f"El número tiene {cantidad_digitos} dígitos.")

#3) Sumar los números enteros comprendidos entre dos valores dados por el usuario, excluyendo los valores:

inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))
suma = sum(range(inicio + 1, fin))
print(f"La suma de los números entre {inicio} y {fin} es: {suma}")
#4) Sumar números enteros en secuencia hasta que el usuario ingrese un 0:

total = 0
while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"El total acumulado es: {total}")
#5) Juego de adivinar un número aleatorio entre 0 y 9:

import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Acertaste! El número era {numero_aleatorio}. Intentos: {intentos}")
        break
    else:
        print("Intenta de nuevo.")
#6) Imprimir números pares entre 0 y 100 en orden decreciente:

for i in range(100, -1, -2):
    print(i)
#7) Calcular la suma de todos los números comprendidos entre 0 y un número entero positivo ingresado por el usuario:

n = int(input("Ingresa un número entero positivo: "))
suma = sum(range(n + 1))
print(f"La suma de los números entre 0 y {n} es: {suma}")
#8) Ingresar 100 números enteros y contar pares, impares, negativos y positivos:

pares = impares = negativos = positivos = 0

for _ in range(100):
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")
#9) Calcular la media de 100 números enteros ingresados por el usuario:

suma = 0

for _ in range(100):
    numero = int(input("Ingresa un número entero: "))
    suma += numero

media = suma / 100
print(f"La media de los números ingresados es: {media}")
#10) Invertir el orden de los dígitos de un número ingresado por el usuario:

numero = input("Ingresa un número: ")
numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")