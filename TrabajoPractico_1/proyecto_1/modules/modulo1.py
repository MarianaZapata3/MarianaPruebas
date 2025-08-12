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

#Prueba TP1 ACT2
class Nodo:
    def __init__(self, dato, anterior=None, siguiente=None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente
class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._longitud = 0

    def esta_vacia(self):
        return self._longitud == 0

    def __len__(self):
        return self._longitud  # O(1)

    def agregar_al_inicio(self, item):
        nuevo = Nodo(item, None, self.primero)
        if self.esta_vacia():
            self.ultimo = nuevo
        else:
            self.primero.anterior = nuevo
        self.primero = nuevo
        self._longitud += 1

    def agregar_al_final(self, item):
        nuevo = Nodo(item, self.ultimo, None)
        if self.esta_vacia():
            self.primero = nuevo
        else:
            self.ultimo.siguiente = nuevo
        self.ultimo = nuevo
        self._longitud += 1

    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            return

        if posicion < 0 or posicion > self._longitud:
            raise IndexError("Posición fuera de rango.")

        if posicion == 0:
            self.agregar_al_inicio(item)
            return
        if posicion == self._longitud:
            self.agregar_al_final(item)
            return

        actual = self.primero
        for _ in range(posicion):
            actual = actual.siguiente
        nuevo = Nodo(item, actual.anterior, actual)
        actual.anterior.siguiente = nuevo
        actual.anterior = nuevo
        self._longitud += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Extraer de lista vacía.")

        if posicion is None:
            posicion = self._longitud - 1

        if posicion < 0 or posicion >= self._longitud:
            raise IndexError("Posición fuera de rango.")

        if posicion == 0:
            dato = self.primero.dato
            self.primero = self.primero.siguiente
            if self.primero:
                self.primero.anterior = None
            else:
                self.ultimo = None
            self._longitud -= 1
            return dato

        if posicion == self._longitud - 1:
            dato = self.ultimo.dato
            self.ultimo = self.ultimo.anterior
            if self.ultimo:
                self.ultimo.siguiente = None
            else:
                self.primero = None
            self._longitud -= 1
            return dato

        actual = self.primero
        for _ in range(posicion):
            actual = actual.siguiente
        dato = actual.dato
        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior
        self._longitud -= 1
        return dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.primero
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia  # O(n)

    def invertir(self):
        actual = self.primero
        self.primero, self.ultimo = self.ultimo, self.primero
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior  # porque ya lo invertimos
        # O(n)

    def concatenar(self, otra_lista):
        if otra_lista.esta_vacia():
            return self
        if self.esta_vacia():
            self.primero = otra_lista.primero
            self.ultimo = otra_lista.ultimo
        else:
            self.ultimo.siguiente = otra_lista.primero
            otra_lista.primero.anterior = self.ultimo
            self.ultimo = otra_lista.ultimo
        self._longitud += len(otra_lista)
        return self

    def __add__(self, otra_lista):
        nueva = self.copiar()
        return nueva.concatenar(otra_lista.copiar())

    def __iter__(self):
        actual = self.primero
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def __repr__(self):
        return "[" + " <-> ".join(str(x) for x in self) + "]"
import time
import matplotlib.pyplot as plt

def medir_tiempo(func, *args):
    inicio = time.perf_counter()
    func(*args)
    return time.perf_counter() - inicio

N_values = [1000, 2000, 5000, 10000, 20000]
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for N in N_values:
    lista = ListaDobleEnlazada()
    for i in range(N):
        lista.agregar_al_final(i)

    tiempos_len.append(medir_tiempo(len, lista))
    tiempos_copiar.append(medir_tiempo(lista.copiar))
    tiempos_invertir.append(medir_tiempo(lista.invertir))

plt.figure(figsize=(8, 5))
plt.plot(N_values, tiempos_len, label="len()")
plt.plot(N_values, tiempos_copiar, label="copiar()")
plt.plot(N_values, tiempos_invertir, label="invertir()")
plt.xlabel("N (número de elementos)")
plt.ylabel("Tiempo (segundos)")
plt.title("N vs Tiempo de ejecución")
plt.legend()
plt.grid(True)
plt.show()
