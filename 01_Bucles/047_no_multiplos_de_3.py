# Definimos una función que imprime los números del 1 al 100 que NO son múltiplos de 3
def no_multiplos_3() -> int:
    for i in range(1, 101):  # Recorremos del 1 al 100 inclusive
        if i % 3 != 0:       # Verificamos que NO sea múltiplo de 3
            print(i)         # Si no lo es, lo imprimimos

# Llamamos a la función para ejecutar el código
no_multiplos_3()