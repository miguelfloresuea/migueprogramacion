# Creación del diccionario inicial con información personal
# Se incluyen las claves: nombre, edad, ciudad y profesion
informacion_personal = {
    "nombre": "Miguel Flores",
    "edad": 35,
    "ciudad": "Tena",
    "profesion": "Docente"
}

# 1. Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Tena"  # Cambiamos la ciudad de residencia

# 2. Acceder y modificar valores
informacion_personal["profesion"] = "Ingeniero en TIC"

# 3. Verificar si existe la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"

# 4. Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# 5. Imprimir el diccionario final
print("Diccionario final de: información personal:")
print(informacion_personal)