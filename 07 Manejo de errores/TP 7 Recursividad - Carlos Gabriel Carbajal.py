
# 1) Factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

limite = int(input("Ingrese un número para calcular los factoriales desde 1 hasta ese número: "))
for i in range(1, limite + 1):
    print(f"Factorial de {i} es {factorial(i)}")

# 2) Serie de Fibonacci
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

posicion = int(input("Ingrese la cantidad de elementos de la serie de Fibonacci a mostrar: "))
print("Serie de Fibonacci:")
for i in range(posicion):
    print(fibonacci(i), end=" ")
print()

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# 4) Decimal a binario (como cadena de texto)
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(numero)
print("Binario:", binario if binario else "0")

# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra para verificar si es un palíndromo: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))

# 6) Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingrese un número para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(numero))

# 7) Pirámide de bloques
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel_base = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
print("Total de bloques necesarios:", contar_bloques(nivel_base))

# 8) Contar dígito específico
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        coincidencia = 1 if numero % 10 == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese el dígito a contar (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
