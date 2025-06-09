#Búsqueda lineal
import time

tamanio_lista1 = 10000
tamanio_lista2 = 10000000

lista1 = [i for i in range(tamanio_lista1)]
lista2 = [i for i in range(tamanio_lista2)]


# Algoritmo de búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:    
            return i
    return "El objetivo no está en la lista"

objetivo1 = 9999
objetivo2 = 9999999

print("Tiempos de busqueda lineal")
inicio1 = time.perf_counter_ns()
resultado = busqueda_lineal(lista1, objetivo1)
fin1 = time.perf_counter_ns()
tiempo_ejecucion1 = fin1 - inicio1
print(f"El objetivo1 está en la posición {resultado} y el tiempo de ejecicion es de {((tiempo_ejecucion1)*10**-9):.8f} segundos.")

inicio2 = time.perf_counter_ns()
resultado = busqueda_lineal(lista2, objetivo2)
fin2 = time.perf_counter_ns()
tiempo_ejecucion2 = fin2 - inicio2
print(f"El objetivo2 está en la posición {resultado} y el tiempo de ejecicion es de {((tiempo_ejecucion2)*10**-9):.8f} segundos.")