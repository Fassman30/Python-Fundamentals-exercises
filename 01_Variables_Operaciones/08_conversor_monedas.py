#definimos una funcion para cambiar la moneda
def cambia_moneda (moneda_cop):
     return (moneda_cop*4056.76)
print("cambio de dolar a moneda colombiana")
print("cual es la cantidad de dinero q desea cambiar : ")
moneda_cop = float (input())

cambio = cambia_moneda(moneda_cop)
print(f"el dinero a cambiar es de {cambio}")
     
