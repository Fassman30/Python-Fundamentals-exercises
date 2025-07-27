import math  # Librería estándar para operaciones matemáticas avanzadas

def raiz_cuadrada(numero: float) -> float:
    """
    Calcula la raíz cuadrada de un número.

    Parámetros:
    - numero (float): El número al que se le desea calcular la raíz cuadrada.

    Retorna:
    - float: La raíz cuadrada del número, redondeada a 2 decimales.
    """
    return round(math.sqrt(numero), 2)

# --- Ejecución principal del programa ---

print("//// RAÍZ CUADRADA ////")
try:
    numero = float(input("¿Qué número deseas calcular?: "))
    raiz = raiz_cuadrada(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz}")
except ValueError:
    print("Error: Ingresa un número válido.")
