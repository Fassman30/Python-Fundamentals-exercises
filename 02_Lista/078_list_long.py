universo=["sol", "luna", "estrellas", "tierra"]

def Longitud(Lista):
    # ¡Aquí está la comprensión de lista!
    nueva_Lista = [len(palabra) for palabra in Lista] # <-- ¡Esta es la línea mágica!
    print(f"Tu nueva lista es {nueva_Lista}")
    return nueva_Lista

# Llamada a la función
Longitud(universo)