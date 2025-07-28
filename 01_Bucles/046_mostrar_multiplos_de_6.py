# Definimos una función llamada multiplos_6 que no recibe parámetros y no retorna nada
def multiplos_6() -> int:
    # Recorremos los números del 1 al 100 (incluye el 100)
    for i in range(1, 101):
        # Si el número es divisible por 6
        if i % 6 == 0:
            print(i)  # Lo imprimimos

# Llamamos a la función para que se ejecute
multiplos_6()