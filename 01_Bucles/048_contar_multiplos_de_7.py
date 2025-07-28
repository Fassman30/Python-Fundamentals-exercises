# Esta función imprime todos los múltiplos de 7 del 1 al 200 y cuenta cuántos hay
def multiplo_7() -> int:
    sumar = 0  # Inicializamos un contador

    for i in range(1, 201):  # Recorremos del 1 al 200 inclusive
        if i % 7 == 0:       # Si el número es múltiplo de 7
            sumar += 1       # Aumentamos el contador
            print(i)         # Imprimimos el número

    return sumar  # Retornamos la cantidad de múltiplos encontrados

# Guardamos el total retornado
total = multiplo_7()

# Mostramos el resultado
print(f"Su total de números múltiplos de 7 es de {total}")