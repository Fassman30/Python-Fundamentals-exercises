def sumar_positivos() -> int:
    suma = 0
    while True:
        try:
            numero = int(input("Ingresa un número positivo (negativo o 0 para salir): "))
            if numero <= 0:
                break
            suma += numero
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return suma

total = sumar_positivos()
print(f"La suma de los números positivos es: {total}")