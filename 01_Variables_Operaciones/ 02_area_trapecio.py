# 🌟 area_trapecio.py 🌟

# 🎯 --- Definición de función ---
def area_de_un_trapecio(base_mayor: float, base_menor: float, altura: float) -> float:
    """
    📝 Calcula el área de un trapecio a partir de su base mayor, base menor y altura.

    📐 Fórmula:
        Área = ((base_mayor + base_menor) * altura) / 2

    📥 Parámetros:
        base_mayor (float): Longitud de la base mayor del trapecio.
        base_menor (float): Longitud de la base menor del trapecio.
        altura (float): Altura del trapecio.

    📤 Retorna:
        float: Área del trapecio redondeada a 2 decimales.
    """
    return round(((base_mayor + base_menor) * altura) / 2, 2)

# 🚀 --- Ejecución principal del programa ---
try:
    print("🎀📐 Cálculo del área de un trapecio 📐🎀")
    base_mayor = float(input("🧮 Ingrese la base mayor del trapecio: "))
    base_menor = float(input("📏 Ingrese la base menor del trapecio: "))
    altura = float(input("📐 Ingrese la altura del trapecio: "))

    area = area_de_un_trapecio(base_mayor, base_menor, altura)
    print(f"✅ El área del trapecio es: {area} unidades cuadradas. 🎊")

except ValueError:
    print("❌🚫 Error: Ingrese un número válido para los cálculos, porfis. 🙈")
