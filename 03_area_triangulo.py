# Definimos una función que calcula el área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Programa principal
print("******* Cálculo de Triángulo **********")
print("¿Cuál es la altura?")
altura = int(input())

print("¿Cuál es la base?")
base = float(input())

# Usamos la función para obtener el área
area = calcular_area_triangulo(base, altura)
