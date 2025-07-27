def verificar_signo(numero: float) -> str:
    """
    Verifica si un número es positivo, negativo o cero.

    Parámetros:
        numero (float): Número a evaluar.

    Retorna:
        str: Resultado indicando si es positivo, negativo o cero.
    """
    if numero > 0:
        return "El número es positivo"
    elif numero < 0:
        return "El número es negativo"
    else:
        return "El número es cero"
#  Programa principal
print("///Verificar número///")
try:
    numero_usuario = float(input("Ingresa un número: "))
    resultado = verificar_signo(numero_usuario)
    print("Resultado:", resultado)
except ValueError:
    print("Por favor, ingresa un número válido.")
