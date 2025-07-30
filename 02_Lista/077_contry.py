def country():
    Dictionary={"Colombia":["Bogota","Medillin","Cali"],
                "Mexico":["Mexicali","Hermollsio","Porito"],
                "España":["Madrid","Barcelona","sevilla"]}
    pais_god=str(input("que pais le gustaria ver las ciudades mas god :"))
    for pais_actual in Dictionary:
       if pais_actual.lower() == pais_god.lower():
             print(f"Las ciudades importantes de {pais_actual} son: {Dictionary[pais_actual]}")
             return
    print(f"Lo siento, no encontramos información para el país '{pais_god}'.")
country()