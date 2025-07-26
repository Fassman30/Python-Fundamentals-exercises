def area_triangulo(base: float, altura: float) -> float:
    """
    ////////////Calcula el área de un triángulo/////////.

    Parámetros:
        base (float): La base del triángulo.
        altura (float): La altura del triángulo.

    Retorna:
        float: El área calculada del triángulo.
    """
    return (base * altura) / 2


def iniciar_programa():
    """
    Ejecuta un ciclo para que el usuario verifique el área de su triángulo
    tantas veces como desee.
    """
    print("-//////Calculo de área////-")
    while True:
        try:
            base = float(input("Indíqueme la base por favor: "))
            altura = float(input("Indíqueme la altura por favor: "))
            Area = area_triangulo(base, altura) # Usar el nombre de función corregido
            print(f"El Área de su Triángulo es de {Area} cm")

        except ValueError:
            print("⚠️ Por favor, ingrese solo números válidos.⚠️")

        continuar = input("¿Desea evaluar el área de otros triángulos? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias, cuídese mucho <3.")
            break


# Ejecutar el programa principal
if __name__ == "__main__":
    iniciar_programa()

