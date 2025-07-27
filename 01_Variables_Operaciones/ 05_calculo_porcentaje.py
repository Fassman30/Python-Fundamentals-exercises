def porcentaje_numero(numero,porcentaje_usuario):
    total = (numero * porcentaje_usuario ) /100
    return total
   

print("que numero desea saber su porcentaje :")
numero = int(input())
print("q porcentaje desea % :" ) 
porcentaje_usuario = int(input())

total = porcentaje_numero(numero,porcentaje_usuario)

print(f"el porcentaje de su numero es <3 : {total}")
