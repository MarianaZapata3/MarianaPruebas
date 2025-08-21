# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0

    def agregar_al_inicio(self, item):
        nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nodo
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            return

        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            self.agregar_al_inicio(item)
            return
        if posicion == self.tamanio:
            self.agregar_al_final(item)
            return

        nodo = Nodo(item)
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        nodo.anterior = actual.anterior
        nodo.siguiente = actual
        actual.anterior.siguiente = nodo
        actual.anterior = nodo
        self.tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("Lista vacía")

        if posicion is None:
            posicion = self.tamanio - 1

        if posicion < 0:
            posicion = self.tamanio + posicion

        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            nodo = self.cabeza
            self.cabeza = nodo.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
            return nodo.dato

        if posicion == self.tamanio - 1:
            nodo = self.cola
            self.cola = nodo.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamanio -= 1
            return nodo.dato

        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return actual.dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior  # porque intercambiamos los punteros
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra_lista):
        if otra_lista.esta_vacia():
            return
        otra_copia = otra_lista.copiar()   # copiar para no modificar original
        if self.esta_vacia():
            self.cabeza = otra_copia.cabeza
            self.cola = otra_copia.cola
        else:
            self.cola.siguiente = otra_copia.cabeza
            otra_copia.cabeza.anterior = self.cola
            self.cola = otra_copia.cola
        self.tamanio += len(otra_copia)


    def __len__(self):
        return self.tamanio

    def __add__(self, otra_lista):
        nueva = self.copiar()
        nueva.concatenar(otra_lista)
        return nueva

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente