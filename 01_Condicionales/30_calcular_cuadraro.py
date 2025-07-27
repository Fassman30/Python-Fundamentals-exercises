def cuadrado(numero: float) -> float:
    """
    Calcula el cuadrado de un número dado.

    Parámetros:
        numero (float): El número a elevar al cuadrado.

    Retorna:
        float: El resultado del número elevado al cuadrado.
    """
    return numero ** 2

# Ejecución del programa
try:
    numero = float(input(" Indique el número que desea elevar al cuadrado: "))
    resultado = cuadrado(numero)
    print(f" El cuadrado de {numero} es: {resultado}")
except ValueError:
    print(" Por favor, ingrese un número válido.")
