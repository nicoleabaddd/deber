class Nodo:
    def __init__(self, valor=None):
        self.valor = valor  # Valor almacenado en el nodo
        self.nodo_siguiente = None  # Puntero al siguiente nodo
        self.nodo_anterior = None  # Puntero al nodo anterior

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primer_nodo = None  # Primer nodo de la lista
        self.ultimo_nodo = None  # Último nodo de la lista
        self.puntero_cursor = None  # Cursor para el editor de texto

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.primer_nodo:  # Si la lista está vacía
            self.primer_nodo = self.ultimo_nodo = nuevo_nodo
        else:
            self.ultimo_nodo.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_anterior = self.ultimo_nodo
            self.ultimo_nodo = nuevo_nodo
        if not self.puntero_cursor:  # Inicializar el cursor si no está ya inicializado
            self.puntero_cursor = self.primer_nodo

    def eliminar(self):
        if not self.puntero_cursor:  # Si el cursor no está en ningún nodo
            return
        if self.puntero_cursor == self.primer_nodo:  # Si el cursor está en la cabeza
            self.primer_nodo = self.primer_nodo.nodo_siguiente
            if self.primer_nodo:
                self.primer_nodo.nodo_anterior = None
        elif self.puntero_cursor == self.ultimo_nodo:  # Si el cursor está en la cola
            self.ultimo_nodo = self.ultimo_nodo.nodo_anterior
            if self.ultimo_nodo:
                self.ultimo_nodo.nodo_siguiente = None
        else:  # Si el cursor está en el medio
            self.puntero_cursor.nodo_anterior.nodo_siguiente = self.puntero_cursor.nodo_siguiente
            self.puntero_cursor.nodo_siguiente.nodo_anterior = self.puntero_cursor.nodo_anterior
        self.puntero_cursor = self.puntero_cursor.nodo_siguiente if self.puntero_cursor.nodo_siguiente else self.ultimo_nodo

    def mover_cursor_adelante(self):
        if self.puntero_cursor and self.puntero_cursor.nodo_siguiente:
            self.puntero_cursor = self.puntero_cursor.nodo_siguiente

    def mover_cursor_atras(self):
        if self.puntero_cursor and self.puntero_cursor.nodo_anterior:
            self.puntero_cursor = self.puntero_cursor.nodo_anterior

    def mostrar_lista(self):
        nodo_actual = self.primer_nodo
        elementos = []
        while nodo_actual:
            elementos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente
        return elementos

    def obtener_texto(self):
        nodo_actual = self.primer_nodo
        texto = ""
        while nodo_actual:
            texto += nodo_actual.valor
            nodo_actual = nodo_actual.nodo_siguiente
        return texto

class EditorTexto:
    def __init__(self):
        self.lista = ListaDoblementeEnlazada()

    def insertar_texto(self, texto):
        for char in texto:
            self.lista.insertar(char)

    def eliminar_texto(self):
        self.lista.eliminar()

    def mover_cursor_derecha(self):
        self.lista.mover_cursor_adelante()

    def mover_cursor_izquierda(self):
        self.lista.mover_cursor_atras()

    def mostrar_texto(self):
        return self.lista.obtener_texto()

# Ejemplo de uso del editor de texto simple
editor = EditorTexto()
editor.insertar_texto("Buenas Tardes ")
print("Texto actual:", editor.mostrar_texto())

editor.mover_cursor_izquierda()
editor.eliminar_texto()
print("Texto después de eliminar:", editor.mostrar_texto())

editor.mover_cursor_izquierda()
editor.insertar_texto("s")
print("Texto después de insertar 's':", editor.mostrar_texto())
