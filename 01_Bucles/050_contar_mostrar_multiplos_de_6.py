# Esta función imprime y cuenta los múltiplos de 6 entre 1 y 99
def multiplo_6() -> int:
    sumar = 0  # Inicializamos el contador

    for i in range(1, 100):  # Recorremos del 1 al 99
        if i % 6 == 0:       # Si el número es múltiplo de 6
            sumar += 1       # Aumentamos el contador
            print(i)         # Imprimimos el número

    return sumar  # Retornamos el total de múltiplos encontrados

# Llamamos la función y guardamos el total
total = multiplo_6()

# Mostramos el total al final
print(f"Total de múltiplos de 6 es: {total}")
