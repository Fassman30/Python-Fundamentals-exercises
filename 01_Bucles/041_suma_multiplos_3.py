# Definimos una función llamada multiplo_3 que no recibe parámetros y retorna un entero
def multiplo_3() -> int:
    suma = 0  # Inicializamos una variable para acumular la suma de los múltiplos de 3

    # Recorremos los números del 1 al 100 (inclusive el 100)
    for i in range(1, 101):
        # Verificamos si el número actual es múltiplo de 3
        if i % 3 == 0:
            suma += i  # Si lo es, lo sumamos a la variable 'suma'

    return suma  # Al terminar el bucle, devolvemos el total de la suma

# Llamamos a la función y guardamos el resultado en la variable 'total'
total = multiplo_3()

# Imprimimos el resultado final
print(f"La suma es de {total}")