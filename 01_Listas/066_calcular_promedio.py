def calcular_promedio(lista):
    """
    Calcula el promedio de los elementos en una lista numérica.

    Parámetros:
    lista (list): Lista de números (int o float)

    Retorna:
    float: Promedio de los elementos de la lista.
    """
    if not lista:
        return 0  # Evita división por cero si la lista está vacía

    suma_total = sum(lista)         # Suma todos los elementos de la lista
    cantidad_elementos = len(lista) # Cuenta cuántos elementos hay
    promedio = suma_total / cantidad_elementos  # Calcula el promedio

    return promedio

# Lista de números a evaluar
numeros = [4, 8, 15, 16, 23, 42]

# Llamada a la función
resultado = calcular_promedio(numeros)

# Imprime el resultado
print(f"El promedio de la lista es: {resultado}")
    
    
    
    
    
    
    
    
    
    
    