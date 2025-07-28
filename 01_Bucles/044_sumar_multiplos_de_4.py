# Definimos una función llamada multiplo_4 que no recibe parámetros y retorna un entero
def multiplo_4() -> int:
    suma = 0  # Inicializamos la variable para acumular los múltiplos de 4

    # Recorremos los números del 1 al 99 (el 100 no se incluye)
    for i in range(1, 100):
        # Verificamos si el número actual es múltiplo de 4
        if i % 4 == 0:
            suma += i  # Si lo es, lo sumamos a 'suma'

    return suma  # Retornamos la suma total al final

# Llamamos la función y guardamos su resultado en la variable 'suma'
suma = multiplo_4()

# Imprimimos el resultado
print(f"La suma es {suma}")