class Cola:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        """Añade un elemento al final de la cola"""
        self.elementos.insert(0, elemento)

    def quitar(self):
        """Remueve y retorna el elemento del frente de la cola"""
        if not self.esta_vacia():
            return self.elementos.pop()
        raise IndexError("quitar de una cola vacía")

    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        return len(self.elementos) == 0

    def tamano(self):
        """Devuelve el número de elementos en la cola"""
        return len(self.elementos)

    def ver_primero(self):
        """Obtiene el elemento del frente sin removerlo"""
        if not self.esta_vacia():
            return self.elementos[-1]
        raise IndexError("ver primero de una cola vacía")

class AdministradorTareas:
    def __init__(self):
        self.cola_tareas = Cola()

    def agregar_tarea(self, tarea):
        """Añade una tarea a la cola"""
        self.cola_tareas.agregar(tarea)
        print(f"Tarea '{tarea}' añadida.")

    def procesar_tarea(self):
        """Procesa la tarea del frente de la cola"""
        if not self.cola_tareas.esta_vacia():
            tarea = self.cola_tareas.quitar()
            print(f"Procesando tarea: {tarea}")
        else:
            print("No hay tareas para procesar.")

    def mostrar_proxima_tarea(self):
        """Muestra la próxima tarea a ser procesada"""
        if not self.cola_tareas.esta_vacia():
            tarea = self.cola_tareas.ver_primero()
            print(f"Próxima tarea: {tarea}")
        else:
            print("No hay tareas en la cola.")

    def mostrar_todas_tareas(self):
        """Muestra todas las tareas en la cola"""
        if not self.cola_tareas.esta_vacia():
            tareas = self.cola_tareas.elementos[::-1]
            print("Tareas en cola:")
            for tarea in tareas:
                print(f"- {tarea}")
        else:
            print("No hay tareas en la cola.")

if __name__ == "__main__":
    administrador = AdministradorTareas()

    while True:
        print("\nSistema de Gestión de Tareas")
        print("1. Añadir tarea")
        print("2. Procesar tarea")
        print("3. Mostrar próxima tarea")
        print("4. Mostrar todas las tareas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            tarea = input("Introduce la tarea: ")
            administrador.agregar_tarea(tarea)
        elif opcion == '2':
            administrador.procesar_tarea()
        elif opcion == '3':
            administrador.mostrar_proxima_tarea()
        elif opcion == '4':
            administrador.mostrar_todas_tareas()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
