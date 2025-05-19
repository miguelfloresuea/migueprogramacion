# Definimos la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Solicita que ingrese la fila y columna para buscar en la matriz
fila = int(input("Ingresa el número de fila (0-2): "))
columna = int(input("Ingresa el número de columna (0-2): "))

# Verificar si los índices están dentro del rango de la matriz
encontrado = False

# Usamos un bucle for para recorrer la matriz
for i in range(len(matriz)):  # Recorre las filas
    for j in range(len(matriz[i])):  # Recorre las columnas
        if i == fila and j == columna:  # Compara la posición actual con la solicitada
            valor = matriz[i][j]  # Si es la posición correcta, obtenemos el valor
            encontrado = True
            break
    if encontrado:
        break

# Mostrar el resultado
if encontrado:
    print(f"El valor en la posición ({fila}, {columna}) es: {valor}")
else:
    print(f"La posición ({fila}, {columna}) está fuera del rango de la matriz.")
