def promedio_longitud_palabras_largas(lista,umbral):
    nueva_lista=[]
    for palabra in lista:
        if len(palabra)>umbral:
            nueva_lista.append(palabra)
    if nueva_lista :
        suma_total = sum(len(palabra)for palabra in nueva_lista)
        cantidad_elementos = len(nueva_lista)
        promedio = suma_total / cantidad_elementos
        
        print(f"Las palabrs mayores a  {umbral} son: {nueva_lista}")
        print(f"Cantidad: {cantidad_elementos}")
        print(f"Promedio: {promedio}")
        return promedio
    else:
        print("No hay elementos mayores al umbral.")
        return None
promedio_longitud_palabras_largas(["hola", "programación", "IA", "perro", "extraordinario"], 5)