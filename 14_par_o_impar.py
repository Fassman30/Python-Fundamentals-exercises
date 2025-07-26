def par_impar(numero: float) -> bool:
    return numero % 2 == 0

while True:
    print("/// Número par o impar ///")
    numero = float(input("¿Con qué número desea verificar si es par o impar?: "))
    
    if par_impar(numero):
        print("✅ El número es par.")
    else:
        print("❌ El número es impar.")
    
    respuesta = input("¿Desea intentar con otro número? (s/n): ")
    if respuesta.lower() != 's':
        print("¡Gracias por jugar! 👋")
        break