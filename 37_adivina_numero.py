import random

def numero_aleatorio() -> int:
    return random.randint(1, 10)

numero = numero_aleatorio()
print("🎲 He pensado un número entre 1 y 10. ¡Adivínalo!")

while True:
    try:
        numero_usuario = int(input("¿Qué número crees que es? ➤ "))
        
        if numero_usuario <= 0:
            print("🚫 El número no puede ser 0 o menor.")
            continue

        if numero_usuario == numero:
            print("🎉 ¡Ganaste!")
            break
        elif numero_usuario > numero:
            print("📉 El número es muy alto.")
        else:
            print("📈 El número es muy bajo.")

    except ValueError:
        print("⚠️ Entrada inválida. Por favor, escribe un número.")

    continuar = input("¿Deseas volver a adivinar el número? (s/n): ").strip().lower()
    if continuar != 's':
        print("👋 ¡Gracias por jugar!")
        break
