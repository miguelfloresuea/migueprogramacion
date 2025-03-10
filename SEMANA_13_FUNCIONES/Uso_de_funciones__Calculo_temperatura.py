# Definimos la función
def calcular_temperatura_promedio(temperaturas, ciudades):
    # Calcula la temperatura promedio de cada ciudad.
    # Parámetros:
    #     temperaturas (list): Lista de temperaturas organizadas por ciudad y semanas.
    #     ciudades (list): Lista con los nombres de las ciudades.
    # Retorna:
    #     dict: Diccionario con el nombre de cada ciudad y su temperatura promedio.

    promedios_por_ciudad = {}

    for ciudad_index, ciudad in enumerate(temperaturas):
        suma_total = 0
        total_dias = 0

        # Iteramos sobre cada semana de la ciudad
        for semana in ciudad:
            for dia in semana:
                suma_total += dia['temp']  # Sumamos las temperaturas de cada día
                total_dias += 1  # Contamos los días totales

        # Calculamos el promedio dividiendo la suma total entre el número de días
        promedio_ciudad = suma_total / total_dias
        # Guardamos el resultado en el diccionario con el nombre de la ciudad
        promedios_por_ciudad[ciudades[ciudad_index]] = round(promedio_ciudad, 2)  #round(valor, 2)  redondea a 2 decimales el promedio

    return promedios_por_ciudad


# Ejemplo de uso
temperaturas = [
    [  # Quito
        [  # Semana 1
            {"dia": "Lunes", "temp": 12},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 13},
            {"dia": "Jueves", "temp": 11},
            {"dia": "Viernes", "temp": 13},
            {"dia": "Sábado", "temp": 12},
            {"dia": "Domingo", "temp": 15}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 14},
            {"dia": "Martes", "temp": 12},
            {"dia": "Miércoles", "temp": 13},
            {"dia": "Jueves", "temp": 15},
            {"dia": "Viernes", "temp": 14},
            {"dia": "Sábado", "temp": 13},
            {"dia": "Domingo", "temp": 12}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 11},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 12},
            {"dia": "Jueves", "temp": 13},
            {"dia": "Viernes", "temp": 14},
            {"dia": "Sábado", "temp": 13},
            {"dia": "Domingo", "temp": 15}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 12},
            {"dia": "Jueves", "temp": 11},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 14},
            {"dia": "Domingo", "temp": 13}
        ]
    ],
    [  # Ibarra
        [  # Semana 1
            {"dia": "Lunes", "temp": 16},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 16},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 17}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 17},
            {"dia": "Martes", "temp": 19},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 19},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 17}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 18},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 16},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 17}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 18},
            {"dia": "Miércoles", "temp": 19},
            {"dia": "Jueves", "temp": 16},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 19}
        ]
    ],
    [  # Tena
        [  # Semana 1
            {"dia": "Lunes", "temp": 22},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 22},
            {"dia": "Viernes", "temp": 21},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 24}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 24},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 22}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 23},
            {"dia": "Martes", "temp": 22},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 23},
            {"dia": "Viernes", "temp": 21},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 24}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 22},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 20},
            {"dia": "Jueves", "temp": 23},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 22}
        ]
    ]
]

ciudades = ["Quito", "Ibarra", "Tena"]
# Llamamos a la función y mostramos el resultado
resultado = calcular_temperatura_promedio(temperaturas, ciudades)
print(resultado)
