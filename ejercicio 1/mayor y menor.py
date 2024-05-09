def encontrar_max_menor(arreglo):
    if not arreglo:
        return None, None  # Si el arreglo está vacío, devolvemos None para ambos
    else:
        max = min = arreglo[0]  # Inicializamos el número mayor y el número mínimo con el primer elemento del arreglo
        for num in arreglo:
            if num > max:
                max = num
            elif num < min:
                min = num
        return max, min

def main():
    entrada = input("Por favor ingrese una serie de números enteros separados por espacios: ")
    numeros = list(map(int, entrada.split()))  # Convertimos la entrada a una lista de enteros
    max, min = encontrar_max_menor(numeros)
    if max is None or min is None:
        print("No has ingresado ningún número.")
    else:
        print("El número máximo de su arreglo es:", max)
        print("El número mínimo de su arreglo es:", min)

if __name__ == "__main__":
    main()

