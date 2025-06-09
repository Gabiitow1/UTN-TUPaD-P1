#BUBBLE SORT
#Compara elementos de a pares y los intercambia si están en el orden incorrecto.
#Los números grandes van “flotando” al final, por eso el nombre "burbujas"

def bubble_sort(arr):
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

#INSERTION SORT
#Se asemeja a un mazo de cartas
#Va insertando los numeros en la posición correcta de los anteriores ya ordenados.

def insertion_sort(arr): 
    for i in range(1, len(arr)):     
        key = arr[i]  
        j = i - 1 
        while j >=0 and arr[j] > key: 
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = key 

#SELECTION SORT
#Busca el número más chico y lo pone al principio, luego repite lo mismo con el resto

def selection_sort(arr):
    n = len(arr) 
    for i in range(n): # Recorremos toda la lista desde el primer hasta el último elemento
        min_idx = i #min_idx es la posicion donde está el valor minimo
        for j in range(i+1, n): 
            if arr[j] < arr[min_idx]: 
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 

# Hacemos una lista random para probar el ordenamiento
datos = [64, 25, 12, 22, 11]

# Copiamos las listas para cada prueba
lista_bubble = datos[:]
lista_insertion = datos[:]
lista_selection = datos[:]

#Ordenamos la lista con el algoritmo correspondiente
bubble_sort(lista_bubble)
insertion_sort(lista_insertion)
selection_sort(lista_selection)

#Mostramos el resultado en pantalla
print("Bubble Sort:", lista_bubble)
print("Insertion Sort:", lista_insertion)
print("Selection Sort:", lista_selection)
