def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Encontrar el índice del elemento mínimo en el subarreglo no ordenado
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambiar el elemento mínimo con el primer elemento del subarreglo no ordenado
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    entrada = input("Ingresa una serie de números enteros separados por espacios: ")
    numeros = list(map(int, entrada.split()))  # Convertimos la entrada a una lista de enteros
    selection_sort(numeros)
    print("Arreglo ordenado:", numeros)

if __name__ == "__main__":
    main()
