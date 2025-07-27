def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """
    Calcula los grados Celsius a partir de los Fahrenheit
    que nos indique el usuario.

    Parámetros:
    - fahrenheit (float): Temperatura en grados Fahrenheit.

    Retorna:
    - float: Temperatura convertida a grados Celsius.
    """
    return round((fahrenheit - 32) * 5 / 9, 2)

# --- Ejecución principal del programa ---
try:
    print("///// Conversor de Fahrenheit a Celsius /////")
    fahrenheit = float(input("Señor usuario, indique los grados Fahrenheit que desea convertir a Celsius: "))
    total_celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"🌡️ Los grados Celsius equivalentes son: {total_celsius}°C")
except ValueError:
    print("❌ Error: Ingrese un número válido, por favor.")
