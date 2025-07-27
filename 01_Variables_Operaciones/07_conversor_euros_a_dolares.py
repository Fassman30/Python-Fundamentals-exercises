import random
def cambio_euros ( dolar):
   return dolar * 1.18
print("////cambio dolar a euro ////")
print("cuantos dolares quiere convertir a euro")
dolar=float(input())
eurosT=cambio_euros(dolar)
print(f"Tu conversión es de: €{round(eurosT, 2)}")
