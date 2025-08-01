def conteo_elementos():
    temperaturas_raw = [22.5, 24.1, 23.0, 22.5, 25.3, 24.1, 23.0, 26.0]
    print(f"sus datos son{temperaturas_raw}")
    # Convierte la lista a un set para eliminar duplicados.
    # El set no mantiene el orden original.
    temperaturas_unicas = set(temperaturas_raw)
    # Esta línea ordena la lista ORIGINAL 'temperaturas_raw', de menor a mayor
    temperaturas_raw.sort(reverse=True)
    # Imprime el set de temperaturas únicas (el orden puede variar).
    print(temperaturas_unicas)
    palabras_texto = ["modelo", "datos", "entrenamiento", "modelo", "algoritmo", "datos", "prediccion", "modelo", "algoritmo", "datos"]
    frecuencia_palabras = {} # Inicializa un diccionario vacío para guardar las frecuencias.
    # Itera sobre cada palabra en la lista.
    for palabra in palabras_texto:
        # Verifica si la palabra ya es una clave en el diccionario de frecuencia.
        if palabra not in frecuencia_palabras:
            # Si no está, la añade como nueva clave con un contador de 1.
            frecuencia_palabras[palabra] = 1
        else:
            # Si ya está, incrementa su contador en 1.
            frecuencia_palabras[palabra] += 1
    # Imprime el diccionario con las frecuencias de cada palabra.
    print(frecuencia_palabras)
    # Usando una Comprensión de Lista (más conciso)
    errores_api_lc= [] # Inicializa una lista vacía para los errores.
    codigos_estado = [200, 404, 200, 500, 200, 404, 200]
    errores_api_lc = [codigo for codigo in codigos_estado if codigo != 200]
    print(f"Errores (con LC): {errores_api_lc}")
    print(errores_api_lc)

conteo_elementos()