#Definimos la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    #Calcula el descuento dado un monto total y un porcentaje de descuento
    #orcentaje_descuento=10: Si al llamar a la función no se proporciona un valor, se utilizará el valor 10 por defecto

    # Calcula el descuento multiplicando el monto total por el porcentaje de descuento y dividiendo para 100
    descuento = (monto_total * porcentaje_descuento) / 100
    # Retorna el monto del descuento calculado
    return descuento

def main():
    # Llamada a la función con el valor predeterminado de descuento (10%)
    monto_total_1 = 100.0
    descuento_1 = calcular_descuento(monto_total_1)
    # Calcula el monto final restando el descuento del monto total
    monto_final_1 = monto_total_1 - descuento_1
    # Imprime los detalles de la compra con el descuento predeterminado
    print(f"Monto total: ${monto_total_1}")
    print(f"Descuento aplicado: ${descuento_1}")
    print(f"Monto final a pagar: ${monto_final_1}\n")

    # Llamada a la función con un porcentaje de descuento específico (15%)
    monto_total_2 = 200.0
    porcentaje_descuento_2 = 15
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    # Calcula el monto final restando el descuento del monto total
    monto_final_2 = monto_total_2 - descuento_2
    # Imprime los detalles de la compra con el descuento específico
    print(f"Monto total: ${monto_total_2}")
    print(f"Descuento aplicado: ${descuento_2}")
    print(f"Monto final a pagar: ${monto_final_2}")

if __name__ == "__main__":
    # Llama a la función principal
    main()