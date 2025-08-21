import random
import time
import matplotlib.pyplot as plt
from actividad1 import ListaDobleEnlazada

# Funciones para acceder a la lista doblemente enlazada por índice
def obtener(lista, indice):
    """Devuelve el dato en la posición 'indice'"""
    if indice < 0 or indice >= len(lista):
        raise IndexError("Índice fuera de rango")
    actual = lista.cabeza
    for _ in range(indice):
        actual = actual.siguiente
    return actual.dato

def setear(lista, indice, valor):
    """Cambia el dato en la posición 'indice'"""
    if indice < 0 or indice >= len(lista):
        raise IndexError("Índice fuera de rango")
    actual = lista.cabeza
    for _ in range(indice):
        actual = actual.siguiente
    actual.dato = valor

#Algoritmos para ordenar
# BURBUJA
def burbuja_lde(ld):
    n = len(ld)
    for i in range(n-1):
        for j in range(n-1-i):
            if obtener(ld, j) > obtener(ld, j+1):
                temp = obtener(ld, j)
                setear(ld, j, obtener(ld, j+1))
                setear(ld, j+1, temp)
    return ld

# QUICKSORT
def quicksort_lde(ld):
    if len(ld) <= 1:
        return ld
    
    pivote = obtener(ld, 0)
    menores = ListaDobleEnlazada()
    mayores = ListaDobleEnlazada()
    
    for i in range(1, len(ld)):
        if obtener(ld, i) <= pivote:
            menores.agregar_al_final(obtener(ld, i))
        else:
            mayores.agregar_al_final(obtener(ld, i))
    
    menores = quicksort_lde(menores)
    mayores = quicksort_lde(mayores)
    
    resultado = ListaDobleEnlazada()
    for i in range(len(menores)):
        resultado.agregar_al_final(obtener(menores, i))
    resultado.agregar_al_final(pivote)
    for i in range(len(mayores)):
        resultado.agregar_al_final(obtener(mayores, i))
    
    return resultado

# RADIX
def radix_sort_lde(ld):
    lista = [obtener(ld, i) for i in range(len(ld))]
    if len(lista) == 0:
        return ld
    
    max_num = max(lista)
    exp = 1
    while max_num // exp > 0:
        contar = [0] * 10
        salida = [0] * len(lista)

        for num in lista:
            index = (num // exp) % 10
            contar[index] += 1

        for i in range(1, 10):
            contar[i] += contar[i-1]

        for num in reversed(lista):
            index = (num // exp) % 10
            salida[contar[index]-1] = num
            contar[index] -= 1

        lista = salida[:]
        exp *= 10

    resultado = ListaDobleEnlazada()
    for num in lista:
        resultado.agregar_al_final(num)
    return resultado

#Generar listas Aleatorias y medir tiempo
import random
import time
import matplotlib.pyplot as plt

def generar_lde(n):
    ld = ListaDobleEnlazada()
    for _ in range(n):
        ld.agregar_al_final(random.randint(10000, 99999))
    return ld

lista_sizes = list(range(50, 1001, 50))
tiempos_burbuja = []
tiempos_quick = []
tiempos_radix = []
tiempos_sorted = []

for n in lista_sizes:
    ld = generar_lde(n)

    # BURBUJA
    l = ListaDobleEnlazada()
    for i in range(len(ld)):
        l.agregar_al_final(obtener(ld, i))
    inicio = time.time()
    burbuja_lde(l)
    tiempos_burbuja.append(time.time() - inicio)

    # QUICKSORT
    l = ListaDobleEnlazada()
    for i in range(len(ld)):
        l.agregar_al_final(obtener(ld, i))
    inicio = time.time()
    quicksort_lde(l)
    tiempos_quick.append(time.time() - inicio)

    # RADIX
    l = ListaDobleEnlazada()
    for i in range(len(ld)):
        l.agregar_al_final(obtener(ld, i))
    inicio = time.time()
    radix_sort_lde(l)
    tiempos_radix.append(time.time() - inicio)

    # SORT DE PYTHON
    lista_normal = [obtener(ld, i) for i in range(len(ld))]
    inicio = time.time()
    sorted(lista_normal)
    tiempos_sorted.append(time.time() - inicio)

#Graficar
plt.figure(figsize=(10,6))
plt.plot(lista_sizes, tiempos_burbuja, label="Burbuja")
plt.plot(lista_sizes, tiempos_quick, label="Quicksort")
plt.plot(lista_sizes, tiempos_radix, label="Radix")
plt.plot(lista_sizes, tiempos_sorted, label="Python sorted")
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de algoritmos usando ListaDobleEnlazada")
plt.legend()
plt.grid(True)
plt.show()
