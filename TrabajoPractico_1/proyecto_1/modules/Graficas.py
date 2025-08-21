import time
import matplotlib.pyplot as plt
from actividad1 import ListaDobleEnlazada
import random

# Tamaños de prueba
N_list = list(range(100, 10001, 500))
# Guardamos los tiempos
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for N in N_list:
    lde = ListaDobleEnlazada()
    for i in range(N):
        lde.agregar_al_final(random.randint(0, 1000))

    # medir len
    start = time.perf_counter()
    _ = len(lde)
    end = time.perf_counter()
    tiempos_len.append(end - start)

    # medir copiar
    start = time.perf_counter()
    _ = lde.copiar()
    end = time.perf_counter()
    tiempos_copiar.append(end - start)

    # medir invertir
    start = time.perf_counter()
    lde.invertir()
    end = time.perf_counter()
    tiempos_invertir.append(end - start)

# Graficar
plt.figure(figsize=(10,6))
plt.plot(N_list, tiempos_len, marker='o', label='len()')
plt.plot(N_list, tiempos_copiar, marker='s', label='copiar()')
plt.plot(N_list, tiempos_invertir, marker='^', label='invertir()')
plt.xlabel('Número de elementos N')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución vs tamaño de lista')
plt.legend()
plt.grid(True)
plt.show()
