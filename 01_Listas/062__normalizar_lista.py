def normalizar_lista(lista):
    """
    Recibe una lista de números positivos y devuelve una nueva lista
    donde cada número está dividido por el valor máximo de la lista.
    """
    if not lista:
        return []

    maximo = max(lista)
    nueva_lista = []

    for numero in lista:
        resultado = numero / maximo
        nueva_lista.append(resultado)

    return nueva_lista

# Ejemplo de uso:
numeros = [2, 4, 6, 8]
normalizados = normalizar_lista(numeros)
print(f"la anterior lista es de {numeros} y la nueva es {normalizados}")