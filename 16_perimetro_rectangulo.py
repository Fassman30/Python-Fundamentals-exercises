
#definimos la funcion para el pereimetro
def calculo_de_rectangulo(base,altura):
    return ((base) + (altura)) * 2

print("********perimetro de un rectangulo")
print("cual es la base de su rectangulo")
base=int(input())   
print("cual es altura de su rectangulo")
altura=int(input())

perimetro = calculo_de_rectangulo(base,altura)
print(f"el perimetro de su rectangulo es :{perimetro}")