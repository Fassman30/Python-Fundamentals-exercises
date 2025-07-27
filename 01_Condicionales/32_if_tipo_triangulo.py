def tipo_triangulo(a: int, b: int, c: int) -> str:
    if a + b > c and a + c > b and b + c > a:
        print("Su triángulo es válido")
        if a == b == c:
            return "equilátero"
        elif a == b or a == c or b == c:
            return "isósceles"
        else:
            return "escaleno"
    else:
        return "no válido"

"""
Calculamos qué tipo de triángulo es: equilátero, isósceles o escaleno.
Parámetros: evaluamos tres entradas a (int), b (int), c (int) dadas por el usuario.
Retorna: el tipo de triángulo que es.
"""

while True:
    try:
        a = int(input("¿Cuál es el lado a?: "))
        b = int(input("¿Cuál es el lado b?: "))
        c = int(input("¿Cuál es el lado c?: "))
        
        resultado = tipo_triangulo(a, b, c)
        print(f"Su triángulo es: {resultado}")

    except ValueError:
        print("⚠️ El dato ingresado no es válido. Por favor, ingrese números enteros.")

    continuar = input("¿Desea verificar otros números? (s/n): ").strip().lower()
    if continuar != 's':
        print("Gracias por usar el verificador de triángulos.")
        break
