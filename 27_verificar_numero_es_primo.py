def es_primo(numero: int) -> bool:
    """
    Determina si un número entero es primo.
    
    Parámetro:
        numero (int): Número a evaluar.
        
    Retorna:
        bool: True si es primo, False si no lo es.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Bucle principal del programa
while True:
    try:
        numero = int(input("Indique qué número desea saber si es primo: "))
        if es_primo(numero):
            print(f" {numero} es un número primo.")
        else:
            print(f" {numero} no es un número primo.")
    except ValueError:
        print("⚠️ Por favor, ingrese un número válido.")
        continue

    continuar = input("¿Desea verificar otro número? (s/n): ").strip().lower()
    if continuar != 's':
        print("Gracias por usar el programa. ¡Ten un buen día! ")
        break  # <-- Estaba mal identado, ahora sí funciona perfecto
