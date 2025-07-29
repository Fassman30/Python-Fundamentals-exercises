def sumar_hasta_1000() ->int:
     suma=0
     while  suma < 1000:
         try:
             numero=int(input("indiqueme un numero :"))
             if numero ==0:
                print("solo se permiten numeros positivos")
                continue
             suma+=numero  
         except ValueError:
             print("El número no es válido. Por favor, digite un dato real.")
     return suma
 
total=sumar_hasta_1000()
print(f"la suma total es de {total}")
     
    