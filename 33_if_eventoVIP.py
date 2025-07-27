def evento_vip(edad: int, clave: str) -> str:
    """
    Creamos un programa para dar acceso VIP a nuestros clientes.

    Parámetros: 
    edad (int), clave (str) deben cumplir con lo establecido para ingresar: edad mayor o igual a 21 y clave 'VIP2025'

    Retorna: 
    str: Si puede pasar o no
    """
    if edad >= 21 and clave == 'VIP2025':
        return "✅ Acceso concedido al evento VIP"
    else:
        return "⛔ Acceso denegado: edad o código incorrectos"


# Entradas del usuario
name = input("¿Cuál es su nombre?: ")
edad = int(input(f"¿Cuál es su edad, señor/a {name}?: "))
clave = input(f"Señor/a {name}, su edad es de {edad}. Indíqueme la clave para poder pasar: ")

# Llamada a la función y resultado
resultado = evento_vip(edad, clave)
print(resultado)
