# Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actividad 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Actividad 3
frutas = list(precios_frutas.keys())

# Actividad 4
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# Actividad 5
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Actividad 6
def esta_balanceado(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    for char in cadena:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila or pila.pop() != pares[char]:
                return False
    return not pila

# Actividad 7
from collections import deque

cola_banco = deque()

def agregar_cliente(nombre):
    cola_banco.append(nombre)

def atender_cliente():
    if cola_banco:
        return cola_banco.popleft()
    return "No hay clientes."

def siguiente_cliente():
    if cola_banco:
        return cola_banco[0]
    return "No hay clientes."

# Actividad 8
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Actividad 9
def invertir_lista(lista):
    anterior = None
    actual = lista.cabeza
    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente
    lista.cabeza = anterior