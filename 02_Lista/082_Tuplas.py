def tupla ():
    punto_carteseano=(10,25)
    #Acceder a los elementos de la tupla :
    print(f"el valor de x es de {punto_carteseano[0]}")
    print(f"el valor de y es de {punto_carteseano[1]}")
    #Tuplas en una lista:
    puntos_mapa=[(40.71, -74.00), (34.05, -118.24), (51.50, 0.12)]
    a ,b,c= puntos_mapa
    print(f"la primera latitud y longitud es de {a}")
    print(f"la segunda latitud y longitud es de {b}")
    print(f"la tercera latitud y longitud es de {c}")
    

tupla()