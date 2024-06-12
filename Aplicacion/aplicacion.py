class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def agregar(self, valor_cancion):
        nuevo_nodo = Nodo(valor_cancion)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            nodo_actual = self.primero
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar(self, valor_cancion):
        if self.primero is None:
            print("La lista está vacía.")
            return
        
        if self.primero.valor == valor_cancion:
            self.primero = self.primero.siguiente
            return
        
        nodo_actual = self.primero
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.valor == valor_cancion:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            nodo_actual = nodo_actual.siguiente
        print("El valor no se encuentra en la lista.")

    def mostrar(self):
        nodo_actual = self.primero
        while nodo_actual is not None:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

class Playlist:
    def __init__(self):
        self.lista_canciones = ListaEnlazada()

    def agregar_cancion(self, cancion):
        self.lista_canciones.agregar(cancion)
        print(f"Canción '{cancion}' agregada a la playlist.")

    def eliminar_cancion(self, cancion):
        self.lista_canciones.eliminar(cancion)
        print(f"Canción '{cancion}' eliminada de la playlist.")

    def mostrar_playlist(self):
        print("Playlist actual:")
        self.lista_canciones.mostrar()

# Ejemplo de uso:
playlist_musical = Playlist()
playlist_musical.agregar_cancion("Canción 1")
playlist_musical.agregar_cancion("Canción 2")
playlist_musical.mostrar_playlist()
playlist_musical.eliminar_cancion("Canción 1")
playlist_musical.mostrar_playlist()