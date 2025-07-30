Lista_inicial = [5, 2, None, 8, 2, 10, None, 5, 1]
def limpieza_y_ordenamiento_final(lista_original):
    # Paso 1: Eliminar duplicados (convirtiendo a set y luego a lista)
    # El set quita duplicados, pero pierde el orden. Volvemos a lista.
    sin_duplicados = list(set(lista_original))
    print(f"1. Después de quitar duplicados: {sin_duplicados}")

    # Paso 2: Eliminar valores None usando una comprensión de lista
    sin_none = [elemento for elemento in sin_duplicados if elemento is not None]
    print(f"2. Después de quitar los None: {sin_none}")

    # Paso 3: Ordenar la lista (¡aquí está la clave!)
    # sorted() devuelve una NUEVA lista ordenada.
    lista_ordenada = sorted(sin_none)
    print(f"3. Lista Final y Ordenada: {lista_ordenada}")

    return lista_ordenada

# Probamos la función completa
resultado_final = limpieza_y_ordenamiento_final(Lista_inicial)
print(f"\nEl resultado final esperado del ejercicio 9 es: {resultado_final}")