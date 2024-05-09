def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        intercambio = False  # Bandera para detectar si se realizó algún intercambio en esta pasada
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambio de elementos
                intercambio = True
        # Si no se ha realizado ningún intercambio en esta pasada, significa que el arreglo ya está ordenado
        if not intercambio:
            break

def main():
    entrada = input("Ingresa una serie de números enteros separados por espacios: ")
    numeros = list(map(int, entrada.split()))  # Convertimos la entrada a una lista de enteros
    bubble_sort(numeros)
    print("Arreglo ordenado:", numeros)

if __name__ == "__main__":
    main()
