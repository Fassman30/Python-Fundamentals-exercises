def factorial(num: int) -> int:
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.

    Parámetros:
        num (int): El número entero no negativo para el cual se calculará el factorial.

    Retorna:
        int: El valor factorial del número dado.

    Lanza:
        ValueError: Si el número de entrada es negativo, ya que el factorial
                    no está definido para números negativos.
    """
    if num < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    # Caso base: el factorial de 0 es 1.
    # Caso recursivo: n! = n * (n-1)!
    return 1 if num == 0 else num * factorial(num - 1)


def iniciar_programa_factorial():
    """
    Permite al usuario calcular el factorial de números de forma interactiva.
    """
    print("--- Calculadora de Factorial ---")
    while True:
        try:
            numero_str = input("Ingrese el número para calcular su factorial (o 'salir' para terminar): ").strip()

            if numero_str.lower() == 'salir':
                print("Gracias por usar la calculadora de factorial. ¡Hasta pronto! 👋")
                break

            numero_usuario = int(numero_str)
            
            # Llamada a la función factorial con manejo de errores específicos
            resultado_factorial = factorial(numero_usuario)
            print(f"El factorial de {numero_usuario} es: {resultado_factorial}")

        except ValueError as e:
            # Captura errores de conversión a int y errores lanzados por la función factorial
            print(f"⚠️ Error: {e}. Por favor, ingrese un número entero no negativo válido.")
        except RecursionError:
            # Captura errores si el número es demasiado grande para la recursión (Stack Overflow)
            print("⚠️ Error: El número es demasiado grande para calcular el factorial de forma recursiva. Intente con un número más pequeño.")
        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"⚠️ Ocurrió un error inesperado: {e}")

        # No se necesita preguntar si desea continuar si ya se ofrece 'salir' en el input
        # si el bucle es infinito hasta que se ingrese 'salir'

# Punto de entrada principal del programa
if __name__ == "__main__":
    iniciar_programa_factorial()
