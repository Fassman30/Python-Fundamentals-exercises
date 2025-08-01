def claves_usario():
    perfil_usario={"Nombre":"Ana",
                   "Edad" : 28,
                   "Ciudad": "Madrid"}
       #Acceder a los valores
    print(f"el nombre del usario es {perfil_usario["Nombre"]} \n y su edad es de {perfil_usario["Edad"]}")
    #Añadimos una nueva clave
    perfil_usario["Ocupacion"]='Cientifica de datos'
    #Modificamos la clave edad
    perfil_usario["Edad"]=29
    #Removemos un elemento
    del perfil_usario["Ciudad"]
    print(f"Su nuevo diccionario es {perfil_usario}")
    #Imprimimos con for keys , values y items 
    for claves in perfil_usario.keys():
        print(f"las claves son : {claves}")
    for valor in perfil_usario.values():
        print(f"Los valores son : {valor}")
    for claves,valor in perfil_usario.items():
        print(f"Clave: {claves}, Valor: {valor}")
    
claves_usario()
    