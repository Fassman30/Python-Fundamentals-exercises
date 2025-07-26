def clasificar_edades(edades: int) -> str:
    if edades >= 0 and edades <= 12:
        return "usted es un niño"
    elif edades >= 13 and edades <= 17:
        return "usted es un adolescente"
    elif edades >= 18 and edades <= 64:
        return "usted es un adulto"
    else:
        return "usted es un adulto mayor"


edad = int(input("¿Cuál es su edad? "))
clasificacion = clasificar_edades(edad)
print(f"Usted es {clasificacion}")