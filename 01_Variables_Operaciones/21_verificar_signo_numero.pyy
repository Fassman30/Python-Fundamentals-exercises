def es_bisiesto(año: int) -> bool:
    """
    Verifica si un año es bisiesto.

    Un año es bisiesto si:
    - Es divisible por 4
    - No es divisible por 100, a menos que también sea divisible por 400
    """
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Entrada del usuario
print("///Verificar año bisiesto///")
año = int(input("Ingresa un año: "))

# Evaluación
if es_bisiesto(año):
    print(" El año es bisiesto")
else:
    print(" El año NO es bisiesto")
