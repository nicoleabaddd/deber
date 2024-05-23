# Sistema de Gestión de Tareas

Este proyecto implementa una clase Cola y un sistema de gestión de tareas que utiliza esta clase para manejar las tareas en una cola. La cola se implementa utilizando una lista en Python.

## Clase Cola

La clase Cola proporciona métodos para manejar una cola de elementos. Estos métodos incluyen:

- `agregar(elemento)`: Añade un elemento al final de la cola.
- `quitar()`: Remueve y retorna el elemento del frente de la cola.
- `esta_vacia()`: Verifica si la cola está vacía.
- `tamano()`: Devuelve el número de elementos en la cola.
- `ver_primero()`: Obtiene el elemento del frente de la cola sin removerlo.

## Sistema de Gestión de Tareas

El sistema de gestión de tareas utiliza la clase Cola para manejar las tareas en una cola. Las tareas se pueden añadir a la cola, procesar, y se pueden mostrar la próxima tarea o todas las tareas en la cola.

### Interfaz de Usuario

El sistema proporciona una interfaz de usuario simple en la línea de comandos. Las opciones disponibles son:

1. Añadir tarea
2. Procesar tarea
3. Mostrar próxima tarea
4. Mostrar todas las tareas
5. Salir

## Ejecución

Para ejecutar el sistema de gestión de tareas:

1. Abre una terminal o línea de comandos.
2. Navega hasta el directorio donde se encuentra el archivo.
3. Ejecuta el archivo Python con el siguiente comando:

   ```bash
   python task_manager.py
