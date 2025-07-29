def sumar_y_contar_hasta_negativo() ->int :
        suma=0
        contador=0
        while True :
            numero=int(input("ingrese un numero :"))
            if numero<0:
                break
            suma+=numero
            contador+=1            
        print(f"Ingresaste {contador} números positivos.")
        return suma

total_suma=sumar_y_contar_hasta_negativo()
print(f"la suma total es de {total_suma}")
