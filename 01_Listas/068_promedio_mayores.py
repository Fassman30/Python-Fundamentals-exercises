def promedio_mayores(lista, umbral):
    nueva_lista = []
    for numero in lista:
        if numero > umbral:
            nueva_lista.append(numero)

    if nueva_lista:  # si no está vacía
        suma_total = sum(nueva_lista)
        cantidad_elementos = len(nueva_lista)
        promedio = suma_total / cantidad_elementos

        print(f"Los números mayores a {umbral} son: {nueva_lista}")
        print(f"Cantidad: {cantidad_elementos}")
        print(f"Promedio: {promedio}")
        return promedio
    else:
        print("No hay elementos mayores al umbral.")
        return None

# Llamada:
promedio_mayores([4, 8, 15, 16, 23, 42], 10)
