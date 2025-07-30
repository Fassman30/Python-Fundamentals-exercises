def New_dictionary2():
    Manzana={"Nombre": "manzana",
             "Color" : "rojo",}
    Pera = {"Nombre":"pera",
            "Color" : "amarillo"}
    Mango={"Nombre" : "mango",
           "Color" : "Naranja",}
    Frutas=[Manzana,Pera,Mango]
    for elemento in Frutas:
     print(f"Nombre: {elemento['Nombre']}, Color: {elemento['Color']}")
    return Frutas
New_dictionary2()