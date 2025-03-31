# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado 'my_notes.txt' y escribir notas personales
with open('my_notes.txt', 'w') as file:
    # Escribir al menos tres líneas de notas personales
    file.write("1. Recordar comprar leche y pan mañana.\n")
    file.write("2. Revisar el correo electrónico antes del mediodía.\n")
    file.write("3. Preparar la presentación para el proyecto de programación.\n")
    # El uso de 'with' asegura que el archivo se cierre automáticamente

# Lectura de Archivo de Texto
# Abrir el archivo 'my_notes.txt' en modo lectura
print("\nLeyendo el archivo línea por línea:")
with open('my_notes.txt', 'r') as file:
    # Leer la primera línea
    line1 = file.readline()
    print(line1.strip())  # strip() elimina espacios y saltos de línea

    # Leer la segunda línea
    line2 = file.readline()
    print(line2.strip())

    # Leer la tercera línea
    line3 = file.readline()
    print(line3.strip())

# No es necesario cerrar explícitamente el archivo cuando se usa 'with'
# El archivo se cierra automáticamente al salir del bloque with