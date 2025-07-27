def calcular_total_y_porcentaje(propina: float, total_inicial: float) -> tuple:
    # Calcular el porcentaje de propina
    porcentaje_propina = (propina / total_inicial) * 100

    # Calcular el total final a pagar
    total_final = propina + total_inicial

    # Devolvemos ambos valores: el porcentaje y el total final
    return porcentaje_propina, total_final

# Pedimos los datos al usuario
total_inicial = float(input("¿Cuánto es su total?: "))
propina = float(input("¿Cuánta propina desea dejar?: "))

# Llamamos a la función y guardamos los dos resultados
porcentaje_calculado, total_a_pagar = calcular_total_y_porcentaje(propina, total_inicial)

# Mostramos los resultados
print(f"Su propina es del {porcentaje_calculado:.2f}% y su total final a pagar es de {total_a_pagar:.2f}")
