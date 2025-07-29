def ejercicio_multiplo_10()->int:
     suma=0
     contador=0
     while True:
         try:
             numero=int(input("Indiqueme un numero por favor :"))
             if numero %10==0:
                 break
             suma+=numero
             contador+=1           
         except ValueError:
             print("por favor dijite un numero valido")
     print(f"los numeros contados fueron :{contador}")              
     return suma
 
total_suma=ejercicio_multiplo_10()
print(f"la suma total es de {total_suma}")
          