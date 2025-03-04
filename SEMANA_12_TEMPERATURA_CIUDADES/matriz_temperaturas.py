# Matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (Quito, Ibarra, Tena)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"dia": "Lunes", "temp": 12},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 13},
            {"dia": "Jueves", "temp": 11},
            {"dia": "Viernes", "temp": 13},
            {"dia": "Sábado", "temp": 12},
            {"dia": "Domingo", "temp": 15}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 14},
            {"dia": "Martes", "temp": 12},
            {"dia": "Miércoles", "temp": 13},
            {"dia": "Jueves", "temp": 15},
            {"dia": "Viernes", "temp": 14},
            {"dia": "Sábado", "temp": 13},
            {"dia": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 11},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 12},
            {"dia": "Jueves", "temp": 13},
            {"dia": "Viernes", "temp": 14},
            {"dia": "Sábado", "temp": 13},
            {"dia": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 12},
            {"dia": "Jueves", "temp": 11},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 14},
            {"dia": "Domingo", "temp": 13}
        ]
    ],
    [   # Ibarra
        [   # Semana 1
            {"dia": "Lunes", "temp": 16},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 16},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 17},
            {"dia": "Martes", "temp": 19},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 19},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 17}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 18},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 16},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 17}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 18},
            {"dia": "Miércoles", "temp": 19},
            {"dia": "Jueves", "temp": 16},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 19}
        ]
    ],
    [   # Tena
        [   # Semana 1
            {"dia": "Lunes", "temp": 22},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 22},
            {"dia": "Viernes", "temp": 21},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 24},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 22}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 23},
            {"dia": "Martes", "temp": 22},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 22},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 24}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 22},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 23},
            {"dia": "Viernes", "temp": 21},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 24}
        ]
    ]
]

# Definimos el nombre de las 3 ciudades
ciudades = ["Quito", "Ibarra", "Tena"]
# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_index, ciudad in enumerate(temperaturas):
    print(f"Ciudad: {ciudades[ciudad_index]}")
    # Recorremos las semanas de la ciudad actual
    # Enumerate nos da el índice de la semana (semana_index) y los días de la semana (semana)
    for semana_index, semana in enumerate(ciudad):
        # Inicializamos una variable para almacenar la suma de las temperaturas de los días
        suma = 0
        # Recorremos los días de la semana
        # Cada "dia" es un diccionario que contiene el nombre del día y la temperatura
        for dia in semana:
            # Sumamos la temperatura de ese día al total (suma)
            suma += dia['temp']
        # Calculamos el promedio de temperaturas de la semana
        # dividimos la suma de las temperaturas entre el número de días en la semana
        promedio = suma / len(semana)
        # Imprimir el promedio de temperaturas de la semana
        print(f"  Semana {semana_index + 1}: Promedio de temperatura: {promedio:.2f}°C")

