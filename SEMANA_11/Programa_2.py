# Definimos la matriz 3x3
matriz = [
    [9, 2, 7],
    [4, 5, 3],
    [8, 1, 6]
]


# Función para ordenar una fila específica usando el algoritmo Bubble Sort
def ordenar_fila_bubble_sort(matriz, fila):
    # Obtener la fila que se va a ordenar
    fila_a_ordenar = matriz[fila]

    # Implementación del algoritmo Bubble Sort para ordenar la fila
    for i in range(len(fila_a_ordenar)):
        for j in range(0, len(fila_a_ordenar) - i - 1):
            if fila_a_ordenar[j] > fila_a_ordenar[j + 1]:
                # Intercambiar los elementos si están en el orden incorrecto
                fila_a_ordenar[j], fila_a_ordenar[j + 1] = fila_a_ordenar[j + 1], fila_a_ordenar[j]


# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Solicitar  que ingrese el número de fila que desea ordenar
fila_a_ordenar = int(input("\nIngresa el número de fila a ordenar (0-2): "))

# Verificar que el número de fila esté dentro del rango
if fila_a_ordenar >= 0 and fila_a_ordenar < len(matriz):
    # Llamar a la función para ordenar la fila seleccionada
    ordenar_fila_bubble_sort(matriz, fila_a_ordenar)

    # Mostrar la matriz con la fila ordenada
    print("Matriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Número de fila fuera de rango. Debes ingresar un número entre 0 y 2.")
