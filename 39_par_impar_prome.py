import random

def numero_aleatorio() -> int:
    return random.randint(1, 10)

while True:
    try:
        prediccion = input("¿Crees que la suma será par o impar? (par/impar): ").strip().lower()
        numero_usuario = int(input("Elige un número del 1 al 10: "))
        numero_maquina = numero_aleatorio()
        print(f"Mi número es: {numero_maquina}")
        
        suma = numero_usuario + numero_maquina
        print(f"La suma es: {suma}")
        
        if suma % 2 == 0 and prediccion == "par":
            print("✅ ¡Ganaste! La suma es par.")
        elif suma % 2 != 0 and prediccion == "impar":
            print("✅ ¡Ganaste! La suma es impar.")
        else:
            print("❌ Perdiste. Intenta otra vez.")
        
    except ValueError:
        print("⚠️ Ingresa un número válido, porfis.")
        continue
    
    continuar = input("¿Deseas jugar otra vez? (s/n): ").strip().lower()
    if continuar != 's':
        print("👋 ¡Gracias por jugar!")
        break