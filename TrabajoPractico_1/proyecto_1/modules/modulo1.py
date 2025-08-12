# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
print("Mariana")
print(not((5==4) and (4==3)))
lasuma = 1
print(not(lasuma == 2))
print(lasuma + 5)
lista = [5,"nani","sustituto",10]
print(lista)
lista.append(4)



#Prueba TP1 ACT1
import random
import time
import matplotlib.pyplot as plt

# ------------------------------
# Algoritmo 1: Burbuja
# ------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ------------------------------
# Algoritmo 2: Quicksort
# ------------------------------
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivot]
    medio = [x for x in arr if x == pivot]
    derecha = [x for x in arr if x > pivot]
    return quicksort(izquierda) + medio + quicksort(derecha)

# ------------------------------
# Algoritmo 3: Radix Sort
# ------------------------------
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# ------------------------------
# Generación de datos y medición de tiempos
# ------------------------------
sizes = list(range(1, 1001))
tiempos_burbuja = []
tiempos_quick = []
tiempos_radix = []
tiempos_sorted = []

for n in sizes:
    lista_base = [random.randint(10000, 99999) for _ in range(n)]
    
    # Burbuja
    copia = lista_base.copy()
    inicio = time.time()
    bubble_sort(copia)
    tiempos_burbuja.append(time.time() - inicio)

    # Quicksort
    copia = lista_base.copy()
    inicio = time.time()
    quicksort(copia)
    tiempos_quick.append(time.time() - inicio)

    # Radix
    copia = lista_base.copy()
    inicio = time.time()
    radix_sort(copia)
    tiempos_radix.append(time.time() - inicio)

    # sorted()
    copia = lista_base.copy()
    inicio = time.time()
    sorted(copia)
    tiempos_sorted.append(time.time() - inicio)

# ------------------------------
# Gráfico
# ------------------------------
plt.figure(figsize=(10, 6))
plt.plot(sizes, tiempos_burbuja, label="Burbuja (O(n²))")
plt.plot(sizes, tiempos_quick, label="Quicksort (O(n log n))")
plt.plot(sizes, tiempos_radix, label="Radix Sort (O(n·k))")
plt.plot(sizes, tiempos_sorted, label="sorted()")
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (s)")
plt.title("Comparación de algoritmos de ordenamiento")
plt.legend()
plt.grid(True)
plt.show()
