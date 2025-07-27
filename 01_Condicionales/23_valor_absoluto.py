def valor_absoluto(valor):
    """
    Devuelve el valor absoluto de un número.
    
    Parámetros:
        valor (int): Número a evaluar.
    
    Retorna:
        int: Valor absoluto del número.
    """
    return abs(valor)

print("/// Verificar valor absoluto ///")
try:
    valor = int(input("Indica el número del que deseas saber el valor absoluto: "))
    valorT = valor_absoluto(valor)
    print(f"Resultado: El valor absoluto es {valorT}")
except ValueError:
    print("Por favor, ingresa un número válido.")
