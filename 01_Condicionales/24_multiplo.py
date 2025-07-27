def es_multiplo(dividendo: int, divisor: int) -> bool:
    """
    Verifica si el primer número es múltiplo del segundo.

    Parámetros:
    - dividendo (int): Número que se desea verificar.
    - divisor (int): Número con el cual se verifica si es múltiplo.

    Retorna:
    - bool: True si es múltiplo, False en caso contrario.
    """
    return divisor != 0 and dividendo % divisor == 0


def iniciar_programa():
    """
    Ejecuta un ciclo para que el usuario verifique múltiples veces
    si un número es múltiplo de otro.
    """
    print(" Verificador de múltiplos ")
    while True:
        try:
            num1 = int(input(" Ingrese el primer número (dividendo): "))
            num2 = int(input(" Ingrese el segundo número (divisor): "))

            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            elif es_multiplo(num1, num2):
                print(f" {num1} es múltiplo de {num2}.")
            else:
                print(f" {num1} NO es múltiplo de {num2}.")
        except ValueError:
            print(" Por favor, ingrese solo números válidos.")

        continuar = input("¿Desea verificar otros números? (s/n): ").strip().lower()
        if continuar != 's':
            print(" Gracias por usar el verificador de múltiplos.")
            break


# Ejecutar programa
if __name__ == "__main__":
    iniciar_programa()
