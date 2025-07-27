def precio_final(precio_original,descuento):
    return precio_original - (precio_original * descuento / 100)

print("que precio tiene su producto : ")
precio_original=int(input())
print("de cuanto es el descuento : ")
descuento = int (input())

total= precio_final(precio_original,descuento)
print(f"el precio es de {total}")
