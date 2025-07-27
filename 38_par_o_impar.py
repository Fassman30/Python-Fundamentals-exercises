import random

def generar_numero() -> int:
    return random.randint(1, 10)

"""
Juego de par o impar entre el usuario y la máquina.
El usuario elige par o impar, elige un número, se suma con un número aleatorio,
y se determina quién gana.
"""

while True:
    try:
        eleccion = input("¿Quieres ser par o impar? (par/impar): ").strip().lower()
        if eleccion not in ['par', 'impar']:
            print("⚠️ Por favor, elige solo 'par' o 'impar'.")
            continue

        num_usuario = int(input("Elige un número entre 1 y 10: "))
        if num_usuario < 1 or num_usuario > 10:
            print("🚫 Número fuera de rango. Intenta entre 1 y 10.")
            continue

        num_maquina = generar_numero()
        print(f"La máquina eligió el número: {num_maquina}")

        total = num_usuario + num_maquina
        print(f"La suma total es: {total}")

        if total % 2 == 0:
            resultado = "par"
        else:
            resultado = "impar"

        print(f"El resultado es: {resultado}")

        if resultado == eleccion:
            print("🎉 ¡Ganaste!")
        else:
            print("😢 Perdiste. ¡Intenta de nuevo!")

    except ValueError:
        print("⚠️ Solo se permiten números válidos.")

    continuar = input("¿Deseas jugar otra vez? (s/n): ").strip().lower()
    if continuar != 's':
        print("👋 ¡Gracias por jugar par o impar!")
        break
