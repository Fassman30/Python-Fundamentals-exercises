# Definimos una función llamada numeros_pares que no recibe parámetros y retorna un entero
def numeros_pares() -> int:
    suma = 0  # Inicializamos la variable suma para acumular los números pares

    # Recorremos los números del 1 al 50 (incluye el 50)
    for i in range(1, 51):
        # Verificamos si el número actual es par
        if i % 2 == 0:
            suma += i  # Si es par, lo sumamos a 'suma'

    return suma  # Al finalizar el bucle, devolvemos la suma total

# Llamamos la función y guardamos el resultado en 'total'
total = numeros_pares()

# Imprimimos el resultado
print(f"Los números pares son: {total}")
    