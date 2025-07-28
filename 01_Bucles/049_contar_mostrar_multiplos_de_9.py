# Esta función imprime e identifica cuántos múltiplos de 5 hay del 1 al 50
def multiplos() -> int:
    sum = 0  # Inicializamos contador

    for i in range(1, 51):  # Recorremos del 1 al 50
        if i % 5 == 0:      # Si el número es múltiplo de 5
            sum += 1        # Aumentamos el contador
            print(i)        # Imprimimos el número múltiplo

    return sum  # Retornamos el total de múltiplos encontrados

# Llamamos la función y guardamos el total
total = multiplos()

# Mostramos el total de múltiplos
print(f"Los números múltiplos de 5 son: {total}")