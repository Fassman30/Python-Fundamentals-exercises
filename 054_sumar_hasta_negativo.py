def sumar_hasta_negativo()->int :
   suma=0
   while True:
       try:
           numero=int(input("dijite el numero que desea:"))
           if numero <= 0 :
               break
           suma += numero
       except ValueError:
           print("dijite un numero valido")
           continue
   return suma
total = sumar_hasta_negativo()
print(f"la suma total es de {total}")
