def contar_hasta_100() -> int:
     suma=0
     while True:
         numero=int(input("que numero desea ingresar :"))
         if numero > 100 :
            break
         suma +=1          
     return suma
total=contar_hasta_100()
print(f"la los numeros son antes de q ingresas uno mayor a {total}")
         