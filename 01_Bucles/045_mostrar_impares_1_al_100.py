# Definimos la función que mostrará los números impares y contará cuántos hay
def mostrar_impares() -> int:
    suma = 0  # Esta variable será usada como contador

    # Recorremos del 1 al 100 inclusive
    for i in range(1, 101):
        if i % 2 != 0:  # Verificamos si el número es impar
            suma += 1   # Contamos uno más
            print(i)    # Mostramos el número impar

    return suma  # Retornamos la cantidad total de impares

# Guardamos el total de impares retornado por la función
total = mostrar_impares()

# Mostramos el total
print(f"Total de impares: {total}")