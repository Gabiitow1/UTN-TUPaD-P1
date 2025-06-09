import time

# Búsqueda binaria recursiva
def busqueda_recursiva(lista, objetivo, inicio = 0, fin = None):
    if fin == None:
        return -1

    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_recursiva(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_recursiva(lista, objetivo, inicio, medio - 1)

# Algoritmo de búsqueda binaria iterativa
def busqueda_iterativa(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return "El objetivo no está en la lista"


tamanio_lista1 = 10000
tamanio_lista2 = 10000000

lista1 = [i for i in range(tamanio_lista1)]
lista2 = [i for i in range(tamanio_lista2)]

objetivo1 = 9999
objetivo2 = 9999999

# Tiempos de busqueda con algoritmo binaro recursivo
print("Tiempos de ejecucion búsqueda binaria iterativa")
inicio1 = time.perf_counter_ns()
resultado = busqueda_iterativa(lista1, objetivo1)
fin1 = time.perf_counter_ns()
tiempo_ejecucion1 = fin1 - inicio1
print(f"El objetivo1 está en la posición {resultado} y el tiempo de ejecicion es de {((tiempo_ejecucion1)* 10**-9):.8f} segundos.")

inicio2 = time.perf_counter_ns()
resultado = busqueda_iterativa(lista2, objetivo2)
fin2 = time.perf_counter_ns()
tiempo_ejecucion2 = fin2 - inicio2
print(f"El objetivo2 está en la posición {resultado} y el tiempo de ejecicion es de {((tiempo_ejecucion2)* 10**-9):.8f} segundos.")

print("")

# Tiempos de busqueda con algoritmo binaro recursivo
print("Tiempos de ejecucion búsqueda binaria recursiva")
inicio1 = time.perf_counter_ns()
resultado = busqueda_recursiva(lista1, objetivo1, 0, len(lista1)-1)
fin1 = time.perf_counter_ns()
tiempo_ejecucion1 = fin1 - inicio1
print(f"El objetivo1 está en la posición {resultado} y el tiempo de ejecicion es de {((tiempo_ejecucion1)*10**-9):.8f} segundos.")

inicio2 = time.perf_counter_ns()
resultado = busqueda_recursiva(lista2, objetivo2, 0, len(lista2)-1)
fin2 = time.perf_counter_ns()
tiempo_ejecucion2 = fin2 - inicio2
print(f"El objetivo2 está en la posición {resultado} y el tiempo de ejecicion es de {((tiempo_ejecucion2)*10**-9):.8f} segundos.")