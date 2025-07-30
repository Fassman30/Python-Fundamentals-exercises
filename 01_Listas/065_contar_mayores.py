def contar_mayores(lista, umbral):
    """
    Cuenta cuántos elementos en una lista son mayores que un valor umbral.

    Parámetros:
    lista (list): Lista de números a evaluar.
    umbral (int o float): Valor de referencia para comparar los elementos.

    Retorna:
    int: Cantidad de elementos que son mayores que el umbral.
    """
    contador = 0
    for numero in lista:
        if numero > umbral:
            contador += 1
    return contador

# Lista de datos a evaluar
datos = [3, 10, 15, 2, 8]

# Llamada a la función con un umbral de 7
resultado = contar_mayores(datos, 7)

# Imprime el resultado
print(f"Cantidad de números mayores que 7: {resultado}")