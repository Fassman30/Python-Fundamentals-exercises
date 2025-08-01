def limpiar_y_filtrar_nombres():
    limpiar_y_filtrar_nombres=[]
    nombres_sucios = ["  Ana ", "juan  ", "MARIA", "pedro", "luis", "Elena  "]
    print(f"Su lista actual es { nombres_sucios}")
    for nombre in nombres_sucios:
        #aqui se pasan los nombres a minisculas y se eliminan los espacios
            nombre=nombre.lower().strip()
        #aqui evaluamos si los caracteres del nombre son mayores a 4 y los filtamos      
            if len(nombre) > 4:
             limpiar_y_filtrar_nombres.append(nombre)      
    print(f" su nueva lista es {limpiar_y_filtrar_nombres}")
   #Calcula la suma total de las calificaciones (sum).
    calificaciones = [4.5, 3.8, 5.0, 4.2, 3.0] 
    print(calificaciones)
    sum_total =sum(calificaciones)
    print(f"la suma total es de : {sum_total}")
    #Calcular el numero de calificaciones dentro de la lista (len)
    numero_califcaciones= len(calificaciones)
    print(f"el numero de notas son : {numero_califcaciones}")
    #Calculamos el promedio dentro de la lista (media)
    promedio = sum(calificaciones)/len(calificaciones)
    print(f"el promedio de las califcaciones es de {promedio:.2f}")
    #Invertir cadena de listas 
    invertir_cadenas_lista=["python", "programacion", "curso"] 
    lista_invertida=[]     
    for palabra in invertir_cadenas_lista:
        palabra_invertida=palabra[::-1]
        lista_invertida.append(palabra_invertida)
    print(lista_invertida)
    
limpiar_y_filtrar_nombres()